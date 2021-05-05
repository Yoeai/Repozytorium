#include <iostream>

using namespace std;

int main(){
float a,b,wynik;
	char wybor;
	do
	{
		cout<<"1.Dodawanie\n";
		cout<<"2.Odejmowanie\n";
		cout<<"3.Mnozenie\n";
		cout<<"4.Dzielenie\n";
		cout<<"5.Wyjdz\n";
		cin>>wybor;
		switch(wybor)
		{
			case '1' : cout<<"Wpisz dwie liczby : ";
				cin>>a>>b;
				wynik=a+b;
				cout<<"Wynik = "<<wynik;
				break;
			case '2' : cout<<"Wpisz dwie liczby : ";
				cin>>a>>b;
				wynik=a-b;
				cout<<"Wynik = "<<wynik;
				break;
			case '3' : cout<<"Wpisz dwie liczby : ";
				cin>>a>>b;
				wynik=a*b;
				cout<<"Wynik = "<<wynik;
				break;
			case '4' : cout<<"Wpisz dwie liczby : ";
				cin>>a>>b;
				wynik=a/b;
				cout<<"Wynik = "<<wynik;
				break;
			case '5' : return 0;
				break;
			default : cout<<"Zly wybor!!";
				break;
		}
		cout<<"\n------------------------------------\n";
	}while(wybor!=5);
return 0;
}
