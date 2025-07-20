import unittest
from unittest.mock import patch, MagicMock
from pipeline.generate_sql import generate_sql_for_sors

class TestGenerateSqlForSors(unittest.TestCase):
    @patch('pipeline.generate_sql.call_llama3')
    @patch('pipeline.generate_sql.build_prompt')
    @patch('pipeline.generate_sql.build_schema_context')
    @patch('pipeline.generate_sql.get_sor_metadata')
    def test_generate_sql_for_sors(self, mock_get_metadata, mock_build_context, mock_build_prompt, mock_call_llama3):
        mock_get_metadata.return_value = [{
            'sor_nm': 'Customer 360',
            'table_nm': 'users',
            'attribute_nm': 'email',
            'attribute_value': 'test@example.com',
            'identifier_expr': 'user_id',
            'filter_predicate_sql': 'is_active = TRUE',
            'range_of_date_expr': 'created_date BETWEEN ...'
        }]
        mock_build_context.return_value = 'schema context'
        mock_build_prompt.return_value = 'final prompt'
        mock_call_llama3.return_value = 'SELECT * FROM users;'
        target_sors = ['Customer 360']
        user_question = 'Get all emails.'
        pg_config = {}
        llama3_endpoint = 'fake-endpoint'
        llama3_api_key = 'fake-key'
        sql = generate_sql_for_sors(target_sors, user_question, pg_config, llama3_endpoint, llama3_api_key)
        self.assertEqual(sql, 'SELECT * FROM users;')

if __name__ == '__main__':
    unittest.main() 