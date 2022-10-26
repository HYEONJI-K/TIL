#include <stdio.h>
int main() {
  int a[5][5], j = 0, sw = 1, k = 1;
  for (int i = 0; i < 5; i++) {
    while (j <= 4 && j >= 0) {
      a[i][j] = k++;
      j += sw;
    }
    sw *= -1;
    j += sw;
    printf("%d ", sw);
    printf("%d \n", j);
  }
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < 5; j++) {
      printf("%3d", a[i][j]);
    }
    printf("\n");
  }
}
