import random
import string
a=int(input("enter"))

def generate_password(length=a, include_uppercase=True, include_digits=True, include_special_chars=True):
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''
    
    
    all_chars = lowercase + uppercase + digits + special_chars
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if include_uppercase else '',
        random.choice(digits) if include_digits else '',
        random.choice(special_chars) if include_special_chars else ''
    ]

    password += random.choices(all_chars, k=length - len(password))
    random.shuffle(password)
    return ''.join(password)

password = generate_password(length=a, include_uppercase=True, include_digits=True, include_special_chars=True)
print(f"Generated Password: {password}")

