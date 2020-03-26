#!/bin/bash

for SRR in $(cat SRR_AccList_shortReads.txt); do
  # -X 10 added to limit the amount of the fastq stored for testing
  fastq-dump -X 10 --split-files --gzip -I -O \
  "/home/sykes/PycharmProjects/LongReadAccuracyVerification_pythonProject/SRRshortReads_Files_GZ/" $SRR
done
