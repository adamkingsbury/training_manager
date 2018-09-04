// Copyright (c) 2018, LogiKal and contributors
// For license information, please see license.txt

//Array to accurately return the month string part from javascript Date.getDate()
const monthText = ["01","02","03","04","05","06","07","08","09","10","11","12"];

frappe.ui.form.on('Training Events', {


	refresh: function(frm){

		//get all of the registrations related to this event
		frappe.db.get_list("Training Registrations",{
			"filters": {"event": frm.doc.name},
			"fields": ["name", "trainee", "status"]
		}).then(result => processRegistrations(result));

		function processRegistrations(result){
			console.log(result);

			//Add a "custom button" to register for the training event if the event Status
			//is "Open for Registration".
			//Custom buttons appear above the main part of the form
			let registrationsByUser = result.filter(rec => rec.trainee === frappe.session.user);
			if(frm.doc.status == "Open for Registration" && registrationsByUser.length == 0){
				frm.add_custom_button(__("Register for this Event"), function() {
					var doc = frappe.model.get_new_doc('Training Registrations');
					doc.event = frm.doc.name;
					doc.trainee = frappe.session.user;
					frappe.set_route('Form', 'Training Registrations', doc.name);
				});
			}

			//Get a count of the number of registrations for the training event.
			//Only count those with a status or Registered or approved (no rejected)
			let validRegistrations = result.filter(rec => rec.status !== "Rejected");
			frm.set_value("registrations_recieved", validRegistrations.length);
		}
	},

	// Toggle visibility of a form field with type "Button"
	// This code was switched off because the button wouldn't appear if the
	// User had read-only access (eg. trainees who can only look at the available events)
	// register_button: function(frm){
	// 	if(frm.doc.status === "Open for Registration"){
	// 		var doc = frappe.model.get_new_doc('Training Registrations');
	// 		doc.event = frm.doc.name;
	// 		doc.trainee = frappe.session.user;
	// 		frappe.set_route('Form', 'Training Registrations', doc.name);
	// 	}
	// },

	//don't save the doc if the finish date is less than the start date
	validate: function(frm) {
		if(frm.doc.start > frm.doc.finish) {
			frappe.throw(__("Finish date cannot be earlier than start date"));
		}
	},

	//If start field changes, change the finish date by adding the duration minus 1
	start: function(frm) {
		let d = frm.doc.duration;
		if(d){
			let dur = Math.ceil(parseFloat(frm.doc.duration));
			let daysToAdd = dur - 1;
			let date = new Date(frm.doc.start);
			let curFin = new Date(frm.doc.finish);
			date.setDate(date.getDate() + daysToAdd);
			if (((date - curFin)/(1000*60*60*24)) != 0) {
					let newDateString = date.getFullYear()+"-"+monthText[date.getMonth()]+"-"+date.getDate();
					frm.set_value("finish", newDateString);
			}
		}

		//Also set the Event year field to allow for simpler searching
		let date = new Date(frm.doc.start);
		frm.set_value("event_year", date.getFullYear());
	},

	// //If finish field changes, adjust the duration
	finish: function(frm) {
		let d = frm.doc.duration;
		let st = frm.doc.start;
		if(d && st){
			let sDate = new Date(frm.doc.start);
			let fDate = new Date(frm.doc.finish);

			let newDur = Math.ceil((fDate - sDate)/(1000*60*60*24)) + 1;
			let curDur = Math.ceil(frm.doc.duration);
			if (curDur != newDur){
				frm.set_value("duration", newDur);
			}
		}
	},

	// If duration field changes, adjust the finish date
	duration: function(frm) {
		let st = frm.doc.start;
		if(st){
			let dur = Math.ceil(parseFloat(frm.doc.duration));
			let daysToAdd = dur - 1;
			var date = new Date(frm.doc.start);
			var curFin = new Date(frm.doc.finish);
			date.setDate(date.getDate() + daysToAdd);
			if ((date -  curFin) != 0) {
					let newDateString = date.getFullYear()+"-"+monthText[date.getMonth()]+"-"+date.getDate();
					frm.set_value("finish", newDateString);
			}
		}
	}
});
