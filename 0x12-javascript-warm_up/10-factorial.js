#!/usr/bin/node
//  factorial

function factorial (a) {
    let total = 1;
    for (let i = 1; i <= a; i++) {
        total = total * i;
    }
    return total;
  }

  console.log(factorial(process.argv[2]));
