const root=document.getElementById('root');

let btn = document.createElement('button');
btn.innerHTML='MOVE!';


let box = document.createElement('div');
	box.style.backgroundColor = 'red';
	box.style.width='50px';
	box.style.height='50px';
	box.style.position = 'fixed';
	box.setAttribute('draggable','true');

box.addEventListener('dragend', function(event){
	let x = event.clientX;
	let y = event.clientY;
			box.style.left = x + 'px';
			box.style.top = y + 'px';
			console.log(x,y);
})

// btn.addEventListener('click',function(){   
//   var pos = 0;
//   var id = setInterval(frame, 5);
//   function frame() {
//     if (pos == 350) {
//       clearInterval(id);
//     } else {
//       pos++; 
//       elem.style.top = pos + "px"; 
//       elem.style.left = pos + "px"; 
//     }
//   }
// })


root.appendChild(btn);
root.appendChild(box);









// document.write('hello');