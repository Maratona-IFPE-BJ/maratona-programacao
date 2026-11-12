#include <iostream>
#include <vector>
#include <iomanip>

int main(){
    std::vector<float> lista{};
    float a;

    for(int i = 0; i < 100; i++){
        std::cin >> a;
        lista.push_back(a);
    }

    std::cout << std::fixed << std::setprecision(1);

    for (int i = 0; i < 100; i++) {
        if (lista[i] <= 10.0) {
            std::cout << "A[" << i << "] = " << lista[i] << "\n";
        }
    }

    return 0;
}