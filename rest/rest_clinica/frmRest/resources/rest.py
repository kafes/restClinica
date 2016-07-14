import requests

headers = {'content-type': 'application/json'}
base = "http://localhost:8080/clinicaTest-war/ws/"


class resources:
    # GET
    def get(self, url):
        try:
            response = requests.get(base + url, headers=headers)
            if str(response.status_code).startswith('5') | str(response.status_code).startswith('4'):
                if str(response.status_code).startswith('5'):
                    print("Problemas al obtener los datos desde el server")
                elif str(response.status_code).startswith('4'):
                    print("Problemas al obtener los datos, el usuario ha generado un error")
                response.raise_for_status()
            elif str(response.status_code).startswith('2'):
                return response.text
        except requests.RequestException as e:
            print(str(e))

    # POST
    def post(self, url, payload):
        try:
            response = requests.post(base + url, data=payload, headers=headers)
            if str(response.status_code).startswith('5') | str(response.status_code).startswith('4'):
                if str(response.status_code).startswith('5'):
                    print("Problemas con el server al hacer post")
                elif str(response.status_code).startswith('4'):
                    print("Problemas con los datos enviados por el usuario, ha generado un error")
                response.raise_for_status()
            elif str(response.status_code).startswith('2'):
                return response.text
        except requests.RequestException as e:
            print(str(e))

    # PUT
    def put(self, url, payload):
        try:
            response = requests.put(base + url, data=payload, headers=headers)
            if str(response.status_code).startswith('5') | str(response.status_code).startswith('4'):
                if str(response.status_code).startswith('5'):
                    print("Problemas con el server al hacer generar nuevo registro")
                elif str(response.status_code).startswith('4'):
                    print("Problemas con los datos enviados por el usuario, ha generado un error")
                response.raise_for_status()
            elif str(response.status_code).startswith('2'):
                return response.text
        except requests.RequestException as e:
            print(str(e))

    # DELETE
    def delete(self, url):
        try:
            response = requests.delete(base + url, headers=headers)
            if str(response.status_code).startswith('5') | str(response.status_code).startswith('4'):
                if str(response.status_code).startswith('5'):
                    print("Problemas con el server al eliminar")
                elif str(response.status_code).startswith('4'):
                    print("Problemas con los datos enviados por el usuario, ha generado un error")
                response.raise_for_status()
            elif str(response.status_code).startswith('2'):
                return "Se ha eliminado con éxito"
        except requests.RequestException as e:
            print(str(e))
