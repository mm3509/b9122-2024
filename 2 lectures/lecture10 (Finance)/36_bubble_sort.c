#include <stdio.h>
#include <time.h>


void swap(int* arr, int i, int j) {
  // TODO: complete this.
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
          // TODO: complete this.
    }
}

int main() {
  int arr[] = {39, 12, 18, 85, 72, 10, 2, 18};
  int n = sizeof(arr) / sizeof(arr[0]);

  clock_t start, end;
  double cpu_time_used;

  start = clock();
  bubbleSort(arr, n);
  double elapsed = ((double) (clock() - start)) * 1000 / CLOCKS_PER_SEC;
  printf("Elapsed time: %.20f", elapsed);
  
  return 0;
}
