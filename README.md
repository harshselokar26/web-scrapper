# 🔎 Business Intelligence Web Scraper

> A dynamic NLP-powered business discovery and web scraping application
> that finds real businesses, enriches their public information, and
> exports structured results to Excel.

## 🚀 Overview

This project lets users search for businesses using a natural-language
requirement and a selected Indian state.

For example:

``` text
Business / Requirement: oil factories
State: Maharashtra
```

The application discovers real businesses, collects available business
details, attempts to enrich them through their websites, and presents
the results in an interactive Streamlit dashboard.

### Core workflow

``` text
Natural Language Requirement
            ↓
     Dynamic NLP Parsing
            ↓
      Query Expansion
            ↓
     Business Discovery
            ↓
       Real Businesses
            ↓
       Website Crawling
            ↓
   Contact Information Extraction
            ↓
     Cleaning & Deduplication
            ↓
    Streamlit Dashboard + Map
            ↓
        Excel Export
```

------------------------------------------------------------------------

## ✨ Features

### 🧠 Dynamic Natural Language Search

Users can describe the type of business they need without choosing from
a fixed category list.

Examples:

``` text
oil factories
rice mills
pharmaceutical manufacturers
steel companies
wedding venues
solar panel manufacturers
cold storage facilities
industrial automation companies
```

The NLP layer normalizes the requirement and dynamically generates
relevant search variations.

### 📍 State Selection

The location is selected through a state dropdown rather than relying on
NLP to guess the state.

Supported use case:

``` text
Requirement: rice mills
State: Chhattisgarh
```

### 🏢 Real Business Discovery

The discovery layer is designed to prioritize real-world business/place
results instead of generic web results such as articles, videos, and
social media posts.

Business records can include:

-   Business name
-   Website
-   Phone number
-   Address
-   Business type
-   Rating
-   Rating count
-   Latitude
-   Longitude

### 🌐 Website Enrichment

When a business has a website, the scraper attempts to inspect relevant
pages such as:

-   Homepage
-   Contact
-   Contact Us
-   About
-   About Us
-   Reach Us
-   Enquiry
-   Location
-   Sitemap

The crawler does not need a business-specific scraper for every
industry.

### 📧 Contact Extraction

The application attempts to extract publicly available:

-   Email addresses
-   Phone numbers
-   Contact page URLs
-   Website information

It also handles common HTML contact mechanisms such as `mailto:` and
`tel:` links.

### 🗺️ Location Mapping

Businesses with coordinates can be displayed on an interactive map
directly inside the Streamlit application.

### 📊 Excel Export

The collected data can be exported as a structured `.xlsx` file for
further analysis.

### ♻️ Deduplication

Multiple search variations can return the same business. The application
attempts to remove duplicates using available business identifiers such
as website, place ID, or business name and address.

------------------------------------------------------------------------

## 🏗️ Architecture

``` text
                         USER
                          │
                          ▼
              ┌─────────────────────┐
              │ Natural Language     │
              │ Business Requirement │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Dynamic NLP Layer   │
              │                     │
              │ Normalization       │
              │ Intent Understanding│
              │ Query Expansion     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Business Discovery  │
              │                     │
              │ Places Search API   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Business Records    │
              │                     │
              │ Name                │
              │ Website             │
              │ Phone               │
              │ Address             │
              │ Coordinates         │
              │ Rating              │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Website Crawler     │
              │                     │
              │ Homepage            │
              │ Contact Pages       │
              │ About Pages         │
              │ Sitemap             │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Data Extraction     │
              │                     │
              │ Email               │
              │ Phone               │
              │ Contact URLs        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Cleaning &          │
              │ Deduplication       │
              └──────────┬──────────┘
                         │
                    ┌────┴────┐
                    ▼         ▼
              Streamlit      Excel
              Dashboard      Export
                    │
                    ▼
                   Map
```

------------------------------------------------------------------------

## 📁 Project Structure

