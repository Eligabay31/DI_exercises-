const MYWORD = 'Javascript';
const NUMOF = 10;
let wordArr = MYWORD.split('');
let arrToShow = [];
for (var i = 0; i < wordArr.length; i++) {
  if(i == 0 || i == wordArr.length-1){
    arrToShow.push(wordArr[i]);
  }
  else {
    arrToShow.push('*');
  }
}
alert(arrToShow.join(''));
for (let i = 0; i < 10; i++) {
  let g = prompt('Please enter a something');
  if(g.length <= 1){
    for (let j = 0; j < wordArr.length; j++) {
      let gg = g.toLowerCase();
      let ww = wordArr[j].toLowerCase();
      if (wordArr[j].toLowerCase() == g.toLowerCase()) {
        arrToShow[j] = wordArr[j];
      }
    }
    console.log(arrToShow.join(''));
    if(MYWORD == arrToShow.join('')){
      console.log('WON');
      break;
    }
  }
}