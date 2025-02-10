#include <stdio.h>

void swap_ints(int *px, int *py) {
  *px -= *py;
  *py += *px;
  *px = *py - *px;
}

int main() {
  int x = 10;
  int y = 24;
  int *px = &x;
  int *py = &y;
  printf("Before running the function: x = %d, y = %d\n", x, y);
  swap_ints(px, py);
  printf("After running the function: x = %d, y = %d\n", x, y);
}
