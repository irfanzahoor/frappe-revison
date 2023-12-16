# Copyright (c) 2023, nextash and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = get_columns(), get_data(filters)
	return columns, data

def get_columns():
    columns= [
			{"fieldname": "item_name", "label": "Item Name", "fieldtype": "Data"},
   
			{"fieldname": "quantity", "label": "Quantity", "fieldtype": "Float"},
   
			{"fieldname": "date", "label": "Date", "fieldtype": "Date"},
   
			{"fieldname": "price", "label": "Price", "fieldtype": "Currency"},
   
			{"fieldname": "total_amount", "label": "Total Amount", "fieldtype": "Float"},
   
			{"fieldname": "reciept", "label": "Reciept", "fieldtype": "Small Text"},
   
			{"fieldname": "description", "label": "Description", "fieldtype": "Small Text"},
       
    ]
    return columns

def get_condition(c_f):
    new_filter={}
    
    if c_f.get("from_date") and c_f.get("to_date"):
        new_filter['date']=['between', [c_f.get("from_date"),c_f.get("to_date")]]
    return new_filter
def get_data(d_filter):
    data = []
    condition=get_condition(d_filter)
    field_name=['*']
    list_doc =frappe.db.get_list('Patty cash',filters=condition,fields=field_name)
    for row in list_doc:
        data.append({
            "quantity":row.quantity,
            "item_name":row.item_name,
            "date":row.date,
            "price":row.price,
            "total_amount":row.total_amount,
            "reciept":row.receipt,
            "description":row.description,
        })
    
    return data