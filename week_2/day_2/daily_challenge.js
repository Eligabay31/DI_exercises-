// daily challenge day_2:
// part1:
var array = ["banana","apples","oranges","blueberries"];
array.shift();
console.log(array);
array.sort();
console.log(array);
array.push("kiwi");
console.log(array);
array.shift();
console.log(array);
array.reverse();
console.log(array);
// ------------------
// part2:
var array2 = ["banana",["apples",["oranges"],"blueberries"]];
console.log(array2[0][0][0]);