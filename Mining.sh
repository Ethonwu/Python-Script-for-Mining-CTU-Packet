#!/bin/bash
name="Jan"
for i in `seq 1 27`
do
  filename=$name$i".txt"
  outputfile="output_"$filename
  tablefile="Table_"$outputfile
  final_result="final_"$filename

  python2.7 pre.py -f $filename -o $outputfile
  java -jar ../spmf.jar run Apriori $outputfile ddd 0.5
  sed -i 's/ /,/g' ddd
  sed -i 's/,,#SUP:,/ /' ddd
  sed -i 's/,#SUP:,/ /' ddd
  python2.7 Value_to_Item.py -f ddd -t $tablefile > $final_result
  rm ddd



done
