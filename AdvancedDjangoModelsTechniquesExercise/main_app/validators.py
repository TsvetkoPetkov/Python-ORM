from django.core.exceptions import ValidationError


def validate_customer_name(value):
    for char in value:
        if not (char.isalpha() or char == " "):
            raise ValidationError("Name can only contain letters and spaces")


def phone_validator(value):
    if value[:4] != '+359' and all(x.isdigit() for x in value[4:]) == False:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")





