### Script to wrap two bash scripts for dumping FASTQ files
### 26.03.2020

import subprocess
import os

topLevelPATH = '/home/sykes/PycharmProjects/LongReadAccuracyVerification_pythonProject/'

def unpack_fastq():
    # This wraps the shell script below
    bashScript_short = subprocess.call(['./srr_unpacker_shortReads.sh'])
    bashScript_long = subprocess.call('./srr_unpacker_longReads.sh')

    shortRead_dir = os.listdir(f'{topLevelPATH}SRRshortReads_Files_GZ')
    longRead_dir = os.listdir(f'{topLevelPATH}SRRlongReads_Files_GZ')

    if len(shortRead_dir) != 0:
        print('Short read fastq files pulled successfully')

    if len(longRead_dir) != 0:
        print('Long read fastq files pulled successfully')


