from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    log_info = models.CharField(max_length=100, blank=True)
    date_time_logged = models.DateTimeField('date and time of activity', blank=True)
    username = models.CharField(max_length=150, blank=True)

    def create_log(cls, username, loginfo, datetimeinfo):
        log = cls(log_info=loginfo, date_time_logged=datetimeinfo, username=username)
        log.save()

    def __str__(self):
        return '{} | {}{}'.format(self.date_time_logged, self.username, self.log_info)

# Create your models here.
