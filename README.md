Gemini client
=============

This repo contains a small `GeminiClient` wrapper in `gemini_client.py` that
calls the Google Gemini REST `generateText` endpoint.

Usage
-----

- Set your API key in the environment: `export GEMINI_API_KEY=...`
- Run the example in `main.py`:

```bash
python main.py
```

The example prints the raw JSON response returned by the Gemini endpoint.

Notes
-----
- The client uses `requests` and expects an API key; it will send it as a
	bearer token by default. If your setup requires a different header, pass
	`use_bearer=False` to `GeminiClient` to use `x-api-key` instead.
