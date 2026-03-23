import json

DATA_FILE = "data.log"


def append_record(record):
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        position = f.tell()
        f.write(json.dumps(record) + "\n")
    return position


def read_all():
    records = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                records.append(json.loads(line))
    except FileNotFoundError:
        pass

    return records