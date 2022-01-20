"""Fixtures for IntelliFire integration tests."""
from collections.abc import Generator
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock, None, None]:
    """Mock setting up a config entry."""
    with patch(
        "homeassistant.components.intellifire.async_setup_entry", return_value=True
    ) as mock_setup:
        yield mock_setup


@pytest.fixture
def mock_intellifire_config_flow() -> Generator[None, MagicMock, None]:
    """Return a mocked IntelliFire client."""
    data_mock = Mock()
    data_mock.serial = "12345"

    with patch(
        "homeassistant.components.intellifire.config_flow.IntellifireAsync",
        autospec=True,
    ) as intellifire_mock:
        intellifire = intellifire_mock.return_value
        intellifire.data = data_mock
        yield intellifire
