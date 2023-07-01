from django.shortcuts import render , redirect,HttpResponse
#admin password and id vaibhav and vaibhav 
#ironman Iron pass
#akshay ak123
#aditi aditi


from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import logout,login
from django.contrib.auth import authenticate


# Create your views here.
def index(request):
    # if request.user.is_anonymous:
    #         return redirect("login")
   
    return render(request,'index.html')



def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        print(username,password,email)
      
        if len(password)<8 :
            messages.warning(request,"password must be of minimum 8 characters ")
        else :
            if password==cpassword:
                if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                    messages.warning(request,"User name or Email was not unique please choose another one")
               
                    return render(request,'signin.html')
                else :
                    user=User.objects.create_user(username=username,password=password,email=email)
                    user.save()
                    messages.success(request, "RECORDS ADDED SUCCESSFULLY !!!!.")
                    return render(request,'login.html')
            else :
                messages.warning(request,'Both passwords donot match Kindly check them')
                return  render(request,'signin.html')

        
    return render(request,'signin.html')

    
    # user authrnticate here 

def loginUser(request):
    if request.method=="POST":
        # check credentials 
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        print(username,password,email)

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'loggedin.html')

   


        else:
            messages.warning(request,"Enter valid credentials ")
            return render(request,'login.html')
            # No backend authenticated the credentials signin
            ...

    return render(request,'login.html')





def logoutuser(request):
    logout(request)
    return render(request,'index.html')
    # Redirect to a success page.


# def signin(request):
#     if request.method == "POST":
#         username=request.POST['username']
#         email=request.POST['email']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#         if len(password) < 8 :
#                     # checkin password minimum length 
#                     messages.warning(request,"please make a strong password atleast of 8 charactersand must include a special character")
#                     return render(request,'signin.html')
#         else :
           
#             if password == cpassword : 
#                 # checking password integrity   
#                 if User.objects.filter(username=username).exists():
#                     messages.warning(request,"user name was taken please choose another one")
               
#                     return render(request,'signin.html')
                
                
#                 else:
                    
#                     # cretingh user after integrity was checked 
#                     user1=User.objects.create_user(username=username,password=password,email=email)
#                     user1.is_active=False
#                     messages.success(request,"you account  was created successfully thank you for choosing us ")
#                     return render( request,'login.html')
                

#             else:
#                 messages.info(request,"please verify your passwords")
#                 return  render(request,'signin.html')    
  
#     else:
#         return render(request,'signin.html')   