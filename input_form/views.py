from django.shortcuts import render , redirect
from input_form.models import class_1
import pickle

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')

        obj = class_1(name = name , year = year)
        obj.save()

        lin_regressor = pickle.load( open('lin_reg_virat.pkl' , 'rb'))
        predicted_val = lin_regressor.predict( [[int(year)]] ) 
        
        dic = {'predicted_val' : int(predicted_val) , 'year' : '(' +str(year) + ')'}
        return render(request , 'home.html' , dic)

    
    dic = {'predicted_val' : '___' , 'year' : '(__)'}
    return render(request , 'home.html' , dic)
    