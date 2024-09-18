import requests,json

def obtenerIpDesdeDominio(dominio):
    print("Dominio ->"+str(dominio))
    resultadoBusqueda = requests.get("https://networkcalc.com/api/dns/lookup/"+str(dominio))
    if resultadoBusqueda.json()["records"] !=None:
      for i in range(len(resultadoBusqueda.json()["records"]["A"])):
          ip = resultadoBusqueda.json()["records"]["A"][i]["address"]
          resultadoRegion = requests.get("https://ipinfo.io/"+ str(ip)+"/json")
          print("la region de la ip -> " +str(ip)+" es " +str(resultadoRegion.json()["region"]))

dominios_empresas = [

   "ecopetrol.com.co",
    "bancolombia.com",
    "grupoaval.com",
    "nutresa.com",
    "exito.com",
    "davivienda.com",
    "terpel.com",
    "avianca.com",
    "grupoargos.com",
    "alpina.com.co",
    "colpatria.com",
    "celsia.com",
    "postobon.com",
    "cocacola.com.co",
    "claro.com.co",
    "movistar.co",
    "etb.com.co",
    "isagen.com.co",
    "carvajal.com",
    "grupoenergiabogota.com",
    "sura.com",
    "colombina.com",
    "cerrejon.com",
    "copetrol.com",
    "biomax.co",
    "carulla.com",
    "almacenesexito.com",
    "pepsico.com.co",
    "unilever.com.co",
    "procterandgamble.com.co",
    "samsung.com.co",
    "huawei.com.co",
    "bavaria.com.co",
    "peldar.com.co",
    "carvajal.com",
    "tigo.com.co",
]

#for i in dominios_empresas:
#    obtenerIpDesdeDominio(i)

def obtenerEmailDesdeDominio(dominio):
    resultadoEmail = requests.get("")
    print(json.dumps(resultadoEmail.json(),indent=4))

obtenerIpDesdeDominio("tiktok.com")