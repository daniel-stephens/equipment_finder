from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Equipment (models.Model):
    equipment = models.CharField(max_length=100)

    def __str__(self):
        return str(self.equipment)

class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return str(self.location)



class Finder(models.Model):
    description = models.CharField(max_length=200)
    rating = models.IntegerField(null=True)
    equipment = models.ForeignKey(Equipment, on_delete=CASCADE)
    location = models.ForeignKey(Location, on_delete=CASCADE)
    #image = models.ImageField(upload_to='static/finder/images', null=True)
    date = models.DateField(null=False, default='21/08/2021')

    def __str__(self):
        return str(self.description), str(self.equipment), str(self.rating), str(self.location), str(self.date)
 

