#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
  int N;
  cin >> N;
  vector<int> steps(N + 1, INT_MAX);
  steps[N] = 0;
  vector<int> next_num(N + 1, -1);

  for (int i = N; i > 1; --i) {
    int s = steps[i] + 1;
    
    if (!(i % 3) && steps[i / 3] > s) {
      steps[i / 3] = s;
      next_num[i / 3] = i;
    }
    
    if (!(i % 2) && steps[i / 2] > s) {
      steps[i / 2] = s;
      next_num[i / 2] = i;
    }
    
    if (steps[i - 1] > s) {
      steps[i - 1] = s;
      next_num[i - 1] = i;
    }
  }

  cout << steps[1] << endl;
  for (int i = 1; i != -1; i = next_num[i])
    cout << i << ' ';
  cout << endl;
}