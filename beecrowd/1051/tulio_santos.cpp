#include <iostream>
#include <string>

using namespace std;

int main() {
    string lixo;
    int dia_inicio, hora_inicio, min_inicio, seg_inicio;
    int dia_fim, hora_fim, min_fim, seg_fim;

    cin >> lixo >> dia_inicio;
    cin >> hora_inicio >> lixo >> min_inicio >> lixo >> seg_inicio;

    cin >> lixo >> dia_fim;
    cin >> hora_fim >> lixo >> min_fim >> lixo >> seg_fim;

    long segundos_iniciais = (dia_inicio * 86400) + (hora_inicio * 3600) + (min_inicio * 60) + seg_inicio;
    long segundos_finais = (dia_fim * 86400) + (hora_fim * 3600) + (min_fim * 60) + seg_fim;

    long diferenca = segundos_finais - segundos_iniciais;

    int dias = diferenca / 86400;
    diferenca = diferenca % 86400;

    int horas = diferenca / 3600;
    diferenca = diferenca % 3600;

    int minutos = diferenca / 60;
    diferenca = diferenca % 60;

    int segundos = diferenca;

    cout << dias << " dia(s)" << endl;
    cout << horas << " hora(s)" << endl;
    cout << minutos << " minuto(s)" << endl;
    cout << segundos << " segundo(s)" << endl;

    return 0;
}