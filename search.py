import os
import requests
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv(
    "SERPER_API_KEY"
)

PLACES_URL = "https://google.serper.dev/places"


def search_businesses(
    category,
    location,
    num_results=20,
    variations=None
):

    if not SERPER_API_KEY:

        raise ValueError(
            "SERPER_API_KEY not found in .env"
        )

    # If NLP supplied variations, use them
    if variations:

        search_terms = variations

    else:

        search_terms = [
            category,
            f"{category} company",
            f"{category} manufacturer",
            f"{category} factory"
        ]

    all_results = {}

    for term in search_terms:

        query = f"{term} in {location}"

        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }

        payload = {
            "q": query,
            "gl": "in",
            "hl": "en",
            "num": min(num_results, 20)
        }

        try:

            response = requests.post(
                PLACES_URL,
                headers=headers,
                json=payload,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            places = data.get(
                "places",
                []
            )

            print(
                f"Query: {query} | "
                f"Found: {len(places)}"
            )

            for place in places:

                name = place.get(
                    "title",
                    ""
                ).strip()

                website = place.get(
                    "website",
                    ""
                ).strip()

                address = place.get(
                    "address",
                    ""
                ).strip()

                phone = place.get(
                    "phoneNumber",
                    ""
                ).strip()

                latitude = place.get(
                    "latitude"
                )

                longitude = place.get(
                    "longitude"
                )

                place_id = place.get(
                    "placeId"
                )

                # Better deduplication
                if website:

                    key = website.lower().rstrip("/")

                elif place_id:

                    key = place_id

                else:

                    key = (
                        name.lower()
                        + "|"
                        + address.lower()
                    )

                if not key:
                    continue

                if key not in all_results:

                    all_results[key] = {

                        "name": name,

                        "website": website,

                        "phone": phone,

                        "address": address,

                        "latitude": latitude,

                        "longitude": longitude,

                        "type": place.get(
                            "type",
                            ""
                        ),

                        "rating": place.get(
                            "rating"
                        ),

                        "rating_count": place.get(
                            "ratingCount"
                        ),

                        "place_id": place_id,

                        "description": place.get(
                            "description",
                            ""
                        ),

                        "search_term": term
                    }

        except requests.RequestException as e:

            print(
                f"Search failed: {query}"
            )

            print(e)

        except Exception as e:

            print(
                f"Unexpected error: {e}"
            )

    return list(
        all_results.values()
    )[:num_results]