import pandas as pd
import os
from shutil import copy


def find_palms(labels):
    """
    Remove all rows in dataframe that are not palm files
    :param labels:
    :return:
    """
    palm_df = labels.copy()
    return palm_df[palm_df.aspectOfHand.str.contains("palmar")]


def create_palm_folder():
    path = "../data/PalmImages"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Created the directory %s " % path)


def fill_palm_folder(df):

    for file_name in df.imageName:
        src = "../data/Hands/" + file_name
        dst = "../data/PalmImages"
        copy(src, dst)


def main():
    label_file_name = "../data/HandInfo.csv"
    label_df = pd.read_csv(label_file_name)

    palm_df = find_palms(label_df)
    create_palm_folder()
    fill_palm_folder(palm_df)

    palm_df.to_csv("../data/PalmInfo.csv")


if __name__ == "__main__":
    main()
