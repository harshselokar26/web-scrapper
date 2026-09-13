from nlp_parser import parse_query
from search import search_businesses
from scraper import scrape_website
from extractor import extract_email, extract_phone
from excel_export import export_excel


def run_scraper(category, state):

    parsed = parse_query(
        category,
        state
    )

    category = parsed["category"]
    location = parsed["location"]

    print("Category:", category)
    print("Location:", location)

    # --------------------------------
    # 2. Search REAL PLACES
    # --------------------------------

    businesses = search_businesses(
        category,
        location,
        num_results=20
    )

    print(
        f"Found {len(businesses)} real places"
    )

    final_results = []

    # --------------------------------
    # 3. Process businesses
    # --------------------------------

    for business in businesses:

        website = business.get(
            "website",
            ""
        )

        emails = []
        scraped_phones = []
        contact_pages = []
        mailto_emails = []
        website_status = "FAILED"
        pages_scraped = 0

        # --------------------------------
        # 4. Scrape website for email
        # --------------------------------

        if website:

            print(
                f"Scraping: {website}"
            )

            scraped_data = scrape_website(
                website
            )

            text = scraped_data.get(
                "text",
                ""
            )

            contact_pages = scraped_data.get(
                "contact_pages",
                []
            )

            mailto_emails = scraped_data.get(
                "mailto_emails",
                []
            )

            website_status = scraped_data.get(
                "website_status",
                "FAILED"
            )

            pages_scraped = scraped_data.get(
                "pages_scraped",
                0
            )

            if text:

                emails = extract_email(
                    text,
                    mailto_emails
                )

                scraped_phones = extract_phone(
                    text
                )

        # --------------------------------
        # 5. Prefer Places phone
        # --------------------------------

        phone = business.get(
            "phone",
            ""
        )

        if not phone and scraped_phones:

            phone = scraped_phones[0]

        if website_status == "FAILED":

            status = "FAILED"

        elif emails and phone:

            status = "COMPLETE"

        elif emails or phone:

            status = "PARTIAL"

        else:

            status = "WEBSITE_FOUND"

        # --------------------------------
        # 6. Build final record
        # --------------------------------

        final_results.append({

            "name": business.get(
                "name",
                ""
            ),

            "category": category,

            "website": website,

            "emails": emails,

            "phones": [phone] if phone else [],

            "contact_pages": contact_pages,

            "pages_scraped": pages_scraped,

            "website_status": website_status,

            "address": business.get(
                "address",
                ""
            ),

            "location": location,

            "latitude": business.get(
                "latitude"
            ),

            "longitude": business.get(
                "longitude"
            ),

            "type": business.get(
                "type",
                ""
            ),

            "rating": business.get(
                "rating"
            ),

            "rating_count": business.get(
                "rating_count"
            ),

            "place_id": business.get(
                "place_id",
                ""
            ),

            "description": business.get(
                "description",
                ""
            ),

            "status": status

        })

    # --------------------------------
    # 7. Export Excel
    # --------------------------------

    export_excel(
        final_results,
        "output/results.xlsx"
    )

    return final_results