#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> lista{};
    for (int i = 0; i < n; i++) {
        int val;
        std::cin >> val;
        lista.push_back(val);
    }

    int resultado = 1;

    if (n == 2) {
        if (lista[0] == lista[1]) {
            resultado = 0;
        }
    } else {
        for (int i = 1; i < n - 1; i++) {
            int anterior = lista[i - 1];
            int atual = lista[i];
            int proximo = lista[i + 1];

            if (atual > anterior && atual > proximo) {
                // Equivalente ao pass (não faz nada)
            } else if (atual < anterior && atual < proximo) {
                // Equivalente ao pass (não faz nada)
            } else {
                resultado = 0;
                break;
            }
        }
    }

    std::cout << resultado << "\n";

    return 0;
}