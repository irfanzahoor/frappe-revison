// Copyright (c) 2023, nextash and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Employee Repo"] = {
	"filters": [{
		"fieldname": "employee",
		"label": "Employee ",
		"fieldtype": "Link",
		"options": "Employee Performance",
		// "reqd": 1,

	},
	{
		"fieldname": "attitude",
		"label": "Attitude ",
		"fieldtype": "Select",
		"options": "\nExcellent\nGood\nFair\nPoor",
		// "default": "Good"
	},
	{
		"fieldname": "attendance",
		"label": "Attendance ",
		"fieldtype": "Select",
		"options": "\nExcellent\nGood\nFair\nPoor",
		// "default": "Good"
	}

	]
};
