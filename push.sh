#!/bin/bash

git config --global user.name "parisChatz"
git config --gobal user.email "parischatz94@gmail.com"

git pull
git add .
git commit -m "update from uni"
git push 

git config --global --unset user.name
git config --global --unset user.email