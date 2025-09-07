import random
import string

def generate_password(length=12):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits

    
    password_chars = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
    ]

    
    all_chars = upper + lower + digits
    remaining_length = length - len(password_chars)
    password_chars += random.choices(all_chars, k=remaining_length)

    
    random.shuffle(password_chars)

    
    return ''.join(password_chars)


print("Generated Password:", generate_password(12))