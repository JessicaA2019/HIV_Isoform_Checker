# HIV Isoform Checker
### Overview
This package is a module in the [APHIX pipeline][APHIX]. HIV_Isoform_Checker takes a .gtf file of preliminarily filtered HIV transcripts and filters them to include only correctly assigned transcripts using the following filters. It also calculates the usage counts and percentages for each isoform type, donor site, acceptor site, and pairwise splice site combination.
- FILTER 1: only include class codes =, J, and m
- FILTER 2: only include samples with end values >= min_end_bp and
           start values <= max_start_bp
- FILTER 3: get rid of any samples with read errors/small gaps
- FILTER 4: keep only correct Env samples
- FILTER 5: keep only correct Nef samples(long samples added to possible_misassigned)  
- FILTER 6: keep only correct Rev samples(long samples added to possible_misassigned)  
- FILTER 7: keep only correct Tat samples(long samples added to possible_misassigned)   
- FILTER 8: keep only correct Vif samples
- FILTER 9: keep only correct Vpr samples
- FILTER 10:  check possible_misassigned for fully spliced then partial splice compatibility (tat -> rev -> nef - > vif -> vpr -> unspliced_tat -> env)

> Note: This code currently relies on a very specific setup of the gtf file to work properly. The note must be in the order designated in the [].
transcript entry = ref genome, analysis_pathway, transcript, start, end, ".", "+", ".", [transcript id; gene id; gene_name; xloc; ref_gene_id; contained_in; cmp_ref; class_code; tss_id]
>exon entry = ref genome, analysis_pathway, exon, start, end, ".", "+", ".", [transcript id; gene id; exon number]

******************
## Installation
### Quick Install
```bash
pip install HIV_Isoform_Checker
```
### Manual Install
```bash
git clone https://github.com/JessicaA2019/HIV_Isoform_Checker.git 
cd HIV_Isoform_Checker
python setup.py install
```
### Dependencies
Some dependencies currently do not install with Chimera_Buster. Please pip install the following dependencies:
* mappy
* regex
* argparse

### Testing
To test if the installation was successful run the following command with the test files provided:
```bash
HIV_Isoform_Checker HIC_test.gtf HIV_Isoform_Checker_test NL43.fa
 ```
 ******************
## Usage
```bash
HIV Isoform Checker [options] input_file_name output_file_prefix ref_file
```
### Inputs
To run the pipeline the following input files are required:
| Input | Description |
| ------ | ------ |
|input_file_name  |    Designates .gtf to be filtered. This is required.|
|output_file_prefix  |  Designates output file prefix. This is required.|
| ref_file | The location of the reference genome fasta file.|

The following input files are optional:
| Arguement | Function |
| ------ | ------ |
|-h, --help |  Prints help message to terminal. |
|-g value, --gap value |  Sets gap tolerance. If a read has a gap longer than this value that is not associated with known splice sites, the read will be filtered out as a sequencing error. The default value is 15. |
|-a value, --startBP value |  Sets maximum starting bp in order to insure the presence of the first exon and by proxy a full read. Default is 700. |
|-z value, --endBP value |  Sets minimum ending bp in order to insure the presence of the last exon and by proxy a full read. Default is 9500. |
|-l value, --lengthFS value |  Sets maximum fully spliced transcript length. If a read is longer than this value, then it will be considered partial spliced. This is based off HIV-1 references without any major insertions or deletions. If your sequences have larger deletions (ex: deltaENV or deltaMA) or insertions (ex: multiple markers such as eGFP), this value may need to be adjusted. Default is 2500. |
|-n value, --NCE value | When set to True, the output csv file will have y/n columns for the precence of NCEs. Default is False.|

### Outputs
 The main output files created by the pipeline are:
| Output | Description |
|--------|-------------|
| {output_file_prefix}.csv | A csv containing the sample ID, cluster size, isoform ID, starting and ending base pair, gffcompare class code, exon boundaries, coverage length, size normalized counts, precence of NCEs (optional), and any additional notes for each sample. |
| {output_file_prefix}_altered.txt | A list of all sample IDs with altered exons to fill in small gaps. |
| {output_file_prefix}_pass.txt | A list of all sample IDs that passed all filters. |
| {output_file_prefix}_fail.txt | A list of all sample IDs that failed one or more filters. |
| {output_file_prefix}_isoform_counts.csv | A csv of the usage counts and percentages for each isoform type. |
| {output_file_prefix}_splice_site_usage.csv | A csv of the the usage counts and percentages for each donor site, acceptor site, and pairwise splice site combination. |
| {output_file_prefix}_ref_coordinates.txt | A list of splice site and CDS coordinates for given reference. |
| {output_file_prefix}.log | A log of the arguments given to the script. |

**************************
## Help
For issues or bugs, please report them on the [issues page][issues]. 

## License

MIT - Copyright (c) 2024 Jessica Lauren Albert


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [APHIX]: <https://github.com/JessicaA2019/APHIX>
   [issues]: <https://github.com/JessicaA2019/HIV_Isoform_Checker/issues>