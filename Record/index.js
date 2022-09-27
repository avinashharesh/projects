class record
{
    constructor(fname,lname,gender,age,spec,exp,achv)
    {
        this.fname=fname;
        this.lname=lname;
        this.gender=gender;
        this.age=age;
        this.spec=spec;
        this.exp=exp;
        this.achv=achv;
    }
}
let count=0;
let r=[];
let x=0,y=0;
function submit()
{
    let a=document.getElementById("fn").value;
    let b=document.getElementById("ln").value;
    let c=document.getElementById("g").value;
    let d=document.getElementById("ag").value;
    let e=document.getElementById("s").value;
    let f=document.getElementById("ex").value;
    let g=document.getElementById("ac").value;
    r[count]=new record(a,b,c,d,e,f,g);
    let table=document.getElementById("myTable");
    let row=table.insertRow(1);
    let cell1=row.insertCell(0);
    let cell2=row.insertCell(1);
    let cell3=row.insertCell(2);
    let cell4=row.insertCell(3);
    let cell5=row.insertCell(4);
    let cell6=row.insertCell(5);
    let cell7=row.insertCell(6);
    cell1.innerText=a;
    cell2.innerText=b;
    cell3.innerText=c;
    cell4.innerText=d;
    cell5.innerText=e;
    cell6.innerText=f;
    cell7.innerText=g;
    count++;


}
function ml()
{
    dlt();
    x=1;
    document.getElementById("filter1").innerText="Specialization:Machine Learing";
    if(y==1)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Machine Learning" && r[i].exp>=0 && r[i].exp<=10)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==2)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Machine Learning" && r[i].exp>=11 && r[i].exp<=20)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==3)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Machine Learning" && r[i].exp>=21 && r[i].exp<=30)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==4)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Machine Learning" && r[i].exp>=31 && r[i].exp<=40)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Machine Learning")
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    
}
function ds()
{
    dlt();
    x=2;
    document.getElementById("filter1").innerText="Specialization:Data Science";
    if(y==1)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Data Science" && r[i].exp>=0 && r[i].exp<=10)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Data Science" && r[i].exp>=11 && r[i].exp<=20)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Data Science" && r[i].exp>=21 && r[i].exp<=30)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Data Science" && r[i].exp>=31 && r[i].exp<=40)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Data Science")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }

}
function cs()
{
    dlt();
    x=3;
    document.getElementById("filter1").innerText="Specialization:Cybersecurity";
    if(y==1)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Cybersecurity" && r[i].exp>=0 && r[i].exp<=10)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cybersecurity" && r[i].exp>=11 && r[i].exp<=20)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cybersecurity" && r[i].exp>=21 && r[i].exp<=30)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cybersecurity" && r[i].exp>=31 && r[i].exp<=40)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cybersecurity")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function cc()
{
    dlt();
    x=4;
    document.getElementById("filter1").innerText="Specialization:Cloudcomputing";
    if(y==1)
    {
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        if(r[i].spec=="Cloudcomputing" && r[i].exp>=0 && r[i].exp<=10)
        {
            let row=table.insertRow(1);
            let cell1=row.insertCell(0);
            let cell2=row.insertCell(1);
            let cell3=row.insertCell(2);
            let cell4=row.insertCell(3);
            let cell5=row.insertCell(4);
            let cell6=row.insertCell(5);
            let cell7=row.insertCell(6);
            cell1.innerText=r[i].fname;
            cell2.innerText=r[i].lname;
            cell3.innerText=r[i].gender;
            cell4.innerText=r[i].age;
            cell5.innerText=r[i].spec;
            cell6.innerText=r[i].exp;
            cell7.innerText=r[i].achv;
        }
    }
    }
    else if(y==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cloudcomputing" && r[i].exp>=11 && r[i].exp<=20)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cloudcomputing" && r[i].exp>=21 && r[i].exp<=30)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(y==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cloudcomputing" && r[i].exp>=31 && r[i].exp<=40)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].spec=="Cloudcomputing")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function ze()
{
    dlt();
    y=1;
    document.getElementById("filter2").innerText="Experience:0-10";
    if(x==1)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=0 && r[i].exp<=10 && r[i].spec=="Machine Learning")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=0 && r[i].exp<=10 && r[i].spec=="Data Science")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=0 && r[i].exp<=10 && r[i].spec=="Cybersecurity")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=0 && r[i].exp<=10 && r[i].spec=="Cloudcomputing")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=0 && r[i].exp<=10)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function el()
{
    dlt();
    y=2;
    document.getElementById("filter2").innerText="Experience:11-20";
    if(x==1)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=11 && r[i].exp<=20 && r[i].spec=="Machine Learning")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=11 && r[i].exp<=20 && r[i].spec=="Data Science")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=11 && r[i].exp<=20 && r[i].spec=="Cybersecurity")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=11 && r[i].exp<=20 && r[i].spec=="Cloudcomputing")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=11 && r[i].exp<=20)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function tw()
{
    dlt();
    y=3;
    document.getElementById("filter2").innerText="Experience:21-30";
    if(x==1)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=21 && r[i].exp<=30 && r[i].spec=="Machine Learning")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=21 && r[i].exp<=30 && r[i].spec=="Data Science")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=21 && r[i].exp<=30 && r[i].spec=="Cybersecurity")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=21 && r[i].exp<=30 && r[i].spec=="Cloudcomputing")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=21 && r[i].exp<=30)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function th()
{
    dlt();
    y=4;
    document.getElementById("filter2").innerText="Experience:31-40";
    if(x==1)
    {
        dlt();
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=31 && r[i].exp<=40 && r[i].spec=="Machine Learning")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==2)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=31 && r[i].exp<=40 && r[i].spec=="Data Science")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==3)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=31 && r[i].exp<=40 && r[i].spec=="Cybersecurity")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else if(x==4)
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=31 && r[i].exp<=40 && r[i].spec=="Cloudcomputing")
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
    else
    {
        let table=document.getElementById("myTable");
        for(let i=0;i<count;i++)
        {
            if(r[i].exp>=31 && r[i].exp<=40)
            {
                let row=table.insertRow(1);
                let cell1=row.insertCell(0);
                let cell2=row.insertCell(1);
                let cell3=row.insertCell(2);
                let cell4=row.insertCell(3);
                let cell5=row.insertCell(4);
                let cell6=row.insertCell(5);
                let cell7=row.insertCell(6);
                cell1.innerText=r[i].fname;
                cell2.innerText=r[i].lname;
                cell3.innerText=r[i].gender;
                cell4.innerText=r[i].age;
                cell5.innerText=r[i].spec;
                cell6.innerText=r[i].exp;
                cell7.innerText=r[i].achv;
            }
        }
    }
}
function filter()
{
    document.getElementById("filter1").innerText="Specialization:";
    document.getElementById("ml").innerText="Machine Learning";
    document.getElementById("ds").innerText="Data Science";
    document.getElementById("cs").innerText="Cybersecurity";
    document.getElementById("cc").innerText="Cloudcomputing";
    document.getElementById("filter2").innerText="Experience:";
    document.getElementById("ze").innerText="0-10";
    document.getElementById("el").innerText="11-20";
    document.getElementById("tw").innerText="21-30";
    document.getElementById("th").innerText="31-40";

}
function dlt()
{
    let a=document.getElementById("myTable");
    let b=a.rows.length;
    for(let i=0;i<b-1;i++)
    document.getElementById("myTable").deleteRow(1);
}
function display()
{
    dlt();
    document.getElementById("filter1").innerText="";
    document.getElementById("ml").innerText="";
    document.getElementById("ds").innerText="";
    document.getElementById("cs").innerText="";
    document.getElementById("cc").innerText="";
    document.getElementById("filter2").innerText="";
    document.getElementById("ze").innerText="";
    document.getElementById("el").innerText="";
    document.getElementById("tw").innerText="";
    document.getElementById("th").innerText="";
    let table=document.getElementById("myTable");
    for(let i=0;i<count;i++)
    {
        let row=table.insertRow(1);
        let cell1=row.insertCell(0);
        let cell2=row.insertCell(1);
        let cell3=row.insertCell(2);
        let cell4=row.insertCell(3);
        let cell5=row.insertCell(4);
        let cell6=row.insertCell(5);
        let cell7=row.insertCell(6);
        cell1.innerText=r[i].fname;
        cell2.innerText=r[i].lname;
        cell3.innerText=r[i].gender;
        cell4.innerText=r[i].age;
        cell5.innerText=r[i].spec;
        cell6.innerText=r[i].exp;
        cell7.innerText=r[i].achv;
    }

}
