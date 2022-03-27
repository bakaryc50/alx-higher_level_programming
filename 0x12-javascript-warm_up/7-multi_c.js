#!/usr/bin/node
// script that that prints x times “C is fun”
const myX = parseInt(process.argv[2]);
if (Number.isNaN(myX)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myX; i++) {
    console.log('C is fun');
  }
}
