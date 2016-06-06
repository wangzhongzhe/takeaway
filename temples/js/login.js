
function myFunction(x)
{
	var x=document.getElementById("judge_1");	
    if(x.value==""){
        document.getElementById("out_1").style.display="block";
        document.getElementById("judge_1").style.border="2px solid red";
    }
    else{
        document.getElementById("out_1").style.display="none";
        document.getElementById("judge_1").style.border="1px solid blue";
    }
} 
function myFunction_2(x){
    var y=document.getElementById("judge_2");
    if(y.value==""){
        document.getElementById("out_2").style.display="block";
        document.getElementById("judge_2").style.border="2px solid red";
    }
    else{
        document.getElementById("out_2").style.display="none";
        document.getElementById("judge_2").style.border="1px solid blue";
    }
}
function myFunction_3(x){
    var z=document.getElementById("judge_3");
    if(z.value==""){
        document.getElementById("out_3").style.display="block";
        document.getElementById("judge_3").style.border="2px solid red";
    }
    else{
        document.getElementById("out_3").style.display="none";
        document.getElementById("judge_3").style.border="1px solid blue";
    }
}
function change_1(a){
	a.style.opacity="0.6"; 
}
function change_2(a){
	a.style.opacity="1"; 
}
$(document).ready(function(){
    $(".flip").click(function(){
        $(".panel").slideToggle("slow");
    });
});
function rule()
{
    document.getElementById("light").style.display="block";
    document.getElementById("fade").style.display="block"
}