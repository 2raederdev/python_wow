import pytest 
from such_wow import such_wow, short_such_wow


@pytest.fixture
def such_wow_output(capfd):
    such_wow()
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split('\n') if line.strip()]
    return output

@pytest.fixture
def short_such_wow_output(capfd):
    short_such_wow()
    out, _ = capfd.readouterr()
    output = [line.strip() for line in out.split('\n') if line.strip()]
    return output


def test_length_such_wow(such_wow_output):
    output = such_wow_output
    assert len(output) == 100

def test_length_short_such_wow(short_such_wow_output):
    output = short_such_wow_output
    assert len(output) == 100

def test_such_wow(such_wow_output):
    output = such_wow_output
    expected = [1, 2, 'Such', 4, 'Wow', 'Such', 7, 8, 'Such', 'Wow', 11, 'Such', 13, 14, 'SuchWow']

    for  index, exp in enumerate(expected):
        assert str(output[index]) == str(exp)

def test_short_such_wow(short_such_wow_output):
    output = short_such_wow_output
    expected = [1, 2, 'Such', 4, 'Wow', 'Such', 7, 8, 'Such', 'Wow', 11, 'Such', 13, 14, 'SuchWow']

    for  index, exp in enumerate(expected):
        assert str(output[index]) == str(exp)