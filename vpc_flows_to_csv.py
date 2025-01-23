#!/usr/bin/env python3.11
# -*- coding: utf-8 -*-
# Author: David Manouchehri

import csv
import gzip
import sys
import glob
import os

# All possible fields as per the documentation
ALL_FIELDS = [
    'version', 'account-id', 'interface-id', 'srcaddr', 'dstaddr', 'srcport',
    'dstport', 'protocol', 'packets', 'bytes', 'start', 'end', 'action',
    'log-status', 'vpc-id', 'subnet-id', 'instance-id', 'tcp-flags', 'type',
    'pkt-srcaddr', 'pkt-dstaddr', 'region', 'az-id', 'sublocation-type',
    'sublocation-id', 'pkt-src-aws-service', 'pkt-dst-aws-service',
    'flow-direction', 'traffic-path', 'reject-reason',
]

def process_flow_logs(directory):
    # List to store all records
    all_records = []
    
    # Process each .log.gz file in the directory and its subdirectories
    for filepath in glob.glob(os.path.join(directory, '**/*.log.gz'), recursive=True):
        try:
            with gzip.open(filepath, 'rt') as f:
                # Read header line
                header = f.readline().strip().split()
                
                # Create a mapping of field positions
                field_positions = {field: pos for pos, field in enumerate(header)}
                
                # Process each line
                for line in f:
                    values = line.strip().split()
                    record = {field: '' for field in ALL_FIELDS}  # Initialize with empty strings
                    
                    # Map values to their corresponding fields
                    for field in header:
                        if field in field_positions:
                            pos = field_positions[field]
                            if pos < len(values):
                                # Convert '-' to empty string
                                value = values[pos]
                                record[field] = '' if value == '-' else value
                    
                    all_records.append(record)
                    
        except Exception as e:
            print(f"Error processing file {filepath}: {str(e)}", file=sys.stderr)

    # Sort records by start time
    all_records.sort(key=lambda x: int(x['start']) if x['start'] else 0)

    # Write to stdout as CSV
    writer = csv.DictWriter(sys.stdout, fieldnames=ALL_FIELDS)
    writer.writeheader()
    writer.writerows(all_records)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>", file=sys.stderr)
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    process_flow_logs(directory)
