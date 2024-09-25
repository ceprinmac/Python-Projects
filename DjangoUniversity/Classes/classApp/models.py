from django.db import models

# Create your models here.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    course_number = models.IntegerField()
    duration = models.FloatField()

    objects = models.Manager()
    # Naming the database object by title
    def __str__(self):
        return self.title
