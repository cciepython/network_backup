from django.db import models






# Create your models here.

cihaz_tipi = (
                ('cisco_ios' , 'cisco_ios'),
                ('cisco_nxos_ssh','cisco_nxos_ssh'),
                ('juniper', 'juniper'),
                ('cisco_asa', 'cisco_asa'),
                ('fortinet', 'fortinet'),
                ('hp_comware', 'hp_comware'),
                ('arista_eos', 'arista_eos'),
                ('dell_force10', 'dell_force10'),
                ('mellanox', 'mellanox'),

            )



class Confiback(models.Model):
    device_type = models.CharField (max_length=20, choices = cihaz_tipi, default ='cisco_ios')
    name = models.CharField(max_length=20)
    ip = models.GenericIPAddressField(max_length=50, protocol='both')
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    port = models.IntegerField(blank=True, default=int(22))
    command = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=50, blank=True)


    def __str__(self):
        return "%s %s" %(self.name, self.device_type)






