#include "exercise8.c"
#include <stdio.h>
#include <stdlib.h>

int mymain(int argc, char **argv) {
  printf("%.8f\n", approximate_pi(atoi(argv[1])));
  return 0;
}
