// Hanyang Popularity Exceeding Competition

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    int n;
    std::cin >> n;
    int x = 0;
    int p = 0, c = 0;
    for(int i = 0; i < n; i++){
        std::cin >> p >> c;
        if(abs(p - x) <= c){
            x++;
        }
    }
    std::cout << x;
    return 0;
}