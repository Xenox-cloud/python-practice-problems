import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

print(validate_email("test@domain.com"))
print(validate_email("invalid-email"))