### Script to parse reads from SRR files
### 17.03.2020

# THIS TAKES A LONG TIME TO RUN, PLEASE BE PATIENT

import os
import gzip
import shutil
import re
from Bio import SeqIO
from SRR_AccUnpacker import unpack_fastq

SRRshort_initial_loc = 'SRRshortReads_Files_GZ/'
SRRlong_initial_loc = 'SRRlongReads_Files_GZ/'
Unzip_SRR_dest = 'SRR_Files_Unzipped/'

# loads in our fastq files from accessions using fastq-dump in bash
unpack_fastq()

# UNZIP THE .GZ FILES HERE
for file in os.listdir(SRRshort_initial_loc):  # Short Reads
    # Regex to build file_out name
    pattern = '^SRR[0-9]+'
    search_string = file
    SRR_tag = re.match(pattern, search_string)
    # print(SRR_tag.group(0)) # Output test
    if file != 'README.txt':
        with gzip.open(f'{SRRshort_initial_loc}{file}', 'rb') as file_in, \
                open(f'{Unzip_SRR_dest}{SRR_tag.group(0)}_shortRead.fastq', 'wb') as file_out:
            shutil.copyfileobj(file_in, file_out)

for file in os.listdir(SRRlong_initial_loc):
    pattern = '^SRR[0-9]+'
    search_string = file
    SRR_tag = re.match(pattern, search_string)
    if file != 'README.txt':
        with gzip.open(f'{SRRlong_initial_loc}{file}', 'rb') as file_in, \
                open(f'{Unzip_SRR_dest}{SRR_tag.group(0)}_longRead.fastq', 'wb') as file_out:
            shutil.copyfileobj(file_in, file_out)
# print(os.listdir(SRR_initial_loc)) # Output test

# COUNT TOTAL NUMBER OF READS IN FASTQs HERE
for file in os.listdir(Unzip_SRR_dest):
    count = 0
    for read in SeqIO.parse(f'{Unzip_SRR_dest}{file}', 'fastq'):
        count += 1
    print(file, 'contains %i reads' % count)

# REMOVE READS WITH PHRED SCORE < 20 HERE
good_shortReads = []
good_longReads = []
count_short = 0
count_long = 0
for file in os.listdir(Unzip_SRR_dest):
    pattern_short = '^SRR[0-9]+_short'  # Start RegEx
    pattern_long = '^SRR[0-9]+_long'
    search_string = file
    SRR_tag_shortReads = re.match(pattern_short, search_string)
    SRR_tag_longReads = re.match(pattern_long, search_string)  # End RegEx
    if pattern_short in f'{file}':
        for read in SeqIO.parse(f'{Unzip_SRR_dest}{file}', 'fastq'):
            if min(read.letter_annotations['phred_quality']) >= 20:
                good_shortReads.append(read)
        count_short = SeqIO.write(good_shortReads,
                                  f'{SRR_tag_shortReads.group(0)}_SRS_goodPHRED.fastq', 'fastq')  # SRS = Short reads
    elif pattern_long in f'{file}':
        for read in SeqIO.parse(f'{Unzip_SRR_dest}{file}', 'fastq'):
            if min(read.letter_annotations['phred_quality']) >= 20:
                good_longReads.append(read)
        count_long = SeqIO.write(good_longReads,
                                 f'{SRR_tag_longReads.group(0)}_LRS_goodPHRED.fastq', 'fastq')  # LRS = Long Reads
print('Saved %i short reads with PHRED score >= 20' % count_short)
print('Saved %i long reads with PHRED score >= 20' % count_long)
