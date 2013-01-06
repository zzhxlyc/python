from django.db import models

class User(models.Model):
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )
    name = models.CharField(max_length = 60)
    gender = models.SmallIntegerField(choices = GENDER_CHOICES)
    birthday = models.DateField(auto_now_add = True)
    lastLogin = models.DateTimeField(auto_now = True)
    photo = models.ImageField(upload_to = '/media/photos/%Y/%m')
    ip = models.IPAddressField()
    father = models.ForeignKey('self', default = 0)
    
    class Meta:
        db_table = 'users'
        ordering = ['name'] #-name is for desc
    
    def __str__(self):
        return '%s, %s' % (self.name, self.gender)
        
    def __unicode__(self):
        return u'%s, %s' % (self.name, self.gender)
    
    def get_absolute_url(self):
        return "/user/%i/" % self.id