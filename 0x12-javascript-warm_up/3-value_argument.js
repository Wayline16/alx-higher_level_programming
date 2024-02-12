#!/usr/bin/node
// Print if argument is found

if (process.argv[2] === undefined) {
    console.log('No argument');
  } else {
    console.log(process.argv[2]);
  }