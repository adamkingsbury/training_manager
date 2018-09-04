# Copyright (c) 2013, LogiKal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

# {"fields": [["name", "Training Events"], ["docstatus", "Training Events"], ["course", "Training Events"], ["course_title", "Training Events"], ["duration", "Training Events"], ["start", "Training Events"], ["finish", "Training Events"], ["trainer_name", "Training Events"], ["status", "Training Events"], ["event_year", "Training Events"]], "add_totals_row": 0, "order_by": "`tabTraining Events`.`modified` desc", "filters": [["Training Events", "status", "in", ["Draft", "Open for Registration", "Registration Closed", null], false], ["Training Events", "finish", "<", "2018-08-31", false]], "add_total_row": 0}


def execute(filters=None):
	columns = getColumns()
	data = getData(filters)
	return columns, data


def getColumns():
	cols = [
				"Event:Link/Training Events:60",
				"Course::120",
				"Duration::30",
				"Start::30",
				"Finish::30",
				"Trainer::50",
				"Status::40"
			]

	return cols


def getData(filters=[]):

	qry = """
		SELECT name,
				course_title,
				duration,
				start,
				finish,
				trainer_name,
				status
		FROM `tabTraining Events`
		WHERE finish < "{date}"
		AND   status in ("Draft", "Open for Registration", "Registration Closed")
		""".format(date=frappe.utils.nowdate())

	result = frappe.db.sql(qry, filters, as_list=1)
	return result
