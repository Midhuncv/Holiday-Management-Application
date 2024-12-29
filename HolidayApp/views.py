from django.http import JsonResponse
import requests
import os
from django.core.cache import cache

def get_holidays(request):
    country = request.GET.get('country')
    year = request.GET.get('year')

    if not country or not year:
        return JsonResponse({'error': 'Country and Year are required parameters'}, status=400)

    api_key = os.getenv('CALENDARIFIC_API_KEY')
    if not api_key:
        return JsonResponse({'error': 'API key is not configured'}, status=500)

    cache_key = f"{country}_{year}"
    holidays = cache.get(cache_key)  

    if not holidays:
        url = "https://calendarific.com/api/v2/holidays"
        params = {
            'api_key': api_key,
            'country': country,
            'year': year
        }

        try:
            response = requests.get(url, params=params)
            print(f"API Response: {response.json()}")  # Debugging log

            if response.status_code == 200:
                holidays = response.json()

                # Validate API response structure
                if 'response' in holidays:
                    # Handle empty response
                    if not holidays['response']:
                        return JsonResponse(
                            {'error': 'No holidays found for the specified country and year'},
                            status=404
                        )

                    # Validate holidays key in response
                    if 'holidays' in holidays['response']:
                        cache.set(cache_key, holidays, timeout=86400)  
                    else:
                        return JsonResponse(
                            {'error': 'Unexpected API response structure', 'details': holidays},
                            status=500
                        )
                else:
                    return JsonResponse(
                        {'error': 'Unexpected API response structure', 'details': holidays},
                        status=500
                    )
            else:
                return JsonResponse(
                    {'error': f"Failed to fetch holidays. Status: {response.status_code}, Content: {response.text}"},
                    status=response.status_code
                )
        except requests.RequestException as e:
            return JsonResponse({'error': f"Request failed: {str(e)}"}, status=500)

    # Extract holidays from the cached or fetched data
    if isinstance(holidays, dict):
        holiday_list = holidays.get('response', {}).get('holidays', [])
    else:
        holiday_list = []

    return JsonResponse({'holidays': holiday_list}, status=200)
