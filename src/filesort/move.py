"""Moving module.

Contains a function for copying files.
"""

import logging
import pathlib as pl
import shutil as sh

logger = logging.getLogger(__name__)

def move(classified: dict[str, list[pl.Path]], dst_path: pl.Path) -> None:
    """Copies files from their source paths to a classified destination.

    This function returns nothing.

    Parameters
    ----------
    classified : dict[str, list[pl.Path]]
        A dictionary with "type"-to-"file path list", containing classified
        paths.
    dst_path : pl.Path
        A pathlib.Path object with the destination path.
    """

    for t, src_paths in classified.items():
        if len(src_paths) == 0:
            continue

        tmp_dst_dir = dst_path / t
        tmp_dst_dir.mkdir()
        logging.info(f"Created directory '{t}'.")

        for src in src_paths:
            tmp_dst_path = tmp_dst_dir / src.name
            sh.copyfile(src, tmp_dst_path)
            logging.info(f"Copied file: '{src.name}'.")
