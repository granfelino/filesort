"""Scanning module for file detection.

The module contains a function for scanning a directory.
"""

import pathlib as pl

def scan(path: pl.Path) -> list[pl.Path]:
    """Function for scanning a directory for files.

    Parameters
    ----------
    path : pl.Path
        Path pointing to the directory.

    Returns
    -------
    list[pl.Path]
        List of paths pointing to detected files.
    """

    return [x for x in path.iterdir() if x.is_file()]
