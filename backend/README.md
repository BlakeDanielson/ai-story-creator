# AI Story Creator Backend

This is the backend service for the AI Story Creator application, built with FastAPI.

## Dependency Management

### Decision: Poetry

For this project, we've chosen to use `Poetry` for dependency management over alternatives like requirements.txt or PDM. This decision was made for the following reasons:

- **Robust Dependency Resolution**: Poetry resolves dependencies more reliably and handles complex dependency graphs
- **Integrated Virtual Environment Management**: Poetry creates and manages virtual environments automatically
- **Lockfile System**: Poetry.lock ensures consistent installs across all environments
- **Project Packaging**: Built-in packaging capabilities for publishing if needed
- **Development Groups**: Separation of development and production dependencies

Poetry offers these advanced features while maintaining a straightforward workflow through its intuitive CLI commands.

### Usage Guidelines

When adding new dependencies:

1. Add a package: `poetry add package_name`
2. Add a development dependency: `poetry add --group dev package_name`
3. Update dependencies: `poetry update`
4. Install all dependencies: `poetry install`
5. Commit both pyproject.toml and poetry.lock to version control

## Environment Setup

### Local Development

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   poetry install
   ```

3. Activate the Poetry shell (virtual environment):
   ```bash
   poetry shell
   ```

4. Environment variables:
   This project uses a shared `.env` file at the project root (parent directory of `backend/`) to support both backend and frontend configuration.
   
   ```
   # Project root directory
   .env                # Active environment variables (development)
   .env.example        # Template showing required variables
   ```
   
   Key backend environment variables (prefixed with `aistory_`):
   ```
   aistory_debug=True
   aistory_database_url=postgresql+asyncpg://user:password@localhost:5432/story_creator_db
   # See .env.example for the complete list
   ```

5. Run the application:
   ```bash
   poetry run uvicorn main:app --reload
   ```

### Docker Development

The project includes Docker support. To use it:

```bash
# From the root directory of the project:
docker-compose up --build
```

## Project Structure

```
backend/
├── __init__.py
├── main.py              # Application entry point
├── config.py            # Configuration management
├── pyproject.toml       # Poetry dependency management and project metadata
├── poetry.lock          # Locked dependencies (commit this!)
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic schemas for data validation
├── routers/             # API route definitions
├── services/            # Business logic
├── repositories/        # Database access
├── middlewares/         # Custom middleware
├── utils/               # Helper functions
├── tests/               # Test suite
│   ├── __init__.py
│   └── test_main.py     # Tests for main.py
└── docs/                # Documentation
    └── api_design_principles.md
```

## Configuration Management

The application uses `pydantic-settings` to handle configuration. Settings are loaded from environment variables, with `.env` file support for local development. The configuration system looks for the `.env` file in the project root directory, not in the backend directory.

Key environment variables:
- `aistory_debug`: Set to "True" for development mode
- `aistory_database_url`: PostgreSQL connection string
- `aistory_secret_key`: Secret key for JWT and security features

Environment variables for the backend are prefixed with `aistory_` to distinguish them from frontend variables in the shared `.env` file.

## Testing

Run tests with:

```bash
poetry run pytest
```

This will automatically discover and run all tests in the `tests` directory.

You can also use coverage:

```bash
poetry run pytest --cov=backend
```

## Environment Variable Verification

You can verify that your environment variables are correctly configured by running:

```bash
poetry run python verify_env.py
```

This script checks that:
- All required dependencies are installed
- Environment variables are being loaded properly
- Database connection (if configured) works