#include <iostream>
#include <string>
using namespace std;
int main (){
    string name;
    cout << "Enter your GF name: ";
    cin >> name;
    int num = (name[0] - 'A' + 1) + 900;
    cout << "The number that represent the first letter of her name: " << num <<endl;
    return 0;
}