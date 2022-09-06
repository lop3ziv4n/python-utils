import os
import time


def remove(path, days=30):
    limit = time.time() - days * 86400
    for filename in os.listdir(path):
        path_file = os.path.join(path, filename)
        if os.path.isfile(path_file) and os.stat(path_file).st_mtime < limit:
            print(path_file)
            os.remove(path_file)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Remove files after days")
    parser.add_argument("-p", "--path",
                        help="Indicate the location of the files")
    parser.add_argument("-d", "--days",
                        help="limit in days to delete, example 30",
                        default=30)

    # parse arguments
    args = parser.parse_args()
    path = args.path
    days = int(args.days)

    remove(path, days)
