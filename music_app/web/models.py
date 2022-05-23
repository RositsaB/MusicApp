from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def username_validate(value):
    for char in value:
        if char.isalnum() or char == '_':
            pass
        else:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            username_validate,
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        ),
    )


class Album(models.Model):
    NAME_MAX_LEN = 30

    ARTIST_MAX_LEN = 30

    GENRE_MAX_LEN = 30
    GENRE = (
            ('Pop', 'Pop Music'),
            ('Jaz', 'Jazz Music'),
            ('R&B', 'R&B Music'),
            ('Rock', 'Rock Music'),
            ('Country', 'Country Music'),
            ('Dance', 'Dance Music'),
            ('Hip Hop', 'Hip Hop Music'),
            ('Other', 'Other'),
        )

    PRICE_MIN_VALUE = 0

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRE,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(PRICE_MIN_VALUE),
        ),
    )

    