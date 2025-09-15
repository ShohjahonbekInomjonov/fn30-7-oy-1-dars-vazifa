from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class Genre(models.Model):
    type = models.CharField(verbose_name="Nomi", max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['type']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        db_table = 'genres'

class Movie(models.Model):
    title = models.CharField(verbose_name="Nomi", max_length=75, unique=True)
    director = models.CharField(verbose_name="Rejissori", max_length=100, null=True, blank=True)
    description = models.TextField(verbose_name="Ma'lumoti", null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies', verbose_name="Janri")
    cover = models.ImageField(verbose_name="Posteri", upload_to='covers/', null=True, blank=True)
    video = models.FileField(verbose_name="Kinosi", upload_to='videos/', null=True, blank=True,
                             validators=[FileExtensionValidator(["mp4", "avi", "mov", "mkv"])])
    release = models.DateField(verbose_name="Chiqgan sanasi")
    views = models.IntegerField(verbose_name="Ko'rishlar soni", default=0)
    published = models.BooleanField(verbose_name="Saytga chiqarish?", default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Muallifi")

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-release']
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        db_table = 'movies'

class Comment(models.Model):
    text = models.CharField(verbose_name="Matni", max_length=500)
    movie  = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Kino")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'comments'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="user/images", null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    telegram = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profillar"
        ordering = ['job']
        permissions = [
            ("can_view_all_profiles", "Barcha profillarni ko'rish imkoni"),
            ("can_edit_own_profile", "O'z profilini tahrirlash imkoni"),
            ("can_delete_own_profile", "O'z profilini o'chirish imkoni"),
        ]