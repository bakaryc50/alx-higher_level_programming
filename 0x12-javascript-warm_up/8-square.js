#!/usr/bin/node
// script that prints a square of height x
const myX = parseInt(process.argv[2]);
if (Number.isNaN(myX)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myX; i += 1) {
    console.log('X'.repeat(myX));
  }
}
