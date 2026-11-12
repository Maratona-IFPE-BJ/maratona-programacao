#include <iostream>
#include <string>
#include <map>
#include <iomanip>

int main() {
    int n;
    std::cin >> n;

    std::cout << std::fixed << std::setprecision(2);

    for (int i = 0; i < n; i++) {
        int m;
        std::cin >> m;

        std::map<std::string, double> precos{};

        for (int j = 0; j < m; j++) {
            std::string produto;
            double valor;
            std::cin >> produto >> valor;
            precos[produto] = valor;
        }

        int p;
        std::cin >> p;
        double total = 0.0;

        for (int j = 0; j < p; j++) {
            std::string produto;
            int qtd;
            std::cin >> produto >> qtd;
            total += precos[produto] * qtd;
        }

        std::cout << "R$ " << total << "\n";
    }

    return 0;
}