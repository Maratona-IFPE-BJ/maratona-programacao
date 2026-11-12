#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> pares{};
    std::vector<int> impares{};

    for (int i = 0; i < n; i++) {
        int num;
        std::cin >> num;

        if (num % 2 == 0) {
            pares.push_back(num);
        } else {
            impares.push_back(num);
        }
    }


    std::sort(pares.begin(), pares.end());

    std::sort(impares.rbegin(), impares.rend());

    for (int j = 0; j < pares.size(); j++) {
        std::cout << pares[j] << "\n";
    }

    for (int k = 0; k < impares.size(); k++) {
        std::cout << impares[k] << "\n";
    }

    return 0;
}