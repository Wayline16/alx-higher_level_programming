#!/usr/bin/node
// Added the constructor to the Rectangle class
class Rectangle {
    constructor(w,h){
        if (w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }
}
module.exports = Rectangle;
