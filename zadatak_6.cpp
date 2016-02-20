#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>

#define PI 3.14159265

using namespace std;

float x,y,z,i,j,k, pom;

void unos(){
    cout << "Unesite koordinate koje zelite transformirati: " << endl;
    cout << "\tx = ";
    cin >> x;
    cout << "\ty = ";
    cin >> y;
    cout << "\tz = ";
    cin >> z;
    }

void translacija(){
    unos();
    cout << "Unesite koordinate jedinicnog vektora v" << endl;
    cout << "\ti = ";
    cin >> i;
    cout << "\tj = ";
    cin >> j;
    cout << "\tk = ";
    cin >> k;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x+i << ", " << y+j << ", " << z+k << ")" << endl;
}

void rotacija_x(){
    unos();
    float kut, co, si;
    cout << "Za koliko stupnjeva zelite rotirati tocku: ";
    cin >> kut;

    if      (kut == 180) si=0;
    else    si = sin(kut*PI/180);
    if      (kut == 90) co = 0;
    else    co = cos(kut*PI/180);

    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << y*co-z*si<< ", " << y*si+z*co<< ")" << endl;
}

void rotacija_y(){
    unos();
    float kut, co, si;
    cout << "Za koliko stupnjeva zelite rotirati tocku: ";
    cin >> kut;

    if      (kut == 180) si=0;
    else    si = sin(kut*PI/180);
    if      (kut == 90) co = 0;
    else    co = cos(kut*PI/180);

    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << z*si+x*co << ", " << y << ", " << z*co-x*si<< ")" << endl;
}

void rotacija_z(){
    unos();
    float kut, co, si;
    cout << "Za koliko stupnjeva zelite rotirati tocku: ";
    cin >> kut;

    if      (kut == 180) si=0;
    else    si = sin(kut*PI/180);
    if      (kut == 90) co = 0;
    else    co = cos(kut*PI/180);

    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x*co-y*si << ", " << x*si+y*co << ", " << z << ")" << endl;
}

void homotetija_ishodiste(){
    unos();
    cout << "Unesite faktor k:" << endl;
    cout << "\tk = ";
    cin >> pom;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x*pom << ", " << y*pom << ", " << z*pom << ")" << endl;
}

void homotetija_tocka(){
    unos();
    cout << "Unesite faktor k:" << endl;
    cout << "\tk = ";
    cin >> pom;
    cout << "Unesite koordinate tocke za homotetiju:" << endl;
    cout << "\tx = ";
    cin >> i;
    cout << "\ty = ";
    cin >> j;
    cout << "\tz = ";
    cin >> k;
    cout << "Unesite koordinate tocke:" << endl;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << (x-i)*pom+i << ", " << (y-j)*pom+j << ", " << (y-k)*pom+k << ")" << endl;
}

void zrcaljenje_xy(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << y << ", " << -z << ")" << endl;
}

void zrcaljenje_xz(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << -y << ", " << z << ")" << endl;
}

void zrcaljenje_yz(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << -x << ", " << y << ", " << z << ")" << endl;
}

void zrcaljenje_x(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << -y << ", " << -z << ")" << endl;
}

void zrcaljenje_y(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << -x << ", " << y << ", " << -z << ")" << endl;
}

void zrcaljenje_z(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << -x << ", " << -y << ", " << z << ")" << endl;
}

void rastezanje(){
    unos();
    cout << "Unesite faktore rastezanja: " << endl;
    cout << "\tkx = ";
    cin >> i;
    cout << "\tky = ";
    cin >> j;
    cout << "\tkz = ";
    cin >> k;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << i*x << ", " << j*y << ", " << k*z << ")" << endl;
}

void cent_simetrija_ishodiste(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << -x << ", " << -y << ", " << -z << ")" << endl;
    }

void cent_simetrija_tocka(){
    unos();
    cout << "Unesite tocku simetrije: " << endl;
    cout << "\tx = ";
    cin >> i;
    cout << "\ty = ";
    cin >> j;
    cout << "\tz = ";
    cin >> k;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << -(x-i)+i << ", " << -(y-j)+j << ", " << -(z-k)+k << ")" << endl;
}

void orto_projekcija_x(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << 0 << ", " << 0 << ")" << endl;
    }

void orto_projekcija_y(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << 0 << ", " << y << ", " << 0 << ")" << endl;
    }

