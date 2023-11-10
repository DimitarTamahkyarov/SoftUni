import re
from django.forms import ValidationError


def validate_only_letters_and_spaces(value):
    
    for letter in value:
        if not (letter.isalpha() or letter.isspace()):
            raise ValidationError("Name can only contain letters and spaces")
        

def validate_phone_number(value):
    if not re.match(r'^\+359\d{9}$', value):
        raise ValidationError("Phone number must start with a '+359' followed by 9 digits")
