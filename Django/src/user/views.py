from django.shortcuts import render_to_response
from user.models import User
from django.db.models import Q

def list(request):
    user_list = User.objects.all()
    return render_to_response('user/list.html', {'user_list':user_list}) 

def add(request):
    return render_to_response('user/add.html')

def doAdd(request):
    param = request.POST
    user = User()
    user.name = param['name']
    user.gender = param['gender']
    user.ip = request.META['REMOTE_ADDR']
    filename = '/a.jpg'
    f = file(filename, 'w+')
    f.write(request.FILES['photo'])
    f.close
    user.photo = filename
    user.save()
    return render_to_response('user/add.html')

def select():
    User.objects.all()
    User.objects.all()[0:10]
    User.objects.filter(name = 'stariy')
    User.objects.filter(name__startswith = 'lyc')   #istartswith for case sensitive
    User.objects.filter(name__endswith = 'riy')     #iendswith for case sensitive
    User.objects.filter(name__contains = 'yc')      #icontains for case sensitive
    User.objects.filter(pk__in = [1, 2, 3])         #pk for primary key
    User.objects.filter(pk__range = (1,3))
    User.objects.filter(birthday__year = 1988)      #year, month, day, week_day
    User.objects.filter(birthday__gte = '1988-09-17')   #gte is >=, gt is >
    User.objects.filter(birthday__lte = '2012-12-12')   #lte is <=, lt is <
    
    User.objects.get(   #get() must have one result 
        Q(name__startswith = 'lyc'),
        Q(birthday = '1988-9-17') | Q(birthday = '2012-9-17')
    )
    
    User.objects.filter(name = 'error').delete()
    User.objects.filter(name = 'error').count()
    
    #only fields
    #map, return the field's dict
    User.objects.values('name', 'birthday')
    #list, element is tuple which value is in
    User.objects.values_list('name')
    #list, element is value
    User.objects.values_list('name', flat = True)
    
    #order
    User.objects.order_by('name', '-birthday')
    #latest
    User.objects.latest('birthday')
    
    #select_related() if for ForeignKey select, no this will be a lazy select
    User.objects.select_related().get(id=2) 
    
    #raw sql
    name = 'lyc'
    User.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [name])
    
    name_map = {'first': 'first_name', 'last': 'last_name', 'bd': 'birth_date', 'pk': 'id'}
    for u in User.objects.raw('SELECT id, name FROM users', translations=name_map):
        print u.id, u.name
                
                
                