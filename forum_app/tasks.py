from celery import shared_task
from .models import *
from home_app.models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import EmailMultiAlternatives
from habit_tracker import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# this is for forum previous page
@shared_task(bind=True)
def add_to_previous_winner(self):
    
    date = datetime.now()
    today = date.date()
    forum_groups = ForumGroups.objects.all()

    for forum_group in forum_groups:
        if forum_group.delete_time == today:
            winner_info = ForumAddLog.objects.filter(group_name=forum_group.id).order_by('-track_unit')[:1]
         
            for win in winner_info:
                # incrementing coins for users
                prf = Profile.objects.get(user=win.user.id)
                default_coins = prf.coins
                increment_coins = default_coins + 100
                prf.coins = increment_coins
                mail_subject = f"Congraluations You are won the challenge"
                html_message = render_to_string('home_app/forum_mail.html' ,{'forum_name':win.group_name.name,'username':prf.user})
                plain_message = strip_tags(html_message)
                to_email = prf.Confirm_email

                email = EmailMultiAlternatives(
                    mail_subject,
                    plain_message,
                    settings.EMAIL_HOST_USER,
                    [to_email]
                )

                email.attach_alternative(html_message,'text/html')
                # email.send()
                # prf.save() # <--uncomment this

                # Adding data to other table
                previous = Previous_Group(name=forum_group.name,
                                      desc=forum_group.desc,
                                      image_url = forum_group.image_url,
                                      winner_user = win.user
                )
                # previous.save() # <--uncomment this table

                #deleting the data from original table
             
                delete_table = ForumGroups.objects.get(id=forum_group.id)
               
                # delete_table.delete()
         
  
                   
