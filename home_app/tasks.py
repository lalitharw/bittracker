from celery import shared_task
from .models import *

# from .models import *
from datetime import date
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from habit_tracker import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task(bind=True)
def add_db_data(user_id:int):
    habits = Habit.objects.all()
    for habit in habits:
        habit_id =  habit.id 
        habits = Habit.objects.get(pk=habit_id)
        habit_name =  habits.title
        logs = HabitLog.objects.filter(habit=habits)
        for log in logs:
            if  log.date == date.today():
                pass
          
            else:
               
                f = HabitLog.objects.filter(habit=habits).last()
                if f.date != date.today():
                    fm = HabitLog(habit=habits,track_unit=0,date=date.today())
                    # fm.save() #uncommment this to save to database


@shared_task(bind=True)
def send_mail_to_user(self):
    users = Profile.objects.all()
    
    habits = Habit.objects.all()
    for habit in habits:
        habit_id =  habit.id
        habits = Habit.objects.get(pk=habit_id)
        habit_name =  habits.title
        logs = HabitLog.objects.filter(habit=habits).last()
        print(f"Sending email to: {logs.habit}")
        if logs.date != date.today():

            # print(f"Sending email to: {logs.date} {logs.habit}")
            mail_subject = f"Look like you Forgot something!!"
            html_message = render_to_string('home_app/send_mail.html', {'habit_name': logs.habit.title,'username':logs.habit.author.user})
            plain_message = strip_tags(html_message)
            to_email = logs.habit.author.Confirm_email
         

            email = EmailMultiAlternatives(
            mail_subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [to_email]
            )

            email.attach_alternative(html_message,'text/html')
            # email.send()
            
