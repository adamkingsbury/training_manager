# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Drafts",
			"label": "Draft Events",
			"_doctype": 'Training Events',
			"icon": "octicon octicon-paintcan",
			"_report": "Draft Training Events",
			"type": "link",
			"link": "List/Training Events/Report/Draft Training Events"
        },
		{
			"module_name": "My Requests",
			"label": "My Requests",
			"_doctype": 'Training Registrations',
			"icon": "octicon octicon-star",
			"_report": "My Upcoming Training Registrations",
			"type": "link",
			"link": "query-report/My Upcoming Training Registrations"
        },
		{
			"module_name": "Available",
			"label": "Open Training",
			"_doctype": 'Training Events',
			"icon": "octicon octicon-checklist",
			"_report": "Training Open for Registration",
			"type": "link",
			"link": "List/Training Events/Report/Training Open for Registration"
        },
		{
			"module_name": "Training Manager",
			"color": "grey",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Training Manager")
		}
	]
