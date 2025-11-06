import pathlib as pl
from filesort import constants as cs

TEST_DIR_SCAN = "scan_test"
TEST_SUBDIR_NAME = "subdir"
TEST_SUBDIRS_NUM = 3

def create_dummy_files_scan(path: pl.Path) -> pl.Path:
    """Creates temporary dummy directories and files for a scanning test.

    Takes one file extension from each file category from `constants` 
    module and makes a temporary files with them. Also, subdirectories are 
    created (with intention to be skipped).

    Parameters
    ----------
    path : pathlib.Path
        Path to location where the temporary files and 
        directory will be created.

    Returns
    -------
    pathlib.Path
        The path to the temporary directory with temporary files inside.
    """

    d = path / TEST_DIR_SCAN
    d.mkdir()
    for ext_type in cs.ALL_EXTENSION_LISTS:
        tmp_name = cs.TEST_FILE_NAME + ext_type[0]
        tmp_path = d / tmp_name
        tmp_path.touch()

    for i in range(TEST_SUBDIRS_NUM):
        tmp_path = d / (TEST_SUBDIR_NAME + str(i))
        tmp_path.mkdir()

    return d


TEST_DIR_MOVE = "move_dir"
SRC_SUBDIR_MOVE = "source"
DST_SUBDIR_MOVE = "destination"
def create_dummy_files_move(path: pl.Path, files: list[pl.Path]) -> tuple[pl.Path, pl.Path]:
    test_path = path / TEST_DIR_MOVE
    test_path.mkdir()

    test_src_path = test_path / SRC_SUBDIR_MOVE
    test_src_path.mkdir()

    test_dst_path = test_path / DST_SUBDIR_MOVE
    test_dst_path.mkdir()

    for f in files:
        tmp_path = test_src_path / f
        tmp_path.touch()

    return (test_src_path, test_dst_path)
