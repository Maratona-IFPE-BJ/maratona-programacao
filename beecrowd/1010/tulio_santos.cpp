#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    int cod_1, quant_1, cod_2, quant_2;
    double valor_unit_1, valor_unit_2;

    cin >> cod_1 >> quant_1 >> valor_unit_1;
    cin >> cod_2 >> quant_2 >> valor_unit_2;

    double resultado = (quant_1 * valor_unit_1) + (quant_2 * valor_unit_2);

    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << resultado << endl;

    return 0;
}