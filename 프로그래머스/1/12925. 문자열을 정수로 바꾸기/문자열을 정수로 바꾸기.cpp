#include <iostream>
#include <string>
using namespace std;

int solution(string s) {
    int answer = 0;
    bool negative = false;
    
    if (s[0] == '-'){
        negative = true;
        s = s.substr(1,s.length());
    }
    else if (s[0] == '+'){
        s = s.substr(1,s.length());
    }
    
    for (int i=0; i<s.length(); i++){
        int num = s[i]-'0';
        for (int j=s.length()-1; j>i; j--){
            num *= 10;
        }
        answer += num;
    }
    
    if (negative) return -answer;
    else return answer;
}