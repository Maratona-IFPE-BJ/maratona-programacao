#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main() {
    string linha;

    while (getline(cin, linha)) {
        bool maiuscula = true;
        string linha_final = "";

        for (char c : linha) {
            if (c == ' ') {
                linha_final += c;
            } else {
                if (maiuscula) {
                    linha_final += toupper(c);
                    maiuscula = false;
                } else {
                    linha_final += tolower(c);
                    maiuscula = true;
                }
            }
        }
        cout << linha_final << endl;
    }

    return 0;
}
