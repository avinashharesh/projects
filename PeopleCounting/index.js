let count = 0;
let x=document.getElementById("count");
console.log(x);
function increment()
{
    count=count+1;
    x.innerText=count;
}
function save()
{
    console.log(count);
    let y=document.getElementById("ayin");
    y.textContent+=count+"-";
    x.innerText=0;
    count=0;
}