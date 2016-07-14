import json
import jsondate

separators = (',', ':')


class json_formato:
    def deserializar(self, response):
        data = json.loads(response)
        return data

    def serializar(self, payload):
        data = json.dumps(payload, separators=separators)
        return data

    def serializar_datetime(self, payload):
        data = jsondate.dumps(payload)
        return data

    def deserializar_datetime(self, payload):
        data = jsondate.loads(payload)
        return data
