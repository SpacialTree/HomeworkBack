// HW Problem 1: Range of type int and double

#include <iostream>
#include <math.h>
using namespace std;

/*
Main function
Computes and prints out successive powers of 2, with exponents
ranging from 1 to 1024.
*/
int main() 
{
  double val=1.; // starting value, 2^0
  for (double i = 1.; i<1025.; i++)
    {
      val *= 2.; // sets val to itself times 2
      cout << val << ", ";
    }
  cout << endl;
}
