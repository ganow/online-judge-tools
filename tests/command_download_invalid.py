import unittest

import requests.exceptions
import tests.command_download


class DownloadInvalid(unittest.TestCase):
    def snippet_call_download_raises(self, *args, **kwargs):
        tests.command_download.snippet_call_download_raises(self, *args, **kwargs)

    def snippet_call_download_twice(self, *args, **kwargs):
        tests.command_download.snippet_call_download_twice(self, *args, **kwargs)

    def test_call_download_invalid(self):
        self.snippet_call_download_raises(requests.exceptions.InvalidURL, 'https://not_exist_contest.jp/tasks/001_a')

    def test_call_download_twice(self):
        self.snippet_call_download_twice('https://atcoder.jp/contests/abc114/tasks/abc114_c', 'https://atcoder.jp/contests/abc003/tasks/abc003_4', [
            {
                "input": "575\n",
                "output": "4\n"
            },
            {
                "input": "3600\n",
                "output": "13\n"
            },
            {
                "input": "999999999\n",
                "output": "26484\n"
            },
        ], type='json')
