# WMS Logs Service

Service for storing logs for various actions such as execution steps, validation outcomes, and deployment statuses in the workflow management system.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/mydb
```

3. Run the service:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- GET /logs - List all logs
- POST /logs - Create a new log
- GET /logs/{log_id} - Retrieve a log by ID
- PUT /logs/{log_id} - Update an existing log
- DELETE /logs/{log_id} - Delete a log by ID