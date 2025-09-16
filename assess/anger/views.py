from django.shortcuts import render,redirect
from anger.models import Attend


def attendance(request):
    if request.method == 'POST':
        form_data = request.POST
        sent_name = form_data.get('name')
        sent_studentid = form_data.get('studentid')
        sent_ispresent ='ispresent' in form_data
        sent_date = form_data.get('date')
        
        new_record = Attend()
        new_record.name = sent_name
        new_record.student_id = sent_studentid
        new_record.is_present = sent_ispresent
        new_record.date = sent_date
        new_record.save()
        return redirect('/')
    return render(request,'add.html')
def home(request):
    all_records = Attend.objects.all()
    context ={
        'all_records':all_records
    }
    return render(request,'index.html',context)
def viewOneStudent(request,record_id):
    selected = Attend.objects.get(id=record_id)
    context ={
        'selected':selected
    }
    return render(request,'view.html',context)
def deleteRecord(request,record_id):
    record_to_delete = Attend.objects.get(id=record_id)
    if request.method == 'POST':
        record_to_delete.delete()
        return redirect('/')
    context = {
       'selected' :record_to_delete

    }
    return render(request,'delete.html',context)
def updatePage(request,record_id):
    record_to_update = Attend.objects.get(id=record_id)
    if request.method == 'POST':
        record_to_update.is_present = 'is_present' in request.POST
        record_to_update.save()
        return redirect('/update/'+str(record_to_update.id))
    context = {
            'selected':record_to_update
        }
    return render(request,'update.html',context)  
def editRecord(request,record_id):
    record_to_edit = Attend.objects.get(id=record_id)
    if request.method == 'POST':
        form_data = request.POST
        record_to_edit.name = form_data.get('name')
        record_to_edit.student_id = form_data.get('studentid')
        record_to_edit.is_present ='ispresent' in request.POST
        record_to_edit.save()
        return redirect('/view/'+str(record_to_edit.id))
    context = {
        'selected':record_to_edit
    }
    return render(request,'edit.html',context)


        
        
   
        

# Create your views here.
