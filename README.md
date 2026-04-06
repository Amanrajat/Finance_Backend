# Finance Management Backend API

A robust and scalable RESTful API backend for managing financial records and user portfolios. Built with Django REST Framework, featuring JWT authentication, role-based access control, and comprehensive filtering capabilities.

---
<!-- Swagger UI available at: -->
http://127.0.0.1:8000/swagger/

## Table of Contents

1. [Key Features](#key-features)
2. [Assumptions](#assumptions)
3. [Tech Stack](#tech-stack)
4. [Installation & Setup](#installation--setup)
5. [Running the Project](#running-the-project)
6. [Environment Configuration](#environment-configuration)
7. [API Base URL](#api-base-url)
8. [Authentication Flow](#authentication-flow)
9. [API Documentation](#api-documentation)
10. [Role-Based Access Control](#role-based-access-control)
11. [Filtering & Query Parameters](#filtering--query-parameters)
12. [Pagination](#pagination)
13. [Throttling](#throttling)
14. [Testing APIs](#testing-apis)
15. [Project Folder Structure](#project-folder-structure)
16. [Future Improvements](#future-improvements)
17. [Troubleshooting](#troubleshooting)
18. [Author](#author)

---

## Key Features

✅ **JWT Authentication** - Secure login with access and refresh tokens  
✅ **Role-Based Access Control** - Three-tier permission system (Admin, Analyst, Viewer)  
✅ **User Data Isolation** - Users can only access their own financial records  
✅ **Advanced Filtering** - Filter by category, type, date range, and more  
✅ **Search Functionality** - Search across categories and notes  
✅ **Pagination** - Efficient data retrieval with customizable page sizes  
✅ **Rate Throttling** - API rate limiting to prevent abuse  
✅ **API Documentation** - Interactive Swagger UI and ReDoc  
✅ **PostgreSQL Database** - Reliable relational data persistence  
✅ **RESTful Design** - Standard HTTP methods (GET, POST, PUT, DELETE)  
✅ **Custom Permissions** - Granular permission control based on roles  
✅ **Error Handling** - Comprehensive error responses with meaningful messages  

---

## Assumptions

The following assumptions have been made during the development of this API:

| Assumption | Description |
|------------|-------------|
| **Python Version** | Python 3.10+ is installed on your system |
| **Django Version** | Django 4.2+ is required for optimal performance |
| **DRF Version** | Django REST Framework 3.14+ supports all implemented features |
| **Database** | PostgreSQL 12+ is running and accessible |
| **Authentication** | All API requests (except login) require a valid JWT token |
| **User Isolation** | Each user's data is completely isolated; users cannot access other users' records |
| **Role Assignment** | Users are assigned one of three roles: admin, analyst, or viewer |
| **Record Ownership** | Every financial record is owned by exactly one user |
| **Timestamps** | `created_at` and `updated_at` are automatically managed by the system |
| **Inactive Users** | Inactive users cannot authenticate even if password is correct |
| **Token Expiry** | Access tokens expire after 60 minutes; refresh tokens after 7 days |
| **API Convention** | Snake_case is used for all JSON field names |
| **Timezone** | All timestamps are stored in UTC timezone |
| **Decimal Precision** | Financial amounts use Decimal fields with 10 digits, 2 decimal places |

---

## Tech Stack

### Backend Framework
- **Python** `3.10.x` or higher
- **Django** `4.2.x` or higher
- **Django REST Framework** `3.14.x` or higher

### Authentication & Security
- **django-rest-framework-simplejwt** `5.2.x` - JWT token management
- **python-dotenv** `0.21.x` - Environment variable management

### Database
- **PostgreSQL** `12.x` or higher
- **psycopg2-binary** `2.9.x` - PostgreSQL adapter

### Additional Libraries
- **django-filter** `23.x` - Advanced filtering capabilities
- **drf-yasg** `1.21.x` - Swagger/OpenAPI documentation

### Development Tools
- **Git** - Version control
- **pip** - Package management
- **virtualenv/venv** - Python virtual environment

---

## Installation & Setup

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10 or higher ([Download](https://www.python.org/downloads/))
- PostgreSQL 12 or higher ([Download](https://www.postgresql.org/download/))
- Git ([Download](https://git-scm.com/))
- pip (comes with Python)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/Amanrajat/Finance_Backend.git
cd finance-backend
```

#### 2. Create a Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. Create Environment Configuration File

Create a `.env` file in the project root directory:

```bash
# Security
SECRET_KEY=your-very-secure-secret-key-here-min-50-chars
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database Configuration
DB_ENGINE=django.db.backends.postgresql
DB_NAME=finance_db
DB_USER=postgres
DB_PASSWORD=your-secure-password
DB_HOST=localhost
DB_PORT=5432

# JWT Configuration
JWT_ACCESS_TOKEN_LIFETIME=15 minutes
JWT_REFRESH_TOKEN_LIFETIME=7 days
JWT_ALGORITHM=HS256

# API Settings
PAGE_SIZE=20
```

#### 5. Create PostgreSQL Database

**Using psql:**
```sql
-- Connect to PostgreSQL
psql -U postgres

-- Create database
CREATE DATABASE finance_db;

-- Create user (if not exists)
CREATE USER finance_user WITH PASSWORD 'your-secure-password';

-- Grant privileges
ALTER ROLE finance_user SET client_encoding TO 'utf8';
ALTER ROLE finance_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE finance_user SET default_transaction_deferrable TO on;
GRANT ALL PRIVILEGES ON DATABASE finance_db TO finance_user;

-- Exit psql
\q
```

**Or using pgAdmin (GUI tool):**
1. Open pgAdmin
2. Right-click on "Databases" → Create → Database
3. Enter database name as `finance_db`
4. Create a new login role with appropriate permissions

#### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

---

## Running the Project

### Start the Development Server

```bash
python manage.py runserver
```

You should see output similar to:
```
Starting development server at http://127.0.0.1:8000/
```

### Access the API

- **API Root:** http://localhost:8000/api/
- **Swagger Documentation:** http://localhost:8000/api/docs/swagger/
- **ReDoc Documentation:** http://localhost:8000/api/docs/redoc/
- **Admin Panel:** http://localhost:8000/admin/

### Verify Installation

Access the API root URL and you should see a list of available endpoints if everything is configured correctly.

---

## Environment Configuration

### Environment Variables Explained

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `SECRET_KEY` | String | Django secret key for security | `your-secret-key-min-50-chars` |
| `DEBUG` | Boolean | Enable/disable debug mode | `False` (Production only) |
| `ALLOWED_HOSTS` | String | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `DB_NAME` | String | PostgreSQL database name | `finance_db` |
| `DB_USER` | String | PostgreSQL username | `postgres` |
| `DB_PASSWORD` | String | PostgreSQL password | `secure-password` |
| `DB_HOST` | String | PostgreSQL host | `localhost` |
| `DB_PORT` | String | PostgreSQL port | `5432` |
| `JWT_ACCESS_TOKEN_LIFETIME` | Integer | Access token lifetime in seconds | `3600` |
| `JWT_REFRESH_TOKEN_LIFETIME` | Integer | Refresh token lifetime in seconds | `604800` |

### Security Best Practices

 **Important:** Never commit `.env` file to version control!

```bash
# Add to .gitignore
echo ".env" >> .gitignore
```

For production:
- Set `DEBUG=False`
- Use strong `SECRET_KEY` (minimum 50 characters)
- Specify all `ALLOWED_HOSTS`
- Use environment-specific settings
- Rotate tokens regularly
- Enable HTTPS only
- Use strong database passwords

---

## API Base URL

### Development
```
http://localhost:8000/api/
```

### Production
```
https://your-domain.com/api/
```

### API Version
Current API Version: `v1` (included in base URL where applicable)

---

## Authentication Flow

### Overview

The API uses **JWT (JSON Web Token) authentication**. To access protected endpoints, you must:

1. **Login** - Obtain access and refresh tokens
2. **Use Token** - Include token in request headers
3. **Refresh** - When access token expires, use refresh token to get new access token

### Step 1: Login and Get Tokens

**Endpoint:** `POST /api/users/login/`

**Request:**
```json
{
  "email": "user@example.com",
  "password": "your-password"
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "role": "analyst"
  }
}
```

**Error Response (401 Unauthorized):**
```json
{
  "detail": "Invalid email or password"
}
```

### Step 2: Make Authenticated Requests

Include the access token in the `Authorization` header:

```bash
curl -H "Authorization: Bearer <access_token>" \
  http://localhost:8000/api/records/
```

**Header Format:**
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Step 3: Refresh Access Token (When Expired)

**Endpoint:** `POST /api/users/token/refresh/`

**Request:**
```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Token Lifecycle

```
Access Token
├── Lifetime: 1 hour
├── Used for: API requests
└── Expires: Returns 401 Unauthorized

Refresh Token
├── Lifetime: 7 days
├── Used for: Getting new access tokens
└── Expires: User must login again
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `401 Unauthorized` | No token provided | Add `Authorization: Bearer <token>` header |
| `401 Unauthorized` | Invalid token | Login again to get new token |
| `401 Unauthorized` | Token expired | Use refresh token to get new access token |
| `403 Forbidden` | Insufficient permissions | Check user role and endpoint requirements |

---

## API Documentation

### Complete API Endpoints

#### **1. User Authentication APIs**

##### Login
```http
POST /api/users/login/
Content-Type: application/json

{
  "email": "analyst@example.com",
  "password": "SecurePassword123!"
}
```

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | String | Yes | User email address |
| `password` | String | Yes | User password |

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9...",
  "user": {
    "id": 2,
    "email": "analyst@example.com",
    "first_name": "Jane",
    "last_name": "Smith",
    "role": "analyst",
    "is_active": true
  }
}
```

**Response (401 Unauthorized):**
```json
{
  "detail": "Invalid email or password."
}
```

---

##### Refresh Access Token
```http
POST /api/users/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response (200 OK):**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9..."
}
```

---

#### **2. Records Management APIs**

##### Get All Records (with Filtering & Pagination)
```http
GET /api/records/?category=expense&type=food&page=1&page_size=20
Authorization: Bearer <access_token>
```

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `category` | String | No | Filter by category (case-insensitive) |
| `type` | String | No | Filter by type (e.g., income, expense) |
| `search` | String | No | Search in category and notes |
| `date_from` | String | No | Start date for date range (YYYY-MM-DD) |
| `date_to` | String | No | End date for date range (YYYY-MM-DD) |
| `page` | Integer | No | Page number (default: 1) |
| `page_size` | Integer | No | Records per page (default: 20, max: 100) |
| `ordering` | String | No | Sort by field (e.g., -created_at, amount) |

**Response (200 OK):**
```json
{
  "count": 150,
  "next": "http://localhost:8000/api/records/?page=2",
  "previous": null,
  "page_size": 20,
  "total_pages": 8,
  "records": [
    {
      "id": 1,
      "user": 2,
      "amount": 25.50,
      "category": "expense",
      "type": "food",
      "note": "Lunch at downtown restaurant",
      "transaction_date": "2026-04-06",
      "created_at": "2026-04-06T14:30:00Z",
      "updated_at": "2026-04-06T14:30:00Z"
    },
    {
      "id": 2,
      "user": 2,
      "amount": 1500.00,
      "category": "income",
      "type": "salary",
      "note": "Monthly salary",
      "transaction_date": "2026-04-01",
      "created_at": "2026-04-01T09:00:00Z",
      "updated_at": "2026-04-01T09:00:00Z"
    }
  ]
}
```

**Response (401 Unauthorized):**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

##### Get Single Record
```http
GET /api/records/{id}/
Authorization: Bearer <access_token>
```

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | Integer | Record ID |

**Response (200 OK):**
```json
{
  "id": 1,
  "user": 2,
  "amount": 25.50,
  "category": "expense",
  "type": "food",
  "note": "Lunch at downtown restaurant",
  "transaction_date": "2026-04-06",
  "created_at": "2026-04-06T14:30:00Z",
  "updated_at": "2026-04-06T14:30:00Z"
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Not found."
}
```

---

##### Create Record
```http
POST /api/records/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "amount": 50.00,
  "category": "expense",
  "type": "utilities",
  "note": "Monthly electricity bill",
  "transaction_date": "2026-04-06"
}
```

**Request Body:**
| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `amount` | Decimal | Yes | Transaction amount | > 0, max 2 decimals |
| `category` | String | Yes | Expense/Income category | min 3 chars, max 100 chars |
| `type` | String | Yes | Transaction type | max 50 chars |
| `note` | String | No | Additional notes | max 500 chars |
| `transaction_date` | Date | Yes | Date of transaction | Format: YYYY-MM-DD |

**Response (201 Created):**
```json
{
  "id": 125,
  "user": 2,
  "amount": 50.00,
  "category": "expense",
  "type": "utilities",
  "note": "Monthly electricity bill",
  "transaction_date": "2026-04-06",
  "created_at": "2026-04-06T15:45:00Z",
  "updated_at": "2026-04-06T15:45:00Z"
}
```

**Response (400 Bad Request):**
```json
{
  "amount": ["Ensure this field is greater than or equal to 0.01"],
  "category": ["This field is required."]
}
```

**Response (403 Forbidden):**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

---

##### Update Record
```http
PUT /api/records/{id}/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "amount": 75.00,
  "note": "Updated electricity bill amount"
}
```

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | Integer | Record ID |

**Request Body:** (Same as Create - all updateable fields)

**Response (200 OK):**
```json
{
  "id": 125,
  "user": 2,
  "amount": 75.00,
  "category": "expense",
  "type": "utilities",
  "note": "Updated electricity bill amount",
  "transaction_date": "2026-04-06",
  "created_at": "2026-04-06T15:45:00Z",
  "updated_at": "2026-04-06T16:20:00Z"
}
```

**Response (403 Forbidden):**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Not found."
}
```

---

##### Delete Record
```http
DELETE /api/records/{id}/
Authorization: Bearer <access_token>
```

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `id` | Integer | Record ID |

**Response (204 No Content):** (Empty body)

**Response (403 Forbidden):**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Not found."
}
```

---

#### **3. Dashboard APIs** (Read-Only)

##### Get Dashboard Summary
```http
GET /api/dashboard/summary/
Authorization: Bearer <access_token>
```

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `date_from` | String | Start date (YYYY-MM-DD) |
| `date_to` | String | End date (YYYY-MM-DD) |

**Response (200 OK):**
```json
{
  "total_income": 5000.00,
  "total_expense": 1200.50,
  "net_balance": 3799.50,
  "record_count": 45,
  "category_breakdown": {
    "expense": {
      "food": 340.00,
      "utilities": 150.00,
      "entertainment": 200.00,
      "transportation": 120.50
    },
    "income": {
      "salary": 5000.00
    }
  }
}
```

---

### API Response Format

All successful responses follow this format:

```json
{
  "status": "success",
  "data": { ... },
  "message": "Optional message"
}
```

All error responses follow this format:

```json
{
  "status": "error",
  "code": "ERROR_CODE",
  "message": "Error description",
  "details": { ... }
}
```

---

## Role-Based Access Control

### Role Definitions

| Role | Description | Access Level |
|------|-------------|--------------|
| **Admin** | Full system access with elevated privileges | Can create, read, update, delete all records |
| **Analyst** | Data modification rights with restrictions | Can create, read, update records; limited delete |
| **Viewer** | Read-only access | Can only view records; no modifications |

### Permission Matrix

| Operation | Endpoint | Admin | Analyst | Viewer | Public |
|-----------|----------|-------|---------|--------|--------|
| **Read Records** | `GET /api/records/` | ✅ | ✅ | ✅ | ❌ |
| **Create Record** | `POST /api/records/` | ✅ | ✅ | ❌ | ❌ |
| **Update Record** | `PUT /api/records/{id}/` | ✅ | ✅ | ❌ | ❌ |
| **Delete Record** | `DELETE /api/records/{id}/` | ✅ | ✅ | ❌ | ❌ |
| **Read Dashboard** | `GET /api/dashboard/summary/` | ✅ | ✅ | ✅ | ❌ |
| **Manage Users** | `POST /api/users/` | ✅ | ❌ | ❌ | ❌ |
| **Admin Panel** | `/admin/` | ✅ | ❌ | ❌ | ❌ |

### Assigning Roles

**Via Admin Panel:**
1. Login to http://localhost:8000/admin/
2. Navigate to Users
3. Select user
4. Set role dropdown
5. Save

**Via Django Shell:**
```bash
python manage.py shell

from apps.users.models import User
user = User.objects.get(email='user@example.com')
user.role = 'analyst'  # or 'admin', 'viewer'
user.save()
```

### Access Control Implementation

The API uses custom permission classes:

```python
# Permission classes used
from apps.records.permissions import IsAdminOrAnalyst

class RecordListCreateView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrAnalyst]
```

**Error when insufficient permission:**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

---

## Filtering & Query Parameters

### Supported Filters

#### Category Filter
Filter records by category field:
```bash
GET /api/records/?category=expense
GET /api/records/?category=income
```

#### Type Filter
Filter records by transaction type:
```bash
GET /api/records/?type=food
GET /api/records/?type=salary
```

#### Search Filter
Search across multiple fields (category, notes):
```bash
GET /api/records/?search=restaurant
GET /api/records/?search=salary
```

#### Date Range Filter
Filter records within date range:
```bash
GET /api/records/?date_from=2026-01-01&date_to=2026-03-31
```

**Date Format:** `YYYY-MM-DD`

#### Combined Filters
Combine multiple filters (AND logic):
```bash
GET /api/records/?category=expense&type=food&date_from=2026-04-01&date_to=2026-04-06&search=lunch
```

### Query Parameter Details

| Parameter | Type | Format | Example | Multiple Values |
|-----------|------|--------|---------|-----------------|
| `category` | String | Any string | `expense`, `income` | ❌ |
| `type` | String | Any string | `food`, `salary` | ❌ |
| `search` | String | Any string | `lunch`, `restaurant` | ❌ |
| `date_from` | Date | YYYY-MM-DD | `2026-04-01` | ❌ |
| `date_to` | Date | YYYY-MM-DD | `2026-04-30` | ❌ |
| `page` | Integer | Positive integer | `1`, `2`, `3` | ❌ |
| `page_size` | Integer | 1-100 | `10`, `50`, `100` | ❌ |

### Filter Examples

**All expenses in April:**
```bash
curl "http://localhost:8000/api/records/?category=expense&date_from=2026-04-01&date_to=2026-04-30" \
  -H "Authorization: Bearer <token>"
```

**All food-related transactions:**
```bash
curl "http://localhost:8000/api/records/?search=food" \
  -H "Authorization: Bearer <token>"
```

**Search with pagination:**
```bash
curl "http://localhost:8000/api/records/?search=lunch&page=2&page_size=10" \
  -H "Authorization: Bearer <token>"
```

---

## Pagination

### Overview

Pagination is enabled by default for list endpoints to improve performance and reduce data transfer.

### Default Settings

| Setting | Value | Configurable |
|---------|-------|--------------|
| **Default Page Size** | 20 records/page | ✅ Via query parameter |
| **Maximum Page Size** | 100 records/page | ✅ In settings |
| **Pagination Type** | Cursor-based offset | - |

### Pagination Response Format

```json
{
  "count": 150,
  "next": "http://localhost:8000/api/records/?page=2",
  "previous": null,
  "page_size": 20,
  "total_pages": 8,
  "records": [...]
}
```

**Response Fields:**
| Field | Type | Description |
|-------|------|-------------|
| `count` | Integer | Total number of records |
| `next` | String/Null | URL to next page |
| `previous` | String/Null | URL to previous page |
| `page_size` | Integer | Records on current page |
| `total_pages` | Integer | Total number of pages |
| `records` | Array | Array of data objects |

### Pagination Query Parameters

| Parameter | Type | Default | Min | Max | Description |
|-----------|------|---------|-----|-----|-------------|
| `page` | Integer | 1 | 1 | ∞ | Page number |
| `page_size` | Integer | 20 | 1 | 100 | Records per page |

### Pagination Examples

**Request first 20 records (default):**
```bash
curl "http://localhost:8000/api/records/" \
  -H "Authorization: Bearer <token>"
```

**Request second page:**
```bash
curl "http://localhost:8000/api/records/?page=2" \
  -H "Authorization: Bearer <token>"
```

**Request with custom page size (50 records/page):**
```bash
curl "http://localhost:8000/api/records/?page_size=50" \
  -H "Authorization: Bearer <token>"
```

**Navigate to last page:**
```bash
# Calculate: total_pages from response, then request that page
curl "http://localhost:8000/api/records/?page=8" \
  -H "Authorization: Bearer <token>"
```

### Pagination Flow

1. **First Request** → Returns page 1, total_pages=8, next URL
2. **Follow `next` URL** → Returns page 2, previous URL
3. **Continue** → Until `next` is null (last page reached)

---

## Throttling

### Overview

Rate throttling protects the API from abuse by limiting request frequency per user/IP.

### Throttle Rates

| Endpoint | Rate | Time Window | Description |
|----------|------|-------------|-------------|
| `/users/login/` | 5 requests | 1 minute | Prevents brute-force attacks |
| `/users/register/` | 10 requests | 1 hour | Prevents spam registration |
| `/records/` (GET) | 100 requests | 1 minute | Safe operation (read-only) |
| `/records/` (POST/PUT/DELETE) | 30 requests | 1 minute | Write operations |

### Throttle Scope

Throttling is applied **per user** (authenticated) and **per IP** (unauthenticated).

### Throttle Response

When rate limit exceeded:

```
HTTP/1.1 429 Too Many Requests

{
  "detail": "Request was throttled. Expected available in 45 seconds."
}
```

**Response Headers:**
```
Retry-After: 45
```

### Handling Throttled Requests

**Example - Login Throttling:**
```bash
# Request 1-5: Success (200)
curl -X POST http://localhost:8000/api/users/login/ ...

# Request 6: Throttled (429)
{
  "detail": "Request was throttled. Expected available in 60 seconds."
}

# Wait 60 seconds, then retry
sleep 60
curl -X POST http://localhost:8000/api/users/login/ ...
```

### Best Practices

✅ **DO:**
- Implement exponential backoff for retries
- Cache responses when possible
- Use batch operations when available
- Monitor Retry-After headers

❌ **DON'T:**
- Retry immediately after throttling
- Make requests in rapid succession
- Bypass throttling with different IPs
- Ignore rate limit warnings

### Configuring Throttle Rates

Edit `config/settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_RATES': {
        'login': '10/minute',      # Change from 5 to 10
        'records': '200/minute',   # Change from 100 to 200
    }
}
```

---

## Testing APIs

### Option 1: Swagger UI (Interactive Documentation)

**Access:** http://localhost:8000/api/docs/swagger/

**Steps:**
1. Navigate to Swagger URL
2. Click "Authorize" button
3. Paste your access token
4. Try different endpoints directly in browser

**Advantages:**
- Interactive requests without code
- Real-time API documentation
- Built-in schema validation
- Automatic response examples

**Visual Guide:**
```
[Authorize Button] → Paste Token → [Try it out Button] → [Execute]
```

### Option 2: ReDoc (Alternative Documentation)

**Access:** http://localhost:8000/api/docs/redoc/

Similar to Swagger but with read-only documentation focused on reference.

### Option 3: Postman (Recommended for Advanced Testing)

**Setup:**
1. Download [Postman](https://www.postman.com/downloads/)
2. Create new collection "Finance API"
3. Add requests (see below)

**Step 1 - Login Request:**
```
Method: POST
URL: http://localhost:8000/api/users/login/

Headers:
  Content-Type: application/json

Body (raw JSON):
{
  "email": "analyst@example.com",
  "password": "SecurePassword123!"
}
```

**Step 2 - Set Token Variable:**
After login, copy access token and set as variable:
```
In Postman: Settings → Variables (tab)
Create variable: token = <paste_access_token_here>
```

**Step 3 - Get Records with Token:**
```
Method: GET
URL: http://localhost:8000/api/records/

Headers:
  Authorization: Bearer {{token}}
  Content-Type: application/json
```

**Step 4 - Create Record:**
```
Method: POST
URL: http://localhost:8000/api/records/

Headers:
  Authorization: Bearer {{token}}
  Content-Type: application/json

Body (raw JSON):
{
  "amount": 50.00,
  "category": "expense",
  "type": "utilities",
  "note": "Monthly electricity",
  "transaction_date": "2026-04-06"
}
```

### Option 4: Curl Commands (Command Line)

**Login:**
```bash
curl -X POST http://localhost:8000/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "analyst@example.com",
    "password": "SecurePassword123!"
  }'
```

**Save Token:**
```bash
export TOKEN="<access_token_from_response>"
```

**Get Records:**
```bash
curl -X GET http://localhost:8000/api/records/ \
  -H "Authorization: Bearer $TOKEN"
```

**Create Record:**
```bash
curl -X POST http://localhost:8000/api/records/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 50.00,
    "category": "expense",
    "type": "utilities",
    "note": "Monthly electricity",
    "transaction_date": "2026-04-06"
  }'
```

### Option 5: Python Requests (Programmatic Testing)

**Example Script:**
```python
import requests
import json

BASE_URL = "http://localhost:8000/api"

# 1. Login
login_response = requests.post(
    f"{BASE_URL}/users/login/",
    json={
        "email": "analyst@example.com",
        "password": "SecurePassword123!"
    }
)

access_token = login_response.json()["access"]
headers = {"Authorization": f"Bearer {access_token}"}

# 2. Get Records
records_response = requests.get(
    f"{BASE_URL}/records/",
    headers=headers
)
print(json.dumps(records_response.json(), indent=2))

# 3. Create Record
create_response = requests.post(
    f"{BASE_URL}/records/",
    headers=headers,
    json={
        "amount": 50.00,
        "category": "expense",
        "type": "utilities",
        "note": "Monthly electricity",
        "transaction_date": "2026-04-06"
    }
)
print(json.dumps(create_response.json(), indent=2))
```

### Testing Checklist

- ✅ Authentication (login, token refresh)
- ✅ Create records with valid data
- ✅ Create records with invalid data (error handling)
- ✅ Retrieve records with filters
- ✅ Update own records
- ✅ Delete own records
- ✅ Access control (test different roles)
- ✅ Pagination (test page navigation)
- ✅ Search functionality
- ✅ Date range filtering
- ✅ Rate limiting (send multiple requests quickly)
- ✅ Error messages (try invalid tokens)

---

## Project Folder Structure

```
finance_backend/
│
├── apps/                           # Django applications
│   ├── common/                     # Shared utilities
│   │   ├── __init__.py
│   │   ├── admin.py               # Admin panel registration
│   │   ├── apps.py
│   │   ├── models.py              # Shared models
│   │   ├── pagination.py          # Custom pagination class
│   │   ├── permissions.py         # Custom permission classes
│   │   ├── tests.py
│   │   ├── views.py               # Shared views
│   │   └── migrations/
│   │       └── __init__.py
│   │
│   ├── users/                      # User management app
│   │   ├── __init__.py
│   │   ├── admin.py               # User admin configuration
│   │   ├── apps.py
│   │   ├── jwt.py                 # JWT token configuration
│   │   ├── managers.py            # Custom user manager
│   │   ├── middleware.py          # Custom middleware
│   │   ├── models.py              # User model
│   │   ├── permissions.py         # User-specific permissions
│   │   ├── serializers.py         # User serializers
│   │   ├── tests.py               # User tests
│   │   ├── throttles.py           # User throttle classes
│   │   ├── urls.py                # User URL routing
│   │   ├── views.py               # User views (login, etc)
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   │
│   ├── records/                    # Financial records app
│   │   ├── __init__.py
│   │   ├── admin.py               # Records admin
│   │   ├── apps.py
│   │   ├── models.py              # Record model
│   │   ├── permissions.py         # Record-level permissions
│   │   ├── serializers.py         # Record serializers
│   │   ├── tests.py               # Record tests
│   │   ├── throttles.py           # Record throttle classes
│   │   ├── urls.py                # Record URL routing
│   │   ├── views.py               # Record CRUD views
│   │   └── migrations/
│   │       ├── __init__.py
│   │       └── 0001_initial.py
│   │
│   └── dashboard/                  # Analytics/dashboard app
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── throttles.py
│       ├── urls.py
│       ├── views.py               # Dashboard summary views
│       └── migrations/
│           ├── __init__.py
│           └── 0001_initial.py
│
├── config/                         # Django project settings
│   ├── __init__.py
│   ├── asgi.py                    # ASGI configuration (async)
│   ├── settings.py                # Main settings file
│   ├── urls.py                    # Project URL configuration
│   └── wsgi.py                    # WSGI configuration (production)
│
├── manage.py                       # Django management command
├── requirements.txt                # Python dependencies
├── .env.example                    # Example environment variables
├── .env                            # Environment variables (gitignored)
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
└── db.sqlite3                      # Development database (if using SQLite)
```

### Key Folders Explained

| Folder | Purpose |
|--------|---------|
| `apps/` | Django applications with business logic |
| `config/` | Django project configuration |
| `apps/users/` | Authentication and user management |
| `apps/records/` | Financial records CRUD operations |
| `apps/dashboard/` | Analytics and summary endpoints |
| `apps/common/` | Shared utilities (pagination, permissions) |

---

## Future Improvements

### Phase 1: Enhanced Features
- [ ] **Export Functionality** - CSV/Excel export for records
- [ ] **Recurring Records** - Automated recurring transaction creation
- [ ] **Categories Management** - API for managing custom categories
- [ ] **Budget Management** - Set budgets with alerts
- [ ] **Advanced Analytics** - Trend analysis, forecasting
- [ ] **Multi-Currency Support** - Handle multiple currencies with conversion

### Phase 2: User Experience
- [ ] **Webhooks** - Real-time event notifications
- [ ] **Email Notifications** - Budget alerts, summary emails
- [ ] **Mobile API** - Optimized endpoints for mobile apps
- [ ] **Bulk Operations** - Batch create/update/delete
- [ ] **Audit Logging** - Track all data changes
- [ ] **Data Import** - Import from CSV/Excel

### Phase 3: Security & Compliance
- [ ] **Two-Factor Authentication (2FA)** - Enhanced security
- [ ] **API Key Authentication** - Alternative auth method
- [ ] **Encryption at Rest** - Sensitive data encryption
- [ ] **GDPR Compliance** - Data deletion/export endpoints
- [ ] **Audit Trail** - Complete activity logging
- [ ] **Rate Limiting by Endpoint** - More granular throttling

### Phase 4: Infrastructure
- [ ] **Caching Layer** - Redis integration
- [ ] **Search Engine** - Elasticsearch integration
- [ ] **Async Tasks** - Celery for background jobs
- [ ] **Database Replication** - High availability setup
- [ ] **API Version Management** - Multiple API versions
- [ ] **Documentation Generation** - Auto-generated API docs

### Phase 5: Performance
- [ ] **Query Optimization** - Database indexing
- [ ] **Response Compression** - GZIP compression
- [ ] **CDN Integration** - Scale static content
- [ ] **Database Sharding** - Horizontal scaling
- [ ] **Load Balancing** - Multiple server instances
- [ ] **Performance Monitoring** - APM integration (NewRelic, DataDog)

---

## Troubleshooting

### Common Issues & Solutions

#### Issue 1: Cannot Connect to PostgreSQL
**Error Message:**
```
django.db.utils.OperationalError: could not connect to server
```

**Solutions:**
1. Verify PostgreSQL is running:
   ```bash
   # Windows
   Get-Service postgresql*
   
   # macOS
   brew services list | grep postgres
   
   # Linux
   systemctl status postgresql
   ```

2. Check database credentials in `.env`
3. Verify database exists:
   ```sql
   psql -U postgres -l
   ```
4. Restart PostgreSQL service

---

#### Issue 2: Export Error: `No module named 'dotenv'`
**Error Message:**
```
ModuleNotFoundError: No module named 'dotenv'
```

**Solution:**
```bash
pip install python-dotenv
pip freeze > requirements.txt
```

---

#### Issue 3: Migrations Not Applied
**Error Message:**
```
django.core.exceptions.ImproperlyConfigured
```

**Solution:**
```bash
python manage.py makemigrations apps.users apps.records apps.dashboard
python manage.py migrate
```

---

#### Issue 4: JWT Token Invalid/Expired
**Error Message:**
```json
{
  "detail": "Given token not valid for any token type"
}
```

**Solution:**
1. Login again to get new token
2. Check token hasn't expired:
   ```bash
   pip install PyJWT
   python -c "import jwt; print(jwt.decode('<token>', options={'verify_signature': False}))"
   ```

---

#### Issue 5: Permission Denied on Record Operations
**Error Message:**
```json
{
  "detail": "You do not have permission to perform this action."
}
```

**Solutions:**
1. Verify user role:
   ```bash
   python manage.py shell
   from apps.users.models import User
   user = User.objects.get(email='user@example.com')
   print(user.role)
   ```

2. Change role to analyst or admin:
   ```bash
   user.role = 'analyst'
   user.save()
   ```

---

#### Issue 6: Port 8000 Already in Use
**Error Message:**
```
Error: That port is already in use.
```

**Solution:**
```bash
# Find process using port 8000
# Windows
netstat -ano | findstr :8000

# macOS/Linux
lsof -i :8000

# Kill process or use different port
python manage.py runserver 8001
```

---

#### Issue 7: Static Files Not Loading
**Error Message:**
```
GET /static/... 404 Not Found
```

**Solution:**
```bash
python manage.py collectstatic --noinput
```

---

#### Issue 8: Database Not Created
**Error Message:**
```
FATAL: database "finance_db" does not exist
```

**Solution:**
```sql
psql -U postgres
CREATE DATABASE finance_db;
\q
```

Then run migrations:
```bash
python manage.py migrate
```

---

## Additional Resources

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Tools & Extensions
- [Postman API Client](https://www.postman.com/)
- [VS Code REST Client Extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
- [Thunder Client (VS Code)](https://www.thunderclient.com/)
- [Insomnia REST Client](https://insomnia.rest/)

### Learning Resources
- [Real Python - Django](https://realpython.com/tutorials/django/)
- [DRF Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)
- [JWT Concepts](https://jwt.io/introduction)

---

## Author

**Finance Management Backend API**

Created with ❤️ by the Development Team

### Contact & Support
- **Email:** support@example.com
- **Issues & Feature Requests:** [GitHub Issues](https://github.com/yourusername/finance-backend/issues)
- **Documentation:** See this README and Swagger UI
- **Live Demo:** https://finance-api.example.com (if available)

### Contributing
Contributions are welcome! Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

### License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-04-06 | Initial release with core functionality |

---

## Support

For issues, questions, or suggestions:
1. Check [Troubleshooting](#troubleshooting) section
2. Review [API Documentation](#api-documentation)
3. Check existing [GitHub Issues](https://github.com/yourusername/finance-backend/issues)
4. Create new issue with detailed description

---

**Last Updated:** April 6, 2026  
**Status:** Active Development ✅
