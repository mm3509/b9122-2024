#include "exercise6.c"
#include <stdio.h>
#include <stdlib.h>

int mymain(int argc, char **argv) {
  printf("%d\n", count_steps(atoi(argv[1])));
  return 0;
}
