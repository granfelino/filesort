import pathlib as pl
from filesort import constants as cs
from filesort import classify as cl

CLASSIFY_PATH = pl.Path("/tmp/")
CLASSIFY_FILES = [ext_list[0] for ext_list in cs.ALL_EXTENSION_LISTS]
CLASSIFY_MANY_VAL = [CLASSIFY_PATH / (cs.TEST_FILE_NAME + ext) for ext in CLASSIFY_FILES]
CLASSIFY_RETS = cs.ALL_EXTENSION_TYPES


def test_classify_single():
    for i in range(len(CLASSIFY_MANY_VAL)):
        assert cl.classify_single(CLASSIFY_MANY_VAL[i]) == CLASSIFY_RETS[i]

def test_classify_many():
    ret = cl.classify_many(CLASSIFY_MANY_VAL)
    assert ret == {k : [v] for k, v in zip(CLASSIFY_RETS, CLASSIFY_MANY_VAL)}
