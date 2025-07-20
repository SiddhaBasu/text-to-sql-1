from db.metadata import get_sor_metadata
from llm.prompt import build_schema_context, build_prompt
from llm.llama3 import call_llama3


def generate_sql_for_sors(
    target_sors,
    user_question,
    pg_config,
    llama3_endpoint,
    llama3_api_key
):
    # 1. Get metadata
    metadata = get_sor_metadata(target_sors, pg_config)
    if not metadata:
        raise ValueError("No metadata found for the specified SORs.")

    # 2. Build schema context for LLM
    schema_context = build_schema_context(metadata)

    # 3. Build prompt
    prompt = build_prompt(schema_context, user_question)

    # 4. Call Llama 3
    sql = call_llama3(prompt, llama3_endpoint, llama3_api_key)
    return sql 