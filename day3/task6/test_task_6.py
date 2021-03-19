import datetime
from unittest import TestCase
from unittest.mock import Mock, patch

from requests import codes

from day3.task6 import task_6

JSON_RESPONSE = [
    {
        "author": {
            "login": "shestakoven"
        },
        "commit": {
            "author": {
                "date": "datetime.datetime.now()",
                "email": "shestakoven@users.noreply.github.com",
                "name": "shestakoven"
            },
            "comment_count": 0,
            "committer": {
                "date": datetime.datetime.now() - datetime.timedelta(days=100),
                "email": "shestakoven@users.noreply.github.com",
                "name": "shestakoven"
            },
            "message": "working version"
        },
        "committer": {
            "login": "shestakoven"
        }
    },
    {
        "author": {
            "login": "test"
        }
    }
]


class ResponseMock:

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.ok = True
        self.data = data

    def json(self):
        return self.data


class TestTask6(TestCase):

    @patch('day3.task_6.requests.get')
    def test_get_unique_authors(self, get_mock):
        get_mock.return_value = ResponseMock(status_code=codes.OK,
                                             data=JSON_RESPONSE)
        http_response = get_mock
        result = task_6.get_unique_authors(http_response)
        self.assertCountEqual(result, ('test', 'shestakoven',))

    @patch('day3.task_6.requests.get')
    def test_get_commits_count(self, get_mock):
        get_mock.return_value = ResponseMock(status_code=codes.OK,
                                             data=JSON_RESPONSE)
        http_response = get_mock
        result = task_6.get_commits_count(http_response)
        self.assertEqual(2, result)

    @patch('day3.task_6.requests.get')
    def test_get_comment_info(self, get_mock):
        get_mock.return_value = ResponseMock(status_code=codes.OK,
                                             data=JSON_RESPONSE)
        task_6.get_most_active_committee = Mock(return_value='test_name')
        result = task_6.get_commits_info('', '')
        self.assertListEqual(
            ['shestakoven', 'test'],
            sorted(result[task_6.UNIQUE_AUTHORS])
        )
        self.assertEqual(2, result[task_6.LAST_COMMITS])
        self.assertEqual('test_name', result[task_6.MOST_ACTIVE_USER])
