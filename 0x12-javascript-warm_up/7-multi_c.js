#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop

const number = process.argv[2];
const x = parseInt(number);

if (!isNaN(x)) {
    for (let i = 0; i < x; i++) {
        console.log('C is fun');
      }
  } else {
    console.log('Missing number of occurrences');
  }
