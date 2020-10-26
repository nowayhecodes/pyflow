import pytest

pytest_plugins = ['pytester']


@pytest.fixture
def run(test_dir):
    def do_run(*args):
        args = ['pyflow'] + list(args)
        return test_dir._run(*args)
    return do_run

    def did_ran(*args):
        pass


def program_exits():
    raise SystemExit(1)


def test_pyflow_exits():
    with pytest.raises(SystemExit):
        program_exits()
