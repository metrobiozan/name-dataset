import copy
import json
import operator
import os
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Optional



def _read_json_from_zip(zip_file):
    with zipfile.ZipFile(zip_file) as z:
        with z.open(z.filelist[0]) as f:
            return json.load(f)

def _write_json_to_zip(zip_file, json_data):
    with zipfile.ZipFile(zip_file, "w") as z:
        with z.open(zip_file.replace(".zip", ".json"), "w") as c:
            c.write(json.dumps(json_data, indent=2).encode("utf-8"))


def filter_names(large_names, n=2000):
    small_names = {}
    for n in large_names.keys():
        fno = large_names[n]
        if "rank" in fno and "US" in fno["rank"] and fno["rank"]["US"] < 2000:
            small_names[n] = fno
            print(n)
    return small_names



first_names_original = _read_json_from_zip("first_names_original.zip")
first_names = filter_names(first_names_original, 2000)
_write_json_to_zip("first_names.zip", first_names)

last_names_original = _read_json_from_zip("last_names_original.zip")
last_names = filter_names(first_names_original, 2000)
_write_json_to_zip("last_names.zip", first_names)
