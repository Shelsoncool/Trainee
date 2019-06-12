
function Turnoff() {
  var x = document.getElementsByClassName("dot");
  x[0].style.backgroundColor = 'grey';
   x[1].style.backgroundColor = 'grey';
    x[2].style.backgroundColor = 'grey';
}

function yblink(){
	yblink=setInterval(blinkyellow,2000);
}
function blinkyellow() {    				
  				 var x = document.getElementById('s3');
  				 x.style.backgroundColor= x.style.backgroundColor == 'yellow'?'grey': 'yellow';  				 
}


function stopblink()
{
        var x = document.getElementsByClassName("dot");
          x[0].style.backgroundColor = 'grey';
          x[1].style.backgroundColor = 'grey';
          x[2].style.backgroundColor = 'grey';
           clearInterval(yblink);
           clearInterval(r);
}

function signal()
{
		var x=document.getElementById('s1');
    var y=document.getElementById('s3');
		var z=document.getElementById('s2');

    x.style.backgroundColor= x.style.backgroundColor == 'red'?'grey': 'red';
    //y.style.backgroundColor= x.style.backgroundColor == 'grey'?'yellow': 'grey';
    z.style.backgroundColor= x.style.backgroundColor =='grey'?'green': 'grey';


  }
  
  function signalblink(){
  	r=setInterval(signal,3000);
  	signal();

  }
