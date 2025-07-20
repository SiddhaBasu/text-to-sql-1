import unittest
from unittest.mock import patch, MagicMock
from llm.llama3 import call_llama3

class TestCallLlama3(unittest.TestCase):
    @patch('requests.post')
    def test_call_llama3(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{"text": "SELECT * FROM users;"}]
        }
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response
        prompt = "Test prompt"
        endpoint_url = "http://fake-endpoint"
        api_key = "fake-key"
        result = call_llama3(prompt, endpoint_url, api_key)
        self.assertEqual(result, "SELECT * FROM users;")

if __name__ == '__main__':
    unittest.main() 