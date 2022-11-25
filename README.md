# Kinesis Stream Reader

The script that dumps the content of specified Kinesis stream in to directory so that it can be inspected further on.

### Usage

```
% » python3 kinesis_reader.py -h
usage: kinesis_reader.py [-h] [--dir DIR] stream-name

positional arguments:
  stream-name  the name of the stream to dump records from

options:
  -h, --help   show this help message and exit
  --dir DIR    the name of the directory to store shards content (default value is "records")
```

By default script writes result into `records` directory. It can be changed via argument:
```
% » python3 kinesis_reader.py --dir <target directory> <stream name>
```
The script will then create an output directory if it does not exist or will empty an existing one.

Example
```
% » python3 kinesis_reader.py test
"Records" directory is not empty. Removing files...
Listing shards..
Shard shardId-000000000105 contains 12 records
Writting records...
Shard shardId-000000000106 contains 21 records
Writting records...
Shard shardId-000000000107 contains 16 records
Writting records...
Shard shardId-000000000108 contains 9 records
Writting records...
Shard shardId-000000000109 contains 21 records
Writting records...
Shard shardId-000000000110 contains 38 records
Writting records...
Shard shardId-000000000111 contains 806 records
Writting records...
Shard shardId-000000000112 contains 777 records
Writting records...
Shard shardId-000000000113 contains 812 records
Writting records...
Shard shardId-000000000114 contains 849 records
Writting records...
Shard shardId-000000000115 contains 0 records
Skipping...
Shard shardId-000000000116 contains 23 records
Writting records...
Shard shardId-000000000117 contains 37 records
Writting records...
Shard shardId-000000000118 contains 43 records
Writting records...
Shard shardId-000000000119 contains 33 records
Writting records...
Shard shardId-000000000120 contains 42 records
Writting records...

Complete!
Files written to /records
```

### Dependencies

Following software should be installed on machine:
- [Python](https://www.python.org/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [jq](https://stedolan.github.io/jq/)

You might also need to configure AWS profile before script execution. It can be done, for example, using [awsp](https://github.com/antonbabenko/awsp) utility.
```
awsp <profile>
```
