from django import forms
from django.contrib.admin import widgets
import pypyodbc
import pandas as pd

class ContactForm(forms.Form):

    conn = pypyodbc.connect("Driver={SQL Server Native Client 10.0};"
                        "Server=LAPTOP-77C7OI12;"
                        "Database=PRESALES;"
                        "uid=sa;pwd=1234")
    
    df2=pd.read_sql_query('Select distinct U_UserName from [dbo].[@OMTR]',conn)
    df_usrnm=list(df2['u_username'])
    users = []
    for x in range(len(df_usrnm)):
        users.append([df_usrnm[x],df_usrnm[x]])
    name = forms.CharField(widget=
    forms.Select(choices=users,attrs={"id":'user'}))
