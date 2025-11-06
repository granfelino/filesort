from tests import utils
from filesort import scan as scan
from filesort import constants as cs

SCAN_RET = sorted([cs.TEST_FILE_NAME + x[0] for x in cs.ALL_EXTENSION_LISTS])

def test_scan(tmp_path):
    path = utils.create_dummy_files_scan(tmp_path)
    ret = scan.scan(path)
    ret_fmt = sorted([str(p.relative_to(path)) for p in ret])

    assert all([x.is_file() for x in ret])
    assert ret_fmt == SCAN_RET
