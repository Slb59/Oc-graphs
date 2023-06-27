from django.contrib.auth import models as auth_models


class User(auth_models.AbstractUser):

    def get_full_name(self):
        return self.first_name + " " + self.last_name
