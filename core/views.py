import datetime
from django.shortcuts import redirect
from django.shortcuts import render

#Modelos creados
from .models import Link, Capturado
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def hunt_usuario(request, link_id):
    "Obtenemos el link trampa"
    l = Link.objects.get(pk=link_id)
    "Aqui debemos guardar la informacion obtenida"
    if l.monitorizar:
        c = Capturado()
        c.link = l
        c.datetime = datetime.datetime.now()
        c.meta =  '\n'.join('{}: {}'.format(k, v)
                            for k, v in request.META.items())
        c.ip_extra = [request.META.get(x) for x in ['HTTP_X_FORWARDED_FOR', 
                                    'X_FORWARDED_FOR',
                                    'HTTP_CLIENT_IP',
                                    'HTTP_X_REAL_IP',
                                    'HTTP_X_FORWARDED',
                                    'HTTP_X_CLUSTER_CLIENT_IP',
                                    'HTTP_FORWARDED_FOR',
                                    'HTTP_FORWARDED',
                                    'HTTP_VIA',
                                    'REMOTE_ADDR']]
        c.save()
    "Lo enviamos al link destino elegido sin que se entere que lo trackeamos>"
    return redirect(l.link_destino)