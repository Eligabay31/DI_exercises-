const root= document.getElementById('root');

let header = document.createElement('h1');
let unlisted = document.createElement('ul');
let textbox= document.createElement('input');
let textbox2= document.createElement('input');
let textbox3= document.createElement('input');
let item1=document.createElement('li');
let item2=document.createElement('li');
let item3=document.createElement('li');
let btn = document.createElement('button');



header.innerText='Mad Libs';
item1.innerText='Noun';
item2.innerText='Adjective';
item3.innerText="Someone's Name"; 
btn.innerHTML='Generate';






root.appendChild(header);
item1.appendChild(textbox);
item2.appendChild(textbox2);
item3.appendChild(textbox3);
root.appendChild(item1);
root.appendChild(item2);
root.appendChild(item3);
root.appendChild(btn);



function generate(){
	if ((textbox.value || textbox2.value || textbox3.value )!=="") {
		let space = document.createElement("SPAN");
		let sentence = document.createElement('p')
		sentence.innerText = textbox.value + " is studying" + textbox2.value + " at " + textbox3.value + " .";
		
		space.appendChild(sentence);
		root.appendChild(space);
		space.appendChild(btn);
		
	}
}

btn.addEventListener('click',generate);