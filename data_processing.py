from bs4 import BeautifulSoup
import requests


disorder_gene = {}

def data_extract():

  url = "https://en.wikipedia.org/wiki/List_of_genetic_disorders"
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'html')
  table = soup.find('table', class_ = 'wikitable sortable')

  for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    disorder = cells[0].text.strip()
    if disorder[-2:] == '\n':
      disorder = disorder[:-2]
    gene = cells[2].text.strip()
    if gene == 'dominant' or gene == 'recessive' or gene == 'D':
      disorder_gene[disorder] = gene
    
data_extract()