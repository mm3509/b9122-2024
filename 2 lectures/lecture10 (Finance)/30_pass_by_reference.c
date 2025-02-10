#include <stdio.h>

void addtwo(int *val) {
  *val += 2;
  printf("val (*in addtwo*) = %d\n", *val);
}

int main() {
  int val = 0;
  printf("Starting val = %d\n", val);
  while (val < 10) {
    addtwo(&val);
    printf("val (*in main*) = %d\n", val);
  }
  return 0;
}
