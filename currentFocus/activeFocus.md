# Active Focus: Backend Foundation & Health Check

**Objective:**

*   Establish the core structure for the Python FastAPI backend service.
*   Implement the first API endpoint (`/health`) to verify basic service operation.
*   Adhere strictly to the Test-Driven Development (TDD) cycle (Red-Green-Refactor).

**Critical Context:**

*   **Project Structure:** Assumes a monorepo structure with a dedicated `backend` directory.
*   **Technology Stack:** Python, FastAPI, pytest.
*   **Dependency Management:** Using `pip` and `requirements.txt` (as per Sprint 0 recommendation, unless decided otherwise in Task 1.5).
*   **Environment:** Development occurs locally, ideally within a virtual environment. Docker setup (Task 1.3) is planned but not a strict prerequisite for *this specific task*.
*   **Prerequisites:** Basic Git setup (Task 1.1), IDE/Linter configuration (Task 1.6) should be in place or addressed concurrently.

**Success Criteria:**

*   The `backend/main.py` file exists and initializes a FastAPI application.
*   The `backend/requirements.txt` file lists necessary dependencies.
*   The `backend/tests/test_main.py` file contains a passing test for the `/health` endpoint.
*   A GET request to the running application's `/health` endpoint returns a 200 status code and the JSON body `{"status": "ok"}`.
*   Code implementing the feature and its test is committed to version control.