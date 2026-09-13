import re


EMAIL_PATTERN = (
    r"[A-Za-z0-9._%+-]+"
    r"@[A-Za-z0-9.-]+"
    r"\.[A-Za-z]{2,}"
)


PHONE_PATTERNS = [

    # +91 9876543210
    r"\+91[\s-]?[6-9]\d{9}",

    # 9876543210
    r"\b[6-9]\d{9}\b",

    # 020-12345678
    r"\b0\d{2,4}[\s-]\d{6,8}\b"
]


INVALID_EMAIL_DOMAINS = [
    "example.com",
    "email.com",
    "domain.com"
]


def extract_email(
    text,
    extra_emails=None
):

    emails = []

    if not text:
        text = ""

    matches = re.findall(
        EMAIL_PATTERN,
        text,
        re.IGNORECASE
    )

    for email in matches:

        email = email.lower().strip()

        if email not in emails:

            emails.append(email)

    # Add mailto emails
    if extra_emails:

        for email in extra_emails:

            email = (
                email.lower()
                .strip()
            )

            if (
                email
                and email not in emails
            ):

                emails.append(email)

    # Remove junk
    cleaned = []

    for email in emails:

        domain = email.split(
            "@"
        )[-1]

        if domain in INVALID_EMAIL_DOMAINS:
            continue

        if email not in cleaned:

            cleaned.append(email)

    return cleaned


def extract_phone(text):

    if not text:
        return []

    phones = []

    for pattern in PHONE_PATTERNS:

        matches = re.findall(
            pattern,
            text
        )

        for phone in matches:

            phone = re.sub(
                r"\s+",
                " ",
                phone
            ).strip()

            if phone not in phones:

                phones.append(phone)

    return phones[:10]