#include <stdio.h>

// 5 element array of integers
int main() {
  int data[5];
  data[0] = 10;
  data[1] = 20;
  data[2] = 30;
  data[3] = 40;
  data[4] = 50;
  for (int i = 0; i < 5; i++)  {
    printf("data[%d] = %d\n", i, data[i]);
  }
  return 0;
}
