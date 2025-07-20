import unittest
from llm.prompt import build_schema_context, build_prompt

class TestPromptUtils(unittest.TestCase):
    def test_build_schema_context(self):
        metadata = [
            {
                'sor_nm': 'Customer 360',
                'table_nm': 'users',
                'attribute_nm': 'email',
                'attribute_value': 'test@example.com',
                'identifier_expr': 'user_id',
                'filter_predicate_sql': 'is_active = TRUE',
                'range_of_date_expr': 'created_date BETWEEN ...'
            }
        ]
        context = build_schema_context(metadata)
        self.assertIn('SOR: Customer 360', context)
        self.assertIn('Table: users', context)
        self.assertIn('Attribute: email', context)

    def test_build_prompt(self):
        schema_context = 'schema context here'
        user_question = 'What is the user email?'
        prompt = build_prompt(schema_context, user_question)
        self.assertIn('schema context here', prompt)
        self.assertIn('What is the user email?', prompt)
        self.assertIn('SQL:', prompt)

if __name__ == '__main__':
    unittest.main() 