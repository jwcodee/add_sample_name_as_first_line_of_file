import sys
import argparse
import re

def Parser():
  the_parser = argparse.ArgumentParser(description="add label to first line of file")
  the_parser.add_argument('--input', required=True, action="store", type=str, help="input file")
  the_parser.add_argument('--output', required=True,  action="store", type=str, help="output file path")
  the_parser.add_argument('--label', required=True, action="store", type=str, help="label to add in the first line")
  args = the_parser.parse_args()
  return args

args=Parser()
#input=open(args.input)
#output=open(args.output, 'w')

#print >> output, args.label
#print >> output, input

sample_name = re.sub('(_1.fastq.gz|_2.fastq.gz|.fastq.gz)', '', args.label.rstrip().lstrip())

with open(args.input) as input:
	with open(args.output, 'w') as output:
		output.write(sample_name+"\n")
		for line in input:
			output.write(line)

#input.close()
#output.close()
