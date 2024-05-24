#!/bin/bash
set -xve

#function makeCatalog() {
#  python3.6 /home/kpegion/data-management/SoM-ESPLab-DATASETS-CATALOG/generate_catalog.py $1 $2 $3 $4 $5
#  #/home/kpegion/data-management/SoM-ESPLab-DATASETS-CATALOG/generate_catalog.py $1 $2 $3 $4 $5
#  if [ $? -eq 0 ]
#  then
#      echo "$2 Success"
#  else
#       echo "$2 Failed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
#  fi
#}


# Text file of datasets to be ingested
filename='data.txt'

# Read in the informaiton about each dataset from filename
while IFS=$'\t' read -r -a line ; do
theFile=${line[0]}
theDataset=${line[1]}
theParent=${line[2]}
theTags=${line[3]}
theConcat=${line[4]}


# Create temporary directories
temp_dir=${line[1]}

if [ ! -d ${temp_dir}_temporary ]; then
   mkdir ${temp_dir}_temporary
   pushd ${temp_dir}_temporary
fi

# Print the arguments to the makeCatalog Function
echo "makeCatalog Arguments are:" $theFile $theDataset $theParent $theTags $theConcat


# Call the makeCatalog Function
#makeCatalog $theFile $theDataset $theParent $theTags $theConcat
python3.6 /home/kpegion/data-management/SoM-ESPLab-DATASETS-CATALOG/generate_catalog.py $theFile $theDataset $theParent $theTags $theConcat
echo "---------------------------------------------------------------------------------------"
popd
done < $filename

# Copy files for correct location and delete temporary data directory
