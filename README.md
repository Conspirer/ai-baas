AI Backend as a Service (AI-BaaS)
Overview

AI-BaaS is a production-ready backend service that provides authenticated, rate-limited access to AI endpoints.
It is designed to mirror how real AI platforms (e.g. OpenAI, Stripe-style APIs) handle authentication, API keys, usage tracking, and rate limiting.

The project focuses on backend engineering fundamentals rather than model inference, emphasizing correctness, security, and scalability.




Key Features

JWT-based user authentication for human access

Secure API key system for machine-to-machine communication

Hashed API key storage (raw keys never persisted)

Per-API-key rate limiting using a sliding time window

PostgreSQL-backed usage tracking

Usage analytics endpoint (total usage, 24h usage, per-key breakdown)

Stateless backend architecture

Cloud-deployed with managed PostgreSQL





Architecture:

Client
  └── FastAPI
        ├── JWT Authentication (humans)
        ├── API Key Authentication (machines)
        ├── Rate Limiter
        ├── Usage Tracker
        └── PostgreSQL




Authentication Model

User Authentication (JWT):-

Users authenticate via email & password

Passwords are hashed using bcrypt

JWTs are short-lived and sent via the Authorization header

Used for dashboard-style endpoints (e.g. /usage, /api-keys)



API Key Authentication:-

Users can generate API keys

Raw API keys are shown once and never stored

Only hashed API keys are persisted

API keys authenticate requests via headers (e.g. X-API-Key)

Designed for scripts, services, and integrations



Rate Limiting & Usage Tracking

Rate limiting is enforced per API key, not per user

Requests are tracked in a dedicated api_usage table

Sliding window strategy (e.g. X requests per hour)

Usage analytics include:

Total requests

Requests in the last 24 hours

Per-API-key usage breakdown

This mirrors real SaaS billing and abuse-prevention patterns.



Tech Stack

Backend: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Auth: JWT (python-jose), Passlib (bcrypt)

Deployment: Railway

Configuration: Environment variables



Deployment

Deployed on Railway

Managed PostgreSQL instance

Secrets and configuration injected via environment variables

No hardcoded credentials

.env used only for local development



Future Improvements

API key revocation and rotation

Daily/monthly usage quotas

Admin endpoints

Billing integration

Observability (metrics, tracing)

Horizontal scaling with Redis-based rate limiting



License
MIT