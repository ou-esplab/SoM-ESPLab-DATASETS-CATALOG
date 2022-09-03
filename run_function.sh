#!/bin/bash


function foo() {
  python3.6 /home/kpegion/projects/SoM-ESPLab-DATASETS-CATALOG/generate_catalog.py $1 $2 $3 $4 $5
  if [ $? -eq 0 ]
	then
	  echo "$2 Success"
	else
	  echo "$2 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
	fi
}



filename='data.txt'


while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}
theDataset=${line[1]}
theParent=${line[2]}
theTags=${line[3]}
theConcat=${line[4]}


temp_dir=${line[1]}
mkdir ${temp_dir}_temporary
pushd ${temp_dir}_temporary



foo $theFile $theDataset $theParent $theTags $theConcat
echo "---------------------------------------------------------------------------------------"
popd
done < $filename

