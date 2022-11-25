import json
import os
import argparse


def list_shards(stream_name):
    print('Listing shards.. ')
    with os.popen('aws kinesis list-shards --stream-name ' + stream_name) as f:
        data = json.loads(f.read())
        return list(map(lambda shard: shard['ShardId'], data['Shards']))


def get_iterator(stream_name, shard_id):
    with os.popen('aws kinesis get-shard-iterator --stream-name ' + stream_name +
                  ' --shard-id ' + shard_id +
                  ' --shard-iterator-type TRIM_HORIZON') as f:
        data = json.loads(f.read())
        return data['ShardIterator']


def get_records(iterator):
    with os.popen('aws kinesis get-records --shard-iterator ' + iterator) as f:
        data = json.loads(f.read())
        return list(map(lambda shard: shard['Data'], data['Records']))


def store_into_file(dir_name, shard_name, records):
    print('Shard ' + shard_name + ' contains ' + str(len(records)) + ' records')
    if len(records) > 0:
        print('Writting records...')
        with open(dir_name + "/" + shard_name + ".txt", "w") as file:
            for record in records:
                with os.popen('echo ' + record + ' | base64 -d | jq ') as std:
                    output = std.read()
                    file.write(output)
    else:
        print('Skipping...')


def create_or_empty_directory(dir_name):
    if not os.path.exists(dir_name):
        print('Creating "' + dir_name + '" subdirectory to store result..')
        os.mkdir(dir_name)
    else:
        print('"' + dir_name + '" directory is not empty. Removing files...')
        for file_name in os.listdir(dir_name):
            file = dir_name + '/' + file_name
            if os.path.isfile(file):
                os.remove(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'stream-name', help='the name of the stream to dump records from')
    parser.add_argument(
        '--dir', help='the name of the directory to store shards content (default value is "records")')
    args = parser.parse_args()

    dir = args.dir if args.dir else 'Records'
    stream_name = getattr(args, 'stream-name')

    create_or_empty_directory(dir)

    shards = list_shards(stream_name)
    for shard in shards:
        iterator = get_iterator(stream_name, shard)
        records = get_records(iterator)
        store_into_file(dir, shard, records)

    print('\nComplete!')
    print('Files written to ' + os.path.abspath(dir))
