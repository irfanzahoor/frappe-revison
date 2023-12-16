import frappe
from frappe import _

def execute(filters=None):
    # Get columns for the report
    columns = get_columns()
    # Get data for the report based on filters
    data = get_data(filters)
    # Return columns and data for the report
    return columns, data

def get_columns():
    # Initialize an empty list to store columns
    columns = []
    
    # Get field names for the "Dynamic report" document type and add them to columns
    doc_fields = frappe.get_meta("Dynamic report").fields
    for field in doc_fields:
        # Add a new column to the columns list with label, field type, and width
        column_label = (field.label) + ":" + field.fieldtype + ":180"
        columns.append(column_label)

    return columns

def get_data(filters):
   
    doc_list = frappe.get_list(
        "Dynamic report",
        filters=filters,
        fields=['*'],  # Fetch all fields dynamically
    )

    # Initialize an empty list to store data rows
    data = []
    for doc in doc_list:
        # Create a dictionary with field names as keys and their corresponding values
        row_data = {field: doc.get(field) for field in doc.keys()}
        # Append the row data to the data list
        data.append(row_data)

    return data