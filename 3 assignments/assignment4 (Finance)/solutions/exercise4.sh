#! /bin/bash

if [ "$#" -ne 1 ]; then
  echo "You should pass one argument, and only one: $0 /path/to/directory"
  exit 1
fi

cd $HOME
prefix=my_backup
dst=$prefix
for i in $(seq 1 100); do
    if [ ! -d $dst ]; then
        break
    fi
    dst=$prefix$i
done

mkdir $dst
cd $dst
cp $1/*.txt .
num=$(ls -l *.txt | wc -l)
echo "Copied $num file(s) to $(pwd)"
