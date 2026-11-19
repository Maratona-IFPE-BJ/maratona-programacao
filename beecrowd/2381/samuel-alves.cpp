#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main(){

    int numAlunos, numSorteado;
    cin >> numAlunos >> numSorteado;
    

    vector <string> alunos;


    for (int i = 0; i < numAlunos; i++){
        string nomes;
        cin >> nomes;
        alunos.push_back(nomes);
    }

    sort(alunos.begin(), alunos.end());

    cout << alunos[numSorteado -1] << endl;

    return 0;
}