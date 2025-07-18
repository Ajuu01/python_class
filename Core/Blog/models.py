from django.db import models

# Create your models here.
class Blog(models.Model):
    # id=models.UUIDField()
    title=models.CharField(max_length=100)
    sub_title=models.CharField(max_length=500)

    description=models.TimeField()

    def __str__(self):
        return self.title

    class Meta:
        db_table="Blogs"

class Comments(models.Model):
    review=models.CharField(max_length=200)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
    class Meta:
        db_table="comments"

