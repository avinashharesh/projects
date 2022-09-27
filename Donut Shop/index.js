let z=0;
var y;
function sad()
{
    document.getElementById("pet").src="sad.png";
}
setTimeout(sad,300000);
function hello(str)
{
    if(str!=undefined)
    {


        document.getElementById("gr").innerText="Hello Again "+str+"!";
        document.getElementById("pet").src="helloag.png";
    }

}
function greet()
{
    y=document.getElementById("sd").value;
    document.getElementById("pet").src="greeting.png";
    document.getElementById("name").innerHTML="";
    document.getElementById("smbt").innerHTML="";
    document.getElementById("gr").innerText="Hello "+y+"!";
    
}
function dog()
{
    setTimeout(sad,300000);
    z+=1;
    if(z==1)
    {
        document.getElementById("pet").src="waiting.png";
        let x="ip";
        let blank="";
        document.getElementById("name").innerHTML+="<form><label>Username</label><br /><input id=sd type=text value/></form>";
        document.getElementById("smbt").innerHTML+="<button onclick=greet()>SUBMIT</button>";
    }
    else 
    hello(y);

}
