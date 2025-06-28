import re
from django.core.exceptions import ValidationError

def verify_number(numero):
    regex = re.compile(r"^\+?\d{0,3}\d{10}$") #^matches the start of the line, with \ we scape the special + and whe put a ? to say it's optional that tell us it should begin with 0 to three characters and then the 10 digits with $ to end the string
    result = regex.match(numero)
    if result is None:
        raise ValidationError('The provided phone_number is not valid')


def verify_date(fecha):
    regex = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$")
    result = regex.match(fecha)
    if result is None:
        raise ValidationError('The provided date is not in the required format (dd/mm/yyyy)')

def validate_surgeon(vet):
    if vet.specialty.name != "surgeon":
        raise ValidationError('The provided veterinarian is not a surgeon')