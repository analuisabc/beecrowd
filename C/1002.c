#include <stdio.h>

int main(void){
    double area, r;

    scanf("%lf", &r);
    area = 3.14159 * r * r;
    printf("A=%.4lf\n", area);

    return 0;
}