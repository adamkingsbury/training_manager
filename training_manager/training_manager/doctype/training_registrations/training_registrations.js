// Copyright (c) 2018, LogiKal and contributors
// For license information, please see license.txt

frappe.ui.form.on('Training Registrations', {
	onload: function(frm) {
		let qryDict = parseQueryStringToDictionary();
		if(qryDict.trainee && !frm.doc.trainee){
			frm.set_value("trainee", qryDict.trainee);
		}
		if (qryDict.event && !frm.doc.event){
			frm.set_value("event", qryDict.event);
		}
	}
});


/* Parse QueryString using String Splitting */
function parseQueryStringToDictionary() {
		var queryString = document.location.search;
    var dictionary = {};

    // remove the '?' from the beginning of the
    // if it exists
    if (queryString.indexOf('?') === 0) {
        queryString = queryString.substr(1);
    }
		if (queryString !== ""){
	    // Step 1: separate out each key/value pair
	    var parts = queryString.split('&');

	    for(var i = 0; i < parts.length; i++) {
	        var p = parts[i];
	        // Step 2: Split Key/Value pair
	        var keyValuePair = p.split('=');

	        // Step 3: Add Key/Value pair to Dictionary object
	        var key = keyValuePair[0];
	        var value = keyValuePair[1];

	        // decode URI encoded string
	        value = decodeURIComponent(value);
	        value = value.replace(/\+/g, ' ');

	        dictionary[key] = value;
	    }
		}

    // Step 4: Return Dictionary Object
    return dictionary;
}