void orto_projekcija_z(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << 0 << ", " << 0 << ", " << z << ")" << endl;
    }

void orto_projekcija_xy(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << y << ", " << 0 << ")" << endl;
    }

void orto_projekcija_xz(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << x << ", " << 0 << ", " << z << ")" << endl;
    }

void orto_projekcija_yz(){
    unos();
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << 0 << ", " << y << ", " << z << ")" << endl;
    }

void smicanje(){
   bool ispravno=0;
    unos();
    do{
        cout << "\talfa = ";
        cin >> i;
        cout << "\tbeta = ";
        cin >> j;
        cout << "\tgama = ";
        cin >> k;
        if (i==90 || j==90 || k ==90){
            cout <<  "Kut ne moze biti 90 stupnjeva!" << endl;
            ispravno = 0;
            }
        else ispravno = 1;
    }while(ispravno == 0);

    float tana,tanb,tanc,a,b,c;
    tana = tan(i*PI/180);
    tanb = tan(j*PI/180);
    tanc = tan(k*PI/180);
    a=x+y*tana+z*tana;
    b=x*tanb+y+z*tanb;
    c=x*tanc+y*tanc+z;
    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << a << ", " << b << ", " << c << ")" << endl;
}

void rotacija_pravac(){
    unos();
    float kut,px, py, pz, sinus,kosinus,a,b,c,norm;
    cout << "Unesite koordinate vektora v" << endl;

    do{
        cout << "\tpx = ";
        cin >> px;
        cout << "\tpy = ";
        cin >> py;
        cout << "\tpz = ";
        cin >> pz;
        if ((px==0 && py==0 && pz==0)||(px != 1 && px != 0) || (py != 1 && py != 0) || (pz != 1 && pz != 0))
            cout << "Koordinate vektora moraju biti 1 ili 0 (ne smiju biti sve 0)!" << endl;
    }while((px==0 && py==0 && pz==0)||(px != 1 && px != 0) || (py != 1 && py != 0) || (pz != 1 && pz != 0));
    cout << "Za koliko stupnjeva zelite rotirati tocku: ";
    cin >> kut;

    if      (kut == 180) sinus=0;
    else    sinus = sin(kut*PI/180);
    if      (kut == 90) kosinus = 0;
    else    kosinus = cos(kut*PI/180);

    norm = sqrt(px*px+py*py+pz*pz);
    px=px/norm;
    py=py/norm;
    pz=pz/norm;

    a=x*((1-kosinus)*(px*px)+kosinus)+y*((px*py)*(1-kosinus)-pz*sinus)+z*((pz*px)*(1-kosinus)+(py*sinus));
    b=x*((px*py)*(1-kosinus)+(pz*sinus))+y*((1-kosinus)*(py*py)+kosinus)+z*((py*pz)*(1-kosinus)-(px*sinus));
    c=x*((pz*px)*(1-kosinus)-(pz*sinus))+y*((py*pz)*(1-kosinus)+(px*sinus))+z*((1-kosinus)*(pz*pz)+kosinus);

    cout << "---------------------------------" << endl;
    cout << "Koordinate nove tocke su: (" << a << ", " << b << ", " << c << ")" << endl;
}

