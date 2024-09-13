from datetime import datetime
import re


class InputValidator:
    """
    A class to validate different types of user input such as non-empty strings, dates, positive floats,
    and national ID formats.

    Attributes:
        EMPTY_FIELD_ERROR (str): Error message when a required field is empty.
        DATE_FORMAT_ERROR (str): Error message when the date format is invalid.
        FLOAT_VALUE_ERROR (str): Error message when the input is not a valid float.
        FLOAT_GREATER_ZERO_ERROR (str): Error message when the float is negative.
        NATIONAL_ID_FORMAT_ERROR (str): Error message when the national ID format is invalid.

    Methods:
        validate_non_empty_string(value: str) -> str:
            Validates that a string is not empty.

        validate_date_format(value: str) -> datetime:
            Validates that a string matches the date format "DD-MM-YYYY".

        validate_positive_float(value: str) -> float:
            Validates that a string can be converted to a positive float.

        validate_national_id_format(value: str) -> str:
            Validates that a string matches the national ID format "AB12345".
    """

    EMPTY_FIELD_ERROR = "Ce champ est requis"
    DATE_FORMAT_ERROR = "Entrez un format date valide (01-01-2021)"
    FLOAT_VALUE_ERROR = "Veuillez entrer un nombre valide"
    FLOAT_GREATER_ZERO_ERROR = "Le nombre doit être supérieur ou égale à zéro"
    NATIONAL_ID_FORMAT_ERROR = "Veuillez entrer un format national ID valide (AB12345)"

    def validate_non_empty_string(self, value: str):
        """Validates that a string is not empty."""
        if not value.strip():
            raise ValueError(self.EMPTY_FIELD_ERROR)
        return value.strip()

    def validate_date_format(self, value: str):
        """Validates that a string is in the format (01-01-2021)."""
        try:
            return datetime.strptime(value, "%d-%m-%Y")
        except ValueError:
            raise ValueError(self.DATE_FORMAT_ERROR)

    def validate_positive_float(self, value: str):
        """Validates that a string is a positive float."""
        try:
            float_value = float(value)
        except ValueError:
            raise ValueError(self.FLOAT_VALUE_ERROR)

        if float_value < 0:
            raise ValueError(self.FLOAT_GREATER_ZERO_ERROR)

        return float_value

    def validate_national_id_format(self, value: str):
        """Validates that a string is a valid national ID format (AB12345)."""
        pattern = re.compile(r"[A-Z]{2}\d{5}$")
        try:
            value = self.validate_non_empty_string(value)
        except ValueError:
            raise ValueError(self.NATIONAL_ID_FORMAT_ERROR)

        if not pattern.match(value):
            raise ValueError(self.NATIONAL_ID_FORMAT_ERROR)

        return value
