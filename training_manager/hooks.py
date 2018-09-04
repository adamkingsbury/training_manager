# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "training_manager"
app_title = "Training Manager"
app_publisher = "LogiKal"
app_description = "An frappe framework app to manage training courses, training events and participant registrations."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@logikalprojects.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/training_manager/css/training_manager.css"
# app_include_js = "/assets/training_manager/js/training_manager.js"

# include js, css files in header of web template
# web_include_css = "/assets/training_manager/css/training_manager.css"
# web_include_js = "/assets/training_manager/js/training_manager.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "training_manager.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "training_manager.install.before_install"
# after_install = "training_manager.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "training_manager.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
    "Training Registrations": "training_manager.training_manager.doctype.training_registrations.training_registrations.get_permission_query_conditions"
}



#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
    # "Training Events": "training_manager.training_manager.doctype.training_events.training_events.has_permission"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"training_manager.tasks.all"
# 	],
# 	"daily": [
# 		"training_manager.tasks.daily"
# 	],
# 	"hourly": [
# 		"training_manager.tasks.hourly"
# 	],
# 	"weekly": [
# 		"training_manager.tasks.weekly"
# 	]
# 	"monthly": [
# 		"training_manager.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "training_manager.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "training_manager.event.get_events"
# }