``` text
web-scrapper/
│
├── app.py
├── main.py
│
├── nlp_parser.py
├── search.py
├── scraper.py
├── extractor.py
├── geocoder.py
├── excel_export.py
│
├── output/
│   └── results.xlsx
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

### File responsibilities

  File                Purpose
  ------------------- -------------------------------------------------
  `app.py`            Streamlit user interface
  `main.py`           End-to-end scraping pipeline
  `nlp_parser.py`     Dynamic query understanding and query expansion
  `search.py`         Business/place discovery
  `scraper.py`        Website crawling
  `extractor.py`      Email and phone extraction
  `geocoder.py`       Geocoding utilities
  `excel_export.py`   Excel file generation
  `output/`           Generated files

------------------------------------------------------------------------

## 🛠️ Tech Stack

  Layer                    Technology
  ------------------------ -----------------------------
  Language                 Python
  UI                       Streamlit
  NLP                      Dynamic query understanding
  Business Discovery       Serper Places API
  Web Scraping             Requests
  HTML Parsing             BeautifulSoup
  Information Extraction   Regex + HTML parsing
  Geocoding                OpenStreetMap / Nominatim
  Excel Export             OpenPyXL
  Configuration            python-dotenv

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd web-scrapper
```

### 2. Create a virtual environment

#### Windows

``` powershell
python -m venv venv
.env\Scripts\Activate.ps1
```

#### macOS / Linux

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔐 Environment Variables

Create a `.env` file in the project root:

``` env
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
```

`GROQ_API_KEY` is required only when the dynamic NLP implementation uses
Groq.

### `.gitignore`

Make sure your `.gitignore` contains:

``` gitignore
.env
venv/
__pycache__/
*.pyc
output/*.xlsx
```

> Never commit API keys or secrets to GitHub.

------------------------------------------------------------------------

## ▶️ Run the Application

Start the Streamlit application:

``` bash
streamlit run app.py
```

Then open the local URL shown by Streamlit:

``` text
http://localhost:8501
```

------------------------------------------------------------------------

## 🔄 Example Search

### Input

``` text
Business / Requirement:
oil factories

State:
Maharashtra
```

### NLP layer

The system dynamically interprets the requirement and can generate
related search concepts such as:

``` text
oil factories
oil manufacturers
oil mills
oil processing companies
oil extraction companies
```

These are used to improve business discovery without maintaining a
hardcoded category dictionary.

### Business discovery

The search layer collects real business records.

### Website enrichment

For businesses with websites, the crawler attempts to discover useful
pages and extract publicly available contact information.

### Final output

The application displays the results in Streamlit and allows the user to
download them as Excel.

------------------------------------------------------------------------

## 📋 Output Fields

The generated dataset can contain:

  Field             Description
  ----------------- -------------------------------------------------
  Business Name     Name of the business
  Category          Normalized business requirement
  Business Type     Type returned by the business discovery service
  Website           Business website
  Email             Publicly available email address
  Phone             Publicly available phone number
  Address           Business address
  Location          Selected state
  Latitude          Business latitude
  Longitude         Business longitude
  Rating            Business rating
  Rating Count      Number of ratings
  Contact Pages     Relevant website pages discovered
  Pages Scraped     Number of successfully processed pages
  Website Status    Website processing result
  Scraping Status   Overall extraction status

------------------------------------------------------------------------

## 🧠 Why Dynamic NLP?

The system does not depend on a fixed list such as:

``` text
oil factories → predefined keywords
rice mills → predefined keywords
wedding halls → predefined keywords
```

Instead, the NLP layer works dynamically:

``` text
User Requirement
       ↓
Normalization
       ↓
Intent Understanding
       ↓
Query Expansion
       ↓
Search Queries
```

This allows new business categories to be searched without changing the
application code.

For example, a user can enter:

``` text
renewable energy equipment suppliers
```

even if that exact category was never explicitly defined in the source
code.

------------------------------------------------------------------------

## 🌐 Website Scraping Strategy

The crawler uses a multi-stage approach instead of relying only on the
homepage.

