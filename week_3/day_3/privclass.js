const root= document.getElementById('root');


let header = document.createElement('h1');
let textbox= document.createElement('input');
let btn = document.createElement('button');
let btn2 = document.createElement('button');
let unlist = document.createElement('ul');

header.innerText='Shopping List:';
btn.innerHTML='Add';
btn.addEventListener('click',addItem);
btn2.innerHTML='Clear';
btn2.addEventListener('click',clearItem);

function addItem(){
	if (textbox.value!='') {
		let item=document.createElement('li');
		item.innerHTML=textbox.value;
		

	}	
}
	
	
// to create the delete button is with the FOR loop
// create item that select all the 'Li'

// function clearItem(){
// 	ul.innerHTML='';
// }

root.appendChild(header);
root.appendChild(textbox);
root.appendChild(btn);
root.appendChild(btn2);
root.appendChild(unlist);
