# geocoder.py

import requests


def geocode(address):

    if not address:
        return None, None

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "BusinessResearchScraper/1.0"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        data = response.json()

        if data:

            return (
                data[0]["lat"],
                data[0]["lon"]
            )

    except Exception:
        pass

    return None, None