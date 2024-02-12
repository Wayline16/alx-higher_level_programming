#!/usr/bin/node
// Print two argument if found

const argument = process.argv[2];


const number = parseInt(argument);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
