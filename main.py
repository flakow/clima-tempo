import requests
import pyfiglet

print(pyfiglet.figlet_format("CLIMA - TEMPO"))

#desenvolvido por antonio carlos


cidade = input('DIGITE O NOME DA CIDADE: ')
print('===============================')

print('GERANDO RESULTADO PARA CIDADE: ' + cidade)

url = 'https://wttr.in/{}?m2&lang=pt'.format(cidade)

res = requests.get(url)

print(res.text)

