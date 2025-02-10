#include <stdio.h>

int main() {
  int X;
  int *pX;

  // Set the value of variable X.
  X = 10;
  printf("X address: %u\n", &X);
  printf("X value: %d\n\n", X);

  // Set the value of the pointer to the address of variable X.
  pX = &X;
  printf("pX address: %u\n", pX);
  printf("pX content: %d\n\n", *pX);

  // Change the value of X.
  X = 11;
  printf("pX: %u\n", pX);
  printf("pX content: %d\n\n", *pX);

  // Change the value of variable X by dereferencing its pointer.
  *pX = 20;
  printf("X address: %u\n", &X);
  printf("X value: %d\n\n", X);

  return 0;
}
