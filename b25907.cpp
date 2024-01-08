#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int l = 1, r = 1000000;
    int f=1,l=N;
    while(true){
        int day=(f+l)/2
        cout <<"? "<<day<<endl;
        int s;
        cin <<s;
        int w=day-s;
        if(s==w){
            cout <<"! "<<day<<endl;
            return();
        }
        if(s>w) f=day+1;
        else l=day-1;
    }
}