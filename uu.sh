#!/bin/bash
unzip -d /tmp/$1 /tmp/pybites_bite$1.zip
mkdir $1
cp /tmp/$1/*.py $1/
