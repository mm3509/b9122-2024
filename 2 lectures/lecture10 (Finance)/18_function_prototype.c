#include <stdio.h>

void addtwo(int x);

int main() {
  int x = 0;
  addtwo(x);
  printf("%d\n", x);
  return 0;
}

void addtwo(int x) {
  x += 2;
  return;
}
