from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django import forms
import pandas as pd
import pypyodbc
import cgi
from .form import ContactForm
from .form import *
from datetime import datetime
import geocoder
def index(request):
    conn = pypyodbc.connect("Driver={SQL Server Native Client 10.0};"
                        "Server=LAPTOP-77C7OI12;"
                        "Database=PRESALES;"
                        "uid=sa;pwd=1234")
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            namee = form.cleaned_data['name']
            datee = request.POST['date']
            namee = str(namee)
            uid= pd.read_sql_query('select distinct U_UserCode from [dbo].[@OMTR] where U_UserName = ?',conn,params=[namee])
            time = pd.read_sql_query
            datee=str(datee)
            dat = datetime.strptime(datee, '%Y-%m-%d')
            idd=str(uid.iloc[0]['u_usercode'])
            df = pd.read_sql_query('Select * from [dbo].[@MTR1] INNER JOIN [dbo].[@OMTR] ON [dbo].[@MTR1].DocEntry = [dbo].[@OMTR].DocEntry WHERE [dbo].[@MTR1].U_DateTime=? AND [dbo].[@OMTR].U_UserCode=?',conn,params=[dat,idd])
            df_lat=list(df['u_lat'])
            df_long=list(df['u_long'])
            df_time=list(df['u_time'])
            addresses=[]
            locations=[]
            for x in range(len(df_lat)):
                
                locations.append([float(df_lat[x]),float(df_long[x]),geocoder.osm([float(df_lat[x]),float(df_long[x])],method='reverse'),df_time[x]])
                
            return render(request, 'trackpage/home.html',{'form': form,"loc":locations,"nam":namee,"dat":datee})

            #return HttpResponseRedirect('/')
    else:
        form = ContactForm()     
    args={}
    args['form'] = form
    df_usrnm=form.df_usrnm
    return render(request, 'trackpage/home.html',{"data":df_usrnm,'form': form},args)

