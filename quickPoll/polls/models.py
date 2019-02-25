from django.db import models


class Poll(models.Model):#define fields and behaviors
    form = models.CharField(max_length=255)
    pub_date = models.DateField()


    def __str__(self):
        return self.text

#points to object, views the object




