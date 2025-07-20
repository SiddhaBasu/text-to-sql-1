from config import POSTGRES_CONFIG, LLAMA3_ENDPOINT, LLAMA3_API_KEY, GEMINI_ENDPOINT, GEMINI_API_KEY
from pipeline.generate_sql import generate_sql_for_sors
from pipeline.generate_sql_gemini import generate_sql_for_sors_gemini

if __name__ == "__main__":
    target_sors = ["Customer 360", "Adobe"]
    user_question = "Find all users who signed up in the last 30 days and have an email address."

    # Use Llama 3 by default
    # sql = generate_sql_for_sors(
    #     target_sors,
    #     user_question,
    #     POSTGRES_CONFIG,
    #     LLAMA3_ENDPOINT,
    #     LLAMA3_API_KEY
    # )
    # print("Llama 3 SQL:\n", sql)

    #To use Gemini instead, uncomment below:
    sql_gemini = generate_sql_for_sors_gemini(
        target_sors,
        user_question,
        POSTGRES_CONFIG,
        GEMINI_ENDPOINT,
        GEMINI_API_KEY
    )
    print("Gemini SQL:\n", sql_gemini) 