FOLDER=$1

if [ -d $FOLDER ]; then
    echo $(ls $FOLDER/*.txt | wc -l);
else
    echo -1;
fi
