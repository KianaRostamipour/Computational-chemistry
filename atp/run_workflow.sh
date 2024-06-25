#!/bin/bash

python concate.py
python atp.py
cp final.txt ../ffnonbond 
cd ../ffnonbond 
python nonbond.py
python spacing.py

