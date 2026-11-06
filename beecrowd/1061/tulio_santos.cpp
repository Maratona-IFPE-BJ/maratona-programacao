#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double salario;
    cin >> salario;

    double s_isento = 2000.00;
    double primeira_faixa = 1000.00;

    if (salario <= s_isento) {
        cout << "Isento" << endl;
    } else {
        cout << fixed << setprecision(2);
        if (salario <= 3000.00) {
            double diferenca = salario - s_isento;
            double imposto = diferenca * 0.08;
            cout << "R$ " << imposto << endl;
        } else if (salario <= 4500.00) {
            double diferenca = salario - s_isento;
            double segunda_faixa = diferenca - primeira_faixa;
            double imposto = (primeira_faixa * 0.08) + (segunda_faixa * 0.18);
            cout << "R$ " << imposto << endl;
        } else {
            double imposto = (primeira_faixa * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28);
            cout << "R$ " << imposto << endl;
        }
    }

    return 0;
}