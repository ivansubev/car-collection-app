from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Profile(models.Model):
    VALIDATION_ERROR_MESSAGE = "The username must be a minimum of 2 chars"
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 10
    AGE_MIN_VALUE = 18
    PASS_MAX_LEN = 30
    NAME_MAX_LEN = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN, VALIDATION_ERROR_MESSAGE),
        )
    )
    email = models.EmailField(
        blank=False,
        null=False
    )
    age = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )
    password = models.CharField(
        max_length=PASS_MAX_LEN,

    )
    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True
    )


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    YEAR_MIN_VALUE = 1980
    YEAR_MAX_VALUE = 2049
    YEAR_VALIDATION_ERROR = "Year must be between 1980 and 2049"
    PRICE_MIN_VALUE = 1

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=(
            ("Sports Car", "Sports Car"),
            ("Pickup", "Pickup"),
            ("Crossover", "Crossover"),
            ("Minibus", "Minibus"),
            ("Other", "Other")
        )
    )
    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=(
            MinLengthValidator(MODEL_MIN_LEN),
        )
    )
    year = models.IntegerField(
        blank=False,
        null=False,
        validators=(
            MinValueValidator(YEAR_MIN_VALUE, YEAR_VALIDATION_ERROR),
            MaxValueValidator(YEAR_MAX_VALUE, YEAR_VALIDATION_ERROR),
        )
    )
    image_url = models.URLField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        )
    )
