# AI Story Creator

An interactive application that uses AI to help users create personalized children's stories with their own photos.

## Project Overview

The AI Story Creator allows users to:
- Upload photos of themselves or their children
- Select from various story themes and settings
- Generate personalized AI stories featuring their uploaded images
- View, save, and share the created stories

## Repository Structure

This project uses a monorepo structure with the following main directories:

```
ai-story-creator/
├── frontend/     # Flutter application
├── backend/      # FastAPI service
├── .github/      # GitHub configuration files
```

## Development Workflow

### Branching Strategy

The project follows a Gitflow-lite branching model:

- `main`: Production-ready code
- `develop`: Integration branch for feature development
- `feature/feature-name`: Individual feature branches

### Pull Requests

All code changes must be submitted via pull requests that:
- Reference a Notion task ID
- Include appropriate tests
- Provide screenshots for UI changes
- Pass CI checks

## Setup Instructions

### Prerequisites

- Backend: Python 3.9+
- Frontend: Flutter 3.0+
- Docker & Docker Compose (for local development)

### Getting Started

Detailed setup instructions for both frontend and backend will be added as the project progresses.

## Contributing

Please see the [PR template](.github/pull_request_template.md) for guidelines on contributing to this project.