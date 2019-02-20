from django.db import models
from django.contrib.auth.models import User
#from app.models import cities ##cities is the name of the class in khalid's app.models
##if it is different(name) it's fine just change the name in your code to validate with khalid


# table containing all hotel names and their id
class Hotel(models.Model):
   # city_id = models.ForeignKey(Cities)
    hotel_name = models.CharField(max_length=200)
    hotel_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.hotel_name

# table linking user to hotels
class HotelReservationRequest(models.Model):
    hotel_id = models.ForeignKey(Hotel)
    user_id = models.ForeignKey(User)
    from_date = models.DateField()
    to_date = models.DateField()
    no_of_adults = models.IntegerField()