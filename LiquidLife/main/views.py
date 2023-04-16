import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import JsonResponse
from .models import Filter

# Create your views here.
def index(request):
	filters = Filter.objects.all().values()
	context = {
		"filters": filters,
	}
	return render(request, "index.html", context)

def data(request):
	url = "https://epi.yale.edu/epi-results/2020/component/uwd"
	response = requests.get(url)

	# Parse the HTML content using BeautifulSoup
	soup = BeautifulSoup(response.content, 'html.parser')

	# Find the table element
	table = soup.find('table')
	tr_element = table.find_all('tr')[1:]
	lst = []
	# Loop through each row of the table
	for row in tr_element:
		a_element = row.find("td").find("a")
		rank = row.find('td', {'class': 'epi-scorerank'}).text
		value = row.find('td', {'class': 'epi-scorevalue'}).text
		change = row.find('td', {'class': 'epi-scorechange'}).text
		# Access the text content and href attribute of the a element
		country_name = a_element.text
		country_url = a_element['href']
		url = "https://epi.yale.edu/" + country_url

		dic = {
			"country": country_name.strip(),
			"country_url": country_url.strip(),
			"rank": rank.strip(),
			"value": value.strip(),
			"change": change.strip()
		}
		lst.append(dic)
	return JsonResponse({"data": lst})
