from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    tab_count = models.IntegerField(default=4)

    def __str__(self):
        return self.name


class Text(models.Model):
    text = models.TextField(default="")
    prolang = models.ForeignKey(ProgrammingLanguage, on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=100, default="")
    source_link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class Test(models.Model):
    text = models.ForeignKey(Text, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)
    wpm = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0.0)
    time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
