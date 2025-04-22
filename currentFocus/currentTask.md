# Current Task: Initialize FastAPI Backend & Implement /health Endpoint (TDD)

**Reference:** Sprint 0 - Tasks 2.1 & 2.2

**Goal:** Create the basic FastAPI application structure and implement the initial `/health` check endpoint using Test-Driven Development.

**Actionable Steps:**

1.  **Initialize Project (Task 2.1):**
    *   Ensure you are in the `backend` directory (or create it if using monorepo structure).
    *   Create `backend/main.py`.
    *   Initialize the FastAPI app instance (`app = FastAPI()`) in `main.py`.
    *   Set up basic configuration loading (e.g., using `pydantic-settings`).
    *   Create `backend/requirements.txt` (assuming this choice from Task 1.5).
    *   Add `fastapi`, `uvicorn[standard]`, `pydantic-settings`, `pytest`, `pytest-asyncio`, `httpx` (for TestClient) to `requirements.txt`.
    *   Create and activate a virtual environment (e.g., `python -m venv .venv`, `source .venv/bin/activate` or `.\.venv\Scripts\activate`).
    *   Install dependencies: `pip install -r requirements.txt`.

2.  **Implement /health Endpoint (TDD - Task 2.2):**
    *   **Test First (Red):**
        *   Create `backend/tests/test_main.py`.
        *   Import `TestClient` from `fastapi.testclient` and the `app` from `main`.
        *   Write `test_health_check()` function:
            *   Instantiate `client = TestClient(app)`.
            *   Make a GET request: `response = client.get("/health")`.
            *   Assert status code is 200: `assert response.status_code == 200`.
            *   Assert response body: `assert response.json() == {"status": "ok"}`.
        *   Run tests (`pytest backend/tests`). **Verify failure (e.g., 404 Not Found).**
    *   **Implement (Green):**
        *   In `backend/main.py`, add the endpoint:
          ```python
          @app.get("/health")
          async def health_check():
              return {"status": "ok"}
          ```
    *   **Test Again:**
        *   Run tests (`pytest backend/tests`). **Verify success.**
    *   **Refactor:**
        *   Review the code in `main.py` and `test_main.py` for clarity and simplicity. (Minimal refactoring likely needed here).
    *   **Commit:**
        *   Stage changes (`git add backend/main.py backend/tests/test_main.py backend/requirements.txt`).
        *   Commit (`git commit -m "feat(backend): initialize FastAPI and add /health endpoint via TDD"`).