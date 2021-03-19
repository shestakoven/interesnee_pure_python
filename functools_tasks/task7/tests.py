from unittest import TestCase
from unittest.mock import patch

from functools_tasks.task7.task7 import get_links_from


class ResponseMock:

    def __init__(self, ok, text):
        self.ok = ok
        self.text = text


class TestGetLinks(TestCase):

    @patch('functools_tasks.task7.task7.requests.get')
    def test_normal(self, get_mock):
        get_mock.return_value = ResponseMock(
            ok=True,
            text='<a href="link1"></a>'
                 '<a href="link2"></a>'
        )
        result = get_links_from('')
        self.assertListEqual(['link1', 'link2'], result)

    @patch('functools_tasks.task7.task7.requests.get')
    def test_status_bad(self, get_mock):
        get_mock.return_value = ResponseMock(
            ok=False,
            text='<a href="link1"></a>'
                 '<a href="link2"></a>'
        )
        with self.assertRaises(ConnectionError):
            get_links_from('')
