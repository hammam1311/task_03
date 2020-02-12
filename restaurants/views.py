from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
        "my_list":[
            {
            "restaurant_name":"pizzahut",
            "food_type":"pizza :)",
            }
            ,
            {
            "restaurant_name":"Mcdonals"
            ,"food_type":"Mac Stuff :)",
            },
        ],
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object":{
        "restaurant_name":"pizzahut ",
        "food_type":"pizza ",
        }
    }
    return render(request, 'detail.html', context)
