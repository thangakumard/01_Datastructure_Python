import os
import importlib.util
import pathlib


def _load_solution():
    here = pathlib.Path(__file__).parent
    mod_path = here / "max_consecutive_ones_III.py"
    spec = importlib.util.spec_from_file_location("max_consecutive_ones_III", str(mod_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Solution()


def test_examples_and_given_cases():
    sol = _load_solution()
    assert sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10


def test_edge_cases():
    sol = _load_solution()
    assert sol.longestOnes([], 0) == 0
    assert sol.longestOnes([1, 1, 1], 0) == 3
    assert sol.longestOnes([0, 0, 0], 2) == 2
    assert sol.longestOnes([0, 0, 0], 5) == 3
    assert sol.longestOnes([1, 0, 1, 0, 1], 1) == 3
