import pandas as pd
import cv2
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


def remove_irregulars(labels):
    """
    Removes all rows in dataframe that have a 1 in the irregular column
    :param labels:
    :return:
    """
    palm_df = labels.copy()
    return palm_df[palm_df.irregularities < 1]


def create_folder(path):
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


def convert_image(img_name, i, input_size, input_images_path, output_images_path):
    print(f'{i}/{input_size}')
    try:
        img = cv2.imread(f'{input_images_path}/{img_name}', cv2.IMREAD_GRAYSCALE)  # turn to greyscale
        img = cv2.resize(img[:, 200:-200], (224, 224))  # resize the image
        img_converted = cv2.rotate(img, cv2.ROTATE_180)  # rotate image so fingers face upward

        cv2.imwrite(f'{output_images_path}/{img_name}', img_converted)

    except IOError:
        print(f"Converted file {img_name} not saved.")
    else:
        print(f"Converted file {img_name} saved.")


def main():
    label_file_name = "../data/HandInfo.csv"
    input_images_path = "../data/PalmImages"
    output_images_path = "../data/resized-images"

    label_df = pd.read_csv(label_file_name)

    palm_df = find_palms(label_df)
    palm_df = remove_irregulars(palm_df)

    create_folder(input_images_path)
    create_folder(output_images_path)
    fill_palm_folder(palm_df)

    palm_df.to_csv("../data/PalmInfo.csv")

    img_nums = len(os.listdir(input_images_path))

    for i, img_name in enumerate(os.listdir(input_images_path)):
        convert_image(img_name, i + 1, img_nums, input_images_path, output_images_path)


if __name__ == "__main__":
    main()
