import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

import time


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/131.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,*/*;q=0.8"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}


CONTACT_KEYWORDS = [
    "contact",
    "contact us",
    "contact-us",
    "about",
    "about us",
    "about-us",
    "reach us",
    "reach-us",
    "enquiry",
    "enquire",
    "get in touch",
    "location",
    "locations"
]


def normalize_url(url):

    if not url:
        return ""

    url = url.strip()

    if not url.startswith(
        ("http://", "https://")
    ):

        url = "https://" + url

    return url


def fetch_page(url):

    url = normalize_url(url)

    if not url:
        return None, ""

    try:

        response = requests.get(
            url,
            headers=HEADERS,
            timeout=15,
            allow_redirects=True
        )

        # Retry once if needed
        if response.status_code >= 400:

            time.sleep(1)

            response = requests.get(
                url,
                headers=HEADERS,
                timeout=15,
                allow_redirects=True
            )

        if response.status_code >= 400:

            print(
                f"HTTP {response.status_code}: "
                f"{url}"
            )

            return None, ""

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        return soup, response.text

    except requests.RequestException as e:

        print(
            f"Request failed: {url}"
        )

        print(e)

        return None, ""

    except Exception as e:

        print(
            f"Scraping error: {url}"
        )

        print(e)

        return None, ""


def extract_page_text(soup):

    if not soup:
        return ""

    # Remove noise
    for tag in soup([
        "script",
        "style",
        "noscript",
        "svg",
        "iframe"
    ]):

        tag.decompose()

    return soup.get_text(
        separator=" ",
        strip=True
    )


def find_contact_links(
    base_url,
    soup
):

    if not soup:
        return []

    base_domain = urlparse(
        base_url
    ).netloc.lower()

    found = []

    for link in soup.find_all(
        "a",
        href=True
    ):

        href = link.get(
            "href",
            ""
        ).strip()

        text = link.get_text(
            " ",
            strip=True
        ).lower()

        href_lower = href.lower()

        # Skip junk
        if href_lower.startswith(
            (
                "javascript:",
                "#",
                "tel:",
                "mailto:"
            )
        ):
            continue

        is_contact = any(
            keyword in text
            or keyword in href_lower
            for keyword in CONTACT_KEYWORDS
        )

        if not is_contact:
            continue

        full_url = urljoin(
            base_url,
            href
        )

        parsed = urlparse(
            full_url
        )

        # Only crawl same domain
        if parsed.netloc.lower() != base_domain:

            continue

        if full_url not in found:

            found.append(full_url)

    return found


def find_mailto_emails(soup):

    emails = []

    if not soup:
        return emails

    for link in soup.find_all(
        "a",
        href=True
    ):

        href = link.get(
            "href",
            ""
        )

        if href.lower().startswith(
            "mailto:"
        ):

            email = href[
                7:
            ].split("?")[0].strip()

            if email and email not in emails:

                emails.append(email)

    return emails


def scrape_website(url):

    result = {

        "text": "",

        "contact_pages": [],

        "mailto_emails": [],

        "pages_scraped": 0,

        "website_status": "FAILED"

    }

    if not url:
        return result

    url = normalize_url(url)

    print(
        f"Scraping: {url}"
    )

    # --------------------------------
    # Homepage
    # --------------------------------

    soup, raw_html = fetch_page(
        url
    )

    if not soup:

        return result

    result["website_status"] = (
        "SUCCESS"
    )

    result["pages_scraped"] = 1

    homepage_text = extract_page_text(
        soup
    )

    result["text"] = homepage_text

    # Find mailto links
    result["mailto_emails"] = (
        find_mailto_emails(soup)
    )

    # --------------------------------
    # Contact/About pages
    # --------------------------------

    contact_links = find_contact_links(
        url,
        soup
    )

    # Crawl up to 5 useful pages
    contact_links = contact_links[:5]

    for page_url in contact_links:

        if page_url == url:
            continue

        print(
            f"  → Contact/About: "
            f"{page_url}"
        )

        page_soup, _ = fetch_page(
            page_url
        )

        if not page_soup:
            continue

        page_text = extract_page_text(
            page_soup
        )

        if page_text:

            result["text"] += (
                " " + page_text
            )

        result[
            "contact_pages"
        ].append(page_url)

        result[
            "pages_scraped"
        ] += 1

        # Also extract mailto
        mailto = find_mailto_emails(
            page_soup
        )

        for email in mailto:

            if email not in result[
                "mailto_emails"
            ]:

                result[
                    "mailto_emails"
                ].append(email)

    return result