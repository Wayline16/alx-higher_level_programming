#!/usr/bin/node

exports.esrever = function (list){
    const reversed = []
    counter = 0;
    for (i = list.length - 1; i >= 0; i--){
        reversed.push(list[i]);
    }
    return (reversed);
}
