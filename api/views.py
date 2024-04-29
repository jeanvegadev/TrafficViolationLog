from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Vehiculo, Oficial, Infraccion, AccessToken, Persona
from .forms import InfraccionForm, OficialForm, GenerarInformeForm
from .tokens import generate_access_token


@method_decorator(csrf_exempt, name='dispatch')
class CargarInfraccionView(View):
    def get(self, request):
        form = InfraccionForm()
        return render(request, 'api/infraccion_form.html', {'form': form})

    def post(self, request):
        # Retrieve Bearer token from the request headers
        authorization_header = request.headers.get('Authorization')

        # Check if the Authorization header exists and starts with 'Bearer '
        if authorization_header and authorization_header.startswith('Bearer '):
            # Extract the token value (remove 'Bearer ' prefix)
            bearer_token = authorization_header[len('Bearer '):]
        else:
            # Handle the case where the Authorization header is missing
            return JsonResponse({'error': 'Invalid Bearer token'}, status=401)
        placa_patente = request.POST.get('placa_patente')
        timestamp = request.POST.get('timestamp')
        comentarios = request.POST.get('comentarios')

        if not placa_patente or not timestamp or not comentarios:
            return JsonResponse({'error': 'Faltan parámetros'}, status=400)

        try:
            acceso = AccessToken.objects.get(token=bearer_token)
        except AccessToken.DoesNotExist:
            return JsonResponse({'error': 'El token no existe'},
                                status=404)

        # Verificar si existe el vehículo
        try:
            vehiculo_u = Vehiculo.objects.get(placa_patente=placa_patente)
        except Vehiculo.DoesNotExist:
            return JsonResponse({'error': 'La placa patente no existe'},
                                status=404)

        # Aquí iría el código para registrar la infracción en la base de datos
        infraccion = Infraccion(
            vehiculo=vehiculo_u,
            oficial=acceso.oficial,
            timestamp=timestamp,
            motivo=comentarios)
        infraccion.save()

        return JsonResponse({'message': 'Infracción cargada correctamente'},
                            status=200)


@method_decorator(csrf_exempt, name='dispatch')
class GenerarInformeView(View):
    def get(self, request):
        form = GenerarInformeForm()
        return render(request, 'api/generar_informe.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        try:
            persona = Persona.objects.get(
                correo_electronico=email)
        except Persona.DoesNotExist:
            return JsonResponse({'error': 'La persona no existe'},
                                status=404)
        # Obtener todos los vehículos asociados a la persona
        vehiculos = Vehiculo.objects.filter(propietario=persona)

        # Obtener todas las infracciones asociadas a los vehículos de 
        infracciones = Infraccion.objects.filter(vehiculo__in=vehiculos)

        # Formatear los datos de las infracciones en un formato JSON
        informe = [{'placa_patente': i.vehiculo.placa_patente,
                    'fecha_infraccion': i.timestamp,
                    'comentarios': i.motivo} for i in infracciones]

        # Devolver el informe como respuesta JSON
        return JsonResponse(informe, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class BearerTokenView(View):
    def get(self, request):
        form = OficialForm()
        return render(request, 'api/token_form.html', {'form': form})

    def post(self, request):
        nombre_oficial = request.POST.get('nombre')
        numero_unico = request.POST.get('numero_unico')
        try:
            oficial_user = Oficial.objects.filter(
                numero_identificatorio=numero_unico).get(nombre=nombre_oficial)
        except Oficial.DoesNotExist:
            return JsonResponse({'error': 'El oficial no existe'},
                                status=404)
        token = generate_access_token(oficial_user)
        return JsonResponse({'token': token},
                            status=200)
