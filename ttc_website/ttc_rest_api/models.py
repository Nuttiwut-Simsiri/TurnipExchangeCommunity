from django.db import models
from django.utils import timezone

class TTC_POST_TB(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    postDate = models.DateField()
    modifiedDate = models.DateField()
    postBy = models.CharField(max_length=255)
    uuidPost = models.CharField(max_length=36)

    def __str__(self):
        return f"{self.title} by [{self.postBy}]"



class TTC_COMMENT_TB(models.Model):
    uuidPost = models.ForeignKey(TTC_POST_TB, on_delete=models.CASCADE, related_name="comments")
    commentBy = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return f"{self.text[:25]} - {self.created_date}"