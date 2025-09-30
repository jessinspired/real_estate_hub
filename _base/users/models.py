from django.db import models
from core.models import BaseModel
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
    Group
)
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

    @property
    def role_instance(self):
        if self.is_agent:
            return Agent.objects.filter(id=self.id).first()
        elif self.is_landlord:
            return Landlord.objects.filter(id=self.id).first()
        elif self.is_client:
            return Client.objects.filter(id=self.id).first()
        return None


# agents models
class AgentManager(UserManager):
    """Manager for agent proxy table."""

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(role=User.Role.AGENT)


class Agent(User):
    """Defines the agent proxy model."""

    objects = AgentManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Hello agent"

    def save(self, *args, **kwargs):
        """Saves lister object and adds it to the agents' group."""
        self.role = User.Role.AGENT
        super().save(*args, **kwargs)

        agents_group, created = Group.objects.get_or_create(name="agents")

        if not self.groups.filter(name="agents").exists():
            self.groups.add(agents_group)

    def delete(self, *args, **kwargs):
        """Removes agent from group before deleting."""
        self.groups.remove(Group.objects.get(name='agents'))
        super().delete(*args, **kwargs)


# landlords models
class LandlordManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=User.Role.LANDLORD)


class Landlord(User):
    objects = LandlordManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = User.Role.LANDLORD
        super().save(*args, **kwargs)
        landlords_group, _ = Group.objects.get_or_create(name="landlords")
        if not self.groups.filter(name="landlords").exists():
            self.groups.add(landlords_group)

# client models


class ClientManager(UserManager):
    """Manager to filter only client users."""

    def get_queryset(self):
        return super().get_queryset().filter(role=User.Role.CLIENT)


class Client(User):
    """Proxy model for client users."""
    objects = ClientManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        """Ensure role is CLIENT and add to clients group."""
        self.role = User.Role.CLIENT
        super().save(*args, **kwargs)

        clients_group, _ = Group.objects.get_or_create(name="clients")
        if not self.groups.filter(name="clients").exists():
            self.groups.add(clients_group)

    def delete(self, *args, **kwargs):
        """Remove client from group before deleting."""
        if self.groups.filter(name="clients").exists():
            self.groups.remove(Group.objects.get(name="clients"))
        super().delete(*args, **kwargs)

    def welcome(self):
        return f"Welcome client {self.first_name}"
