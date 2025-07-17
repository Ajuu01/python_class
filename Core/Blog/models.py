from django.db import models

# Create your models here.
class Blog(models.Model):
    # id=models.UUIDField()
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=500)

    description=models.TimeField()

    class Meta:
        db_table="Blogs"

class Comments(models.Model):
    review=models.CharField(max_length=200)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        db_table="comments"

