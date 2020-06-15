#!/bin/bash

# join vector into string
function join { local IFS="$1"; shift; echo "$*"; }

echo "Starting progam at $(date)"

folder=~/repos/covid19-diarios-oficiais/toy-data/covid19/

echo "Scaning folder $folder for states"

echo "Printing list of states"

for state in $(ls -d $folder*); do
  echo "Found state $state"
  for file_address in $(ls $state/*.pdf); do
    # TODO: get the file address
    # IFS is the delimiter
    # r is for raw
    # a for read to an array
    IFS='/' read -ra arr_file_address <<< "$file_address"
    file_name=${arr_file_address[-1]}
    file_address=/$(join / ${arr_file_address[@]::${#arr_file_address[@]}-1})/
    echo "File name $file_name"
    echo "File address $file_address"
    # create a folder to house the file
    folder_name=${file_name::-4}
    echo "The folder name will be $folder_name"
    # TODO: sss
    # mkdir new folder
    new_folder=$file_address$folder_name
    mkdir $new_folder
    # copy the pdf to the new folder
    cp $file_address$file_name $new_folder
    
    # run the command with the new folder + filename
    java -jar ~/pdfbox-app-2.0.20.jar PDFSplit -split 1 $new_folder/$file_name
    # get the list of files of the new folder
    for new_file in $(ls $new_folder/*.pdf); do
      echo "This is the name of one new file: $new_file"
      echo "Converting files to txt"
      java -jar ~/pdfbox-app-2.0.20.jar ExtractText $new_file
    done
  done
done

echo "Ending progam at $(date)"
