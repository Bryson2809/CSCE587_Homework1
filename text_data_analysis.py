import numpy as np
import pandas as pd
import os
import csv

file = open('/mnt/c/CSCE587/Homework1/report.csv', 'w')
writer = csv.writer(file)
fields = ['article-id', 'no-words', 'no-paragraphs']
writer.writerow(fields)
i = 0
directory = os.getcwd() + "/BBC-textdata/bbc"
for dir in os.scandir(directory):
    if dir.is_dir() :
        for filename in os.listdir(dir.path):
            with open(os.path.join(dir.path, filename), 'r') as f:
                i += 1
                data = f.read()
                words = len(data.split())
                lines = len(data.split("\n"))
                row = [i, words, lines]
                writer.writerow(row)
file.close()
