#!/usr/bin/node
//  prints a square

const number = process.argv[2];
const size = parseInt(number);

if (!isNaN(size)) {
    for (let i = 0; i < size; i++) {
        console.log('X'.repeat(size));
      }
  } else {
    console.log('Missing size');
  }
  