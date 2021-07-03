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

    #changing the title of the block object to the title of the blog post
    def __str__(self):
        return self.title

    #post previews
    def summary(self):
        return self.body[:50]
    #to make the time and date looks better
    def pub_date_pretty(self):
        return self.pub_date.strftime( '%b %e %Y' )

# add blog app to settings
# create migrattion
# migrate
# add to admin
