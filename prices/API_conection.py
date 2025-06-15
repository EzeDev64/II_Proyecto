import requests
import xml.etree.ElementTree as ET

url = "https://gee.bccr.fi.cr/Indicadores/Suscripciones/WS/wsindicadoreseconomicos.asmx"

headers = {
    "Content-Type": "text/xml; charset=utf-8",
    #"Content-Length": length
    "SOAPAction": "http://ws.sdde.bccr.fi.cr/ObtenerIndicadoresEconomicosXML"
}

body =f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ObtenerIndicadoresEconomicosXML xmlns="http://ws.sdde.bccr.fi.cr">
      <Indicador>317</Indicador>
      <FechaInicio>#d/#m/#y</FechaInicio>
      <FechaFinal>#d/#m/#y</FechaFinal>
      <Nombre>Client</Nombre>
      <SubNiveles>N</SubNiveles>
      <CorreoElectronico>ezequielbv2305@gmail.com</CorreoElectronico>
      <Token>BZL35UZL1M</Token>
    </ObtenerIndicadoresEconomicosXML>
  </soap:Body>
</soap:Envelope>"""


def get_convertion(day,month,year):
    nbody = body.replace("#d",str(day))
    nbody = nbody.replace("#m",str(month))
    nbody = nbody.replace("#y",str(year))

    respuesta = requests.post(url,data=nbody,headers=headers)

    soap_tree = ET.fromstring(respuesta.text)
    namespaces = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'ns': 'http://ws.sdde.bccr.fi.cr'
    }


    xml_escaped = soap_tree.find('.//ns:ObtenerIndicadoresEconomicosXMLResult', namespaces).text

    data_root = ET.fromstring(xml_escaped)

    for nodo in data_root.findall('INGC011_CAT_INDICADORECONOMIC'):
        fecha = nodo.find('DES_FECHA').text
        valor = nodo.find('NUM_VALOR').text

    return valor

