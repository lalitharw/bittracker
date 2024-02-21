import requests
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.urls import reverse
import datetime
from django.contrib import messages
from django.urls import reverse
import time
import random




# Create your views here.
def congraluations(request):
    return render(request,'home_app/cong.html')

today = date.today()
# This is main page of website
def home(request):
    # this is line is used to check of the user is logged in or else he will be not allowed to access those page
    if request.user.is_authenticated:
        # retriving all the profiles available in User model
        profiles = Profile.objects.all()
        today = datetime.date.today()
        

        # used an api for random quote generator
        # url = 'https://api.quotable.io/random'
        # r = requests.get(url)
        # quote = r.json()
        # value = quote['content']
        # key = quote['author']

        lister  = {
        'Nelson Mandela':'The greatest glory in living lies not in never falling, but in rising every time we fall.',
        'Walt Disney':'The way to get started is to quit talking and begin doing.',
        'Benjamin Franklin': 'Tell me and I forget. Teach me and I remember. Involve me and I learn.',
        'Aristotle':'It is during our darkest moments that we must focus to see the light.',
        'Frederick Douglass':'If there is no struggle, there is no progress.',
        'Ruth Gordo':'Courage is like a muscle. We strengthen it by use.',
        'Dale Carnegie':'Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.',
        'Unknown':'A year from now you will wish you had started today.',
        'Amelia Earhart':'The most difficult thing is the decision to act, the rest is merely tenacity.',
        'Childish Gambino':"If it makes you nervous, you’re doing it right."

    }

        key,value = random.choice(list(lister.items()))

      
        current_user = User.objects.get(pk=request.user.pk)
        if current_user not in [profile.user for profile in profiles]:
            profiles = Profile.objects.create(
                user = request.user,
                coins = 0,
                Confirm_email = request.user.email
            )

            profiles.save()
            return redirect('home')

        coins = Profile.objects.get(user=request.user)
            # return redirect("create_profile")
        profile = Profile.objects.get(user=request.user)
        habits = Habit.objects.filter(author=profile)
        # this is module to check if habit is complete as per today's day
        todies = HabitLog.objects.values("date")
       
        total_streak = 0
        current_streak = 0
        today = datetime.date.today()
        compareDate = today + datetime.timedelta(1) # Tomorrow
            # print(compareDate)

            # Using list() here pulls all the entries from the DB at once
            # Gets all entry dates for this journal and whose dates are <= today
        entry_dates = list(HabitLog.objects.values("date").filter(track_unit__gt=0, date__lte = today).order_by("-date"))
        for date in entry_dates:
            for date in date.values():
                # Get the difference btw the dates
                delta = compareDate - date
                # print(delta)

                if delta.days == 1: # Keep the streak going!
                    current_streak += 1
                elif delta.days == 0: # Don't bother increasing the day if there's multiple ones on the same day
                    pass
                else: # Awwww...
                    break # The current streak is done, exit the loop

                compareDate = date
                    # print(compareDate)

                if current_streak > total_streak:
                    total_streak = current_streak
                        # adder.append(total_streak)
        # print(total_streak)
        return render(request, "home_app/index.html", { 
            "profile": profile,
            "habits": habits,
            'key':key,
            'value':value,
            'todies':todies,
            'today':today,
            'total_streak':total_streak,
            'coins':coins
            })

    else:
        return HttpResponseRedirect('/login')

# This is ask for first and last name after user creates new account
def create_profile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, pk=request.user.pk)

        if request.method == "POST":
            form = ProfileForm(request.POST, initial={"user": user})
            if form.is_valid():
                profile = Profile.objects.create(
                    user=user,
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    Confirm_email = form.cleaned_data['Confirm_email']
                )
                profile.save()
            return redirect("home")
        else:
            form = ProfileForm(request.POST, initial={"user": user})

        return render(request, "home_app/create_profile.html", {"form": form})

    else:
        return HttpResponseRedirect('/login')

# This will let the user add new habit
def add_habit(request):
    coins = Profile.objects.get(user=request.user)
    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
           form = HabitForm(request.POST)
           if form.is_valid():
               habit_title = form.cleaned_data['title']
               print(habit_title)
               
               new_habit = Habit.objects.create(
                   title=form.cleaned_data["title"],
                   author=user_profile,
                   goal=form.cleaned_data["goal"],
                   goal_unit = form.cleaned_data["goal_unit"]
               )               
               new_habit.save()

            #    print(new_habit.id)
               habit_name = Habit.objects.get(pk=new_habit.id)
               adding_default_log = HabitLog.objects.create(
                   habit = habit_name,
                   date = '2023-01-01',
                   track_unit = 0
               )
               adding_default_log.save()


               messages.info(request,"Habit added successfully!!!")
               return redirect("home")
        else:
            
            form = HabitForm()

        return render(request, "home_app/add_habit.html", {"form": form,'coins':coins})

    else:
        return HttpResponseRedirect('/login')

# This will display user`s habit info but not added on website
def habit_info(request, habitpk):
    if request.user.is_authenticated:
        habit = Habit.objects.get(pk=habitpk)
        # habit_logs = HabitLog.objects.filter(habit=habit).order_by("-date")

        return render(
            request, "home_app/habit_info.html", {"habit": habit,'coins':coins}
        )
    else:
        return HttpResponseRedirect('/login')

