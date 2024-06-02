from netmiko import ConnectHandler
from django.contrib import admin
from .models import Confiback
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .forms import ConfibackAdminForm



from django.conf import settings

class ConfibackModelAdmin(admin.ModelAdmin):
    form = ConfibackAdminForm



    def get_backup(self, request, queryset):
        for obje in queryset:
            data = {'device_type': obje.device_type,
                    'ip' : obje.ip,
                    'username' : obje.username,
                    'password' : obje.password,
                    'port' : obje.port,
                    }

        receipent_mail = obje.e_mail
        command = obje.command
        name = obje.name
        ConfibackModelAdmin.connect_and_prepare_backup(self, data, command, name, receipent_mail)
        self.message_user(request, ("{cihaz} Backup alindi kaydedildi.").format(cihaz = name))



    list_display = ("name", "ip")
    search_fields = ("ip", "name")
    actions = [get_backup]


    def connect_and_prepare_backup(self, data, command, name, receipent_mail):
        netconnect = ConnectHandler(**data)              
        output = netconnect.send_command(command)

        datestr = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        append = datestr + '_' + name
        if not os.path.isdir(settings.DEVICE_BACKUP_PATH):
            os.mkdir(settings.DEVICE_BACKUP_PATH)
        folder = os.path.join(settings.DEVICE_BACKUP_PATH, append)

        if not os.path.isdir(folder):
            os.mkdir(folder)

        dest = os.path.join(folder, '%s.txt' %name)
        file =open(dest, 'w')
        file.write(output)
        file.close()


        #ConfibackModelAdmin.send_mail(self, dest, name, receipent_mail)



    def send_mail(self, dest, name, receipent_mail):

        fromaddr = "senderMail"
        toaddr = receipent_mail
        passwd = "senderMailPassword"
        sbj    = "Network Backup"


        message = MIMEMultipart()
        message['from']  = fromaddr
        message['to']   = toaddr
        message['subject'] = sbj
        body = 'Backup'
        message.attach(MIMEText(body, 'plain'))

        attached_file = open(dest, 'rb')
        filename = os.path.join('%s.txt' % name)
        p = MIMEBase("application", "octet-stream")
        p.set_payload(attached_file.read())

        encoders.encode_base64(p)

        p.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        message.attach(p)
        text = message.as_string()

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, passwd)
        s.sendmail(fromaddr,toaddr, text)




# Register your models here.
admin.site.register(Confiback,ConfibackModelAdmin)
