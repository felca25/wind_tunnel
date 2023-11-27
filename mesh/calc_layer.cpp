#include<iostream>
#include<iomanip>
#include<cmath>
#include <string>
#include <typeinfo>

using namespace std;


string cont;
int runs = 0;
bool flag = true;

int main(){
    while (flag && runs < 10){
        int N;
        double h;
        double G;
        
        cout << "\nCalculate the total thickness of a layered mesh\n" << endl;

        while (cout << "Enter the number of layers: " && !(cin >> N)){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Invalid input. Try again.\n";
        }
        while (cout << "Enter the thickness of the first layer: " && !(cin >> h)){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max());
            cout << "Invalid input. Try again.\n";
        }
        while ((cout << "Enter the growth ratio: " && !(cin >> G))){
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max());
            cout << "Invalid input. Try again.\n";
        }

        cout << "\n";

        cout << "The total thickness is " << setprecision(4) << scientific
        << h* (1-pow(G,N))/(1-G) << " m\n\n";

        cout << "Done!\n";

        while (cont != "n" && cont != "y"){
            cout << "Continue trying new layer parameters? (y/n)\n";
            cin >> cont;
            if (cont == "n"){flag = false;}
            else if (cont == "y"){flag = true;}
            else {cout << "Invalid input. Try again.\n";}
        }
    }
    return 0;
}