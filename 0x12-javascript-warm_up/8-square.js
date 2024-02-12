#!/usr/bin/node
// prints 3 lines: (like 1-multi_languages.js) but by
// using an array of string and a loop

const number = process.argv[2];
const size = parseInt(number);

if (!isNaN(size)) {
    for (let i = 0; i < size; i++) {
        console.log('X'.repeat(size));
      }
  } else {
    console.log('Missing size');
  }