import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    # Arrange
    email = "student@lpu.in"

    # Act
    result = is_valid_email(email)

    # Assert
    assert result == True


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    # Arrange
    phone = "555-123-4567"

    # Act
    result = is_valid_phone(phone)

    # Assert
    assert result == True


def test_mask_email_basic():
    """Test masking a typical email address."""
    # Arrange
    email = "priya@example.com"

    # Act
    result = mask_email(email)

    # Assert
    assert result == "pr***@example.com"


def test_mask_email_invalid_raises_value_error():
    """Test invalid emails raise ValueError."""
    with pytest.raises(ValueError):
        mask_email("not-an-email")


def test_mask_email_short_local():
    """Test masking when the local part is shorter than three characters."""
    result = mask_email("a@example.com")
    assert result == "a@example.com"


def test_is_valid_phone_type_error():
    """Test that a non-string phone raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_phone(12345)


def test_normalize_phone_valid_and_invalid():
    """Test phone normalization and invalid input handling."""
    assert normalize_phone("555-123-4567") == "5551234567"
    with pytest.raises(ValueError):
        normalize_phone("123")
