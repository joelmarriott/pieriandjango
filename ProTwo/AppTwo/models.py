from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=264,unique=True)
    lastName = models.CharField(max_length=264)
    email = models.CharField(max_length=264)

    def __str__(self):
        return str(self.email)

# python manage.py migrate
# python manage.py makemigrations first_app
# python manage.py migrate
# python manage.py shell
# >>> from first_app.models import Topic
# >>> print(Topic.objects.all())
# >>> t = Topic(top_name="Social Network")
# >>> t.save()
#
