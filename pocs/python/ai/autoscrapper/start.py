# from autoscraper import AutoScraper

# # url = 'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/?pagina={page}#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'
# url = 'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/?pagina=1#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'

# # We can add one or multiple candidates here.
# # You can also put urls here to retrieve urls.
# # wanted_list = ["What are metaclasses in Python?"]
# wanted_list = ["What are the prices and descryption of the itens?"]



# scraper = AutoScraper()
# result = scraper.build(url, wanted_list)
# print(result)


from autoscraper import AutoScraper

url = 'https://www.vivareal.com.br/venda/santa-catarina/florianopolis/?pagina=1#onde=,Santa%20Catarina,Florian%C3%B3polis,,,,,city,BR%3ESanta%20Catarina%3ENULL%3EFlorianopolis,,,'
wanted_list = ['Endereço', 'Descrição', 'Área', 'Quarto', 'Banheiro', 'Garagem', 'Preço']

scraper = AutoScraper()
result = scraper.build(url, wanted_list)

print(result)