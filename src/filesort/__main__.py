"""
filesort.__main__

Command line entry point for the filesort package.

The program will identify and classify all the files in the `src` and 
create subdirectories inside `dst`, each of which will hold a certain type of 
files. The files from `src` will be copied to their corresponding 
subdirectories inside `dst`.

Usage
-----
Run the package with:
`python -m filesort src dst` 

where `src` is the source directory and `dst` is the destination directory.
"""
from filesort import scan
from filesort import classify
from filesort import move
from filesort import check
import argparse
import logging
import pathlib as pl
import sys

logging.basicConfig(filename="filesort.log",
                    filemode="w",
                    level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

def argparse_prep() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="FileSort",
                                     description="Program for classifying and sorting files.")
    parser.add_argument("src_dir", type=str)
    parser.add_argument("dst_dir", type=str)
    return parser

def get_valid_args() -> list[str]:
    return sys.argv[1:]

def run(src: pl.Path, dst: pl.Path) -> None:
    logging.info("Scanning for files...")
    scan_ret = scan.scan(src)

    logging.info("Classifying files...")
    classify_ret = classify.classify_many(scan_ret)

    logging.info("Moving files...")
    move.move(classify_ret, dst)

def main() -> None:
    parser = argparse_prep()
    args = parser.parse_args(get_valid_args())
    src = pl.Path(args.src_dir)
    dst = pl.Path(args.dst_dir)
    check.check_both_paths(src, dst)
    logging.info("Arguments valid.")

    logging.info("Running...")
    run(src, dst)
    logging.info("Done.")




if __name__ == "__main__":
    main()
