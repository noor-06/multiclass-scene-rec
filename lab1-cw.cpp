#include <iostream> /* header file; input/output stream */
#include <string> /*  */
using namespace std; /* std once instead of using std:: before every statement */

/* >> is a concatenation operator
    main function can be created without classes
    endl or \n for new line
    cout for output
    cin for input
    declaring a string, the constant must be all lowercase "string"
*/

/* int main(){

    int a = 10;
    int b = 20;

    cout<<a<<" + "<<b<<" = "<<(a+b)<<endl;
    
    return 0;
} */

int main(){
    int a, b;

    cout<<"Enter a number: ";
    cin>>a;
    cout<<"Enter a number: ";
    cin>>b;

    cout<<a<<" + "<<b<<" = "<<(a+b);

    return 0;
}