#include <iostream>
#include <iomanip>
using namespace std;

/*
Recursive function factory from factorial.C
Returns factorial of inputted value.
 */
long int factory(long int a)
{
  if (a <= 1){
    return 1;
  }
  else {
    return a * factory(a - 1);
  }
}

/*
Main function
Used for estimating the value of e by calculating sequential values of its expansion
 */
int main()
{
  double tol;
  cout << "What level of accuracy do you want? " << endl;
  cin >> tol; // value must be along the lines of 1.e-10
  int n;
  double enow=2.5, ebe=2.0; // as the loop starts at n=3, these values are needed to be the initial values in the expansion.
  for(n=3;n<1000000;n++){
    ebe = enow; 
    enow = enow + 1. / factory(n);
    if((enow-ebe)/enow < tol) // compares values to tolerance value and breaks the loop if the precision of enow is suffifient. 
      {
	break;
      }
  }
  cout << "The value of e is approx: " << setprecision(16) << enow << endl;
  cout << "Number of expansion terms: " << n << endl;
}
