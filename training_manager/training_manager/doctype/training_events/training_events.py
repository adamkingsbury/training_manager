# -*- coding: utf-8 -*-
# Copyright (c) 2018, LogiKal and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TrainingEvents(Document):

	def on_update(self):

		# Find the training registrations linked to this event
		registrationList = frappe.db.sql("""
				select name
				from `tabTraining Registrations`
				where event = '%s'
			"""%(self.name), as_dict=True)

		# Update each training registration record to match the start and finish
		# dates from the training event record
		for result in registrationList:
			doc = frappe.get_doc("Training Registrations", result.name)
			doc.course_start = self.start
			doc.course_finish = self.finish
			doc.save()
