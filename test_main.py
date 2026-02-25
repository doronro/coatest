"""
QA Test Suite for FastAPI Hello World Application
Tests the GET "/" endpoint for correctness, response shape, and HTTP compliance.
"""

import os

os.environ["ENABLE_DOCS"] = "true"

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestRootEndpoint:
    """Tests for the GET / endpoint."""

    def test_happy_path_status_200(self):
        """Endpoint must return HTTP 200 OK."""
        response = client.get("/")
        assert response.status_code == 200, (
            f"Expected 200, got {response.status_code}"
        )

    def test_response_is_json(self):
        """Endpoint must return a JSON content-type."""
        response = client.get("/")
        content_type = response.headers.get("content-type", "")
        assert "application/json" in content_type, (
            f"Expected application/json content-type, got: {content_type}"
        )

    def test_response_body_structure(self):
        """Response body must be a JSON object with 'message' and 'subtitle' keys."""
        response = client.get("/")
        body = response.json()
        assert isinstance(body, dict), f"Expected dict, got {type(body)}"
        assert "message" in body, f"'message' key missing from response: {body}"
        assert "subtitle" in body, f"'subtitle' key missing from response: {body}"

    def test_response_body_value(self):
        """The 'message' value must be exactly 'Hello World'."""
        response = client.get("/")
        body = response.json()
        assert body["message"] == "Hello World", (
            f"Expected 'Hello World', got '{body.get('message')}'"
        )

    def test_subtitle_field_value(self):
        """The 'subtitle' value must be exactly 'Version Test'."""
        response = client.get("/")
        body = response.json()
        assert "subtitle" in body, f"'subtitle' key missing from response: {body}"
        assert body["subtitle"] == "Version Test", (
            f"Expected 'Version Test', got '{body.get('subtitle')}'"
        )

    def test_no_extra_keys_in_response(self):
        """Response should contain only the expected keys (no accidental leakage)."""
        response = client.get("/")
        body = response.json()
        expected_keys = {"message", "subtitle"}
        extra_keys = set(body.keys()) - expected_keys
        assert not extra_keys, f"Unexpected extra keys in response: {extra_keys}"

    def test_post_method_not_allowed(self):
        """POST to / should return 405 Method Not Allowed."""
        response = client.post("/")
        assert response.status_code == 405, (
            f"Expected 405 for POST /, got {response.status_code}"
        )

    def test_put_method_not_allowed(self):
        """PUT to / should return 405 Method Not Allowed."""
        response = client.put("/")
        assert response.status_code == 405, (
            f"Expected 405 for PUT /, got {response.status_code}"
        )

    def test_delete_method_not_allowed(self):
        """DELETE to / should return 405 Method Not Allowed."""
        response = client.delete("/")
        assert response.status_code == 405, (
            f"Expected 405 for DELETE /, got {response.status_code}"
        )

    def test_unknown_route_returns_404(self):
        """A request to an undefined route should return 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404, (
            f"Expected 404 for unknown route, got {response.status_code}"
        )

    def test_response_is_idempotent(self):
        """Multiple GET requests must return identical responses."""
        r1 = client.get("/")
        r2 = client.get("/")
        assert r1.json() == r2.json(), "Responses differ between calls — non-deterministic behavior detected"
        assert r1.status_code == r2.status_code, "Status codes differ between calls"

    def test_openapi_schema_available(self):
        """FastAPI should expose an OpenAPI schema at /openapi.json."""
        response = client.get("/openapi.json")
        assert response.status_code == 200, (
            f"OpenAPI schema endpoint unavailable: {response.status_code}"
        )

    def test_docs_available(self):
        """FastAPI should expose Swagger UI at /docs."""
        response = client.get("/docs")
        assert response.status_code == 200, (
            f"Swagger docs endpoint unavailable: {response.status_code}"
        )
