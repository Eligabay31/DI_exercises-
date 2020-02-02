// 1
let paragraphs = document.getElementsByTagName('p');
console.log(paragraphs);

for (let i=0; i < paragraphs.length; i++) {

paragraphs[i].classList.add('para_article');

}
console.log(paragraphs);

// ------------------------ 
// 2
 paragraphs[paragraphs.length - 1].remove();
console.log(paragraphs);

