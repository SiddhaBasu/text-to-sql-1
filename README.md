# Text-to-SQL LLM Pipeline for BigQuery (SOR Data Catalog)

## Overview
This project is a Python pipeline that generates BigQuery-compatible SQL queries for retrieving personally identifiable data from multiple Systems of Record (SORs), using metadata from a centralized data catalog (`sor_data_catalog`). It leverages:
- **Google AI embedding model** (for optional schema matching)
- **Llama 3 70B** endpoint (for SQL generation)
- **Postgres** (for the data catalog)

The pipeline passes relevant schema metadata directly to the LLM, which generates the SQL query.

---

## Project Structure
```
tts_1/
│
├── main.py                  # Entry point for running the pipeline
├── config.py                # Configuration for Postgres, GCP, and Llama 3 endpoint
├── requirements.txt         # Python dependencies
│
├── db/
│   └── metadata.py          # Extract SOR metadata from Postgres
│
├── llm/
│   ├── embedding.py         # (Optional) Google AI embedding model utility
│   ├── prompt.py            # Build schema context and LLM prompt
│   └── llama3.py            # Call Llama 3 70B endpoint
│
├── pipeline/
│   └── generate_sql.py      # Main pipeline orchestration
│
└── tests/                   # Unit tests for each module
```

---

## Setup
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your environment:**
   - Edit `config.py` with your Postgres credentials, GCP project/location, and Llama 3 endpoint/API key.
   - Ensure your Google Cloud credentials are set up (for embedding, if used):
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
     ```

3. **Prepare your Postgres database:**
   - Ensure the `sor_data_catalog` table exists and is populated.

---

## Usage
Run the main pipeline:
```bash
python main.py
```
This will print the generated SQL for the example SORs and question in `main.py`.

---

## Testing
Run all tests:
```bash
python -m unittest discover tests
```

---

## What You Need to Implement/Configure
- **Postgres:**
  - Set up your `sor_data_catalog` table and populate it with your SOR metadata.
  - Update `config.py` with your actual Postgres connection details.

- **Llama 3 Endpoint:**
  - Deploy or obtain access to a Llama 3 70B endpoint that accepts prompts and returns completions in the expected format.
  - Update `config.py` with the endpoint URL and API key.

- **Google Cloud (optional):**
  - If you want to use the embedding functionality, ensure you have access to Vertex AI and set up your service account credentials.
  - Update `config.py` with your GCP project and location.

- **Prompt Engineering:**
  - You may want to refine the prompt construction in `llm/prompt.py` for your specific use case and data catalog structure.

- **Security:**
  - Ensure that API keys and credentials are managed securely (consider using environment variables or a secrets manager in production).

---

## Extending the Project
- Add more advanced schema matching using embeddings.
- Integrate with a web UI or API for interactive querying.
- Add logging, monitoring, and error handling for production use.
- Expand test coverage and add integration tests.

---

## License
MIT 

---

## Agent-based Pipeline with Google AI Toolbox (MCP)

This project also supports an agent-based approach using Google AI Toolbox (ToolboxSyncClient), MCP, and Gemini. This allows the LLM to dynamically call tools defined in `tools.yaml` (such as metadata, join/filter predicate queries, and even pgvector similarity search if added).

### How to Use

1. **Start your Toolbox instance** (see [Toolbox documentation](https://github.com/google/toolbox)).
2. **Configure your `tools.yaml`** to point to your Postgres/pgvector database and define your toolset (see the provided example).
3. **Run the agent pipeline:**
   ```bash
   python -m pipeline.toolbox_sql_agent
   ```
   Or import and call `run_toolbox_sql_agent()` from your own code.

### Example
```python
from pipeline.toolbox_sql_agent import run_toolbox_sql_agent
responses = run_toolbox_sql_agent(
    user_question="Generate a BigQuery SQL query to retrieve info on employee payroll",
    toolbox_url="http://127.0.0.1:5000",
    gemini_api_key="YOUR_GEMINI_API_KEY"
)
for text in responses:
    print(text)
```

### Benefits
- The agent can use all tools defined in your toolset, including those that leverage pgvector for similarity search.
- All metadata and query logic is centralized in your Toolbox toolset, not in Python code.
- Easily extensible: add new tools to `tools.yaml` and the agent can use them immediately.

--- 