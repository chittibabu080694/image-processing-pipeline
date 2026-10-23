#!/bin/bash
mkdir -p python
pip install -r requirements.txt -t python/
zip -r pillow_layer.zip python/
rm -rf python
echo "Lambda layer package 'pillow_layer.zip' created successfully!"