# This will let user change the name, description and daily goal to achieve
def edit_habit(request, habitpk):
    if request.user.is_authenticated:
        habit = Habit.objects.get(pk=habitpk)
        if request.method == "POST":
            form = HabitForm(request.POST, instance=habit)
            if form.is_valid():
                form.save()
                messages.info(request,'Habit updated Successfully!')


        else:
            form = HabitForm(instance=habit)

        return render(request, "home_app/edit_habit.html", {"form": form})
    else:
        return HttpResponseRedirect('/login')

# This will let user delete the desired habit
def delete_habit(request, habitpk):
    if request.user.is_authenticated:
        habit = Habit.objects.get(pk=habitpk)
        habit.delete()
        messages.info(request,'Habit deleted successfully!!!')
        return redirect('home')
    else:
        return HttpResponseRedirect('/login')

# This wil add log of desired habit with taking todays log and taking dates
def add_log(request, habitpk):
    global failed
    failed = False
   
    if request.user.is_authenticated:
        habit = Habit.objects.get(pk=habitpk)


            
        
        if request.method == "POST":
            # print(habit)
            form = HabitLogForm(request.POST, initial={"habit": habit.pk,'date':today})

            # when adding log it is checking is form is valid and date is not greater than today
            if form.is_valid():
                form.save()
                
                messages.success(request,'Log added successfully!!!')
                return redirect(reverse('report',kwargs={'id':habitpk}))
        else:
            
            form = HabitLogForm(initial={"habit": habit.pk,'date':today})

        return render(
            request, "home_app/add_log.html", {"form": form, "habit": habit,'failed':failed}
        )
    else:
        return HttpResponseRedirect('login/')

# Will generate chart from the log we added used chart.js
def see_report(request,id):
  

    if request.user.is_authenticated:
        labels = []
        data = []
        habitlabel = Habit.objects.get(pk=id)

        habitgoal = habitlabel.goal
        #for data in chartjs
        queryset = HabitLog.objects.filter(habit=habitlabel.id).order_by('date')
        for habits in queryset:
            appender = habits.track_unit
            per = appender/habitgoal*100

            # to calculate percentage for graph
            if per >= 100:
                per = 100

            data.append(appender)

        # labels for chartjs
        label = HabitLog.objects.filter(habit=habitlabel.id).order_by("date")
        for label in label:
            labels.append(str(label.date))
        return render(request,'home_app/report.html',{
            'labels':labels,
            'data':data,
            "habitlabel":habitlabel,
         
        
        })

    else:
        return HttpResponseRedirect('/login')

# Function for showing specific habit log
def show_log(request,id):
    if request.user.is_authenticated:
        habitlog = Habit.objects.get(pk=id)
        # habit_distinct = HabitLog.objects.values('date','track_unit').distinct()
        habits = HabitLog.objects.filter(habit=habitlog.id,date__gt='2023-01-01').order_by('-date')
        return render(request,'home_app/show_log.html',{'habits':habits})
    else:
        return HttpResponseRedirect('/login')

#This function will del log the user has already entered
def del_log(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            habits = HabitLog.objects.get(pk=id)
            habits.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect('/login')

#This function is used to update the users log
def update_log(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            update_habits = HabitLog.objects.get(pk=id)
            form = HabitLogForm(request.POST, instance=update_habits)
            if form.is_valid():
                form.save()
        else:
            # print(id)
            update_habits = HabitLog.objects.get(pk=id)
            print(update_habits)
        form = HabitLogForm(instance=update_habits)
        return render(request,'home_app/update_log.html',{'form':form})
    else:
        return HttpResponseRedirect('/login')

# this function is used to display calendar⬇️⬇️
def display_calendar(request,id):
    coins = Profile.objects.get(user=request.user)
    if request.user.is_authenticated:
        habitlabel = Habit.objects.get(pk=id)
        display_cal = HabitLog.objects.filter(habit=habitlabel.id)
        # print(display_cal)
        return render(request,'home_app/calendar.html',
        {
            'display':display_cal,
            'habitlabel':habitlabel,
            'coins':coins
        }
        )
    else:
        return HttpResponseRedirect('/login')

def all_func(request,id):
    profile = Profile.objects.get(user=request.user)
    habits = Habit.objects.filter(pk=id)
    coins = Profile.objects.get(user=request.user)
    for habit in habits:
        title = habit
        pass
    context = {'habits':habits,'title':title,'coins':coins}
    return render(request,'home_app/all_func.html',context)


# To let user know that they have completed the habit for today
# <---------------------------------------------------------commented code------------------------------------------->

# add log for completed goals
# def add_log(request, habitpk):
#     habit = Habit.objects.get(pk=habitpk)
#     failed = False
#     if request.method == "POST":
#         form = HabitLogForm(request.POST, initial={"habit": habit})
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             failed = True
#     else:
#         form = HabitLogForm(request.POST, initial={"habit_id": habit.pk})
#     return render(
#         request, "home_app/add_log.html", {"form": form,
#          "habit": habit,
#           "failed": failed
#          })

# Generating reports in chart format used chart.js
# def see_report(request):
#     data = HabitLog.objects.all()
#     context = {
#         'data':data
#     }
    # return render(request,'home_app/report.html',context)

def test(request):
    return render(request,'home_app/send_mail.html')

