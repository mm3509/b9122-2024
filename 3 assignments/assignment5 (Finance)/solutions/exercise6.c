#include <stdio.h>

int count_steps(int n) {
   if (1 == n) {
      return 1;
   }
   if (2 == n) {
      return 2;
   }
   if (3 == n) {
      return 4;
   }
   //printf("At step: %d\n", n);
   return count_steps(n-1) + count_steps(n-2) + count_steps(n-3);
}

int main() {
   // printf() displays the string inside quotation
   printf("%d\n", count_steps(8));
   return 0;
}
