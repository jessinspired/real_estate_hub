from django.utils.text import slugify
import random


def generate_unique_username(first, last, email, UserModel):
    base = slugify(f"{first}{last}") or email.split("@")[0]
    while True:
        candidate = f"{base}{random.randint(1000, 9999)}"
        if not UserModel.objects.filter(username=candidate).exists():
            return candidate
