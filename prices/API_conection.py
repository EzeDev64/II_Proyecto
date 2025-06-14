import requests
import xml.etree.ElementTree as ET

URL = "https://pokeapi.co/api/v2/pokemon/zubat"

respuesta = requests.get(URL)
data = respuesta.json()

#print(data["moves"])

#URL = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx?op=ObtenerIndicadoresEconomicosXML"

url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx"

headers = {
    "Content-Type": "text/xml; charset=utf-8",
    #"Content-Length": length
    "SOAPAction": "http://ws.sdde.bccr.fi.cr/ObtenerIndicadoresEconomicosXML"
}

body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ObtenerIndicadoresEconomicosXML xmlns="http://ws.sdde.bccr.fi.cr">
      <Indicador>317</Indicador>
      <FechaInicio>13/6/2025</FechaInicio>
      <FechaFinal>13/6/2025</FechaFinal>
      <Nombre>Client</Nombre>
      <SubNiveles>N</SubNiveles>
      <CorreoElectronico>ezequielbv2305@gmail.com</CorreoElectronico>
      <Token>BZL35UZL1M</Token>
    </ObtenerIndicadoresEconomicosXML>
  </soap:Body>
</soap:Envelope>"""

params = {
    "Indicador":     "317",          # (ej.) tipo de cambio compra
    "FechaInicio":   "12/06/2025",   # dd/mm/aaaa
    "FechaFinal":    "12/06/2025",
    "Nombre":        "Client",
    "SubNiveles":    "N",
    "CorreoElectronico": "ezequielbv2305@gmail.com",
    "Token":         "BZL35UZL1M"              # sólo si tu suscripción lo exige
}

respuesta = requests.post(url,data=body,headers=headers)
#data = respuesta.json()

# Parsear el SOAP XML
soap_tree = ET.fromstring(respuesta.text)
namespaces = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'ns': 'http://ws.sdde.bccr.fi.cr'
}

# Extraer XML escapado
xml_escaped = soap_tree.find('.//ns:ObtenerIndicadoresEconomicosXMLResult', namespaces).text

# Parsear el XML real de datos
data_root = ET.fromstring(xml_escaped)

for nodo in data_root.findall('INGC011_CAT_INDICADORECONOMIC'):
    fecha = nodo.find('DES_FECHA').text
    valor = nodo.find('NUM_VALOR').text
    print(f"{fecha} → {valor}")

print(respuesta.text)