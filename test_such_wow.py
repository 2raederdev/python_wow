import pytest 
from such_wow import such_wow, short_such_wow


@pytest.fixture
def output(capfd):
    such_wow()
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split('\n') if line.strip()]
    return output

@pytest.fixture
def short_output(capfd):
    short_such_wow()
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split('\n') if line.strip()]
    return output

@pytest.fixture
def expected():
    return [1, 2, 'Such', 4, 'Wow', 'Such', 7, 8, 'Such', 'Wow', 11, 'Such', 13, 14, 'SuchWow']


def test_length_such_wow(output):
    assert len(output) == 100

def test_length_short_such_wow(short_output):
    assert len(short_output) == 100

def test_such_wow(output, expected):
    for  index, exp in enumerate(expected):
        assert str(output[index]) == str(exp)

def test_short_such_wow(short_output, expected):
    for  index, exp in enumerate(expected):
        assert str(short_output[index]) == str(exp)