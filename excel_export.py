from openpyxl import Workbook
from openpyxl.styles import Font


def export_excel(results, filename):

    wb = Workbook()

    ws = wb.active

    ws.title = "Business Leads"

    headers = [
        "Business Name",
        "Category",
        "Business Type",
        "Website",
        "Email",
        "Phone",
        "Address",
        "State/Location",
        "Latitude",
        "Longitude",
        "Rating",
        "Rating Count",
        "Status",
        "Description",
        "Place ID"
    ]

    ws.append(headers)

    # Bold headers
    for cell in ws[1]:

        cell.font = Font(
            bold=True
        )

    for result in results:

        ws.append([

            result.get(
                "name",
                ""
            ),

            result.get(
                "category",
                ""
            ),

            result.get(
                "type",
                ""
            ),

            result.get(
                "website",
                ""
            ),

            ", ".join(
                result.get(
                    "emails",
                    []
                )
            ),

            ", ".join(
                result.get(
                    "phones",
                    []
                )
            ),

            result.get(
                "address",
                ""
            ),

            result.get(
                "location",
                ""
            ),

            result.get(
                "latitude"
            ),

            result.get(
                "longitude"
            ),

            result.get(
                "rating"
            ),

            result.get(
                "rating_count"
            ),

            result.get(
                "status",
                ""
            ),

            result.get(
                "description",
                ""
            ),

            result.get(
                "place_id",
                ""
            )
        ])

    # Auto-size columns
    for column in ws.columns:

        max_length = 0

        column_letter = (
            column[0].column_letter
        )

        for cell in column:

            if cell.value:

                max_length = max(
                    max_length,
                    len(str(cell.value))
                )

        ws.column_dimensions[
            column_letter
        ].width = min(
            max_length + 2,
            50
        )

    ws.freeze_panes = "A2"

    ws.auto_filter.ref = (
        ws.dimensions
    )

    wb.save(filename)