// pipelined

// Lv. 3

#include<iostream>
#include<vector>
#include <algorithm>

using namespace std;

int pipeline(const std::vector<int>& v){ // 벡터 input
    int i = 1;
    int cur_numerator = 1;
    int time = 1;
    while(i < v.size()){ // 벡터 크기 
        float cur = static_cast<float>(cur_numerator) / v[i - 1]; // 변수 type casting
        float nxt = 1.0f / v[i]; // 정수 type casting
        if(nxt <= cur){
            cur_numerator = 1;
            i++;
        }else{
            cur_numerator++;
        }
        time++;
    }
    return time + v.back() - 1; // 벡터의 가장 마지막 원소
}

int main(int argc, char** argv)
{
    int n;
    std::cin >> n;
    
    std::vector<int> s(n);  // 동적 배열
    for(int i = 0; i < n; i++){
        std::cin >> s[i];
    }

    std::sort(s.begin(), s.end()); // 정렬
    int result = pipeline(s);
    std::cout << result;
    return 0;
}