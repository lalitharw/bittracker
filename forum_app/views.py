from django.shortcuts import render,HttpResponseRedirect,redirect
from django.urls import reverse
from .models import *
from home_app.models import Profile
from django.contrib import messages #import messages

from .forms import *

# Create your views here.
# this is the home page of forum
def forum_home(request):
    group = ForumGroups.objects.all()
    coins = Profile.objects.get(user=request.user)
    context = {'group':group,'coins':coins}
    return render(request,'forum_app/forum.html',context)

# this is page for specific forum group
def forumGroupInfo(request,id):
    global hide
    coins = Profile.objects.get(user=request.user)
    grp = ForumGroups.objects.get(pk=id)
    grps=  grp.id
    user = Profile.objects.get(user=request.user)
    # print(user)
    group_log = ForumAddLog.objects.filter(group_name=grp.id).order_by('-track_unit') # type: ignore
    add_logs = ForumAddLog.objects.filter(group_name=grp.id,user=request.user) # type: ignore
    adder = ''
    for add in add_logs:
        # print(add.id)
        adder = add

        
    hide = True
    hello = ForumAddLog.objects.filter(user=request.user,group_name=grp.id ).exists()
    # print('sfb',hello)
    if not ForumAddLog.objects.filter(user=request.user,group_name=grp.id ).exists(): # type: ignore
        hide = False
        if request.method == 'POST':
            fm  = ForumAddLogForm(request.POST,initial={'user':user,'group_name':grp})
            if fm.is_valid():      
                    print('creating new')
                    creating_new_log = ForumAddLog.objects.create(
                            user=request.user,
                        group_name = grp,
                        track_unit = fm.cleaned_data['track_unit']
                    )
                    creating_new_log.save()
                    return redirect(reverse('group_info',kwargs={'id':grps}))
                    

    else:
        hide = True 
     

 
                    
    fm = ForumAddLogForm(initial={'user':user,'group_name':grp})
    context = {'grp':grp,'fm':fm,'group_log':group_log,'hide':hide,'adder':adder,'coins':coins}
    return render(request,'forum_app/forum_grp_info.html',context)  

def update_forum_log(request,id):
    update_logs = ForumAddLog.objects.get(pk=id)
    group_id = update_logs.group_name.id 
    logs  = (update_logs.track_unit)

    if request.method == 'POST':
        fm = ForumAddLogForm(request.POST)
         
        if fm.is_valid():
          
            track_unit = fm.cleaned_data['track_unit']
            result = track_unit + logs
            update_logs.track_unit = result  
            update_logs.save()
            messages.success(request,'Forum Log Updated Successfully!!')
            return redirect(reverse('group_info',kwargs={'id':group_id}))
            

          
           
    else:
        update_logs = ForumAddLog.objects.get(pk=id)
    fm = ForumAddLogForm()
    context = {'update':update_logs,'fm':fm}
    return render(request,'forum_app/update_log.html',context)

#this is page for previous forum page
def previous_winner(request):
    coins = Profile.objects.get(user=request.user)
    group = Previous_Group.objects.all()
    context={'group':group,'coins':coins}
    return render(request,'forum_app/previous_winners.html',context)