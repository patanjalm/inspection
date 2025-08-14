from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

USER_TYPE_CHOICES = (
    (1, "SuperAdmin"),
    (2, "Admin"),
    (3, "User"),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, mobile_no, full_name, user_type, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        if not mobile_no:
            raise ValueError("Mobile number is required")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            mobile_no=mobile_no,
            full_name=full_name,
            user_type=user_type,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
  
        return self.create_user(email=email, mobile_no="0000000000", full_name="Admin", user_type=1, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=255)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    is_active = models.BooleanField(default=True)
  
    createdAt = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["mobile_no", "full_name", "user_type"]

    objects = CustomUserManager()

    class Meta:
        db_table = "users"
        unique_together = ("email", "user_type")  # extra validation

    def __str__(self):
        return f"{self.full_name} ({self.email})"
