# Copyright (c) 2013, LogiKal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = getColumns()
	data = getData()
	return columns, data


def getColumns():
	cols = [
				"Request:Link/Training Registrations:60",
				"Course::120",
				"Trainee::60",
				"Status::30",
				"Course Start::20",
				"Course End::20"
			]

	return cols


def getData(filters=[]):

	qry = """
		SELECT name,
				course_title,
				trainee_name,
				status,
				course_start,
				course_finish
		FROM `tabTraining Registrations`
		WHERE trainee = "{user}"
		AND   course_start >= "{date}"
		""".format(user = frappe.session.user, date=frappe.utils.nowdate())

	result = frappe.db.sql(qry, filters, as_list=1)
	return result
