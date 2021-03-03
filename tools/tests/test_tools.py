from schemas.schemas import Model
from tools.tools import run_test
import pytest
import os
import sys


class Test:

    def test_samples(self):
        dd = {"item": ['1']}
        _ = run_test(Model(**dd))


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.exit(pytest.main([dir_path, "-W", "ignore::DeprecationWarning"]))
