import os
import re
import sys
import shutil
import pprint
import subprocess

import requests

DEEPL_API_KEY = os.environ.get('DEEPL_API_KEY')


def translate_markdown(source_path, text, target_language, git_commit_hash):
	if not text.startswith('---'):
		raise RuntimeError("'{}' doesnt start with '---".format(source_path))

	headerpos = text.index('---', 4)
	headerin = text[:headerpos+4]
	body = text[headerpos+4:]

	# Parse and store header

	header = {}
	for hline in headerin.split('\n'):
		hline = hline.strip()
		if len(hline) == 0:
			continue
		if hline == '---':
			continue
		key, value = hline.split(": ", 1)
		header[key] = value


	# Transfrom admonitions into tags
	admonitions = []
	position = 0

	# Scan for admonitions
	while True:
		try:
			adpos = body.index('\n!!!', position)
		except ValueError:
			break
		position = body.index('\n', adpos+5)
		adtype = body[adpos+5:position]

		# Admonition body
		while position < len(body)-1:
			if body[position+1] == '\n':
				# Empty line is absorbed
				position += 1
				continue
			if body[position+1] == '\t':
				position = body.index('\n', position+1)
				continue
			if body[position+1:].startswith('    '):
				position = body.index('\n', position+1)
				continue

			break

		admonitions.insert(0, (adtype, adpos+1, body.index('\n', adpos+1), position))

	for adtype, adstart, adbody, adend in admonitions:
		adreformedbody = body[adbody:adend].replace('\n\t', '\n').replace('\n    ', '\n')
		if ' ' in adtype:
			adt1, adt2 = adtype.split(' ', 1)
			adt2 = '<admonheader>{}</admonheader>'.format(adt2)
		else:
			adt1 = adtype
			adt2 = ''

		body = body[:adstart] + '\n<admon type="{}">'.format(adt1) + adt2 + adreformedbody + '</admon>\n' + body[adend:]


	# Transform code segments from the Markdown into `<code>` tags
	body = re.sub(r'```(\S+)(.*?)```', r'<code type="\1">\2</code>', body, flags=re.DOTALL)

	base_url = "https://api.deepl.com/v2/translate"
	data = {
		"text": [
			header.get('title'),
			body,
		],
		"source_lang": "EN",
		"target_lang": target_language,
		"tag_handling": "xml",
	}
	response = requests.post(base_url, data=data, headers={'authorization': 'DeepL-Auth-Key {}'.format(DEEPL_API_KEY)}, timeout=30)
	response.raise_for_status()  # Ensure we got a successful response

	responsedata = response.json()

	result = '---\ngit_commit_hash: {}\n'.format(git_commit_hash)
	for key, value in header.items():
		if key == 'title':
			value = responsedata["translations"][0]["text"]
		result += '{}: {}\n'.format(key, value)

	result += '---\n'


	body = responsedata["translations"][1]["text"]

	# Change <admon> tags into `!!! xxx` form
	for m in reversed([*re.finditer(r'<admon type="(\S+)">(.+?)<\/admon>', body, flags=re.DOTALL)]):
		x = "!!! {}".format(m.group(1))
		g2 = m.group(2).replace('\n', '\n\t')

		rgmh = re.match(r'<admonheader>(.+?)<\/admonheader>', g2)
		if rgmh is not None:
			g2 = g2[:rgmh.start(0)] + g2[rgmh.end(0):]
			x += " {}".format(rgmh.group(1))

		body = body[:m.start(0)] + x + '\n\n\t' + g2 + body[m.end(0):]

	# Change <code> tags into Markdown form
	body = re.sub(r'<code type="(\S+?)">(.*?)</code>', r'```\1\2```', body, flags=re.DOTALL)

	result += body

	return result


def read_header(mdfile):
	try:
		with open(mdfile, 'r', encoding='utf-8') as fi:
			line = fi.readline()
			if line != '---\n':
				raise RuntimeError("'{}' doesnt start with '---".format(mdfile))

			header = {}
			while True:
				line = fi.readline()
				if line == '---\n':
					break
				line = line.strip()
				key, value = line.split(": ", 1)
				header[key] = value

			return header
	except FileNotFoundError:
		return {}


def process_directory(source_directory, target_directory, target_language, git_commit_hash):
	os.makedirs(target_directory, exist_ok=True)

	for root, dirs, files in os.walk(source_directory):
		for file in files:
			source_path = os.path.join(root, file)
			rel_path = os.path.relpath(source_path, source_directory) # Relative path to maintain folder structure
			target_path = os.path.join(target_directory, rel_path)
			
			# Create any necessary directories in the target directory
			os.makedirs(os.path.dirname(target_path), exist_ok=True)
			
			if file.endswith('.md'):

				header = read_header(target_path)
				if header.get('git_commit_hash') == git_commit_hash:
					# No change detected, skip translation
					# TODO: Implement "force" flag to enforce the translation
					continue

				print("Translating {} ...".format(file))
				with open(source_path, 'r', encoding='utf-8') as source_file:
					contents = source_file.read()
				translation = translate_markdown(source_path, contents, target_language, git_commit_hash)
				with open(target_path, 'w', encoding='utf-8') as target_file:
					target_file.write(translation)
			else:
				print("Copying {} ...".format(file))
				shutil.copy(source_path, target_path)


if __name__ == '__main__':
	if DEEPL_API_KEY is None:
		print("Provide 'DEEPL_API_KEY' environment variable, please.")
		sys.exit(1)
	git_commit_hash = subprocess.check_output(['git', 'describe', '--abbrev=7', '--always']).decode('utf-8').strip()
	process_directory('./docs', './cs/docs', 'CS', git_commit_hash)
