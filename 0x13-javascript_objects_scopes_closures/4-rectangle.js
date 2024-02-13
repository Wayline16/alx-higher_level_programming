#!/usr/bin/node
// Added the constructor to the Rectangle class
class Rectangle {
    constructor(w,h){
        if (w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }

    print () {
        for (let i = 0; i < this.height; i++) {
            console.log('X'.repeat(this.width));
        }
    }

    rotate () {
        const swap = this.width;
        this.width = this.height;
        this.height = swap;
    }
    
    double () {
        this.height = this.height * 2;
        this.width = this.width * 2;
    }
}
module.exports = Rectangle;
