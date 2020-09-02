from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Author(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255)
    last_login = None
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(verbose_name='Post title', max_length=255)
    link = models.URLField(verbose_name='Link to post')
    votes = models.IntegerField(verbose_name='Amount of upvotes')
    creation_date = models.DateField(auto_now_add=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.author_name
