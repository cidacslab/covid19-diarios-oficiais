#!/bin/bash

echo "Starting progam at $(date)"


folder=~/repos/covid19-diarios-oficiais/full-data/covid19/

echo "Scaning folder $folder for states"

echo "Printing list of states"


for state in $(ls -d $folder*); do
  echo "Found state $state"
  for file in $(ls $state/*.pdf); do
    filename=${file##*\/}
    echo "File name $filename"
    echo "File address $file"
    # create a folder to house the file
    echo "The folder name will be ${file::-4}"
    # TODO: sss
    # mkdir new folder
    # move the pdf to the new folder
    # run the command with the new folder + filename
    # get the list of files of the new folder
    # print the list of files of the new folder
    # (including the non split pdf)
    echo "Splitting file"
  done
done






echo "Ending progam at $(date)"
