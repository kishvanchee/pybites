#!/bin/bash
set -e
git add $1/
git commit -m "submission Bite $1 @ codechalleng.es"
git push origin master
