from argparse import ArgumentParser
import csv 

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument("--in-delimiter", dest="delimiter", default="|")
parser.add_argument("--in-quote", dest="quote", default='"')

args = parser.parse_args()

"""
Notice in both of these open calls we've been specifying newline as an empty string. The reason that the CSV module writes \r\n line endings to our file automatically, but Python will automatically take all LF endings (\n) and convert them to CRLF endings (\r\n) on Windows systems. So when writing CSV files in Python 3, using newline='' is recommended. The newline='' in the reading open isn't necessary because the CSV module handles either \r\n and \n as line endings, but I think it's nice to be consistent when opening files that are meant to represent CRLF-ended delimited data.

Another thing I'll note about the csv reader and writer objects is that the writer's writerows method takes an iterable and the reader object is an iterable. So if we nested our with statements, we could actually write directly while reading but i/o filename has to be different so prefer not to do this. Consider if filesize is big

We've added two more arguments to our argument parser and both are optional (the default for arguments specified with --)

bonus 3 on new file as covers csv detection(sniff)

"""
with open(args.old_filename, newline='') as old_file: 
    rows = list(csv.reader(old_file, delimiter= args.delimiter, quotechar= args.quote)) 
with open(args.new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)