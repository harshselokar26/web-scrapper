
🔎 Business Intelligence Web Scraper
Natural-language business discovery + real-place search + website
intelligence + Excel export

A lightweight NLP-powered business research tool that lets users
describe the type of business they are looking for, select a state,
discover real businesses, collect publicly available contact
information, and export the results to Excel.

✨ What It Does
Instead of searching the web manually, enter a requirement such as:

oil factories
Select:

Maharashtra
The application then:

Natural Language Requirement
            ↓
      Query Understanding
            ↓
      Dynamic Search Queries
            ↓
       Places Discovery
            ↓
     Real Business Results
            ↓
       Website Crawling
            ↓
  Contact / Email Extraction
            ↓
   Data Validation & Cleanup
            ↓
      Streamlit Dashboard
            ↓
         Excel Export
Example searches
Requirement State

oil factories Maharashtra
rice mills Chhattisgarh
pharmaceutical companies Gujarat
steel manufacturers Maharashtra
wedding venues Maharashtra
cold storage facilities Madhya Pradesh

The system is designed to work with new business categories without
requiring a hardcoded category list.

🚀 Key Features
🧠 Natural Language Search
Describe the business you need in normal language rather than selecting
from a fixed category list.

📍 State-based Filtering
Choose the target Indian state from a dropdown for reliable geographic
filtering.

🏢 Real Business Discovery
Uses a Places-focused search rather than generic web search, reducing
irrelevant results such as news articles, videos, and social posts.

🌐 Website Intelligence
For businesses with websites, the scraper attempts to inspect the
homepage and relevant internal pages such as:

Contact

Contact Us

About

About Us

Reach Us

Enquiry

Location

📧 Contact Extraction
Attempts to collect publicly available:

Email addresses

Phone numbers

Contact pages

Business website

Address

🗺️ Location Data
Uses business listing location data where available:

Latitude

Longitude

Address

Results can also be displayed on an interactive map.

📊 Excel Export
Export collected business intelligence into a structured .xlsx file
for further analysis or lead research.

♻️ Deduplication
Search variations are combined while attempting to avoid duplicate
businesses.

📈 Result Metrics
The dashboard summarizes:

Total businesses

Websites found

Emails found

Phone numbers found

Coordinates available

🖥️ Interface
Search
┌──────────────────────────────────────────────────────────┐
│ Business / Requirement        │ State                    │
│ oil factories                 │ Maharashtra ▼           │
└──────────────────────────────────────────────────────────┘

                  🔍 Search & Scrape
Results
🧠 Query Understanding

Business Category: oil factories
Location: Maharashtra

20 Businesses Found

Businesses   Websites   Emails   Phones   Coordinates
    20          16         9       18          20
The result table provides the collected business information and an
interactive location map.

🏗️ Architecture
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
              │ NLP / Query         │
              │ Understanding       │
              │                     │
              │ Normalization       │
              │ Query Expansion     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Places Search       │
              │ Business Discovery  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Business Records     │
              │                     │
              │ Name                │
              │ Phone               │
              │ Address             │
              │ Website             │
              │ Latitude/Longitude  │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Website Crawler     │
              │                     │
              │ Homepage            │
              │ Contact Pages       │
              │ About Pages         │
              │ Sitemap (when found)│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Information         │
              │ Extraction          │
              │                     │
              │ Email               │
              │ Phone               │
              │ Contact URLs        │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Cleaning &           │
              │ Deduplication       │
              └──────────┬──────────┘
                         │
                    ┌────┴────┐
                    ▼         ▼
              Streamlit      Excel
              Dashboard      Export
📁 Project Structure
web-scrapper/
│
├── app.py                 # Streamlit application
├── main.py                # End-to-end scraping pipeline
│
├── nlp_parser.py          # Query understanding / expansion
├── search.py              # Places/business discovery
├── scraper.py             # Website crawling
├── extractor.py            # Email & phone extraction
├── geocoder.py             # Address geocoding utilities
├── excel_export.py         # Excel generation
│
├── output/
│   └── results.xlsx        # Generated output
│
├── .env                   # API credentials - DO NOT COMMIT
├── .gitignore
├── requirements.txt
└── README.md
⚙️ Tech Stack
Component Technology

Language Python
UI Streamlit
NLP Dynamic query understanding
Business discovery Serper Places API
Web scraping Requests + BeautifulSoup
Data extraction Python Regex + HTML parsing
Geocoding OpenStreetMap/Nominatim
Excel OpenPyXL
Configuration python-dotenv

🔧 Installation
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd web-scrapper
2. Create a virtual environment
Windows
python -m venv venv
.\venv\Scripts\Activate.ps1
macOS / Linux
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
python -m pip install -r requirements.txt
🔐 Environment Variables
Create a .env file in the project root:

SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
Only add GROQ_API_KEY if your current NLP implementation uses the
Groq-powered dynamic query parser.

⚠️ Never commit .env
Your .gitignore should include:

.env
venv/
__pycache__/
*.pyc
output/*.xlsx
▶️ Run the Application
Start Streamlit:

streamlit run app.py
Then open the local Streamlit URL shown in the terminal.

Example:

http://localhost:8501
🔄 How a Search Works
Suppose the user enters:

premium wedding venues
and selects:

Maharashtra
The system can transform the requirement into related business-search
concepts such as:

wedding venues
banquet halls
marriage halls
function halls
celebration halls
Those queries are used for business discovery.

The resulting places are then processed individually.

For each business:

Business Listing
      ↓
Website Available?
      │
      ├── No → Keep business listing data
      │
      └── Yes
            ↓
         Homepage
            ↓
       Discover useful
       internal pages
            ↓
      Contact / About
            ↓
       Extract public
       contact details
📋 Output Fields
The Excel output can contain:

Field Description

Business Name Name of the business
Category User's business requirement
Business Type Type returned by business search
Website Official/public website when available
Email Publicly listed email addresses
Phone Publicly listed phone numbers
Address Business address
Location Selected state
Latitude Business latitude
Longitude Business longitude
Rating Listing rating when available
Rating Count Number of ratings when available
Contact Pages Relevant pages discovered
Pages Scraped Number of pages successfully processed
Website Status Website processing result
Scraping Status Overall extraction status

🧪 Example Workflow
Input
Business / Requirement:
rice mills

State:
Chhattisgarh
Processing
✓ Query understood
✓ Search variations generated
✓ Real places discovered
✓ Duplicate results removed
✓ Websites identified
✓ Contact pages inspected
✓ Emails / phones extracted
✓ Coordinates collected
✓ Excel generated
Output
Business Name
Website
Email
Phone
Address
Latitude
Longitude
Rating
Status
🧩 Design Decisions
Why Places search instead of normal web search?
A generic web search can return:

News articles
YouTube videos
Facebook posts
LinkedIn pages
Blogs
For a business discovery application, the goal is to start with
structured real-world place/business records.

The website scraper is then used as a second-stage enrichment layer.

Why not scrape every page?
The crawler prioritizes pages likely to contain business information
instead of crawling an entire website.

This keeps the application:

Faster

Less resource intensive

Easier to operate

More focused on contact information

Why is some information missing?
Public business data is inconsistent.

A business may have:

No website

No public email

No contact page

A website that blocks automated requests

A JavaScript-heavy website

Incomplete business listing data

The application keeps the available information rather than discarding
the entire business.

🛡️ Responsible Scraping
This project is intended for legitimate business research and data
organization.

The scraper should:

Access publicly available pages

Respect website terms and robots policies where applicable

Use reasonable request timeouts

Avoid bypassing authentication or anti-bot protections

Avoid collecting private or sensitive information

Avoid aggressive request rates

The output should be treated as research data and independently verified
before business outreach or commercial use.

🚧 Current Limitations
This is an MVP and has some expected limitations:

Search API results depend on external search coverage

Some businesses do not have websites

Some websites block automated requests

JavaScript-only sites may provide limited content

Email extraction is heuristic

Address extraction may be incomplete

Search/API quotas can limit result volume

Public business information can change over time

🔮 Future Improvements
Potential next steps:

Dynamic relevance scoring

Better company/entity deduplication

Sitemap-aware crawling

Structured-data extraction from JSON-LD

GST/company registration extraction where publicly available

Industry classification

Confidence score for extracted fields

CSV export

Search history

Background scraping jobs

Retry queues for failed websites

Advanced location filtering by city/district

Multi-page pagination

Production deployment

📸 Demo
Add screenshots/GIFs to this section after pushing the project:

docs/
├── search.png
├── results.png
└── workflow.gif
Then embed them:

![Search](docs/search.png)

![Results](docs/results.png)
A short GIF showing:

Enter requirement
      ↓
Select state
      ↓
Search & Scrape
      ↓
Business results
      ↓
Map
      ↓
Download Excel
makes the repository much easier to understand.

🎯 Why This Project?
The project combines several practical engineering concepts:

NLP
+
Search / Information Retrieval
+
Web Scraping
+
Data Extraction
+
Geospatial Data
+
Data Cleaning
+
Excel Automation
+
Interactive UI
The goal is not simply to scrape a website, but to build a small
business intelligence pipeline that converts an unstructured user
requirement into structured, usable business data.

