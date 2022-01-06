from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

# python manage.py migrate
# python manage.py makemigrations first_app
# python manage.py migrate
# python manage.py shell
# >>> from first_app.models import Topic
# >>> print(Topic.objects.all())
# >>> t = Topic(top_name="Social Network")
# >>> t.save()
# 
