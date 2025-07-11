from django.db import models


class Text(models.Model):
    text = models.TextField(default="")
    programming_language = models.CharField(max_length=100, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text