``` text
Website
   │
   ├── Homepage
   │
   ├── Internal Links
   │      ├── Contact
   │      ├── About
   │      ├── Location
   │      └── Enquiry
   │
   └── Sitemap
          └── Relevant URLs
                 ↓
          Information Extraction
```

This improves the chance of finding contact information that is not
visible on the homepage.

------------------------------------------------------------------------

## ♻️ Data Quality

Business data is not always complete.

A business may have:

-   No website
-   No public email
-   No public phone number
-   An inaccessible website
-   A JavaScript-heavy website
-   An incomplete business listing

The application keeps available business information instead of
discarding the entire record.

Possible statuses include:

``` text
COMPLETE
PARTIAL
WEBSITE_FOUND
FAILED
```

------------------------------------------------------------------------

## 🗺️ Geospatial Information

Where available, the application stores:

``` text
Latitude
Longitude
Address
```

These coordinates can be used to visualize discovered businesses on the
Streamlit map.

------------------------------------------------------------------------

## 🧪 Example Queries

The same pipeline can be used for different business categories:

``` text
oil factories
```

``` text
rice mills
```

``` text
pharmaceutical manufacturers
```

``` text
steel companies
```

``` text
wedding venues
```

``` text
solar panel manufacturers
```

``` text
cold storage facilities
```

``` text
industrial automation companies
```

The user only needs to change the business requirement and state.

------------------------------------------------------------------------

## 🛡️ Responsible Scraping

This project is intended for legitimate business research and data
organization.

The scraper should:

-   Access publicly available information
-   Respect applicable website terms and crawling policies
-   Use reasonable request timeouts
-   Avoid aggressive request rates
-   Avoid authentication-protected content
-   Avoid bypassing anti-bot or security mechanisms
-   Avoid collecting private or sensitive information

Collected information should be independently verified before commercial
use or business outreach.

------------------------------------------------------------------------

## 🚧 Current Limitations

This is an MVP, so some limitations are expected:

-   Search results depend on external API coverage
-   Some businesses do not have websites
-   Some websites block automated requests
-   JavaScript-heavy websites may expose limited content
-   Email extraction is heuristic
-   Contact information may be incomplete
-   External API quotas can limit result volume
-   Public business information can change over time

------------------------------------------------------------------------

## 🔮 Future Improvements

-   [ ] Dynamic relevance scoring
-   [ ] Improved business/entity deduplication
-   [ ] Sitemap-aware crawling
-   [ ] JSON-LD structured-data extraction
-   [ ] Confidence scores for extracted fields
-   [ ] City and district level filtering
-   [ ] Search pagination
-   [ ] Retry queues for failed websites
-   [ ] Background scraping jobs
-   [ ] CSV export
-   [ ] Search history
-   [ ] Advanced industry classification
-   [ ] Production deployment

------------------------------------------------------------------------

## 📸 Demo

Add screenshots or a short GIF to the repository:

``` text
docs/
├── search.png
├── results.png
└── workflow.gif
```

Then include them in this section:

``` markdown
![Search Interface](docs/search.png)

![Business Results](docs/results.png)

![Workflow](docs/workflow.gif)
```

A useful demo should show:

``` text
Enter business requirement
        ↓
Select state
        ↓
Search & Scrape
        ↓
NLP query understanding
        ↓
Real business results
        ↓
Website enrichment
        ↓
Map
        ↓
Excel export
```

------------------------------------------------------------------------

## 🎯 Project Objective

The project combines:

-   Natural Language Processing
-   Information Retrieval
-   Business Discovery
-   Web Scraping
-   Information Extraction
-   Data Cleaning
-   Geospatial Data
-   Excel Automation
-   Interactive Visualization

The objective is to automate the process of converting an unstructured
business requirement into structured, usable business intelligence.

------------------------------------------------------------------------

## 👨‍💻 Author

**Harsh Selokar**

NLP • Web Scraping • AI Automation • Data Engineering

------------------------------------------------------------------------

## ⭐ Project

If you find the project useful, consider giving the repository a ⭐.
