# !bin/bash
if [ -d "$1" ];[ -d "$2" ]; then 
   rsync -r -i -v -v --delete-during --info=ALL "$1" "$2" >> rsync.log
   date >> rsync.log
fi
