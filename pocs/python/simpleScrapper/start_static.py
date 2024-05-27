# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import sys

# def get_page(page):
#   #https://www.vivareal.com.br/venda/distrito-federal/brasilia/#onde=,Distrito%20Federal,Bras%C3%ADlia,,,,,city,BR%3EDistrito%20Federal%3ENULL%3EBrasilia,,,
#   url = f'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/?pagina={page}#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'
#   req = requests.get(url, headers={'User-Agent': 'Mozzila/5.0'})
#   pagina = req.text
#   soup = BeautifulSoup(pagina, 'html.parser')
#   # return soup
#   return soup.prettify()


# # Criação das listas que vão receber os valores
# full_adress = []
# full_description = []
# full_area = []
# full_room = []
# full_bath = []
# full_garage = []
# full_price = []


# # print the soup before iterate pages
# # print(soup)
# # print(soup.findAll(class_ = 'js-card-selector'))
# # sys.exit(0)

# # Criando o loop entre as paginas do site
# for page in range(1,1500):
#   soup = get_page(page)
#   for line in soup.findAll(class_ = 'js-card-selector'):
  
#     # Extrai apenas o bairro, a rua e a cidade são irrelevantes 
#     adress = line.find('span', attrs={'class': 'property-card__address'}).text.replace(', Florianópolis', '').strip().split('-')  
#     if adress[0][:3] == 'Rua' or adress[0][:7] == 'Rodovia':
#       full_adress.append(adress[1].strip())
#     else:
#       full_adress.append(adress[0].strip())
    
#     # Extrai a descrição pegando apenas o dado se é casa, apartmento ou lote
#     description = line.find('span', attrs={'class': 'property-card__title js-cardLink js-card-title'}).text.strip().split(' ')[0]
#     full_description.append(description)

#     # Extrai a metragem
#     area = line.find('span', attrs={'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'}).text.strip()
#     full_area.append(area)

#     # Extrai número de quartos
#     room = line.find(class_='property-card__detail-item property-card__detail-room js-property-detail-rooms').text.strip().split(' ')[0]
#     full_room.append(room)

#     # Extrai número de banheiros
#     bath = line.find(class_='property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom').text.strip().split(' ')[0]
#     full_bath.append(bath)

#     # Extrai número de vagas
#     garage = line.find(class_='property-card__detail-item property-card__detail-garage js-property-detail-garages').text.strip().split(' ')[0]
#     full_garage.append(garage)

#     # Extrai preço
#     price = line.find(class_='property-card__price js-property-card-prices js-property-card__price-small').text.replace('R$', '').strip()
#     full_price.append(price)

# df = pd.DataFrame({'Bairro': full_adress, 'Tipo': full_description, 'Metragem': full_area, 'Quartos': full_room, 'Banheiros': full_bath, 'Vagas': full_garage, 'Preço': full_price})
# df

import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import time
from fp.fp import FreeProxy
# import cloudscraper

while True:
    try:
        proxy = FreeProxy(country_id=['BR'], timeout=1, https=True).get()
        break
    except fp.errors.FreeProxyException as e:
        if str(e) != 'There are no working proxies at this time.':
            raise
        else:
            print('Nenhum proxy disponível. Tente novamente em 1 minuto.')
            time.sleep(1)

print(f'Proxy: {proxy}')
def get_page(page):
    # url = f'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/?pagina={page}#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'
    url = f'https://104.18.86.87/venda/santa-catarina/florianopolis/?pagina={page}#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'
    req = requests.get(url, headers={'User-Agent': 'Mozzila/5.0'}, proxies={"http": proxy, "https": proxy})
    content = req.text
    
    # scraper = cloudscraper.create_scraper(delay=10, browser="chrome", proxy=proxy) 
    # content = scraper.get(url).text 

    soup = BeautifulSoup(content, 'html.parser')

    return soup

# Criação das listas que vão receber os valores
full_adress = []
full_description = []
full_area = []
full_room = []
full_bath = []
full_garage = []
full_price = []

# Criando o loop entre as paginas do site
page = 1
max_page = 999
while True:
  soup = get_page(page)
  print(f'Soup', soup)
  break
  # Atualiza o número máximo de páginas
  pagination_items = soup.find_all(attrs={'class': 'js-change-page'})
  if pagination_items:
    max_page = max(int(item.get('data-page')) for item in pagination_items)
    print(f'Página {page} de {max_page}')
    if page > max_page:
      break
  else:
    print('Nenhum item de paginação encontrado')
    break

  for line in soup.findAll(class_ = 'js-card-selector'):
    # Extrai apenas o bairro, a rua e a cidade são irrelevantes 
    adress = line.find('span', attrs={'class': 'property-card__address'}).text.replace(', Florianópolis', '').strip().split('-')  
    if adress[0][:3] == 'Rua' or adress[0][:7] == 'Rodovia':
      full_adress.append(adress[1].strip())
    else:
      full_adress.append(adress[0].strip())
    
    # Extrai a descrição pegando apenas o dado se é casa, apartmento ou lote
    description = line.find('span', attrs={'class': 'property-card__title js-cardLink js-card-title'}).text.strip().split(' ')[0]
    full_description.append(description)

    # Extrai a metragem
    area = line.find('span', attrs={'class': 'property-card__detail-value js-property-card-value property-card__detail-area js-property-card-detail-area'}).text.strip()
    full_area.append(area)

    # Extrai número de quartos
    room = line.find(class_='property-card__detail-item property-card__detail-room js-property-detail-rooms').text.strip().split(' ')[0]
    full_room.append(room)

    # Extrai número de banheiros
    bath = line.find(class_='property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom').text.strip().split(' ')[0]
    full_bath.append(bath)

    # Extrai número de vagas
    garage = line.find(class_='property-card__detail-item property-card__detail-garage js-property-detail-garages').text.strip().split(' ')[0]
    full_garage.append(garage)

    # Extrai preço
    price = line.find(class_='property-card__price js-property-card-prices js-property-card__price-small').text.replace('R$', '').strip()
    full_price.append(price)
  
  page += 1
  # ///
  df = pd.DataFrame({'Bairro': full_adress, 'Tipo': full_description, 'Metragem': full_area, 'Quartos': full_room, 'Banheiros': full_bath, 'Vagas': full_garage, 'Preço': full_price})
  df
  sys.exit()
  # ///
  
  time.sleep(5)

df = pd.DataFrame({'Bairro': full_adress, 'Tipo': full_description, 'Metragem': full_area, 'Quartos': full_room, 'Banheiros': full_bath, 'Vagas': full_garage, 'Preço': full_price})
df

