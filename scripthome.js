const button = document.getElementById("iagree");
button.addEventListener("click", function1);
function function1(){
  //get form data
  console.clear();
  button.disabled = true;
  var name = document.getElementById("inputname").value;
  var gender = document.getElementById("gender").value;
  var age = document.getElementById("age").value;
  var country = document.getElementById("country").value;
  var nativelanguage = document.getElementById("nativelanguage").value;
  var proficiency = document.getElementById("proficiency").value;
  
  if(name==''){
    name = 'no name'
  }
  if(country == ''){
    country = 'no country'
  }
  if(nativelanguage == ''){
    nativelanguage = 'no native language'
  }
  var data = {
    name: name,
    gender: gender,
    age: age,
    country: country,
    nativelanguage: nativelanguage,
    proficiency: proficiency
  };
  emailjs.send('service_avefsxl', 'template_homepage', data)
      .then(function(response) {
         console.log('SUCCESS!', response.status, response.text);
         window.location.replace("secondarypage.html");
      }, function(error) {
         console.log('FAILED...', error);
      }); 
}
