from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.genai import types
from toolbox_core import ToolboxSyncClient
from dotenv import load_dotenv

import os
import asyncio

load_dotenv()

async def run_toolbox_sql_agent(user_question, toolbox_url, gemini_api_key=None, toolset_name="my-toolset"):
    # Set your Google API key from .env if not provided
    if gemini_api_key is None:
        gemini_api_key = os.getenv('GOOGLE_API_KEY')
    os.environ['GOOGLE_API_KEY'] = gemini_api_key

    # Connect to Toolbox
    with ToolboxSyncClient(toolbox_url) as toolbox_client:
        prompt = """
        You are a SQL master expert capable of writing complex SQL queries in BigQuery.
        You do not ask for confirmation. Always provide the best available response with the data you are given.
        Based on SOR_DATA_CATALOGUE, generate BigQuery SQL queries to retrieve data from the System of Records.
        """

        root_agent = Agent(
            model='gemini-2.0-flash-001',  # or 'gemini-2.0-flash-001'
            name='dsar_agent',
            description='A text-to-SQL assistant for SOR data retrieval.',
            instruction=prompt,
            tools=toolbox_client.load_toolset(toolset_name),
        )

        session_service = InMemorySessionService()
        artifacts_service = InMemoryArtifactService()
        session = await session_service.create_session(
            state={}, app_name='dsar_agent', user_id='123'
        )
        runner = Runner(
            app_name='dsar_agent',
            agent=root_agent,
            artifact_service=artifacts_service,
            session_service=session_service,
        )

        # Run the agent with the user question
        content = types.Content(role='user', parts=[types.Part(text=user_question)])
        events = runner.run(session_id=session.id, user_id='123', new_message=content)

        responses = (
            part.text
            for event in events
            for part in event.content.parts
            if part.text is not None
        )

        return list(responses)

if __name__ == "__main__":
    # Example usage
    toolbox_url = "http://127.0.0.1:5000"
    user_question = "Generate a BigQuery SQL query to retrieve all data on a customer with CM15 of 1234567890 in SORs C360, Adobe"
    responses = asyncio.run(run_toolbox_sql_agent(user_question, toolbox_url))
    print("RESPONSES:")
    for text in responses:
        print(text)