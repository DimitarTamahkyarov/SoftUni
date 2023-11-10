from string import ascii_lowercase

from django.forms import ValidationError


def validate_only_letters_and_spaces(value):
    symbols = ascii_lowercase + ' '
    for letter in value:
        if not letter.lower() in symbols:
            raise ValidationError("Name can only contain letters and spaces")
        

def validate_phone_number(value):
    if not value.startswith('+359') or len(value) != 13:
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
