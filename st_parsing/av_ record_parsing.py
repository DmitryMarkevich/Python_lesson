import csv
from av_site_parsing import array_
import pandas as pd


def writer_csv(func):
    """
    The function takes data and writes it to a csv file.

    """
    with open("new_st_1.csv", "w", encoding="utf-8", newline="") as file_csv:
        w = csv.writer(file_csv, delimiter=',')
        for i in func():
            w.writerow(i)


def writer_json():
    """
    The function reads data from csv file and writes this data to json file.

    """
    df = pd.read_csv("file.csv", sep=',')
    df.to_json('file2.json')


def main():
    writer_csv(array_)
    writer_json()


main()
