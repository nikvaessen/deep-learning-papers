################################################################################
# This script will parse all the summaries written in this repository and
# update the main README.md file accordingly.
#
# Usage: python update_readme.py
#
# Author: Nik Vaessen
################################################################################

import os
import re
import datetime

from pathlib import Path

################################################################################
# Implement functionality of script


def main():
    # set working directory to root of path
    script_path = Path(os.path.abspath(__file__))
    root_dir = script_path.parent.parent.as_posix()

    os.chdir(root_dir)

    # parse all the summaries
    raise NotImplemented()


if __name__ == '__main__':
    main()
