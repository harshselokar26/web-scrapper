import streamlit as st
import pandas as pd

from main import run_scraper


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Business Intelligence Web Scraper",
    page_icon="🔎",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------

st.title("🔎 Business Intelligence Web Scraper")

st.write(
    "Find real businesses using a natural-language business requirement."
)


# -----------------------------
# Indian states
# -----------------------------

states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal",
    "Delhi"
]


# -----------------------------
# Input section
# -----------------------------

col1, col2 = st.columns([2, 1])


with col1:

    category = st.text_input(
        "Business / Requirement",
        placeholder="e.g. oil factories, rice mills, pharmaceutical companies",
        help="Describe the type of business you want to find."
    )


with col2:

    state = st.selectbox(
        "State",
        states
    )


# -----------------------------
# Search button
# -----------------------------

search_clicked = st.button(
    "🔍 Search & Scrape",
    type="primary"
)


# -----------------------------
# Search
# -----------------------------

if search_clicked:

    if not category.strip():

        st.warning(
            "Please enter a business requirement."
        )

    else:

        # Build natural-language query
        query = f"{category} in {state}"

        # Show query understanding
        st.subheader("🧠 Query Understanding")

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"**Business Category**\n\n{category}"
            )

        with col2:

            st.info(
                f"**Location**\n\n{state}"
            )

        # Run scraper
        with st.spinner(
            f"Finding {category} in {state}..."
        ):

            results = run_scraper(
    category,
    state
)

        # -----------------------------
        # Results
        # -----------------------------

        if results:

            st.success(
                f"Found {len(results)} businesses"
            )

            # -----------------------------
            # Metrics
            # -----------------------------

            total = len(results)

            websites = sum(
                bool(r.get("website"))
                for r in results
            )

            emails = sum(
                bool(r.get("emails"))
                for r in results
            )

            phones = sum(
                bool(r.get("phones"))
                for r in results
            )

            coordinates = sum(
                r.get("latitude") is not None
                and r.get("longitude") is not None
                for r in results
            )

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric(
                "Businesses",
                total
            )

            c2.metric(
                "Websites",
                websites
            )

            c3.metric(
                "Emails",
                emails
            )

            c4.metric(
                "Phones",
                phones
            )

            c5.metric(
                "Coordinates",
                coordinates
            )

            # -----------------------------
            # Results table
            # -----------------------------

            st.subheader("📋 Business Results")

            display_results = []

            for r in results:

                display_results.append({

                    "Business Name":
                        r.get("name", ""),

                    "Website":
                        r.get("website", ""),

                    "Email":
                        ", ".join(
                            r.get("emails", [])
                        ),

                    "Phone":
                        ", ".join(
                            r.get("phones", [])
                        ),

                    "Address":
                        r.get("address", ""),

                    "Latitude":
                        r.get("latitude"),

                    "Longitude":
                        r.get("longitude"),

                    "Rating":
                        r.get("rating"),

                    "Status":
                        r.get("status", "")
                })

            df = pd.DataFrame(
                display_results
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            # -----------------------------
            # Map
            # -----------------------------

            map_df = df[
                ["Latitude", "Longitude"]
            ].copy()

            map_df = map_df.dropna()

            if not map_df.empty:

                st.subheader(
                    "📍 Business Locations"
                )

                map_df = map_df.rename(
                    columns={
                        "Latitude": "lat",
                        "Longitude": "lon"
                    }
                )

                st.map(map_df)

            # -----------------------------
            # Excel download
            # -----------------------------

            try:

                with open(
                    "output/results.xlsx",
                    "rb"
                ) as file:

                    excel_data = file.read()

                st.download_button(

                    label="⬇️ Download Excel",

                    data=excel_data,

                    file_name=(
                        f"{category}_{state}"
                        ".xlsx"
                    ),

                    mime=(
                        "application/"
                        "vnd.openxmlformats-officedocument"
                        ".spreadsheetml.sheet"
                    )
                )

            except FileNotFoundError:

                st.warning(
                    "Excel file could not be found."
                )

        else:

            st.error(
                "No businesses were found. "
                "Try a different business category."
            )