from django.core.exceptions import ValidationError


def validate_first_name(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")

def validate_password(value):
    if len(value) != 6:
        raise ValidationError("Your passcode must be exactly 6 digits!")