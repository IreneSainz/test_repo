import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import hello


def test_main_output(capsys):
    hello.main()
    captured = capsys.readouterr()
    output_lines = captured.out.strip().splitlines()
    assert output_lines == ["Hello World", "My Name is Carolina"]
