# mynext-e2e-test-suite

E2E test suite repository for testing the evaluator-worker service.

## Purpose

This minimal Python project is designed to test `test_suite` evaluations in the evaluator-worker. It contains a multi-stage Dockerfile with a `test` stage and simple pytest tests.

## Branches

- **main**: All tests pass
- **failing-tests**: Contains intentionally failing tests for E2E testing failure scenarios

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