int main(){
    int izbor;
    char dn;
    do{
    system ("cls");
    cout << "\tIZBORNIK" << endl;
    cout << "---------------------------------------------" << endl;
    cout << "1) Translacija za vektor" << endl;
    cout << "2) Rotacija oko osi x" << endl;
    cout << "3) Rotacija oko osi y" << endl;
    cout << "4) Rotacija oko osi z" << endl;
    cout << "5) Homotetija za faktor k sa centrom u ishodistu" << endl;
    cout << "6) Rotacija oko proizvoljnog pravca" << endl;
    cout << "7) Homotetija za faktor k sa centrom u tocki" << endl;
    cout << "8) Zrcaljenje s obzirom na xy-ravninu" << endl;
    cout << "9) Zrcaljenje s obzirom na xz-ravninu" << endl;
    cout << "10) Zrcaljenje s obzirom na yz-ravninu" << endl;
    cout << "11) Zrcaljenje s obzirom na os x" << endl;
    cout << "12) Zrcaljenje s obzirom na os y" << endl;
    cout << "13) Zrcaljenje s obzirom na os z" << endl;
    cout << "14) Rastezanje duz koordinatnih osi sa faktorima kx, ky kz" << endl;
    cout << "15) Centralna simetrija sa centrom u ishodistu" << endl;
    cout << "16) Centralna simetrija sa centrom u tocku" << endl;
    cout << "17) Ortogonalna projekcija na os x" << endl;
    cout << "18) Ortogonalna projekcija na os y" << endl;
    cout << "19) Ortogonalna projekcija na os z" << endl;
    cout << "20) Ortogonalna projekcija na xy-ravninu" << endl;
    cout << "21) Ortogonalna projekcija na xz-ravninu" << endl;
    cout << "22) Ortogonalna projekcija na yz-ravninu" << endl;
    cout << "23) Smicanje" << endl;
    cout << "---------------------------------------------" << endl;
    cout << "IZBOR: (1-23)";
    cin >> izbor;

    system ("cls");
    switch (izbor){
        case 1:
            cout << "1) Translacija za vektor" << endl;
            cout << "---------------------------------------------" << endl;
            translacija();
            break;
        case 2:
            cout << "2) Rotacija oko osi x" << endl;
            cout << "---------------------------------------------" << endl;
            rotacija_x();
            break;
        case 3:
            cout << "3) Rotacija oko osi y" << endl;
            cout << "---------------------------------------------" << endl;
            rotacija_y();
            break;
        case 4:
            cout << "4) Rotacija oko osi z" << endl;
            cout << "---------------------------------------------" << endl;
            rotacija_z();
            break;
        case 5:
            cout << "5) Homotetija za faktor k sa centrom u ishodistu" << endl;
            cout << "---------------------------------------------" << endl;
            homotetija_ishodiste();
            break;
        case 6:
            cout << "6) Rotacija oko proizvoljnog pravca" << endl;
            cout << "---------------------------------------------" << endl;
            rotacija_pravac();
            break;
        case 7:
            cout << "7) Homotetija za faktor k sa centrom u tocki" << endl;
            cout << "---------------------------------------------" << endl;
            homotetija_tocka();
            break;
        case 8:
            cout << "8) Zrcaljenje s obzirom na xy-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_xy();
            break;
        case 9:
            cout << "9) Zrcaljenje s obzirom na xz-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_xz();
            break;
        case 10:
            cout << "10) Zrcaljenje s obzirom na yz-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_yz();
            break;
        case 11:
            cout << "11) Zrcaljenje s obzirom na os x" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_x();
            break;
        case 12:
            cout << "12) Zrcaljenje s obzirom na os y" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_y();
            break;
        case 13:
            cout << "13) Zrcaljenje s obzirom na os z" << endl;
            cout << "---------------------------------------------" << endl;
            zrcaljenje_z();
            break;
        case 14:
            cout << "14) Rastezanje duz koordinatnih osi sa faktorima kx, ky kz" << endl;
            cout << "---------------------------------------------" << endl;
            rastezanje();
            break;
        case 15:
            cout << "15) Centralna simetrija sa centrom u ishodistu" << endl;
            cout << "---------------------------------------------" << endl;
            cent_simetrija_ishodiste();
            break;
        case 16:
            cout << "16) Centralna simetrija sa centrom u tocku" << endl;
            cout << "---------------------------------------------" << endl;
            cent_simetrija_tocka();
            break;
        case 17:
            cout << "17) Ortogonalna projekcija na os x" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_x();
            break;
        case 18:
            cout << "18) Ortogonalna projekcija na os y" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_y();
            break;
        case 19:
            cout << "19) Ortogonalna projekcija na os z" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_z();
            break;
        case 20:
            cout << "20) Ortogonalna projekcija na xy-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_xy();
            break;
        case 21:
            cout << "21) Ortogonalna projekcija na xz-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_xz();
            break;
        case 22:
            cout << "22) Ortogonalna projekcija na yz-ravninu" << endl;
            cout << "---------------------------------------------" << endl;
            orto_projekcija_yz();
            break;
        case 23:
            cout << "23) Smicanje" << endl;
            cout << "---------------------------------------------" << endl;
            smicanje();
            break;
    }
    cout << endl <<"Zelite li nastaviti? (d/n)";
    cin >> dn;
    if (dn == 'n' || dn == 'N') izbor=0;
    else izbor = 1;
    }while(izbor!=0);

    return 0;
}
