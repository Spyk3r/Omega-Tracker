import os, requests
variable_logo = """\033[33m  .oooooo.   ooo        ooooo oooooooooooo   .oooooo.          .o.       
 d8P'  `Y8b  `88.       .888' `888'     `8  d8P'  `Y8b        .888.      
888      888  888b     d'888   888         888               .8"888.     
888      888  8 Y88. .P  888   888oooo8    888              .8' `888.    
888      888  8  `888'   888   888    "    888     ooooo   .88ooo8888.   
`88b    d88'  8    Y     888   888       o `88.    .88'   .8'     `888.  
 `Y8bood8P'  o8o        o888o o888ooooood8  `Y8bood8P'   o88o     o8888o"""


def main():
  print(variable_logo)
  
  variable_ip = input('\n\033[94m Ingresa la IP: ')
  variable_api = (str(f'http://ip-api.com/json/{variable_ip}?fields=26476543'))
  variable_response = requests.get(variable_api).json()
  os.system("clear")
  try:
    
    print('[!] IP Consultada: ', variable_response['query'])
    print('[!] Continente: ', variable_response['continent'])
    print('[!] Pais: ', variable_response['country'])
    print('[!] Ciudad: ', variable_response['city'])
    print('[!] Región: ', variable_response['regionName'])
    print('[!] Zona Horaria: ', variable_response['timezone'])
    print('[!] Latitud: ', variable_response['lat'])
    print('[!] Longitud: ', variable_response['lon'])
    print('[!] Organización: ', variable_response['org'])
    print('[!] ISP: ', variable_response['isp'])
    print('[!] ZIP: ', variable_response['zip'])
    print('[!] PROXY: ', variable_response['proxy'])
    print('[!] Hosting: ', variable_response['hosting'])
    print('[!] DNS Inverso de la IP: ', variable_response['reverse'])
    
    variable_creador = """\n\033[31m            
            ______________________  
            Creado por: GoldenDark
            ______________________
              Omega Tracker V1
              _______________"""
    print(variable_creador)
  except KeyError:
    print('\n\033[31m Ip Invalida, prueba de nuevo')
  
  
main()
      
  
  