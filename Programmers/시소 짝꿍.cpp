#include <unordered_map>
#include <iostream>
#include <vector>

using namespace std;

unsigned long long solution(vector<int> weights) {
    unsigned long long answer = 0;
    unordered_map<int, unsigned long long> counter;
    for (int w : weights)
        counter[w]++;
    for (auto it = counter.begin(); it != counter.end(); ++it)
    {
        if ((*it).second % 2 == 0)
            answer += (((*it).second / 2) * ((*it).second - 1));
        else
            answer += (((*it).second) * (((*it).second - 1) / 2));
        if ((*it).first % 2 == 0 && counter.find(((*it).first /2) * 3) != counter.end())
            answer += counter[(*it).first] * counter[((*it).first / 2) * 3];
        if ((*it).first % 2 == 0 && counter.find((*it).first / (2)) != counter.end())
            answer += counter[(*it).first] * counter[(*it).first / (2)];
        if ((*it).first % 3 == 0 && counter.find(((*it).first /3)*4) != counter.end())
            answer += counter[(*it).first] * counter[((*it).first /3)*4];
    }
    return answer;
}
