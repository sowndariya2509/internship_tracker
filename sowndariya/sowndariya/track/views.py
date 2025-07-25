from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . import dbCon  # MongoDB connection

# Show the Add Form
def add(request):
    return render(request,'add.html')

# Save New Intern Record
def addsave(request):
    if request.method == 'POST':
        regno = request.POST.get('regno', '')
        name = request.POST.get('name', '')
        department = request.POST.get('department', '')
        company = request.POST.get('company', '')
        duration = request.POST.get('duration', '')
        domain = request.POST.get('domain', '')
        mail = request.POST.get('mail', '')

        data = {
            "regno": regno,
            "name": name,
            "department": department,
            "company": company,
            "duration": duration,
            "domain": domain,
            "mail": mail
        }
        dbCon.col.insert_one(data)
        return redirect('listdata')
    else:
        return redirect('add')  # redirect to form if GET request

# List All Intern Records
def listdata(request):
    interns = dbCon.col.find()
    return render(request,'list.html',{'var': interns})

# Edit an Intern Record
def edit(request, regno):
    entry = dbCon.col.find_one({"regno": regno})
    if request.method == "POST":
        name = request.POST.get("name", "")
        department = request.POST.get("department", "")
        company = request.POST.get("company", "")
        duration = request.POST.get("duration", "")
        domain = request.POST.get("domain", "")
        mail = request.POST.get("mail", "")

        dbCon.col.update_one(
            {"regno": regno},
            {"$set": {
                "name": name,
                "department": department,
                "company": company,
                "duration": duration,
                "domain": domain,
                "mail": mail
            }}
        )
        return redirect('listdata')
    return render(request,"edit.html", {"entry": entry})

# Delete an Intern Record
def delete(request, regno):
    dbCon.col.delete_one({"regno": regno})
    return redirect("listdata")