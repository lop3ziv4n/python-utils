import os

from PIL import Image


def compress(path):
    for filename in os.listdir(path):
        name, extension = os.path.splitext(path + filename)
        if extension in [".jpg", ".jpeg", ".png"]:
            print(path + filename)
            picture = Image.open(path + filename)
            picture.save(path + "compressed_" + filename, optimize=True, quality=60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compress image files")
    parser.add_argument("-p", "--path",
                        help="Indicate the location of the files")

    # parse arguments
    args = parser.parse_args()
    path = args.path

    compress(path)
