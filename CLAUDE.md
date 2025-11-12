# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This project uses Poetry for dependency management and Invoke for task automation.

### Testing
- `invoke test` - Run unit tests
- `invoke test --coverage` - Run unit tests with coverage report
- `poetry run pytest` - Run tests directly with Poetry

### Code Quality
- `invoke lint` - Run ruff linter (check only)
- `invoke lint --fix` - Run ruff linter with auto-fix
- `invoke formatter` - Check code formatting with black
- `invoke formatter --fix` - Format code with black
- `invoke staticcheck` - Run mypy type checking
- `invoke isort` - Run import sorting

### Build & Package
- `invoke build` - Build the package with Poetry
- `poetry build` - Direct Poetry build command

### Dependencies
- `invoke update` - Update all dependencies
- `invoke outdated` - Show outdated packages
- `invoke audit` - Run security audit with safety

## Architecture Overview

This is the AI21 Labs Python SDK, a comprehensive client library for interacting with AI21's language models across multiple deployment platforms.

### Core Client Structure
- **Studio Client** (`ai21.AI21Client`): Primary client for AI21 Studio API
- **Bedrock Client** (`ai21.AI21BedrockClient`): AWS Bedrock integration
- **Azure Client** (`ai21.AI21AzureClient`): Azure AI Studio integration  
- **Vertex Client** (`ai21.AI21VertexClient`): Google Cloud Vertex AI integration
- **Launchpad Client** (`ai21.AI21LaunchpadClient`): AI21 Launchpad platform

All clients support both synchronous and asynchronous operations with corresponding `Async*` variants.

### Key Features
- **Chat Completions**: Modern chat-based API with support for system/user/assistant roles
- **Maestro**: AI Planning & Orchestration System for enterprise workflows
- **Conversational RAG**: Chat with document retrieval from Studio library
- **Streaming**: Real-time response streaming for chat completions
- **File Management**: Upload and manage documents in Studio library

### Module Organization
- `ai21/clients/` - Platform-specific client implementations
- `ai21/models/` - Pydantic models for requests/responses
- `ai21/http_client/` - HTTP layer with retry logic and error handling
- `ai21/stream/` - Streaming response handling
- `ai21/errors.py` - Custom exception hierarchy
- `examples/` - Usage examples for all platforms and features

### Client Resources
Each client exposes resources through attributes:
- `client.chat.completions` - Chat completion API
- `client.beta.maestro.runs` - Maestro orchestration
- `client.library.files` - File upload/management
- `client.beta.conversational_rag` - RAG functionality

### Environment Configuration
The SDK uses `AI21EnvConfig` for environment-based configuration supporting:
- `AI21_API_KEY` - Authentication
- `AI21_API_HOST` - Custom API endpoints
- `AI21_TIMEOUT_SEC` - Request timeouts
- `AI21_NUM_RETRIES` - Retry configuration
- `AI21_LOG_LEVEL` - Logging verbosity

### Testing Structure
- `tests/unittests/` - Unit tests with mocking
- `tests/integration_tests/` - Live API integration tests
- Uses pytest with async support and mock fixtures