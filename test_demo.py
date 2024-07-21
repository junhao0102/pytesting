def setup_module():
    print("a")


def teardown_module():
    print("b")


def setup_function():
    print("c")


def teardown_function():
    print("d")


def test_demo():
    assert 1 + 1 == 2

