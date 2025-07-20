import unittest
from unittest.mock import patch, MagicMock
from db.metadata import get_sor_metadata

class TestGetSorMetadata(unittest.TestCase):
    @patch('psycopg2.connect')
    def test_get_sor_metadata(self, mock_connect):
        # Mock cursor and connection
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        # Mock data
        mock_cursor.fetchall.return_value = [
            ('Customer 360', 'users', 'email', 'test@example.com', 'user_id', 'is_active = TRUE', 'created_date BETWEEN ...')
        ]
        mock_cursor.description = [
            ('sor_nm',), ('table_nm',), ('attribute_nm',), ('attribute_value',),
            ('identifier_expr',), ('filter_predicate_sql',), ('range_of_date_expr',)
        ]
        target_sors = ['Customer 360']
        pg_config = {}
        result = get_sor_metadata(target_sors, pg_config)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['sor_nm'], 'Customer 360')
        self.assertEqual(result[0]['attribute_nm'], 'email')

if __name__ == '__main__':
    unittest.main() 