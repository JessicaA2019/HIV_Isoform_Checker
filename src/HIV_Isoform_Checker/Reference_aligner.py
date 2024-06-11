### 05/15/24
### Jessica L Albert
### Reference Aligner
### last updated 05/15/24 by JLA

import mappy as mp
import re
import pandas as pd

def CIGAR_for_new_ref(wanted_ref):
    a = mp.Aligner("NL43_Complete.fa")
    for name, seq, qual in mp.fastx_read(wanted_ref): # read a fasta/q sequence
        for hit in a.map(seq): # traverse alignments
            CIGAR = hit.cigar_str
    return CIGAR

def calc_shift(CIGAR, pos2shift):
    numbers = re.findall(r'[\d]+', CIGAR)
    letters = re.findall(r'[\D]+', CIGAR)
    data = {'letter': letters, 'number': numbers}
    df = pd.DataFrame(data)

    posInRef = 0
    shift_num = 0
    CIGAR_step = 0
    while posInRef < pos2shift:
        if df.iloc[CIGAR_step]['letter'] == 'M': 
            posInRef = posInRef + int(df.iloc[CIGAR_step]['number'])
        elif df.iloc[CIGAR_step]['letter'] == 'D':
            shift_num = shift_num - int(df.iloc[CIGAR_step]['number'])
        elif df.iloc[CIGAR_step]['letter'] == 'I':
            shift_num = shift_num + int(df.iloc[CIGAR_step]['number'])
        CIGAR_step = CIGAR_step + 1
    posInQuery = pos2shift + shift_num
    return posInQuery


        
                
   
