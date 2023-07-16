#include <string>
#include <vector>

using namespace std;

string solution(string s) {

    int up = 0, down = 0; // 최댓값 최솟값

    //  + : 0, - : 1  상태
    int state = 0;

    // 처음 : 1, 이후 : 0
    int first = 1;

    int num = 0; //현재 int

    for (char ch : s) {

        if (ch == '-') {
            state = 1;
        }

        else if (ch == ' ') {
            if (state == 1) {
                num *= -1;
            }

            if (first == 1) {
                up = num;
                down = num;
                first = 0;
                num = 0;
                state = 0;
                continue;
            }

            if (num > up) {
                up = num;
            }

            if (num < down) {
                down = num;
            }

            num = 0;
            state = 0;
        }

        else {
            num *= 10;
            num += ch - '0';
        }

    }
    
    if (state == 1) {
        num *= -1;
    }

    if (num > up) {
        up = num;
    }

    if (num < down) {
        down = num;
    }


    string result = to_string(down) + " " + to_string(up);

    return result;
}