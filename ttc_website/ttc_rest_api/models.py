from django.db import models

class TTC_POST_TB(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    postDate = models.DateField()
    modifiedDate = models.DateField()
    postBy = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} by [{self.postBy}]"

