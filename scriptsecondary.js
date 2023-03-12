
//console.clear()


const button = document.getElementById("submit");
button.addEventListener("click", clicked);


var globalfluency = '';
var globalgrammar = '';
var globalclarity = '';



//load a random list of the 6 examples
var listnumber = Math.floor(Math.random()*6 + 1);

var listURL = "https://raw.githubusercontent.com/bananko7/bananko7.github.io/main/listTXTs/list"+listnumber.toString()+"txt.txt";
// Load examples
var examples = [];
console.log("URL = ",listURL)
fetch(listURL)
   .then(response => response.text())
   .then((data) => {
      //console.log(data);
      examples = data.split("@");
   });

function loadnewitem(array){
   
   var item = array.pop();
   //console.log(item)
   var returnitem = item.slice(8)
   return returnitem;
}

function clicked(){
   //console.log("examples to show left:",examples.length-1)
   if(examples.length == 1){
      sendemail(globalfluency,globalgrammar,globalclarity)
   }
   else{
      generateresponse()
   }
}
function sendemail(globalfluency,globalgrammar,globalclarity){
   // template object to pass to the email generating function
   var templateParams = {
      fluency: globalfluency,
      grammar: globalgrammar,
      clarity: globalclarity,
      list: listnumber
   };
   emailjs.send('service_i8nk7oo', 'template1', templateParams)
      .then(function(response) {
         //console.log(fluency,grammar,clarity,templateParams)
         //console.log('SUCCESS!', response.status, response.text);
      }, function(error) {
         //console.log('FAILED...', error);
      });
   //console.log(templateParams)
   //var start = new Date().getTime();
   //var end = start;
   //while(end < start + 10000) {
   //  end = new Date().getTime();
   //}
   window.location.replace("thankyou.html");
}
function generateresponse(){


   // get data from the form
   var fluency = document.querySelector('input[name="fluency"]:checked').value;
   var grammar = document.querySelector('input[name="grammar"]:checked').value;
   var clarity = document.querySelector('input[name="clarity"]:checked').value;
   console.log(typeof fluency)


   globalfluency = globalfluency.concat(fluency);
   globalgrammar = globalgrammar.concat(grammar);
   globalclarity = globalclarity.concat(clarity);
   
   console.log("saved response: ",fluency,grammar,clarity);

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
   //clear radio buttons end

   //emailjs.send('service_i8nk7oo', 'template1', templateParams)
   //   .then(function(response) {
   //      console.log(fluency,grammar,clarity,templateParams)
   //      console.log('SUCCESS!', response.status, response.text);
   //   }, function(error) {
   //      console.log('FAILED...', error);
   //   });

   //console.log(shuffledexamples)
   var newtext = loadnewitem(examples);
   document.getElementById('text_article').innerHTML = newtext;
}
