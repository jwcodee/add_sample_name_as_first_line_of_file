import sys
import argparse
import re

def Parser():
  the_parser = argparse.ArgumentParser(description="add sample name as first line of a tab file")
  the_parser.add_argument('--input', required=True, action="store", type=str, help="input tab file")
  the_parser.add_argument('--output', required=True,  action="store", type=str, help="output file")
  the_parser.add_argument('--sample', required=True, action="store", type=str, help="sample name to add as the first line of input file")
  args = the_parser.parse_args()
  return args

args=Parser()

sample_name = re.sub('[_12]*.fastq.gz', '', args.sample.rstrip().lstrip())

with open(args.input) as input:
	with open(args.output, 'w') as output:
		output.write(sample_name+"\n")
		for line in input:
			output.write(line)


