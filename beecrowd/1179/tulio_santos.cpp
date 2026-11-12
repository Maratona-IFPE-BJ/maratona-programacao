#include <iostream>
#include <vector>

int main() {
    std::vector<int> par{};
    std::vector<int> impar{};
    int i = 0;
    int entrada;

    while (i < 15) {
        std::cin >> entrada;

        if (entrada % 2 == 0) {
            if (par.size() == 5) {
                for (int r = 0; r < 5; r++) {
                    std::cout << "par[" << r << "] = " << par[r] << "\n";
                }
                par.clear();
            }
            par.push_back(entrada);
        } else {
            if (impar.size() == 5) {
                for (int j = 0; j < 5; j++) {
                    std::cout << "impar[" << j << "] = " << impar[j] << "\n";
                }
                impar.clear();
            }
            impar.push_back(entrada);
        }

        i++;
    }

    for (int k = 0; k < impar.size(); k++) {
        std::cout << "impar[" << k << "] = " << impar[k] << "\n";
    }

    for (int l = 0; l < par.size(); l++) {
        std::cout << "par[" << l << "] = " << par[l] << "\n";
    }

    return 0;
}