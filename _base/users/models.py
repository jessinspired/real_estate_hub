from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import AbstractUser, BaseUserManager
from users.utils import generate_unique_username


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)

        # Auto-generate username from first_name + last_name
        if not extra_fields.get("username"):
            first = extra_fields.get("first_name", "")
            last = extra_fields.get("last_name", "")
            unique_username = generate_unique_username(
                first, last, email, self.model)
            extra_fields["username"] = unique_username

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(BaseModel, AbstractUser):
    """Defines our custom AUTH_USER_MODEL."""
    class Role(models.TextChoices):
        GUEST = 'guest', 'Guest'
        AGENT = 'agent', 'Agent'
        CLIENT = 'client', 'Client'
        LANDLORD = 'landlord', 'Landlord'

    class AuthenticationMeans(models.TextChoices):
        '''
        -> Helps keep track of how users are authenticated
        Args:
            models (TextChoices): Defines the role choices for users
        '''
        EMAIL = 'email', 'Email'
        FACEBOOK = 'facebook', 'Facebook'
        GOOGLE = 'google', 'Google'

    objects = UserManager()

    # using email sign up instead of username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True)

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.GUEST
    )

    authentication_means = models.CharField(
        max_length=15,
        choices=AuthenticationMeans.choices,
        default=AuthenticationMeans.EMAIL
    )

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    @property
    def is_client(self):
        return self.role == User.Role.CLIENT

    @property
    def is_agent(self):
        return self.role == User.Role.AGENT

    @property
    def is_landlord(self):
        return self.role == User.Role.LANDLORD

    @property
    def is_guest(self):
        return self.role == User.Role.GUEST
