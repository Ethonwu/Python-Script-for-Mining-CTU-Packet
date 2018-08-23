#!/bin/bash
#name="Jan"
mkdir final_result
path=`pwd`
min_sup="0.5"
echo 
for i in ` ls | grep .txt`
do
  filename=$i
  outputfile="output_"$filename
  tablefile="Table_"$outputfile
  final_result="final_"$filename

  echo $outputfile

  python2.7 ~/packet/script/pre.py -f $filename -o $outputfile
  java -jar ~/packet/script/spmf.jar run Apriori $outputfile ddd $min_sup
  sed -i 's/ /,/g' ddd
  sed -i 's/,,#SUP:,/ /' ddd
  sed -i 's/,#SUP:,/ /' ddd
  python2.7 ~/packet/script/Value_to_Item.py -f ddd -t $tablefile > final_$min_sup_result/$final_result
  rm ddd



done

