function calculate()
{
    let a1=document.getElementById("a1").value;
    let a2=document.getElementById("a2").value;
    if(a1=="dozen")
    a1=12;
    else
    a1=parseInt(a1);
    if(a2=="dozen")
    a2=12;
    else
    a2=parseInt(a2);
    let a3=a1+a2;
    let a4=10*a3;
    let a5=a4-0.05*a4;
    document.getElementById("sbt").innerText="Sub Total:"+a3;
    document.getElementById("tax").innerText="Tax:5%";
    document.getElementById("tot").innerText="Total:Rs"+a5;

}