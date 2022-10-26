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
  return 0;
}


/* 실행결과

-1 4
1 0
-1 4
1 0
-1 4
  1  2  3  4  5
 10  9  8  7  6
 11 12 13 14 15
 20 19 18 17 16
 21 22 23 24 25

*/