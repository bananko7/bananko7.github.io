console.clear()
const button = document.getElementById("submit");
button.addEventListener("click", fn1);

//load a random list of the 6 examples
var listnumber = Math.floor(Math.random()*6 + 1);
var listURL = "https://raw.githubusercontent.com/bananko7/bananko7.github.io/main/listTXTs/list"+listnumber.toString()+"txt.txt";
// Load examples
var examples = [];
console.log("URL = ",listURL)
fetch(listURL)
//fetch('https://raw.githubusercontent.com/bananko7/bananko7.github.io/main/list1txt.txt')
//fetch('https://github.com/bananko7/bananko7.github.io/blob/main/list1txt.txt')
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

function fn1(){
   // get data from the form
   var fluency = document.querySelector('input[name="fluency"]:checked').value;
   var grammar = document.querySelector('input[name="grammar"]:checked').value;
   var clarity = document.querySelector('input[name="clarity"]:checked').value;
   
   // template object to pass to the email generating function
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
   //var newtext = "<span style=\"background-color: #ffff00\">amsterdam airport schipol</span> serves <span style=\"background-color: #ffff00\">amsterdam</span>";
   console.log(newtext);
   document.getElementById('text_article').innerHTML = newtext;
}
