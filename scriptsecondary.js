
const button = document.getElementById("submit");
button.addEventListener("click", fn1);

examples = [];
fetch('https://bananko7.github.io/cattcleaned.txt')
//fetch('file:///E:/hons%20project/site/secondarypage.html')
   .then(response => response.text())
   .then((data) => {
      //console.log(data);
      examples = data.split("@");
   });


//console.log(client.responseText);
//client.send();

function getrandomitem(examples){
   const index = Math.floor(Math.random()*examples.length);
   const item = examples[index];
   return item;
}

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
   //clear radio buttons
   var buttonfluency = document.getElementsByName("fluency");
   var buttongrammar = document.getElementsByName("grammar");
   var buttonclarity = document.getElementsByName("clarity");
   for(var i=0;i<buttonfluency.length;i++)
      buttonfluency[i].checked = false;
      if(buttonfluency[3].checked == false){
         buttonfluency[3].checked = true
      }

   for(var i=0;i<buttongrammar.length;i++)
      buttongrammar[i].checked = false;
      if(buttongrammar[3].checked == false){
         buttongrammar[3].checked = true
      }
   for(var i=0;i<buttonclarity.length;i++)
      buttonclarity[i].checked = false;
      if(buttonclarity[3].checked == false){
         buttonclarity[3].checked = true
      }


   //emailjs.send('service_i8nk7oo', 'template1', templateParams)
   //   .then(function(response) {
   //      console.log(fluency,grammar,clarity,templateParams)
   //      console.log('SUCCESS!', response.status, response.text);
   //   }, function(error) {
   //      console.log('FAILED...', error);
   //   });
   //loadnewexample(); 
   var newtext = getrandomitem(examples);
   //var newtext = "<span style=\"background-color: #ffff00\">amsterdam airport schipol</span> serves <span style=\"background-color: #ffff00\">amsterdam</span>";
   console.log(newtext);
   document.getElementById('text_article').innerHTML = newtext;
}
