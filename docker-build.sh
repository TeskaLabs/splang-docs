#!/bin/sh

rm -rf ./output
mkdir ./output
exec docker run --rm -v ${PWD}:/docs -v ${PWD}/output:/output squidfunk/mkdocs-material build --site-dir ./output
