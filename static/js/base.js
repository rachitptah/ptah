var user = {
	signup : function() {
		var firstname = document.signupform.first_name.value;
        var username = document.signupform.username.value;
		var email = document.signupform.email.value;
		var password = document.signupform.password.value;
		var confirmpassword = document.signupform.confirmpassword.value;
		if (firstname == "")
		{
			alert("Please provide your first name!")
			document.signupform.first_name.focus();
		}
        else if (username == "")
        {
            alert("Please provide the username!")
            document.signupform.first_name.focus();
        }
        else if (email == "")
        {
            alert("Please provide your Email!")
            document.signupform.email.focus() ;
        }
		// else if (!validateEmail())
  //       {
  //       	alert("Please provide valid email!")
  //       	document.signupform.email.focus() ;
  //       }
        else if (password == "")
        {
        	alert("Please enter a valid password")
        	document.signupform.password.focus() ;
        }
        else if (password != confirmpassword) 
        {
            alert("Passwords do not match.");
         	document.signupform.confirmpassword.focus() ;
        }
        else
        {
        	return true
        }
        return false
	},

	validateEmail : function()
    {
        var emailID = document.signupform.email.value;
        atpos = emailID.indexOf("@");
        dotpos = emailID.lastIndexOf(".");
        if (atpos < 1 || ( dotpos - atpos < 2 )) 
        {
            return false;
        }
        return true;
        },
}