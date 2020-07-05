"""
The ls command is used in the Linux shell to display directory contents
and file information.
"""

import argparse
import logging.config
import os
import sys


EPILOG = """
List information about the FILEs (the current directory by default).

examples:
  python %(prog)s 
  python %(prog)s name_directory
  python %(prog)s -a name_directory
  python %(prog)s --all name_directory
  python %(prog)s -R name_directory
  python %(prog)s --recursive name_directory
  python %(prog)s -r name_directory
  python %(prog)s --reverse name_directory
  python %(prog)s -d name_directory
  python %(prog)s --directory name_directory
"""

DEFAULT_PATH = "."
LIST_ARGUMENTS = [
    "-a",
    "--all",
    "-R",
    "--recursive",
    "-r",
    "--reverse",
    "-d",
    "--directory",
]

logging.config.fileConfig("logging.conf")
logger = logging.getLogger()


def create_parser():
    """
    The function creates the arguments parser
    :return: The arguments parser
    """
    logger.info("Create parser")
    parser = argparse.ArgumentParser(description=__doc__, epilog=EPILOG)
    parser.add_argument(
        "path",
        nargs="?",
        default=DEFAULT_PATH,
        help="path to the FILEs (the current directory by default)",
    )
    parser.add_argument(
        "-a",
        "--all",
        dest="a_all",
        help="include files with a name starting with a dot"
        " in the list (show hidden files)",
    )
    parser.add_argument(
        "-R",
        "--recursive",
        dest="recursive",
        help="list subdirectories recursively",
    )
    parser.add_argument(
        "-r", "--reverse", dest="reverse", help="reverse order while sorting",
    )
    parser.add_argument(
        "-d",
        "--directory",
        dest="directory",
        help="list directories themselves, not their contents",
    )
    logger.info("Parser created")

    return parser


def ls(path="."):
    """
    Display directory contents and file information.
    :param path: Path to the FILEs (the current directory by default).
    :return: 0 - is successful
    """
    logger.info(f"Executing command 'ls' for path: {path} ")
    names = os.listdir(path)
    for name in names:
        if os.path.isdir(name):
            print(f"{name}/")
            logger.info(f"{name}/")
        else:
            print(name)
            logger.info(name)

    return 0


def a_all(path):
    """
    Show include files with a name starting with a dot
    in the list (show hidden files)
    :param path: Path to the FILEs (the current directory by default).
    :return: 0 - is successful
    """
    logger.info(f"Executing command 'ls -a' for path: {path} ")
    names = [os.curdir, os.pardir] + os.listdir(path)
    for name in names:
        if os.path.isdir(name):
            print(f"{name}/")
            logger.info(f"{name}/")
        else:
            print(name)
            logger.info(name)

    return 0


def recursive(path):
    """
    Show subdirectories recursively
    :param path: Path to the FILEs (the current directory by default).
    :return: 0 - is successful
    """
    logger.info(f"Executing command 'ls -R' for path: {path} ")
    for dir_path, dir_names, file_names in os.walk(path):
        for dir_name in dir_names:
            print(f"{dir_name}/")
            logger.info(f"{dir_name}/")
        for file_name in file_names:
            print(file_name)
            logger.info(file_name)

    return 0


def reverse(path):
    """
    Show reverse order while sorting
    :param path: Path to the FILEs (the current directory by default).
    :return: 0 - is successful
    """
    logger.info(f"Executing command 'ls -r' for path: {path} ")
    names = os.listdir(path)
    names.reverse()
    for name in names:
        if os.path.isdir(name):
            print(f"{name}/")
            logger.info(f"{name}/")
        else:
            print(name)
            logger.info(name)

    return 0


def directory(path):
    """
    Show list directories themselves, not their contents
    :param path: Path to the FILEs (the current directory by default).
    :return: 0 - is successful
    """
    logger.info(f"Executing command 'ls -d' for path: {path} ")
    if os.path.isdir(path):
        print(f"{path}/")
        logger.info(f"{path}/")
    else:
        print(path)
        logger.info(path)

    return 0


def main():
    """
    Main function
    :return: execution status code
    """
    logger.info("**********   Start execution program   **********")

    parser = create_parser()
    args = parser.parse_args()
    path = args.path

    if len(sys.argv) == 1 or (
        len(sys.argv) == 2
        and sys.argv[1]
        and (sys.argv[1] not in LIST_ARGUMENTS)
    ):
        ls(path)
        return 0

    if args.a_all:
        path = args.a_all
        a_all(path)

    if args.recursive:
        path = args.recursive
        recursive(path)

    if args.reverse:
        path = args.reverse
        reverse(path)

    if args.directory:
        path = args.directory
        directory(path)

    logger.info("***********   End  execution program   **********")
    return 0


if __name__ == "__main__":
    exit(main())
