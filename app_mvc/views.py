from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Employee
from .forms import  Form_cofee #EmployeeForms 

def home(request):
    employee = Employee.objects.filter(published=True)
    return render(request, 'app_mvc/home.html', { 'employee': employee })
# ------------------------------------------
def add_form(request):
    if request.method == 'POST':
        if 'Espresso' in request.POST:
            form = Form_cofee(request.POST)
            # test = form.cleaned_data['sum']
            mix = "กาแฟ 1 ช๊อต"
            args = {'mix': mix,
                # 'test':test
                }
            return render(request, 'app_mvc/form.html', args)
        elif 'Cappuccino' in request.POST:
            mix = "กาแฟ 1 ช๊อต และนม 1 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/form.html', args)
        elif 'Latte' in request.POST:
            mix = "กาแฟ 1 ช๊อต และนม 2 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/form.html', args)
        elif 'Americano' in request.POST:
            mix = "กาแฟ 1 ช๊อต และน้ำร้อน 2 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/form.html', args)
        elif 'Summary' in request.POST:
            mix = ""
            args = {'mix': mix}
            return render(request, 'app_mvc/form.html', args)
    else:
        return render(request, 'app_mvc/form.html')
    # elif 'Cappuccino' in request.POST:

    # elif 'Latte' in request.POST:
    
    # elif 'Americano' in request.POST:
    # if request.method == 'POST':
    #     form = EmployeeForms(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse('app_mvc:add-form'))
		
    # else:
    #     form = EmployeeForms(request.POST)
    #     args = {'form': form}
    #     return render(request, 'app_mvc/form.html', args)
# ------------------------------------------
def edit_form(request):
    template = 'app_mvc/edit.html'


    if request.method == 'POST':
        form =  EmployeeForms(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Yess edit')
        except:
            messages.warning(request, 'Not edit'.format())
    
    else:
        form = EmployeeForms()

        context = {
            'form':form,

        }
    return render(request, template, context)

def delete_form(request):
    template = 'app_mvc/edit.html'


    if request.method == 'POST':
        form =  EmployeeForms(request.POST)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Yess delete')
        except:
            messages.warning(request, 'Not delete'.format())
    
    else:
        form = EmployeeForms()

        context = {
            'form':form,

        }
    return render(request, template, context)
