// Copyright (c) 2023, nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Patty Cash"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": "From Date",
			"fieldtype": "Date",
			// "reqd": "1",
			"default": frappe.datetime.add_days(frappe.datetime.nowdate(), -30)
		},
		{
			"fieldname": "to_date",
			"label": "To Date",
			"fieldtype": "Date",
			// "reqd": 1,
			"default": frappe.datetime.nowdate()
		},
	]
};
