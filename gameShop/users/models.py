from django.db import models
from django.contrib.auth.models import User

# Make email field required for user
#User._meta.get_field('email').blank = False # Does not seem to work, maybe need to extend user model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_dev = models.BooleanField(default=False)

    def __str__(self):
        role = 'developer' if self.is_dev else 'player'
        return self.user.username + "'s profile (" + role + ")"


#Using multi-table inheritance to store additional user data if needed
#class PlayerProfile(Profile):
    

#class DevProfile(Profile):

