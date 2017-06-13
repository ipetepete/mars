from django.shortcuts import render

# Create your views here.


def search(request):
    # TODO: Get telescope + intrument combos from db
    tel = type('Telescope', (object,),{})
    telescopes = []
    for i in range(1,10):
        t = tel()
        t.name = "Telescope{0}-Intrument{0}".format(i)
        t.id = i
        telescopes.append(t)

    print(telescopes)
    return render(request, "search.html", {'telescopes':telescopes})
