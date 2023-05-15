from django.db import models


class Story(models.Model):
    """
    Fields: title, content, author, pub_date
    """
    title = models.CharField(max_length=155)
    content = models.TextField()
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
