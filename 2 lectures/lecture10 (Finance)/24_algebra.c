#include <stdio.h>

float data[3];
float sum = 0.0;
float average;

int main() {
  data[0] = 1.20;
  data[1] = 4.38;
  data[2] = 5.39;
  for (int i = 0; i < 3; i++) {
    sum += data[i];
  }
  printf("Sum = %f\n",sum);
  average = sum / 3;
  printf("Average = %f\n" , average);
  return 0;
}
