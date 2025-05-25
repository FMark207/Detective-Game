from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MurderStat(models.Model):
    murderWeapon = models.CharField(max_length=20)
    murderLocation = models.ForeignKey(Location,on_delete=models.CASCADE, null=True, blank=True)
    murderTime = models.TimeField()
    murderNotice = models.TextField(max_length=200)

    def __str__(self):
        return f"Murder Case #{self.id}"

class SuspectList(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    time = models.TimeField()
    isMurder = models.BooleanField()

    def __str__(self):
        return self.name

class Trait(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SuspectTrait(models.Model):
    suspect = models.ForeignKey(SuspectList, on_delete=models.CASCADE)
    trait = models.ForeignKey(Trait, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.suspect.name} - {self.trait.name}"

class Detective(models.Model):
    name = models.CharField(max_length=50)
    years_experience = models.IntegerField()
    birth_year = models.IntegerField()

    def __str__(self):
        return self.name

class Statement(models.Model):
    detective = models.ForeignKey(Detective, on_delete=models.CASCADE)
    suspect = models.ForeignKey(SuspectList, on_delete=models.CASCADE)
    statement_text = models.TextField()

    def __str__(self):
        return f"{self.detective.name} -> {self.suspect.name}"