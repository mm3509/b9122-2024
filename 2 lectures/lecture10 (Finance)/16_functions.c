#include <stdio.h>

void addtwo(int not_x) {
  not_x += 2;
  return;
}

int main() {
  int x = 0;
  addtwo(x);
  printf("%d\n", x);
  return 0;
}
