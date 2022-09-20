from django.db import models


# maps to a database table
class Task(models.Model):
    # varchar(30), NOT NULL
    name = models.CharField(
        max_length=30,
        null=False,
    )

    description = models.TextField()

    priority = models.IntegerField()






