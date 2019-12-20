from django.core.exceptions import ValidationError


# custom validate
def validate_even(number):
    if number % 2:
        raise ValidationError(f'{number} is not even', params={'value': number})


def validate_too_old(number):
    if number > 150:
        raise ValidationError(f'{number} 까지 살 수 없어요..', params={'value': number})


def validate_too_young(age):
    if age < 20:
        raise ValidationError(f'미성년자는 노노')