# Home Services Booking System

## Overview
This project is a minimal full-stack implementation of a home services
marketplace booking system. It demonstrates how to design and implement
real-world booking lifecycle management, provider workflows, failure
handling, manual intervention, and observability.

The focus is on backend correctness, state management, and operational
visibility rather than UI polish.

---

## Tech Stack
- Backend: Django + Django REST Framework
- Frontend: React (Create React App)
- Database: SQLite (default Django database)
- API Style: REST

---

## Core Features Implemented

### 1. Create a Booking
- Customers can create a booking by providing:
  - Customer name
  - Service type
- New bookings are created in the `PENDING` state.

---

### 2. Provider Assignment
- Providers are automatically assigned to bookings.
- If no provider is available, the system fails gracefully and returns
  a clear error response.

---

### 3. Partner / Provider Workflow
- Providers can:
  - View assigned bookings
  - Accept a booking (transition to `IN_PROGRESS`)
  - Reject a booking (transition to `REJECTED`)
- Provider rejections are logged and visible in booking history.

---

### 4. Booking Lifecycle Management
The system enforces a controlled booking state machine:

PENDING → ASSIGNED → IN_PROGRESS → COMPLETED

yaml
Copy code

Additional states:
- CANCELLED
- REJECTED

Invalid state transitions are blocked at the backend to ensure
data consistency and integrity.

---

### 5. Failure Handling
- Customer cancellations supported
- Provider rejections supported
- Provider no-shows handled via admin override
- Failed or invalid operations return clear API errors
- Retry is supported by allowing re-assignment of providers
  for rejected or failed bookings
- All failures are recorded as booking events

---

### 6. Manual Intervention (Admin / Ops)
- Admin/Ops can override booking states using backend APIs
- Manual actions are logged with actor information
- Simulates real-world operational workflows

---

### 7. Observability
- Every booking state change generates a `BookingEvent`
- Booking history is visible in the UI
- Event logs include:
  - Previous state
  - New state
  - Actor (system / admin / provider)
  - Timestamp

---

## UI Screens
- Create booking screen
- View all bookings
- Update booking status
- View booking event logs
- Simple admin/ops-style controls

The UI is intentionally minimal to focus on system behavior.

---

## API Overview

Base URL: `http://localhost:8000`

- `GET  /api/bookings/`
- `POST /api/bookings/create/`
- `POST /api/bookings/<id>/assign/`
- `POST /api/bookings/<id>/status/`
- `GET  /api/bookings/<id>/events/`
- `GET  /api/health/`

A root endpoint (`/`) exposes API metadata and available routes.

---

## How to Run the Project

### Backend
```bash
cd backend/core
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
Frontend
bash
Copy code
cd frontend
npm install
npm start
Frontend runs on:

arduino
Copy code
http://localhost:3000
Backend runs on:

arduino
Copy code
http://localhost:8000
Sample Data
To add sample providers for testing:

bash
Copy code
python manage.py shell
python
Copy code
from bookings.models import Provider

Provider.objects.bulk_create([
    Provider(name="Provider A"),
    Provider(name="Provider B"),
    Provider(name="Provider C"),
])
How to Review Quickly
Start backend and frontend

Open http://localhost:3000

Create a booking

Assign a provider

Move booking through lifecycle states

Open “View Events” to inspect booking history

Design Decisions & Trade-offs
Authentication is intentionally omitted to keep focus on core logic

UI is minimal by design

All state transitions are enforced at the backend

Single provider auto-assignment chosen for simplicity

Future Improvements
Authentication and authorization

Provider availability scheduling

Retry logic using background jobs/queues

Notifications (Email/SMS)

Pagination and filtering

Conclusion
This project demonstrates a realistic slice of a home services
marketplace system, focusing on booking lifecycle correctness,
failure handling, operational control, and observability.