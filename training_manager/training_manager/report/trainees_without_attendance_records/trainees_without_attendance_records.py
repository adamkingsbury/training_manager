# Copyright (c) 2013, LogiKal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = getColumns()
	data = getData(filters)
	return columns, data

# "{\"fields\": [
# [\"name\", \"Training Registrations\"],
# [\"course_title\", \"Training Registrations\"],
# [\"trainee_name\", \"Training Registrations\"],
# [\"status\", \"Training Registrations\"],
# [\"docstatus\", \"Training Registrations\"],
# [\"course_start\", \"Training Registrations\"],
# [\"course_finish\", \"Training Registrations\"]],
#
# \"add_totals_row\": 0,
# \"order_by\": \"`tabTraining Registrations`.`modified` desc\", \"add_total_row\": 0,
#
# \"filters\":
# [[\"Training Registrations\", \"status\", \"=\", \"Accepted\", false],
# [\"Training Registrations\", \"attendance\", \"not in\", [\"Attended\", \"Did Not Attend\", null], false]]}"

def getColumns():
	cols = [
				"Registration:Link/Training Registrations:60",
				"Course::120",
				"Course Date::30"
				"Trainee Name::120",
				"Registration Status::40",
				"Attendance::30",
				"Trainer::120"
			]
	return cols


def getData(filters=[]):

	qry = """
		SELECT `tabTraining Registrations`.name,
				`tabTraining Registrations`.course_title,
				`tabTraining Registrations`.course_start,
				`tabTraining Registrations`.trainee_name,
				`tabTraining Registrations`.status,
				`tabTraining Registrations`.attendance,
				`tabTraining Events`.trainer_name
		FROM `tabTraining Registrations`, `tabTraining Events`
		WHERE `tabTraining Registrations`.status = "Accepted"
		AND `tabTraining Registrations`.event = `tabTraining Events`.name
		AND   `tabTraining Registrations`.attendance NOT IN ("Attended","Did Not Attend")
		AND   `tabTraining Registrations`.course_finish < "{date}"
		AND	  `tabTraining Registrations`.event in (select name from `tabTraining Events` where `tabTraining Events`.trainer = '{user}' )
		""".format(date=frappe.utils.nowdate(), user=frappe.session.user)

	result = frappe.db.sql(qry, filters, as_list=1)
	return result
