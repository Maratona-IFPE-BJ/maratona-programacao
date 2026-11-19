#include <iostream>
#include <vector>

using namespace std;

int main (){
    int valor;
    cin >> valor;

    vector <int> vetor;
    vetor.push_back(valor);

    for( int i = 0; i < 9; i++) {
        int novo_valor = vetor.back() * 2;
        vetor.push_back(novo_valor);
    }

    for (int i = 0; i < vetor.size(); i++) {
        cout <<"N["<< i<< "]" << " = "<< vetor[i] << endl;
    }


    return 0;
}