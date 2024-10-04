#include <cpr/cpr.h>  //gestion communication

#include <iostream>
#include <nlohmann/json.hpp>  // convertisseur json / classe
#include <string>
using json = nlohmann::json;
using namespace std;

class Ville {
 public:
  string nom;
  int code_postal;
  int prixm2;
  //===
  Ville(string n, int cp, int pm2) {  // constructeur manuel
    nom = n;
    code_postal = cp;
    prixm2 = pm2;
  }
  Ville(json data) {  // constructeur json

    // Ville(data["nom"], data["code_postal"], data["prixm2"]);
    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];  // on recupere les elements du json pour les
                              // reintegrer dans notre classe ville
  }
  Ville(string url) {  // constructeur a partir de l'url
    json data = json::parse(cpr::Get(cpr::Url{url}).text);
    // Ville(data["nom"], data["code_postal"], data["prixm2"]);
    /// r.text : text string du json, qu'on convertie en veritable json avec
    /// parse
    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];  // on recupere les elements du json pour les
                              // reintegrer dans notre classe ville
  }

  Ville(int num) {  // constructeur a partir du numero de la villle
    json data = json::parse(
        cpr::Get(cpr::Url{"http://localhost:8000/ville/" + to_string(num)})
            .text);
    // Ville(data["nom"], data["code_postal"], data["prixm2"]);
    /// r.text : text string du json, qu'on convertie en veritable json avec
    /// parse
    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];  // on recupere les elements du json pour les
                              // reintegrer dans notre classe ville
  }
  //=== fonction qui remplace la sortie ostream d'une classe
  // on definit l'operateur sur une autre classe, on est autorisé a la modifier
  // meme si on ne crée pas la clase
  friend ostream& operator<<(ostream& out, const Ville& ville) {
    return out << ville.nom << ", " << ville.code_postal;
  }
  //
  /*auto str() -> string {
    return (Nom + "," + to_string(code_postal));
  }*/
};

class Local {
 public:
  string nom;
  int code_postal;
  int prixm2;
  //===
  Local(string n, int cp, int pm2) {  // constructeur manuel
    nom = n;
    code_postal = cp;
    prixm2 = pm2;
  }
  Local(json data) {  // constructeur json

    // Ville(data["nom"], data["code_postal"], data["prixm2"]);
    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];  // on recupere les elements du json pour les
                              // reintegrer dans notre classe ville
  }
  Local(string url) {  // constructeur a partir de l'url
    json data = json::parse(cpr::Get(cpr::Url{url}).text);

    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];  // on recupere les elements du json pour les
                              // reintegrer dans notre classe ville
  }

  Local(int num) {  // constructeur a partir du numero
    json data = json::parse(
        cpr::Get(cpr::Url{"http://localhost:8000/ville/" + to_string(num)})
            .text);

    nom = data["nom"];
    code_postal = data["code_postal"];
    prixm2 = data["prixm2"];
    /
  }
  //=== fonction qui remplace la sortie ostream d'une classe

  friend ostream& operator<<(ostream& out, const Local& p) {
    return out << p.nom << ", " << p.code_postal;
  }
};

auto main() -> int {
  /* // Main de de test pour recupeperation
    json data;
    auto ville = Ville{"Toulouse", 31400, 1200};
    cout << ville << "\n";

    cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/ville/1"});
                     // 200
    data = json::parse(r.text);          // r.text : text string du json, qu'on
    convertie en veritable json avec parse auto labege =
    Ville{data["nom"],data["code_postal"],data["prixm2"]} ; // on recupere les
    elements du json pour les reintegrer dans notre classe ville cout << labege
    << "\n";
  */
  /*
  string url = "http://localhost:8000/ville/2";
  auto ville = Ville{url};// constructeur par url
  cout << ville << "\n";
  // resultat attendu : Baziege, 31450
  */

  auto ville = Ville{3};
  cout << ville << "\n";  // constructeur par numero de ville
  // resultat attendu : Mascara, 29000

  return 0;
}
