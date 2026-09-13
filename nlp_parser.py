# nlp_parser.py

import re


# Common business-category variations
CATEGORY_EXPANSIONS = {

    "celebration hall": [
        "celebration hall",
        "banquet hall",
        "marriage hall",
        "wedding hall",
        "function hall",
        "wedding venue"
    ],

    "marriage hall": [
        "marriage hall",
        "wedding hall",
        "banquet hall",
        "function hall",
        "wedding venue",
        "celebration hall"
    ],

    "wedding hall": [
        "wedding hall",
        "marriage hall",
        "banquet hall",
        "function hall",
        "wedding venue"
    ],

    "rice mill": [
        "rice mill",
        "rice mills",
        "rice processing",
        "rice processing mill",
        "rice manufacturer"
    ],

    "rice mills": [
        "rice mill",
        "rice mills",
        "rice processing",
        "rice processing mill",
        "rice manufacturer"
    ],

    "oil factory": [
        "oil factory",
        "oil factories",
        "oil mill",
        "oil mills",
        "oil manufacturer",
        "edible oil manufacturer",
        "oil extraction"
    ],

    "oil factories": [
        "oil factory",
        "oil factories",
        "oil mill",
        "oil mills",
        "oil manufacturer",
        "edible oil manufacturer",
        "oil extraction"
    ],

    "pharmaceutical company": [
        "pharmaceutical company",
        "pharmaceutical companies",
        "pharma company",
        "pharma manufacturer",
        "drug manufacturer",
        "pharmaceutical manufacturer"
    ],

    "pharmaceutical companies": [
        "pharmaceutical company",
        "pharmaceutical companies",
        "pharma company",
        "pharma manufacturer",
        "drug manufacturer",
        "pharmaceutical manufacturer"
    ],

    "steel manufacturer": [
        "steel manufacturer",
        "steel manufacturers",
        "steel company",
        "steel companies",
        "steel plant",
        "steel industry"
    ],

    "steel manufacturers": [
        "steel manufacturer",
        "steel manufacturers",
        "steel company",
        "steel companies",
        "steel plant",
        "steel industry"
    ]
}


def clean_category(category):

    category = category.lower().strip()

    # Remove unnecessary phrases
    category = re.sub(
        r"\b(please|find|search|show|me|give|list|get)\b",
        "",
        category
    )

    # Remove location wording if user accidentally includes it
    category = re.sub(
        r"\b(in|at|near|around)\s*$",
        "",
        category
    )

    # Normalize whitespace
    category = re.sub(
        r"\s+",
        " ",
        category
    ).strip()

    return category


def get_search_variations(category):

    category = clean_category(category)

    # Known category
    if category in CATEGORY_EXPANSIONS:

        return CATEGORY_EXPANSIONS[category]

    # Try partial matching
    for key, variations in CATEGORY_EXPANSIONS.items():

        if key in category or category in key:

            return variations

    # Generic variations
    return [
        category,
        f"{category} company",
        f"{category} companies",
        f"{category} manufacturer",
        f"{category} manufacturers",
        f"{category} factory",
        f"{category} factories"
    ]


def parse_query(category, state):

    category = clean_category(category)

    state = state.strip().lower()

    variations = get_search_variations(
        category
    )

    return {
        "category": category,
        "location": state,
        "variations": variations
    }