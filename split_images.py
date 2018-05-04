import os
import csv

from PIL import Image

output = 'decor_split'

with open('decor.csv') as csvfile:
    label_reader = csv.reader(csvfile, delimiter=',')
    next(label_reader)  # skipping header
    for row in label_reader:
        if row[5] == 'product':
            path = os.path.join(output, row[3])
            if not os.path.exists(path):
                os.makedirs(path)
            img = Image.open(row[6]).convert("RGB")
            dst = os.path.join(output, row[3], row[6].replace('.png', '.jpg'))
            img.save(dst)
