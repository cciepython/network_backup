from django.db import models

# Create your models here.

cihaz_tipi = (
                ('cisco_ios' , 'cisco_ios'),
                ('cisco_nxos_ssh','cisco_nxos_ssh'),
                ('juniper', 'juniper'),
                ('cisco_asa', 'cisco_asa'),
                ('fortinet', 'fortinet'),
                ('hp_comware', 'hp_comware'),

            )



class Confiback(models.Model):
    device_type = models.CharField (max_length=20, choices = cihaz_tipi, default ='cisco_ios')
    name = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(max_length=50, protocol='both')
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    port = models.IntegerField(blank=True)
    command = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50, blank=True)


    def __str__(self):
        return "%s %s" %(self.name, self.device_type)






