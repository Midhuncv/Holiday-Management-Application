import os
from dotenv import load_dotenv
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.core.cache import cache


load_dotenv()

@api_view(['GET'])
def get_holidays(request):
    country = request.GET.get('country')
    year = request.GET.get('year')

    if not country or not year:
        return Response({'error': 'Country and Year are required parameters'}, status=400)

    api_key = os.getenv('CALENDARIFIC_API_KEY')
    print(f"API Key from env: {api_key}")  

    if not api_key:
        return Response({'error': 'API key is not configured'}, status=500)

    cache_key = f"{country}_{year}"
    holidays = cache.get(cache_key)  

    
    if not holidays:
        url = "https://calendarific.com/api/v2/holidays"
        params = {
            'api_key': api_key,
            'country': country,
            'year': year
        }
        print(f"API Params: {params}")  

        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                holidays = response.json()

        
                if 'response' in holidays and 'holidays' in holidays['response']:
                    cache.set(cache_key, holidays, timeout=86400)  
                else:
                    return Response({'error': 'Unexpected API response structure'}, status=500)
            else:
                return Response(
                    {'error': f"Failed to fetch holidays. Status: {response.status_code}, Content: {response.text}"},
                    status=response.status_code
                )
        except requests.RequestException as e:
            return Response({'error': f"Request failed: {str(e)}"}, status=500)

    
    return Response(holidays)
