function load(){
    loadexample()
    }
    resultstring = 'at';
    function loadexample(){
        var listURL = "https://raw.githubusercontent.com/bananko7/HC3database/main/"+String(Math.floor(Math.random()*100)+1)+".txt";
        console.log("URL = ",listURL)
        fetch(listURL)
        .then(response => response.text())
        .then((data) => {
            //console.log(data);
            examples = data.split("<>");
            //console.log(examples);
            if(Math.floor(Math.random() * 2)==0){
                document.getElementById('question').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[0]+"</span>";
                document.getElementById('answer1').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[2]+"</span>";
                document.getElementById('answer2').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[1]+"</span>";
                document.getElementById('topic').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[3]+"</span>";
                flipped = true;
            }
            else{
                document.getElementById('question').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[0]+"</span>";
                document.getElementById('answer1').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[1]+"</span>";
                document.getElementById('answer2').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[2]+"</span>";
                document.getElementById('topic').innerHTML = "<span style=\"background-color: #EEEE00\">"+examples[3]+"</span>";
                flipped = false;
            }
    });
    }
    
    buttonsubmit = document.getElementById("endbutton");
    buttonsubmit.addEventListener("click",function(){
        console.log("end button clicked");
        buttonsubmit.disabled = true;
        submit();
    });
    
    
    button1 = document.getElementById("answer1button");
    button1.addEventListener("click",function(){
        console.log("button 1 clicked");
        if (flipped == true){resultstring = resultstring + examples[3].substring(0, 1) + "2";}
        else{resultstring = resultstring + examples[3].substring(0, 1) + "1";}
        loadexample();
    });
        
    
    button2 = document.getElementById("answer2button");
    button2.addEventListener("click",function(){
        console.log("button 2 clicked")
        if(flipped == true){resultstring = resultstring + examples[3].substring(0, 1) + "1";}
        else{resultstring = resultstring + examples[3].substring(0, 1) + "2";}
        loadexample();
    });
    
    button3 = document.getElementById("loadnewbutton");
    button3.addEventListener("click",function(){
        console.log("button load new example clicked");
        loadexample();
    });
    
    function submit(){
        console.log(resultstring)
        // template object to pass to the email generating function
        var templateParams = {
            result: resultstring,
        };
            
            emailjs.send('service_i8nk7oo', 'template3', templateParams)
               .then(function(response) {
                  //console.log(fluency,grammar,clarity,templateParams)
                  console.log('SUCCESS!', response.status, response.text);
                  console.log("EMAIL SENT with data:",templateParams)
                  window.location.replace("thankyou.html");
               }, function(error) {
                  console.log('FAILED...', error);
               });
    }