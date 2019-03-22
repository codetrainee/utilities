import os
import re

path = "."
file_names = os.listdir(path)


def rename_file(file_name):
    # Construct a regex
    regex = re.compile(r'(?<=[AB]{1}-)(\d+)(?=-TAB.+)')
    # Pad the matched number with 3 digits
    new_name = regex.sub(lambda m: m.group(1).zfill(3), file_name)
    return new_name


files = os.listdir(path)

for file in files:
    old_name = os.path.join(path, file)
    new_name = os.path.join(path, rename_file(file))
    os.rename(old_name, new_name)
