#include <stdio.h>

// 5 element array of integers
int data[5] = {10, 20, 30, 40, 50};

int main() {
   for (int i = 0; i < 5; i++) {
     printf("data[%d] = %d\n", i, data[i]);
   }
   return 0;
}
