const button = document.getElementById("submit");
button.addEventListener("click", fn1);

function fn1(){
   // get form data
   var fluency = document.querySelector('input[name="fluency"]:checked').value;
   var grammar = document.querySelector('input[name="grammar"]:checked').value;
   var clarity = document.querySelector('input[name="clarity"]:checked').value;
   // send email
   var templateParams = {
      fluency: fluency,
      grammar: grammar,
      clarity: clarity
   };
   emailjs.send('service_i8nk7oo', 'template1', templateParams)
      .then(function(response) {
         console.log(fluency,grammar,clarity,templateParams)
         console.log('SUCCESS!', response.status, response.text);
      }, function(error) {
         console.log('FAILED...', error);
      });
   }
