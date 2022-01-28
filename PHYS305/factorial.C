// defines recursive function that computes factorial of non-negative integer
#include <iostream>
#include <iomanip>
using namespace std;

/*
Factory is a recursive function used to calculate the factorial of a number.
long int a - the number of which the factorial is to be made
returns 1 if it reaches the end of the factorial
        further rrecursion to continue calculating factorial
 */

long int factory(long int a)
{
  if (a <= 1){ // checks for end of recursion
    return 1;
  }
  else {
    return a * factory(a - 1); // calls self to continue calculation factorial
  }
}

/*
Main function
 */
int main() 
{
  long int a; // declaration of variable to be set by user input
  
  cout << "What number do you want a factorial of? " << endl;
  cin >> a; // sets varaible to the inputted number

  long int fact = factory(a); // variable declared as a call to the function
                              // factroy, has the value of the factorial of a
  cout << fact << endl;
}
