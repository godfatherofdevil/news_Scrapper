# news_Scrapper
web service to scrape news items from BBC and return the result in a JSON response
Currently supported sections:
news, sport, weather, travel, culture, capital, future, food, art, bitsize

to get the data from these section on bbc.com, make a get request with 
two query paramas -> 
chapter : the section from where you want the results, 
news: number of top news that you want


To run:
1. git clone
2. python -m venv env
3. pip install -r requirements.txt
4. python manage.py runserver
