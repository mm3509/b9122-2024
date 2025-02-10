#include <stdio.h>

int matrix[3][2] = {
  {10, 11},
  {20, 21},
  {30, 31}
};

int main() {
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 2; j++){
      printf("Matrix location [%d,%d] = %d\n", i, j, matrix[i][j]);
    }
  }
  return 0;
}
