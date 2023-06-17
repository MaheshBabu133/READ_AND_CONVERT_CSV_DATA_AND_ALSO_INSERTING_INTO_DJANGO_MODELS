from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import csv
from app.models import *
def Bank_Data_Upload(request):
    a='C:\\Users\\Sivananda\\OneDrive\\Desktop\\7EDE6_Batch\\API\\Scripts\\PROJECT_5\\bank.csv'
    # a is my file path 
    with open(a,'r') as file:
        csv_data=csv.reader(file)
        print(next(csv_data))
        #Above next method will skip the rows because 
        #First row contains the headings we dont want it

        for a in csv_data:
            bn=a[0].strip()
            #In order to remove the extra spaces iam using the strip()
            instance=Bank(bname=bn)
#We can insert the data manyways now iam choosing the Instance method 
#instance varible which is took by me
            

            instance.save()

    return HttpResponse("The bank data is inserted successfully")



def Branch_Data_Upload(request):
    a='C:\\Users\\Sivananda\\OneDrive\\Desktop\\7EDE6_Batch\\API\\Scripts\\PROJECT_5\\branch1.csv'
    # a  is my file path 


    with open(a,'r') as file:
        csv_data=csv.reader(file)
        print(next(csv_data))
        #Above next method will skip the rows because 
        #First row contains the headings we dont want it

        for a in csv_data:
            bn=a[0].strip()
            bank_object=Bank.objects.get(bname=bn)

            instance=Branch(bname=bank_object,
            ifcs=a[1],
            branch=a[2],
            address=[3],
            contract=a[4],
            city=a[5],
            district=a[6],
            state=a[7]
            )
            instance.save()


    return HttpResponse("The branch data is uploaded successfully ")
