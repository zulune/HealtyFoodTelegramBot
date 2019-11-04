import random
import string


def username_generator(size=5, first_name=None, last_name=None, chars=string.digits):
    return first_name.lower() + last_name.lower() + ''.join(random.choice(chars) for _ in range(size))


def password_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


"""
Validate Telephone with user enter
Return True if telephone is valid
End return false if telephone not valid
"""
def validate_telephone(value) -> bool:
	if value:
		return False
	return True
