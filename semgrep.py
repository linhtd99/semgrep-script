import argparse
import os
from pathlib import Path
from app import *


# Parse args ('-z' for location of zip file)
# Return location of zip file and project's name
def get_from_cli():
    parser = argparse.ArgumentParser()

    parser.add_argument('-z', '--zipfile',
                        required=True,
                        help="Project's ZIP file")
    args = parser.parse_args()

    if not os.path.basename(args.zipfile).endswith('.zip'):
        print("Not in ZIP format!\nExiting...")
        exit()
    elif not os.path.isfile(args.zipfile):
        print("File does not exist!\nExiting...")
        exit()
    else:
        return args.zipfile, Path(args.zipfile).stem


if __name__ == '__main__':
    zipfile, prj_name = get_from_cli()
    test = Application(zipfile, prj_name)
    print(test.scan())
