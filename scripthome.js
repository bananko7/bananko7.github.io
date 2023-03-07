const button = document.getElementById("iagree");
button.addEventListener("click", function1);
function function1(){
  //get form data
  console.clear()
  var name = document.getElementById("inputname").value;
  var gender = document.getElementById("gender").value;
  var age = document.getElementById("age").value;
  var country = document.getElementById("country").value;
  var nativelanguage = document.getElementById("nativelanguage").value;
  var proficiency = document.getElementById("proficiency").value;
  
  var data = {
    name: name,
    gender: gender,
    age: age,
    country: country,
    nativelanguage: nativelanguage,
    proficiency: proficiency
  };
  //emailjs.send('service_avefsxl', 'template_09gqeyk',data)
  //    .then(function(response) {
  //       console.log(data)
  //       console.log('SUCCESS!', response.status, response.text);
  //    }, function(error) {
  //       console.log('FAILED...', error);
  //    });
  console.log(data);
  window.location.replace("secondarypage.html");
}
