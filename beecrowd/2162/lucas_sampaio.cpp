#include <iostream>
#include <vector>
using namespace std;

int main() { 

    int n;
    cin >> n;

    vector<int> medidas(n);

    for (int i = 0; i < n; i++) {
        cin >> medidas[i];
    }

    bool resultado = true;

    if(medidas[0] == medidas[1])
        resultado = false;

    for(int i=1; i < n-1; i++){
        if (!((medidas[i-1] < medidas[i] && medidas[i] > medidas[i+1]) || 
            (medidas[i-1] > medidas[i] && medidas[i] < medidas[i+1]))){
            resultado = false;
            break;
        } 
    }

    if(resultado)
        cout << 1 << endl;
    else
        cout << 0 << endl;      

    return 0;
}
