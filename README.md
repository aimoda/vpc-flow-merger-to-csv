# VPC Flow Logs Processor

A Python script that processes multiple AWS VPC Flow Log files and combines them into a single CSV output. This tool is particularly useful for analyzing VPC Flow Logs across multiple time periods or VPCs.

## Features

- Processes gzipped VPC Flow Log files (`.log.gz`)
- Recursively searches through directories
- Combines multiple log files into a single CSV output
- Maintains all possible VPC Flow Log fields
- Sorts entries by timestamp
- Handles different field orders across files
- Converts `-` symbols to empty strings for better data analysis

## Requirements

- Python 3.11 or higher
- No external dependencies required (uses only Python standard library)

## Installation

Clone this repository:

```bash
git clone git@github.com:aimoda/vpc-flow-merger-to-csv.git
cd vpc-flow-logs-processor
```

## Usage

```bash
python3.11 vpc_flow_logs_processor.py /path/to/logs/directory > output.csv
```

### Example

Input file structure:
```
/logs/
  ├── 123456789010_vpcflowlogs_us-east-1_fl-1235b8ca123456789_20250123T0925Z_5667961a.log.gz
  ├── 123456789010_vpcflowlogs_us-east-1_fl-1235b8ca123456789_20250123T0930Z_5667961a.log.gz
  └── subdir/
      └── 123456789010_vpcflowlogs_us-east-1_fl-1235b8ca123456789_20250123T0935Z_5667961a.log.gz
```

Run the script:
```bash
python3.11 vpc_flow_logs_processor.py /logs > combined_flows.csv
```

## Output Format

The script outputs a CSV file with the following fields:

| Field | Description |
|-------|-------------|
| version | VPC Flow Logs version |
| account-id | AWS account ID |
| interface-id | Network interface ID |
| srcaddr | Source IP address |
| dstaddr | Destination IP address |
| srcport | Source port |
| dstport | Destination port |
| protocol | IANA protocol number |
| packets | Number of packets |
| bytes | Number of bytes |
| start | Start time (Unix seconds) |
| end | End time (Unix seconds) |
| action | ACCEPT or REJECT |
| log-status | Logging status |
| vpc-id | VPC ID |
| subnet-id | Subnet ID |
| instance-id | EC2 instance ID |
| tcp-flags | TCP flags |
| type | Traffic type |
| pkt-srcaddr | Packet source address |
| pkt-dstaddr | Packet destination address |
| region | AWS region |
| az-id | Availability Zone ID |
| sublocation-type | Sublocation type |
| sublocation-id | Sublocation ID |
| pkt-src-aws-service | Source AWS service |
| pkt-dst-aws-service | Destination AWS service |
| flow-direction | Traffic direction |
| traffic-path | Traffic path |
| reject-reason | Rejection reason |

## Error Handling

- Error messages are written to stderr
- The script continues processing even if individual files fail
- Invalid files are skipped with error messages

## Limitations

- Processes only gzipped VPC Flow Log files
- Requires sufficient memory to hold all records for sorting
- All fields are treated as strings in the output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

David Manouchehri

## Support

For support, please open an issue in the GitHub repository.