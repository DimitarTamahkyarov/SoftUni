from django.core.exceptions import ValidationError


def validate_rating(value):

    if value < 0 or value > 10:
        raise ValidationError(message='The rating must be between 0.0 and 10.0')
    

def validate_release_year(value):

    if value < 1990 or value > 2023:
        raise ValidationError(message='The release year must be between 1990 and 2023')