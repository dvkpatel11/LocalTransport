from django.db import models

# Create your models here.

# Models are a way of telling Django about the structure of the data you want to store inside of a database so that you can migrate these changes in django
class Station(models.Model):
    code = models.CharField(max_length=5)
    location = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.location} : {self.code.upper()}"

class Bus(models.Model):
    # Instead of just having origin/destination store characters as so:
    # origin = models.CharField(max_length = 64)
    # destination = models.CharField(max_length = 64)
    # We can instead create foreign keys to point to the relevant orgin and destination stations

    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="departures")
    # on_delete specifies behavior when the data being referenced to by the Foreign Key gets deleted. models.CASCADE is a specification that states if the Station is deleted, delete the corresponding bus
    # A related_name is a way of accessing a relationship in the reverse orger. So if we have a station and we want to know all buses that have that station as the origin then we can give it a related_name of 'departures'
    
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # def __init__(self, origin, destination, duration):
    #     self.origin = origin
    #     self.destination = destination
    #     self.duration = duration

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    # blank=True here allows us to create passengers who do not have a bus ride planned out yet
    buses = models.ManyToManyField(Bus, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

