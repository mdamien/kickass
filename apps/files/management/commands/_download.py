import json

files = json.load(open('files.json'))
for f in files:
    print(f['download_link'])
