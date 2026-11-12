#include <iostream>
#include <vector>

int main(){
    std::vector<int> lista{};
    int x;

    for(int i = 0; i < 10; i++){
        std::cin >> x;

        if (x <= 0){
            lista.push_back(1);
        }
        else {
            lista.push_back(x);
        }
    }

    for (int i = 0; i < 10; i++) {
        std::cout << "X[" << i << "] = " << lista[i] << "\n";

    }
}