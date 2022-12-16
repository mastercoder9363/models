from django.db import models


class Rang(models.Model):
    rang = models.CharField(max_length=255)

    def __str__(self):
        return self.rang

class Moshina(models.Model):
    rasm = models.ForeignKey(Rang, on_delete=models.SET_NULL, null=True)
    about = models.TextField()
    narx = models.IntegerField(default=100)
    
    def __str__(self) -> str :
        return str(self.narx)