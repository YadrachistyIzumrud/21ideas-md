#!/bin/sh

 for f in $(find . -name *.html -exec grep  -l \<article\>  {} +)
   do
     echo $f
     cat $f |grep -A1 \<article\> $f |sed -n '2p' |python3 htm2md.py > $f.md
     #exit
   done
