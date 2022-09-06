from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for API.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    email = models.EmailField(unique=True, blank=False, null=False)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    company = models.CharField(max_length=100, null=False, default='')
    created_by = models.DateTimeField(auto_now_add=True)
    phonenumber = models.CharField(blank=False, null=False, max_length=30, default='')
    position = models.CharField(max_length=10, blank=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    REQUIRED_FIELDS = ["email", "name", "company", "phonenumber", "position"]

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class NeuralDropTasks(models.Model):
   Taskname = models.CharField(max_length=100, unique=True)
   dateofuse = models.DateTimeField(auto_now_add=True)
   AiFilenametoCompress = models.TextField()
   AiFilepathtoCompress = models.FileField(null=True)
   company_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)







