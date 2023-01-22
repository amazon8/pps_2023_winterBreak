#include <iostream>

/*
1. 이중 배열(b --> t)
*/

using namespace std;

int main() {

  int num;
  int floor, unit;
  int people[10000][15] = {
      0,
  };

  cin >> num;

  for (int i = 0; i < num; i++) {
    cin >> floor;
    cin >> unit;

    for (int nowFloor = 0; nowFloor <= floor; nowFloor++) {
      for (int nowUnit = 1; nowUnit <= unit; nowUnit++) {
        if (people[nowFloor][nowUnit] == 0) {
          if (nowFloor == 0) {
            people[nowFloor][nowUnit] = nowUnit;
          } else {
            for (int tempUnit = 1; tempUnit <= nowUnit; tempUnit++) {
              people[nowFloor][nowUnit] += people[nowFloor - 1][tempUnit];
            }
          }
        }
      }
    }

    cout << people[floor][unit] << endl;
  }
}