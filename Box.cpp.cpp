//OOP in CPP
//created a class box 
//computed its volume using method of the class
#include<stdio.h>
#include<iostream>
using namespace std;
class Box
{ 
    public:
    double length;
    double bredth;
    double height;

};
int main(){
    Box Box1;
    Box Box2;
double volume = 0.0;
    //box 1 specifications
    Box1.length = 6.0;
    Box1.bredth = 7.0;
    Box1.height = 5.0;
    //box 2 specification
    Box2.height = 10.0;
    Box2.length= 12.0;
    Box2.bredth = 14.0;

// volume of box 1 
volume = Box1.length*Box1.bredth*Box1.height;

cout<<"volume of box 1 :"<<volume<<" cm2"<<endl;
// volume of box 2

volume = Box2.length*Box2.bredth*Box2.height;
cout<<"Volume of box 2: "<<volume<<" cm2";
}