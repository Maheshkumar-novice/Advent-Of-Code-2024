#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: $0 <current-day-number>"
    exit 1
fi

day=$(printf %02d $1)

dir=Day-$day

if [ -d "$dir" ]; then
  echo "$dir already exists."
  exit 1
fi

mkdir $dir

cd $dir

touch sample.txt input.txt part-1.py part-2.py

echo -e "with open('sample.txt', 'r') as f:\n    print(f.read())" > part-1.py

curl -v -H "Connection: close" -H 'Cookie: session=$AOC_SESSION_COOKIE' https://adventofcode.com/$2/day/$1/input -o input.txt
