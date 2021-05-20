#!/usr/bin/env bash

tmp=$(tempfile)
read -p "Enter a search word > " word
python3 get_paper_info.py "'${word}'" > $tmp
python3 parse_trans.py $tmp > tmpfile
rm $tmp
