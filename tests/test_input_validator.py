from datetime import datetime
import re
import pytest
from utils.input_validation import InputValidator


def test_validate_non_empty_string():
    input_validator = InputValidator()
    assert input_validator.validate_non_empty_string("test") == "test"

    with pytest.raises(ValueError, match="Ce champ est requis"):
        input_validator.validate_non_empty_string("")


def test_validate_date_format():
    input_validator = InputValidator()
    assert input_validator.validate_date_format("01-01-2021") == datetime(2021, 1, 1)

    with pytest.raises(ValueError, match=re.escape("Entrez un format date valide (01-01-2021)")):
        input_validator.validate_date_format("01/01/2021")


def test_validate_positive_float():
    input_validator = InputValidator()
    assert input_validator.validate_positive_float("1.0") == 1.0

    with pytest.raises(ValueError, match=input_validator.FLOAT_VALUE_ERROR):
        input_validator.validate_positive_float("a")

    with pytest.raises(ValueError, match=input_validator.FLOAT_GREATER_ZERO_ERROR):
        input_validator.validate_positive_float("-1.0")


def test_validate_national_id_format():
    input_validator = InputValidator()
    assert input_validator.validate_national_id_format("AB12345") == "AB12345"

    with pytest.raises(ValueError, match=re.escape("Veuillez entrer un format national ID valide (AB12345)")):
        input_validator.validate_national_id_format("AB123456")

    with pytest.raises(ValueError, match=re.escape("Veuillez entrer un format national ID valide (AB12345)")):
        input_validator.validate_national_id_format("ab12345")

    with pytest.raises(ValueError, match=re.escape("Veuillez entrer un format national ID valide (AB12345)")):
        input_validator.validate_national_id_format("1234567")

    with pytest.raises(ValueError, match=re.escape("Veuillez entrer un format national ID valide (AB12345)")):
        input_validator.validate_national_id_format("12345AB")
