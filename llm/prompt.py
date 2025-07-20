def build_schema_context(metadata):
    """
    Format the metadata as a schema context for the LLM.
    """
    context = "### SOR Data Catalog Schema\n"
    for row in metadata:
        context += (
            f"SOR: {row['sor_nm']}\n"
            f"  Table: {row['table_nm']}\n"
            f"    Attribute: {row['attribute_nm']} (Example: {row['attribute_value']})\n"
            f"    Identifier: {row['identifier_expr']}\n"
            f"    Filter: {row['filter_predicate_sql']}\n"
            f"    Date Range: {row['range_of_date_expr']}\n"
        )
    return context

def build_prompt(schema_context, user_question):
    """
    Build the final prompt for the LLM.
    """
    prompt = (
        f"{schema_context}\n"
        f"### Task\n"
        f"Generate a BigQuery SQL query that answers the following question using the above schema. "
        f"Only use the tables and columns provided. If filters or identifiers are specified, use them appropriately.\n"
        f"Queries should be in the form of SELECT sor_nm, table_nm, attribute_nm, attribute_value, identifier_expr, filter_predicate_sql, range_of_date_expr;\n"
        f"SOR list: {user_question}\n"
        f"SQL:"
    )
    return prompt 