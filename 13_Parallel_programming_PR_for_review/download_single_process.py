import argparse
import io
import os
import sys

from datetime import datetime
from PIL import Image
from urllib.request import urlopen
from urllib.parse import urlparse


EPILOG = """
Console utility for multithreaded file downloading, their subsequent
processing and saving to the local file system. File processing consists
in generating a preview of a given maximum size (while maintaining
aspect ratio) and transcoding to JPEG format

examples:
  python %(prog)s urllist.txt --dir=thumbnails/ --threads=4 --size=128x128
"""

DEFAULT_DIRECTORY = "/"
DEFAULT_THREADS = 1
DEFAULT_SIZE = "100x100"


class BaseArgumentParser(argparse.ArgumentParser):
    """
    Base class for arguments parsing
    """

    def __init__(
        self, *args, formatter_class=argparse.RawTextHelpFormatter, **kwargs
    ):
        super(BaseArgumentParser, self).__init__(
            *args, formatter_class=formatter_class, **kwargs
        )


def create_parser():
    """
    The function creates the arguments parser
    :return: The arguments parser
    """
    parser = BaseArgumentParser(description=__doc__, epilog=EPILOG)
    parser.add_argument(
        "filename", nargs="+", help="set URL list file",
    )
    parser.add_argument(
        "--dir",
        dest="directory",
        default=DEFAULT_DIRECTORY,
        type=str,
        help="set output directory",
    )
    parser.add_argument(
        "--threads",
        dest="threads",
        default=DEFAULT_THREADS,
        type=int,
        help="set number of threads",
    )
    parser.add_argument(
        "--size",
        dest="size",
        default=DEFAULT_SIZE,
        type=str,
        help="set output image sizes",
    )

    return parser


def log_info(msg):
    """
    Log an info message to stdout
    :param msg: message string
    """
    sys.stdout.write(f"[Info] {datetime.now()}: {msg}\n")
    sys.stdout.flush()


def log_error(msg):
    """
    Log an error message to stdout
    :param msg: message string
    """
    sys.stdout.write(f"[Error] {datetime.now()}: {msg}\n")
    sys.stdout.flush()


def download_file(url):
    """
    Download file from URL
    :param url: URL to source file
    :return: file content if download succeed otherwise 1
    """
    try:
        with urlopen(url) as response:
            if response.status != 200:
                log_error(
                    f"Downloading from {url} failed: "
                    f"{response.status} {response.reason}"
                )
                return 1

            return response.read()

    except Exception as exception:
        log_error(exception)
        return 1


def scale_image(input_image, width=None, height=None):
    """
    The scaling method takes into account the aspect ratio of the picture.
    :param input_image: input image
    :param width: output image width
    :param height: output image height
    :return: modified image
    """
    w, h = input_image.size

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        raise RuntimeError("Width or height required!")

    input_image.thumbnail(max_size, Image.ANTIALIAS)

    return input_image


def output_directory(path):
    """
    # Create output directory
    :param path: name output directory
    :return: full path for output directory
    """
    output_dir = os.path.join(os.getcwd(), path)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir, mode=0o777)

    return output_dir


def gen_name():
    """
    Generate new file name
    :return: new file name
    """
    n = 0
    while True:
        yield "%.5d.jpeg" % (n)
        n += 1


def url_validator(url):
    """
    URL address check
    :param url: URL address
    :return: True if URL address is valid, otherwise False
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False



def main():
    """
    Main function single-process implementation
    :return: status code
    """

    parser = create_parser()
    args = parser.parse_args()

    log_info(f"Start execution code.")
    filename = args.filename[0]
    output_dir = output_directory(args.directory)
    threads = args.threads
    width, height = args.size.split("x")
    new_file_name = gen_name()

    try:
        with open(filename, "r") as file:
            urls = file.readlines()
            for url in urls:
                if url_validator(url):
                    image_data = download_file(url)
                    input_image = Image.open(io.BytesIO(image_data))
                    output_image = scale_image(
                        input_image, int(width), int(height)
                    )
                    file_name = next(new_file_name)
                    output_image.save(f"{output_dir}/{file_name}", type="jpeg")
                    log_info(f"File processing completed. A new file was created: {file_name}")

    except (OSError, IOError) as err:
        log_error(f"Unable to read the file {filename}. Reason: {err}")

    return 0


if __name__ == "__main__":
    exit(main())
