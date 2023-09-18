#include<iostream>
#include<time.h>
#include<iomanip>
using namespace std;

void task(){
    for (int i = 0; i<10000; i++){
        cout << "Loop ke :" << i <<  endl;
    }
}


int main(){
    
    time_t start, end;

    time(&start);
    
    ios_base::sync_with_stdio(false);

    task();

    time(&end);

    long double time_taken = double(end - start);
    cout << "\n Eksekusi C++ memerlukan waktu : " << fixed << time_taken ;
    cout << " sec " << endl;


}