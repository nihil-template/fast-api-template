# Gemini Project Analysis: FastAPI Template

**CRITICAL NOTE**: All responses and interactions from the AI agent will be in Korean.

This document provides a comprehensive overview of the `fast-api-template` project, designed to serve as a persistent context for AI-assisted development.

## 1. Project Overview

This is a template project for building RESTful APIs using FastAPI. It establishes a robust and opinionated 3-tier architecture with a strong emphasis on type safety, standardized responses, and clear separation of concerns.

- **Primary Technologies**:
  - **Framework**: FastAPI
  - **ORM**: SQLModel (for type-safe database interactions and data models)
  - **Database**: PostgreSQL (connected via `psycopg`)
  - **Data Validation**: Pydantic (used for settings and Value Objects)
  - **Authentication**: JWT (`python-jose`) with bcrypt for password hashing (`passlib`)
  - **Package Management**: `uv`

- **Core Architecture**: The project follows a strict 3-tier architecture:
  1.  **Router Layer (`src/routers`)**: Defines API endpoints, handles HTTP request/response, and manages Swagger UI documentation. It uses FastAPI's dependency injection to get services.
  2.  **Service Layer (`src/services`)**: Contains all business logic. It orchestrates data flow by calling DAO methods and processing the results.
  3.  **DAO (Data Access Object) Layer (`src/dao`)**: The only layer that interacts directly with the database. It uses SQLModel to perform CRUD operations.

## 2. Key Development Conventions

This project has several strong conventions that should be followed:

- **Standardized API Response**: All API endpoints return an HTTP `200 OK` status. The actual success or failure is indicated within the JSON body using a standard `ApiResponse` schema:
  ```json
  {
    "data": {},
    "error": false,
    "code": "OK",
    "message": "Success"
  }
  ```
  This is a critical design choice. Exception handlers in `src/main.py` intercept FastAPI's default errors (like 422 Validation or 401 Unauthorized) and re-format them into this standard 200 OK response structure.

- **Value Objects (VOs - `src/vos`)**: For each data model (e.g., `UserInfo`), there is a corresponding `UserVo` Pydantic model. This VO acts as a universal Data Transfer Object (DTO) for that resource across all layers and operations (create, read, update, list). This promotes consistency.

- **Dependency Injection**: FastAPI's `Depends` system is used to provide a database `Session` and instantiate `Service` classes within the router functions. This ensures a clean separation of concerns and easy testing.

- **Configuration (`src/settings.py`)**: All configuration is managed via a `Settings` class that loads values from a `.env` file at the project root.

- **Package Management**: The project is configured to use `uv`. All dependencies are listed in `pyproject.toml`.

- **Code Style & Quality**:
  - **Formatting**: `ruff` is used for code formatting. Key rules include a 2-space indent and single quotes (see `pyproject.toml`).
  - **Type Checking**: `pyright` is used for static type analysis, and the code is heavily type-annotated.

## 3. Building and Running the Project

Follow these steps to get the application running.

**1. Install Dependencies:**
Use `uv` to create a virtual environment and install the required packages.

```bash
# This command creates a .venv folder if it doesn't exist
# and installs all dependencies from pyproject.toml.
uv sync
```

**2. Configure Environment:**
Create a `.env` file in the root of the project. It must contain the following variables:

```env
# Database connection string
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# Environment (development or production)
ENVIRONMENT=development

# JWT secrets (replace with strong, random keys)
ACCESS_TOKEN_SECRET=your-access-token-secret-key
REFRESH_TOKEN_SECRET=your-refresh-token-secret-key

# SMTP Email Settings (required for password reset email)
SMTP_HOST=your_smtp_host                    # SMTP server address (e.g., smtp.gmail.com)
SMTP_PORT=your_smtp_port_number            # SMTP port (e.g., 587)
SMTP_USER=your_smtp_username               # SMTP username (email address)
SMTP_PASSWORD=your_smtp_password           # SMTP password
SMTP_FROM_EMAIL=your_sender_email          # Sender email address (defaults to SMTP_USER if not set)
SMTP_USE_TLS=True                          # Whether to use TLS (default: True)
FRONTEND_URL=your_frontend_url             # Frontend URL (for password reset links, e.g., http://localhost:3000)
```

**3. Run the Server:**
Use `uv run` to execute the `uvicorn` web server within the virtual environment.

```bash
uv run uvicorn src.main:app --reload
```

The server will start, and on the first run, `init_db()` will be called to create the necessary database tables based on the SQLModels defined in `src/models`.

- **Swagger UI (API Docs)**: `http://localhost:8000/docs`
- **ReDoc (API Docs)**: `http://localhost:8000/redoc`

## 4. How to Add a New Feature (e.g., a "Product" resource)

1.  **Model (`src/models/`)**: Create a new `ProductInfo` class inheriting from `SQLModel` in a new `src/models/product.py` file. Add it to `src/db.py` so `init_db` recognizes it.
2.  **Value Object (`src/vos/`)**: Create `ProductVo` in `src/vos/product_vo.py`.
3.  **DAO (`src/dao/`)**: Create `ProductDAO` in `src/dao/product_dao.py` with static methods for database operations (`create_product`, `get_product_by_no`, etc.).
4.  **Messages (`src/messages/`)**: Create `ProductMessage` in `src/messages/product_message.py` for response messages.
5.  **Service (`src/services/`)**: Create `ProductService` in `src/services/product_service.py` to implement the business logic.
6.  **Router (`src/routers/`)**: Create `product_router.py` to define the `/products` endpoints.
7.  **Main App (`src/main.py`)**: Import and include the new `product_router` in the main FastAPI app.
