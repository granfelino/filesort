"""Check module.

This module contains code for validating arguments passed to the program.
"""

import pathlib as pl

EXCEPTION_EXIST_MSG = "The path does not exist"
EXCEPTION_DIR_MSG = "The path does not point to a directory"
EXCEPTION_EMPTY_MSG = "The directory does not contain any files"
class PathInvalidError(Exception):
    """
    Raised when a path passed as an argument to the program is invalid.

    Parameters
    ----------
    message : str
        A message displayed with the error.
    path : str
        A path which triggered the error.
    """
    def __init__(self, message: str, path: str):
        super().__init__(message + " ---> '" + path + "'")

def path_has_files(path: pl.Path) -> bool:
    """Checks if the path contains any files.

    Parameters
    ----------
    path : pl.Path
        A path pointing to the directory.
    
    Returns
    -------
    bool
        True if any files are present in the given path.
    """

    for el in path.iterdir():
        if el.is_file():
            return True
    return False

def check_path(path: pl.Path, check_files: bool = True) -> None:
    """Function aggregating the path checks.

    This function returns nothing.

    Parameters
    ----------
    path : pl.Path
        Path being checked.
    check_files : bool, default=True
        Flag if the function should check if any files are present.

    Raises
    ------
    PathInvalidError
        If: 
        - the path does not exist
        - the path points to a file
        - there are no files in the directory pointed to by the path
    """

    if not path.exists():
        raise PathInvalidError(EXCEPTION_EXIST_MSG, str(path))

    if not path.is_dir():
        raise PathInvalidError(EXCEPTION_DIR_MSG, str(path))

    if not check_files:
        return

    if not path_has_files(path):
        raise PathInvalidError(EXCEPTION_EMPTY_MSG, str(path))

def check_both_paths(src: pl.Path, dst: pl.Path) -> None:
    """Function to check the source and the destination path.

    This function returns nothing.

    Parameters
    ----------
    src : pl.Path
        The source path.
    dst : pl.Path
        The destination path.

    Raises
    ------
    PathInvalidError
        If: 
        - the path does not exist
        - the path points to a file
        - there are no files in the directory pointed to by the path
    """

    check_path(src)
    check_path(dst, check_files=False)
