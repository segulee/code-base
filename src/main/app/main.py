# -*- coding: UTF-8 -*-
# Python3.7

# *******************************************************
#
#   brief       main.py
#   author      segulee@gmail.com
#
# *******************************************************

import sys
import logging
import argparse

log = logging.getLogger("app.main")


def something():
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="debug mode",
        required=False,
    )
    args = parser.parse_args()
    if args.debug:
        pass

    log.info("run main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
