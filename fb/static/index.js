console.log("js file activated");

document.getElementById("account1").addEventListener("click", function(){
  this.parentElement.style.display = "none";
});

document.getElementById("account2").addEventListener("click", function(){
  this.parentElement.style.display = "none";
});



// for opening a new page
document.getElementById("login").addEventListener("click", function()
{ 
let email = document.getElementById('email_aj').value;
let password = document.getElementById('password_aj').value;
	
	if ((email == "111arpit1@gmail.com") && (password == "123"))
	{
		window.location="arpit.html";
	}
	else
	{
  alert("The email or password you have entered is incorrect please try again! email is 111arpit1@gmail.com and password  is 123 ");
  window.location="login.html";
	}
});

let alert1 = document.getElementById('alert1');
// for creating a new account
document.getElementById("signup").addEventListener("click", function(){
  // alert("Your account is succesfully created");
  alert1.style.display = "block";
  location.reload();
});

