from django.http.response import HttpResponse, JsonResponse
from django.views import generic
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from pharmaProfile.forms import AddExpenseForm, ChangePasswordForm, RegisterSalesmanForm, PermitSalesmanForm
from django.urls import reverse, reverse_lazy
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from pharmaProfile.models import Profile, Expense


class ManageUser(generic.TemplateView):
    template_name = 'profile/xusers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bosses = []
        users = []

        user = User.objects.all()
        for userToAuth in user:
            if userToAuth.is_superuser or userToAuth.profile.is_boss:
                bosses.append(userToAuth)
                continue
            users.append(userToAuth)
        
        context['add_user_form'] = RegisterSalesmanForm
        context['users'] = users
        context['bosses'] = bosses
        return context


class SalesManRegisterView(generic.View):
    template_name= "profile/profile.html"

    def get(self, request):
        return render(request, self.template_name, {'form': RegisterSalesmanForm})
    
    def post(self, request, **kwargs):
        form = RegisterSalesmanForm(request.POST)

        first_name = request.POST.get('firstName')
        middle_name = request.POST.get('middleName')
        last_name = request.POST.get('lastName')
        gender = request.POST.get('gender') 
        nida = request.POST.get('nida')
        kura = request.POST.get('kura')
        licence = request.POST.get('licence')
        mobile_number = request.POST.get('mobileNumber')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_r = "mganaluka"

        if form.is_valid():
            if username and password_r:
                user_r = User.objects.create_user(username=username, password=password_r)
                user_r.save()
                
                prof  = Profile.objects.get(owner = user_r)
                prof.email = email
                if middle_name:
                    prof.fullname = first_name +" "+middle_name+" "+last_name
                else:
                    prof.fullname = first_name +" "+last_name
                prof.mobile = mobile_number
                if nida:
                    prof.nida = nida
                if licence:
                    prof.licence = licence
                if kura:
                    prof.kura = kura
                prof.gender = gender            
                prof.save()

                new_user = Profile.objects.get(owner = user_r)

                total_nomo = Profile.objects.all().count() - 1

                nomo = Profile.objects.filter(is_boss=False).values()
                return JsonResponse({
                    'nomo': model_to_dict(new_user), 
                    'total_nomo':total_nomo
                    })
                    
            else:
                # print('Please enter valid food informations')
                return HttpResponse('user not added there is an error, right!?')
        

class PermitSalesman(generic.View):

    def post(self, request):
        profile = Profile.objects.get(profileId=request.POST['userid'])
        
        permitted = get_object_or_404(Profile, profileId=profile.pk)

        for a in request.POST:
            if a == 'csrfmiddlewaretoken' or a == 'userid':
                continue
            print(bool(request.POST[a]))
            
 
        form_submitted = PermitSalesmanForm(request.POST, instance=permitted)


        if form_submitted.is_valid():
            form_submitted.save()
            return HttpResponse('hope now user is ready permitted to some of permissions')

        else:
            return  HttpResponse('permitted by the way')


def resetePassword(request, pk):
    user_to_reset = User.objects.get(id=pk)
    user_to_reset.set_password('pharmacy')
    user_to_reset.save()
    bosses = Profile.objects.filter(is_boss=True).values()
    nomo = Profile.objects.filter(is_boss=False).values()
    return JsonResponse({'bosses':list(bosses), 'nomo': list(nomo)})


def changePassword(request):
    form = ChangePasswordForm
    template = 'profile/changepassword.html'
    if request.method == 'POST':
        user_to_change= User.objects.get(id=request.user.pk)

        new_pass = request.POST['new_password']
        new_pass1 = request.POST['new_password1']
        
        if new_pass == new_pass1:
            user_to_change.set_password(new_pass)
            user_to_change.save()
            
            return HttpResponse('changed')

    return render(request, template, {'form': form})



def RemoveUser(request, pk):
    profile_to = Profile.objects.get(profileId=pk)
    User.objects.get(id=profile_to.pk).delete()
    
    bosses = Profile.objects.filter(is_boss=True).values()
    nomo = Profile.objects.filter(is_boss=False).values()
    return JsonResponse({'bosses':list(bosses), 'nomo': list(nomo)})

def GetUser(request, pk):
    profileUser = User.objects.get(id=pk)
    profile = Profile.objects.get(owner=profileUser)
    return JsonResponse({"formData":model_to_dict(profile)})

def showExpenses(request):
    expenses = Expense.objects.filter(user = request.user)
    return JsonResponse({'expenses':expenses})
    pass



class Expenses(generic.View):
    template_name = 'expenses/expenses.html'
    form = AddExpenseForm
    context = {}
    def get(self, request):
        self.context['form'] = self.form
        if self.request.user.is_authenticated:
            self.context['expenses']= Expense.objects.filter(user=self.request.user)

        return render(request, self.template_name, context=self.context)
    
    def post(self, request):
        form = self.form(request.POST)
        print(form)
        user = request.user
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = user
            new_exp = form.save(commit=True)
            total= Expense.objects.all().count()
            return JsonResponse({'expense':model_to_dict(new_exp), 'total':total})
            # return HttpResponse('added successfully')