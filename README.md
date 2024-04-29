# Registro de infracciones de Tráfico

Stack: Django, MySQL, Docker, Docker-compose

1. Instalar docker y docker compose

2. Ejecutar: docker-compose up -d


Endpoints:

1. Obtener Token.

url = "http://127.0.0.1:8000/obtener_token/"

payload = {'nombre': 'Marks',
'numero_unico': '12'}

2. Generar informe.

url = "http://127.0.0.1:8000/generar_informe/"

payload = {'email': 'juan@gmail.com'}

3. Cargar Infraccion.


url = "http://127.0.0.1:8000/cargar_infraccion/"

payload = {'placa_patente': 'XYZ986',
'timestamp': '2024-04-27 00:00',
'comentarios': 'Exceso de velocidad2'}
files=[

]
headers = {
  'Authorization': 'Bearer XYZ'
}