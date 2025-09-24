# Spotify API Testing with OAuth 2.0

**Technologies:** REST API, OAuth 2.0, JSON, HTTP Methods, Python, pytest, Postman

## Project Overview

This project demonstrates testing of Spotify's API, covering OAuth 2.0 authentication, HTTP GET/POST/PUT requests, error handling, data validation, and edge case testing.

## Features

* OAuth 2.0 authentication handling
* GET, POST, PUT request validation
* Edge case and negative scenario testing
* Automated test execution via Python (`pytest`)
* Postman collection for visual API testing

## Repository Structure

```
utils/        --> Helper functions for token and requests
tests/        --> Python test scripts
Postman/      --> Postman collection & environment
requirements.txt --> Python dependencies
.gitignore    --> Git ignore configuration
```

## Python Tests

### Setup

1. Clone repository:

```bash
git clone https://github.com/yourusername/spotify-api-testing.git
cd spotify-api-testing
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Spotify credentials:

```env
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

4. Run tests:

```bash
pytest tests/
```

## Postman Testing

1. Import `Postman/Spotify API Testing.postman_collection.json` into Postman.
2. Import `Postman/Spotify API Testing.postman_environment.json` into Postman.
3. Update environment variables with your Spotify credentials.
4. Run the `Get Access Token` request first, then run other requests.

## Test Coverage

* Authentication
* Endpoint functionality
* Edge cases and error handling
* Invalid method/endpoint handling

## Future Improvements

* CI/CD integration for automated testing
* Expanded security and rate-limit tests
