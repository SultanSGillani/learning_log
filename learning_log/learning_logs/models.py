from django.db import models


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a String Representation of the model Topic.
        :return:
        """
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(to='learning_logs.Topic', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """
        Return a string representation of the model Entry.
        Only return the first 50 Characters of the entry.
        If less than 50 characters don't show ...
        :return:
        """
        text = (self.text[:50] + '...')
        if len(text) > 50:
            return text
        else:
            return self.text

