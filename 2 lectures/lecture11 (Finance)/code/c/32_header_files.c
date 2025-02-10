#include "32_algebra.h"
#include <stdio.h>

int main(void) {

  int a = 3;
  int b = 2;
  printf("%d + %d = %d\n", a,b, addtwo(a,b));
  printf("%d * %d = %d\n", a,b, multiplytwo(a,b));
  printf("%d - %d = %d\n", a,b, subtracttwo(a,b));

  return 0;
}
