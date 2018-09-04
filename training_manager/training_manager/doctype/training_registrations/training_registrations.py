# -*- coding: utf-8 -*-
# Copyright (c) 2018, LogiKal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TrainingRegistrations(Document):
	pass


def get_permission_query_conditions(user):
	if not user: user = frappe.session.user
	roles = frappe.get_roles(user)
	overrideRoles = [
		"Training Manager",
		"Training Approver"
	]
	overrideCount = 0
	for oRole in overrideRoles:
		if oRole in roles:
			overrideCount += 1

	return """
			`tabTraining Registrations`.trainee = '%(user)s'
			OR %(override)d > 0
			OR `tabTraining Registrations`.event in (select name from `tabTraining Events` where trainer = '%(user)s')
		""" % {
			"user": frappe.db.escape(user),
			"override": overrideCount
		}
