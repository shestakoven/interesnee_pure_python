import os
from collections import defaultdict

import pytest
from pytest_mock import MockFixture
from plushkins_helper.main import PlushkinsHelper


@pytest.fixture
def test_files(tmp_path):
    """Create files for tests."""
    new_folder = tmp_path / 'new_folder'
    new_folder.mkdir()
    for i in range(3):
        new_file = new_folder / f'new_file{i}.txt'
        new_file.write_text('a')
    new_file = new_folder / f'unique_file.txt'
    new_file.write_text('unique text')
    return new_folder


@pytest.fixture
def helper_obj(test_files):
    return PlushkinsHelper(test_files)


def test_read_hash(test_files, helper_obj):
    """Test read_hash function for correct hash returns."""
    file_hash = helper_obj.read_hash(os.path.join(test_files, 'new_file0.txt'))
    assert '0cc175b9c0f1b6a831c399e269772661' == file_hash


def test_find_all_duplicates(test_files, helper_obj):
    """Tests that script find all duplicates and write them in dict."""
    helper_obj.find_all_duplicates()
    EXCEPTED_DICT = defaultdict(list)
    EXCEPTED_DICT.update(
        {'0cc175b9c0f1b6a831c399e269772661':
            [
                os.path.join(test_files, 'new_file1.txt'),
                os.path.join(test_files, 'new_file0.txt'),
                os.path.join(test_files, 'new_file2.txt'),
            ]}
    )
    assert helper_obj.not_unique.items() == EXCEPTED_DICT.items()


def test_wait_for_input(test_files, mocker: MockFixture, helper_obj):
    """Test that function don`t accept input value greater then duplicates count."""
    input_mock = mocker.patch('plushkins_helper.main.input')
    print_mock = mocker.patch('plushkins_helper.main.print')
    input_mock.side_effect = ['3', '1']
    helper_obj.wait_for_input(['a', 'a'])
    print_mock.assert_called_with('Incorrect number.')


def test_delete_duplicates(test_files, mocker: MockFixture, helper_obj):
    """Tests that new_file2.txt was removed."""
    wait_input = mocker.patch('plushkins_helper.main.PlushkinsHelper.wait_for_input')
    wait_input.return_value = 1
    helper_obj.find_all_duplicates()
    helper_obj.prepare_to_delete()
    assert not os.path.exists(test_files / 'new_file2.txt')


def test_unique_files(test_files, mocker: MockFixture, helper_obj):
    """Tests that script don`t remove unique files."""
    wait_input = mocker.patch('plushkins_helper.main.PlushkinsHelper.wait_for_input')
    wait_input.return_value = 1
    helper_obj.find_all_duplicates()
    helper_obj.prepare_to_delete()
    assert os.path.exists(test_files / 'unique_file.txt')
