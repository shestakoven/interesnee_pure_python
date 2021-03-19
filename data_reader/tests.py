import os
import pytest

from data_reader.main import Converter

EXCEPTED_DICT = [
    {'name': 'John', 'age': '32', 'city': 'NY', 'birthday': '10-10-1986'},
    {'name': 'Sam', 'age': '18', 'city': 'LA', 'birthday': '01-11-2000'}
]


@pytest.fixture
def make_data(tmp_path):
    """Create files for tests."""
    data = Converter(EXCEPTED_DICT)
    return data


@pytest.fixture
def make_csv(tmp_path):
    """Create files for tests."""
    new_file = tmp_path / f'test_csv.csv'
    new_file.write_text('name,age,city,birthday\n'
                        'John,32,NY,10-10-1986\n'
                        'Sam,18,LA,01-11-2000\n')
    return new_file


@pytest.fixture
def make_json(tmp_path):
    """Create files for tests."""
    new_file = tmp_path / f'test_json.json'
    new_file.write_text("""
                        [
                            {
                                "name": "John",
                                "age": "32",
                                "city": "NY",
                                "birthday": "10-10-1986"
                            },
                            {
                                "name": "Sam",
                                "age": "18",
                                "city": "LA",
                                "birthday": "01-11-2000"
                            }
                        ]
                        """)
    return new_file


@pytest.fixture
def make_yaml(tmp_path):
    """Create files for tests."""
    new_file = tmp_path / f'test_yaml.yaml'
    new_file.write_text("""
                        - age: '32'
                          birthday: 10-10-1986
                          city: NY
                          name: John
                        - age: '18'
                          birthday: 01-11-2000
                          city: LA
                          name: Sam
                        """)
    return new_file


def test_get_csv(make_csv):
    """Test that method correctly read data."""
    data = Converter()
    data.read(make_csv)
    assert EXCEPTED_DICT == data.data


def test_get_json(make_json):
    """Test that method correctly read data."""
    data = Converter()
    data.read(make_json)
    assert EXCEPTED_DICT == data.data


def test_get_yaml(make_yaml):
    """Test that method correctly read data."""
    data = Converter()
    data.read(make_yaml)
    assert EXCEPTED_DICT == data.data


def test_write_csv(make_data, make_csv):
    """Test that method correctly write data."""
    make_data.write('test.csv')
    with open('test.csv') as test:
        with open(make_csv) as excepted:
            assert test.readlines() == excepted.readlines()
    os.remove('test.csv')


def test_write_json(make_data, make_json):
    """Test that method correctly write data."""
    make_data.write('test.json')
    with open('test.json') as test:
        test_text = test.read().split()
        test_text = ''.join(test_text)
        with open(make_json) as excepted:
            excepted_text = excepted.read().split()
            excepted_text = ''.join(excepted_text)
            assert test_text == excepted_text
    os.remove('test.json')


def test_write_yaml(make_data, make_yaml):
    """Test that method correctly write data."""
    make_data.write('test.yaml')
    with open('test.yaml') as test:
        test_text = test.read().split()
        test_text = ''.join(test_text)
        with open(make_yaml) as excepted:
            excepted_text = excepted.read().split()
            excepted_text = ''.join(excepted_text)
            assert test_text == excepted_text
    os.remove('test.yaml')
