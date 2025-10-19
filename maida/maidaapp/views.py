from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myname_view(request):
    data_1 ={}
    data_2 ={}
    data_1["my_name"] = "Maida"

    data_2["student_id"] = "2212175911"
    context = {**data_1, **data_2}

    return render(request, "maida.html", context )


#def my_classes_view(request):
    class_list = {}
    class_list[
        "Web Development",
        "Communication and Report Writing",
    ]

    context = {
        "class_list": class_list
    }

    return render(request, "myclasses.html", context)
def my_classes_view(request):
    class_list = [
        "Web Development",
        "Communication and Report Writing",
    ]

    context = {
        "class_list": class_list
    }

    return render(request, "myclasses.html", context)
