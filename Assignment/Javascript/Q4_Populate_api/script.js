var btn= document.getElementById("mybutton");
function select(){
		var ourRequest=new XMLHttpRequest();
		ourRequest.open('GET',"https://learnwebcode.github.io/json-example/animals-1.json");
		ourRequest.onload=function(){
				var ourData=JSON.parse(ourRequest.responseText);
				renterHTML(ourData);
		}
		ourRequest.send();
}
function renterHTML(data)
{
	var str='';
	for(i=0;i<data.length;i++)
	{
			str+="<p>"+data[i].name+" "+data[i].species+".</p>";
	}
		document.write(str);
}
