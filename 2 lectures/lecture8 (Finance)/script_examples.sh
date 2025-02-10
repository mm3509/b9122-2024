#! /bin/bash

# Function example.
hello () {
    echo Hello world!
}

# Function example with argument.
hello2 () {
    echo Hello $1!
}


# For loop in the style of C.
for ((x=1; x<10; x ++));
do
  echo $x;
done


# Reading a file with a for loop.
IFS=$'\n'
for i in $(cat ./sample.txt);
do
  echo $i
done;


# Reading a file with a while loop.
while read line;
do
  echo "$line"
done < ./sample.txt
