#import numpy as np
#import pandas as pd
import csv

try:
    file = open('data.csv')
    csvreader = csv.reader(file)

    header = next(csvreader)
    #print(header)

    rows = []
    for row in csvreader:
        rows.append(row)
    #print(rows)

except:
    print("An error occured")



