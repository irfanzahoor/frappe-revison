# Copyright (c) 2023, nextash and contributors
# For license information, please see license.txt
import frappe

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    columns = [
        {"fieldname": "employee_name", "label": "Employee Name", "fieldtype": "Data"},
        {"fieldname": "department", "label": "Department", "fieldtype": "Data"},
        {"fieldname": "reviewer", "label": "Reviewer", "fieldtype": "Data"},
        {"fieldname": "date", "label": "Date", "fieldtype": "Data"},
        {"fieldname": "period_of_review", "label": "Period Of Review", "fieldtype": "Data"},
        {"fieldname": "reviews_title", "label": "Reviews Title", "fieldtype": "Data"},
        {"fieldname": "job_knowledge", "label": "Job Knowledge", "fieldtype": "Select"},
        {"fieldname": "productivity", "label": "Productivity", "fieldtype": "Select"},
        {"fieldname": "work_quality", "label": "Work Quality", "fieldtype": "Select"},
        {"fieldname": "work_skills", "label": "Work Skills", "fieldtype": "Select"},
        {"fieldname": "technical_skills", "label": "Technical Skills", "fieldtype": "Select"},
        {"fieldname": "work_consistency", "label": "Work Consistency", "fieldtype": "Select"},
        {"fieldname": "cooperation", "label": "Cooperation", "fieldtype": "Select"},
        {"fieldname": "attitude", "label": "Attitude", "fieldtype": "Select"},
        {"fieldname": "work_relations", "label": "Work Relations", "fieldtype": "Select"},
        {"fieldname": "creativity", "label": "Creativity", "fieldtype": "Select"},
        {"fieldname": "punctuality", "label": "Punctuality", "fieldtype": "Select"},
        {"fieldname": "attendance", "label": "Attendance", "fieldtype": "Select"},
        {"fieldname": "dependance", "label": "Dependence", "fieldtype": "Select"},
        {"fieldname": "communication_skills", "label": "Communication Skills", "fieldtype": "Select"},
        {"fieldname": "overall_rating", "label": "Overall Rating", "fieldtype": "Select"},
    ]
    return columns

def get_data(filters):
    data = []
    my_filter = {}
    # my_filter = {'employee': "Employee-00005", "attitude" : "Excellent",  }
    if filters.get("employee"):
      my_filter['name'] = filters.get("employee")
      
    if filters.get("attitude"):
      my_filter["attitude"] = filters.get("attitude")
    if filters.get("attendance"):
      my_filter["attendance"] = filters.get("attendance")
    doc = frappe.get_list('Employee Performance', filters= my_filter, fields=['*'])
    for row in doc:
        data.append({
            "employee_name": row.employee_name,
            "department": row.department,
            "reviewer": row.reviewer,
            "date": row.date,
            "period_of_review": row.period_of_review,
            "reviews_title": row.reviews_title,
            "job_knowledge": row.job_knowledge,
            "productivity": row.productivity,
            "work_quality": row.work_quality,
            "work_skills": row.work_skills,
            "technical_skills": row.technical_skills,
            "work_consistency": row.work_consistency,
            "cooperation": row.cooperation,
            "attitude": row.attitude,
            "work_relations": row.work_relations,
            "creativity": row.creativity,
            "punctuality": row.punctuality,
            "attendance": row.attendance,
            "dependance": row.dependance,
            "communication_skills": row.communication_skills,
            "overall_rating": row.overall_rating,
        })
    return data


student = {
	"name": 'Shahid',
	'age': 24,
	'class': 10
}
student['height'] = 100
