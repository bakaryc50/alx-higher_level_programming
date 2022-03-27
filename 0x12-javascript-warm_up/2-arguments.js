#!/usr/bin/node
// script that prints message depending of the number of arguments passed
const myMessage = ['No argument', 'Argument found', 'Arguments found'];
console.log(myMessage[Math.min(process.argv.length - 2, 2)]);
