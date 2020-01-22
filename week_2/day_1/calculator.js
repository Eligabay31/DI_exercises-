var number1;
var number2;
var sign;

function my_f(num){
	if (num != "+" && num != "-" && num != "/") {
		if (isNaN(number1)){
			number1=num;
		} else{
			number2=num;
		}
	}else{
		switch(num){
			case "+":
			sign=num;
			break;
			
			case "-":
			sign=num;
			break;
			
			case "/":
			sign=num;
			break;

		}
	}
}

function calc(){
	var ans;
	switch (sign){
		case "+":
		ans=number1+number2;
		break;

		case "-":
		ans=number1-number2;
		break;

		case "/":
		ans=number1/number2;
		break;
	}

	alert('this is your answer'+ans);

}








