const root = document.getElementById('root');

let btn = document.createElement('button');

let outerBox = document.createElement('div');
let innerBox = document.createElement('div');

outerBox.classList.add('container');
innerBox.classList.add('animate');

innerBox.setAttribute('id','animate');


// function setTime(){
// 	setTimeout(function(){
// 		console.log('hello');
// 	},3000)
// }
// let id;
// function setInter(){
// 	id= setInterval(function(){
// 		console.log('hhhhhh');
// 	},1000);
// }

// function clearInter(){
// 	clearInterval(id);
// }




btn.innerHTML='Click Me!'



root.appendChild(btn);
outerBox.appendChild(innerBox);
root.appendChild(outerBox);
