
let num1 = Number( prompt('please enter a number'));
console.log(num1);

let sign = prompt('choose + or -');
console.log(sign);

let num2 = Number(prompt('please enter a number'));
console.log(num2);

if (sign === '-') {
	alert(num1-num2);
}
else if (sign === '+'){
	alert(num1+num2);
}

else{
	alert('you did not enter correct values')
}

switch (sign){
	case '+':
	alert(num1)
 }
// let x = (sign==='+') ? (num1+num2) : (num1-num2);
// alert(x);

// if (sign==='+' || sign !='') {
	
// }

