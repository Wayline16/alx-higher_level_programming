#!/usr/bin/node
// Print if argument is found

if (process.argv.length === 2) {
    console.log('No argument');
  } else if (process.argv.length > 2) {
    console.log('Argument found');
  }
  