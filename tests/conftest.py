import pytest
import os
from src.db.database import Database


@pytest.fixture(autouse=True)
def setup_test_env():
    """Set up test environment variables"""
    os.environ["TICKETMASTER_API_KEY"] = "test_key"
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    yield
    if "TICKETMASTER_API_KEY" in os.environ:
        del os.environ["TICKETMASTER_API_KEY"]
    if "DATABASE_URL" in os.environ:
        del os.environ["DATABASE_URL"]


@pytest.fixture
def test_db():
    """Create a test database in memory"""
    db = Database("sqlite:///:memory:")
    db.create_tables()
    return db


@pytest.fixture
def sample_raw_event():
    """Factory to create sample raw events"""

    def _make_event(
        event_id="test_123", name="Test Event", min_price=30.0, max_price=100.0
    ):
        return {
            "id": event_id,
            "name": name,
            "url": f"https://example.com/{event_id}",
            "dates": {"start": {"dateTime": "2024-12-01T20:00:00Z"}},
            "classifications": [
                {"segment": {"name": "Music"}, "genre": {"name": "Rock"}}
            ],
            "priceRanges": [{"min": 50.0, "max": 150.0, "currency": "USD"}],
            "_embedded": {
                "venues": [
                    {
                        "name": "Venue 1",
                        "city": {"name": "Los Angeles"},
                        "state": {"stateCode": "CA"},
                    }
                ]
            },
        }

    return _make_event


@pytest.fixture
def sample_event():
    """Sample event for database testing"""
    from datetime import datetime
    from src.db.models import Event

    return Event(
        id="test_event_123",
        name="Test Concert",
        event_type="Music/Rock",
        start_date=datetime(2024, 12, 31, 20, 0, 0),
        venue_name="Test Venue",
        city="Los Angeles",
        state="CA",
        url="https://example.com/event",
    )
