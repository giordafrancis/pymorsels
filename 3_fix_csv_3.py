from argparse import ArgumentParser
import csv 

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument("--in-delimiter", dest="delimiter")
parser.add_argument("--in-quote", dest="quote")
args = parser.parse_args()

with open(args.old_filename, newline="") as old_file:
    arguments = {}
    if args.delimiter:
        arguments['delimiter'] = args.delimiter
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delimiter and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0) #iter back to pos 0
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline="") as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)
    
