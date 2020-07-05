from django import forms
from app.models import *
from django.utils.translation import gettext_lazy as l #this for helptext and label attributes

class mcat(forms.ModelForm): #from forms import modelform class 
    class Meta:
        model = category #this create the models
        fields = '__all__' #['catid','age']

class mflip(forms.ModelForm):
    class Meta:
        model = flipkart
        fields = '__all__' #['fid','fname','fprice','catid'] we can choose the which u want
        #exclude = ['fid'] #except fid we can add data to remaining fields
        #widgets = {'columnname':'value1','columnname':'value'...................}
        #labels = {'name':l('ur name'),'url':l('ur url')}

class mzon(forms.ModelForm):
    class Meta:
        model = amazon
        fields = '__all__' #all fields will add

class mcustom(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'