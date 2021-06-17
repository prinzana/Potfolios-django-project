# Create your models here
from django.db import models


class Blog(models.Model):
    #image
    image = models.ImageField(upload_to= 'images/')

    #title
    title = models.CharField(max_length=250)

    #pub-date
    pub_date= models.DateTimeField()

    #body  
    body= models.TextField()



# add blog app to settings
# create migrattion
# migrate
# add to admin
