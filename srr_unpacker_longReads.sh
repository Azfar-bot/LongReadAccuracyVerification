#!/bin/bash

for SRR in $(cat SRR_AccList_longReads.txt); do
  # -X 10 added to limit the amount of reads dumped for testing
  fastq-dump -X 10 --split-files --gzip -I -O \
  "/home/sykes/PycharmProjects/LongReadAccuracyVerification_pythonProject/SRRlongReads_Files_GZ/" $SRR
done

