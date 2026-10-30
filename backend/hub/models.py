from django.db import models


class Score(models.Model):
    player = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    points = models.PositiveIntegerField()

    class Meta:
        ordering = ["-points", "id"]  

    def __str__(self):
        return f"{self.player} - {self.game}: {self.points}"