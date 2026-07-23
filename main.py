def main():
    import os
    from pprint import pprint

    print("Hello from llm-zoomcamp-2026-code!")

    # Example: if GEMINI_API_KEY is set, call Gemini for a simple prompt
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set — skipping Gemini call.")
        return

    try:
        from gemini_client import GeminiClient

        client = GeminiClient(api_key=api_key)
        resp = client.generate_text("What is the capital of France? Answer in one word.")
        print("Gemini response (raw JSON):")
        pprint(resp)
    except Exception as e:
        print("Error calling Gemini:", e)


if __name__ == "__main__":
    main()
