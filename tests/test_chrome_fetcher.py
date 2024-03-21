import unittest
from unittest.mock import patch, MagicMock
from ChromeFetcher.chrome_fetcher import fetch_chrome

class TestFetchChrome(unittest.TestCase):
    @patch('requests.get')
    @patch('osarch.detect_system_architecture')
    def test_fetch_chrome_chromedriver(self, mock_architecture, mock_get):
        mock_architecture.return_value = ('darwin', '64')
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "channels": {
                "Stable": {
                    "downloads": {
                        "chromedriver": [
                            {"platform": "darwin64", "url": "http://example.com/chromedriver_darwin64.zip"}
                            # Updated to darwin64 to match mock
                        ]
                    }
                }
            }
        }
        mock_get.return_value = mock_response

        fetch_chrome(product='chromedriver', unzip=True, delete_zip=True)

        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()
