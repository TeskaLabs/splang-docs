# SP-Lang documentation

The documentation is available at https://docs.teskalabs.com/sp-lang/.

![SP-lang logo](./docs/splang-logo.jpg)


## Editing

This documentation is built using [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).
The content is stored at `./docs` directory of this repository.


## Plugins

* mkdocs-print-site-plugin - https://github.com/timvink/mkdocs-print-site-plugin
* mkdocs-awesome-pages-plugin - https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin


## Localization

Localization is driven by DeepL.
It is driven by the `python3 ./deepl.py` script that translates english pages into czech.
It translates only changed pages; it uses `git` internally to detect changed pages.
The output needs to be checked.

* `cs` (Czech) version is in `/cs` folder.
