#include <math.h>
#include <stdlib.h>
#include <stdio.h>

float generate_random_float(void) {
  // Students: this function generates a random number between 0 and
  // 1. Do not change this function.
  return (float) rand() / (float) RAND_MAX;
}

float approximate_pi(int n) {
  // Students: set the random seed, so results are reproducible on
  // Autograder and similar to the exam copy. Do not change this.
  srand(0);
   
  int count = 0;

  // TODO: complete this function.
  for (int i = 0; i < n; i++) {
    float x = generate_random_float();
    float y = generate_random_float();

    if (x * x + y * y < 1) {
      count++;
    }
  }

  // Students: don't change this, which handles the right syntax for
  // converting from integers to floats.
  return 4 * (float) count / (float) n;
}

int main() {
  // Students: this main function prints the approximation for
  // increasing orders of magnitude. Autograder will ignore this
  // function.
  for (int i = 1; i <= 7; i++) {
    int n = (int) pow((double) 10, (double) i);
    float approximation = approximate_pi(n);
    printf("Approximation at 10^%d: %.6f\n", i, approximation);
  }
  return 0;
}
