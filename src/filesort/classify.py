"""Classication module.

Contains functions used to classify identified files.
"""

import logging
import pathlib as pl
from filesort import constants as cs

logger = logging.getLogger(__name__)

def classify_single(file: pl.Path) -> str:
    """Classifies a single file.

    Parameters
    ----------
    file : pl.Path
        Path pointing to the file being classified.

    Returns
    -------
    str
        File classification.

    See Also
    --------
    classify_many
    """

    suffix = file.suffix
    ret = ""
    for ext_type, ext_set in cs.ALL_EXTENSIONS_SETS.items():
        if suffix in ext_set:
            ret = ext_type
            break

    logger.info(f"Classified {file.name} as {ext_type}.")
    return ret

def classify_many(files: list[pl.Path]) -> dict[str, list[pl.Path]]:
    """Classifies many files.

    If a file is not recognized it is skipped.

    Parameters
    ----------
    files : list[pl.Path]
        List of pathlib.Path paths pointing to files to be classified.

    Returns
    -------
    dict[str, list[pl.Path]]
        A dictionary with "type"-to-"file path list", containing classified
        paths.

    See Also
    --------
    classify_single
    """

    ret: dict[str, list[pl.Path]] = {k : [] for k in cs.ALL_EXTENSION_TYPES}
    for f in files:
        tmp_ret = classify_single(f)
        if tmp_ret == "":
            print(f"{f} is not a known file. Skipping.")

        ret[tmp_ret].append(f)
    return ret
