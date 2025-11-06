from filesort import constants as cs
from filesort import move as mv
from tests import utils
import pathlib as pl

MOVE_EXTS = [ext_list[0] for ext_list in cs.ALL_EXTENSION_LISTS]
MOVE_FILES = [pl.Path(cs.TEST_FILE_NAME + ext) for ext in MOVE_EXTS]

def test_move(tmp_path):
    src_path, dst_path = utils.create_dummy_files_move(tmp_path, MOVE_FILES)
    src_paths_classified = {k : [src_path / v] for k, v in zip(cs.ALL_EXTENSION_TYPES, MOVE_FILES)}

    mv.move(src_paths_classified, dst_path)

    assert set(cs.ALL_EXTENSION_TYPES) == {f.name for f in dst_path.iterdir()}

    for d in dst_path.iterdir():
        expected_path_list = src_paths_classified[d.name]
        expected_name = expected_path_list[0].name
        actual_name = [f for f in d.iterdir()][0].name
        assert expected_name == actual_name
