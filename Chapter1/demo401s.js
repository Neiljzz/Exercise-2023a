console.log("Start running")

console.log("=== problem 1 ===")
s = 0
for (var i=0; i<10; i++)
{
    v = i + 1
    s = s + v
}

console.log(s)


console.log("=== problem 2 ===")
s = 0
for (var i=0; i<100; i++){
    v = i + 1
    s = s + v
}
console.log(s)

console.log("=== problem 3 ===")
s = 0
for (var i=0; i<100; i++){
    v = 1/(i+1)
    s = s + v
}
console.log(s)

console.log("=== problem 4 ===")
var s = " ";
for (var i = 0; i < 5; i++){
    var v = " ".repeat(4 - i);
    s = v + "A".repeat(i * 2 + 1);
    console.log(s);
    }

console.log("=== problem 5 ===")
var s = " ";
for (var i = 0; i < 5; i++){
    var v = "A".repeat(5-i);
    var c = " ".repeat(3);
    s = v + c + "A".repeat(i+1);
    console.log(s);
    }
