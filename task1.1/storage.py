import argparse, os, json, tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--key', help=' random text')
parser.add_argument('--val', help='random_text')
args = parser.parse_args()

STORAGE_PATH = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(STORAGE_PATH):
    if args.val:
        with open(STORAGE_PATH, 'r') as f:
            m = json.load(f)
            if args.key in m:
                m[args.key].append(args.val)
            else:
                m.update({args.key: [args.val]})
        with open(STORAGE_PATH, 'w') as f:
            json.dump(m, f)
    else:
        try:
            with open(STORAGE_PATH, 'r') as f:
                m = json.load(f)
                if m[args.key] == None:
                    print(None)
                if len(m[args.key]) > 1:
                    print(', '.join(m.get(args.key)))
                else:
                    print(*m.get(args.key))
        except:
            print(None)
else:
    d = {}
    with open(STORAGE_PATH, 'w') as f:
        if args.val:
            d = {args.key: [args.val]}
            json.dump(d, f)
        else:
            d = {args.key: None}
            print(None)