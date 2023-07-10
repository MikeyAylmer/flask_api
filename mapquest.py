from secrets_key import API_SECRET_KEY
import requests

response = requests.get('https://www.mapquestapi.com/geocoding/v1/address', 
             params={'key': API_SECRET_KEY, 'location': 'Denver, CO'})