import argparse
import json
import tempfile
import os

STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_data():
    if not os.path.exists(STORAGE_PATH):
        return {}
    with open(STORAGE_PATH, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}


def put(key, value):
    data = get_data()

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(STORAGE_PATH, 'w') as f:
        f.write(json.dumps(data))


def get(key):
    data = get_data()
    return data.get(key)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Key', action='store', dest='key', required=True)
    parser.add_argument('--val', help='Value', action='store', dest='val')

    args = parser.parse_args()

    if args.key and args.val:
        put(args.key, args.val)
    elif get(args.key) is not None:
        print(*get(args.key), sep=", ")
    elif get(args.key) is None:
        print("None")