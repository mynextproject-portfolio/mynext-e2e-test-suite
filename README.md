# mynext-e2e-test-suite

> **Note for Users:** This is an internal repository used for E2E testing of the MyNextProject platform itself. If you're a student or user of the platform, you can safely ignore this repo. However, feel free to explore the code if you're curious about testing practices, and ask on our Discord if you'd like to learn more about how our testing infrastructure works!

## Purpose

This minimal Python project is used for automated testing of the platform's evaluation infrastructure. It contains a multi-stage Dockerfile with a `test` stage and simple pytest tests to verify that our systems correctly handle both passing and failing test scenarios.

## Branches

- **main**: All tests pass (used to verify successful test execution)
- **failing-tests**: Contains intentionally failing tests (used to verify failure handling)

## Structure

- `src/main.py` - Simple functions to test
- `tests/test_passing.py` - Tests that always pass
- `tests/test_failing.py` - Tests that can be configured to fail
- `Dockerfile` - Multi-stage Dockerfile with test, production stages

## Docker Build

```bash
# Build and run tests
docker build --target test -t mynext-e2e-test:test .

# Run the test container
docker run mynext-e2e-test:test
```

## Local Testing

```bash
# Install dependencies
pip install -e ".[test]"

# Run tests
pytest -v
```

