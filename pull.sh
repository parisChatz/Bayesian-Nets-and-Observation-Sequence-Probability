#!/bin/bash

git config --global user.name "parisChatz"
git config --global user.email "parischatz94@gmail.com"

git pull
git add .

git config --global --unset user.name
git config --global --unset user.email
