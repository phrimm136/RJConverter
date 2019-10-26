import argparse as arg
import os
import re
import mir.dlsite.api as dl


def rj_convert(directory: str):
    """Convert name of directories with RJ code to its name."""
    subdirs = [directory + x + '/' for x in os.listdir(directory) if os.path.isdir(directory + x)]
    rj_regex = re.compile("(RJ|rj)[0-9]{6}")
    for subdir in subdirs:
        regex_result = rj_regex.search(subdir)
        if regex_result is not None:
            rj = re.sub(r"rj", "RJ", regex_result.group())
            name = dl.fetch_work(rj).name
            print("{} -> {}".format(subdir, name))
            os.rename(subdir, os.path.join(directory, name))
        else:
            print("Ignore {}".format(subdir))


def rj_convert_recursive(directory: str):
    """Convert like the above function bu recursively."""
    subdirs = [directory + x + '/'
               for x in os.listdir(directory)
               if os.path.isdir(directory + x) and x[0] != '.']
    rj_regex = re.compile("(RJ|rj)[0-9]{6}")
    queue = []
    for subdir in subdirs:
        regex_result = rj_regex.search(subdir)
        if regex_result is not None:
            rj = re.sub(r"rj", "RJ", regex_result.group())
            name = directory + dl.fetch_work(rj).name
            print("{} -> {}".format(subdir, name))
            os.rename(subdir, os.path.join(directory, name))
            queue.append(name)
        else:
            queue.append(subdir)
    while queue:
        subdir = queue.pop(0)
        print("Entering directory {}".format(subdir))
        rj_convert_recursive(subdir)
    print("Leaving directory  {}".format(directory))


if __name__ == "__main__":
    parser = arg.ArgumentParser()
    parser.add_argument("-r", "--recursive",
                        help="recursively convert directories",
                        action="store_true")
    parser.add_argument("directory",
                        help="to convert name of its subdirectories")
    args = parser.parse_args()
    if args.recursive:
        rj_convert_recursive(os.path.abspath(args.directory) + '/')
    else:
        rj_convert(os.path.abspath(args.directory) + '/')
