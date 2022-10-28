from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_only_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '_':
            raise exceptions.ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    MAX_LEN_USERNAME = 15
    MIN_LEN_USERNAME = 2
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        null=False,
        blank=False,
        validators=(
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_only_alphanumeric,
        )
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_LEN_ALBUM = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),

    )

    album_name = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=MAX_LEN_ALBUM,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_LEN_ARTIST,
    )
    genre = models.CharField(
        null=False,
        blank=False,
        choices=MUSICS,
        max_length=MAX_LEN_GENRE,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.0),
        )
    )

    class Meta:
        ordering = ['pk']
