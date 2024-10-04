#include <iostream>
#include <string>
using namespace std;

class Ville {
 public:
  string nom;
  int code_postal;
  int prixm2;
  //===
  Ville(string n, int cp, int pm2) {
    nom = n;
    code_postal = cp;
    prixm2 = pm2;
  }
  //=== fonction qui remplace la sortie ostream d'une classe
  // on definit l'operateur sur une autre classe, on est autorisé a la modifier
  // meme si on ne crée pas la clase
  friend ostream& operator<<(ostream& out, const Ville& ville) {
    return out << ville.nom << ", " << ville.code_postal;
  }
  //===
  /*auto str() -> string {
    return (Nom + "," + to_string(code_postal));
  }*/
};

auto main() -> int {
  auto ville = Ville{"Toulouse", 31400, 1200};
  cout << ville << "\n";
  return 0;
}
