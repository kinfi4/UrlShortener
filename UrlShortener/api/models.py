from django.db import models


class Url(models.Model):
    long_url = models.URLField(db_index=True, unique=True, max_length=200)
    short_url = models.URLField(db_index=True, unique=True, max_length=7)
    pub_date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.short_url
