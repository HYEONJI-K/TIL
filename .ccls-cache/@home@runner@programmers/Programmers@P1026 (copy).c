/*
test case
num1	num2	result
2	    3	    -1
11	  11	  1
7	    99	  -1
*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

int solution(int num1, int num2) {
  if (num1 == num2) {
    return 1;
  } else {
    return -1;
  }
  /*
  if (num1 > num2) {
      return -1;
  } else if (num1 < num2){
      return -1;
  } else {
      return 1;
  } */
}
int main() { printf("%d", solution(11, 11)); }