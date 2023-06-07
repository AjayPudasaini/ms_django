from django.db import models

class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Posts(TimeStampAbstractModel):
    post_by = models.IntegerField(verbose_name="User Id", null=False, blank=False)
    title = models.CharField(max_length=1000, verbose_name="Post Title")
    body = models.TextField(verbose_name="Post Body")
    image = models.ImageField(upload_to="images")