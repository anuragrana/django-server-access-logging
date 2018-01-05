from django.db import models


class AccessLogsModel(models.Model):
    sys_id = models.AutoField(primary_key=True, null=False, blank=True)
    session_key = models.CharField(max_length=1024, null=False, blank=True)
    path = models.CharField(max_length=1024, null=False, blank=True)
    method = models.CharField(max_length=8, null=False, blank=True)
    data = models.TextField(null=True, blank=True)
    ip_address = models.CharField(max_length=45, null=False, blank=True)
    referrer = models.CharField(max_length=512, null=True, blank=True)
    timestamp = models.DateTimeField(null=False, blank=True)

    class Meta:
        app_label = "django_server_access_logs"
        db_table = "access_logs"
