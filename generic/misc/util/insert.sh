#!/bin/bash

# recommend sleeping for 30*number of receivers
# because the initialization is sequential
sleep 120
pq_test_insert -f NGRID -v /home/ldm/LDM6-LDM7-comparison/std_data/7hr_NGRID.txt