from django.db import models


class Tag(models.Model):
    TagNo = models.CharField(max_length=15, unique=True, null=False)    

    def __str__(self):
        return "%s" % self.TagNo


