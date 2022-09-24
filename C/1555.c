#include <stdio.h>

int main(void){
    int x, y, n;
    int r, b, c;

    scanf("%d", &n);
    while (n--){
        scanf("%d%d", &x, &y);
        r = (9 * x * x) + (y*y);
        b = (2 * x * x) + (25 * y * y);
        c = (-100 * x) + (y * y * y);

        if (r > b && r > c){
            printf("Rafael ganhou\n");
        }else if (b > r && b > c){
            printf("Beto ganhou\n");
        }else if (c > r && c > b){
            printf("Carlos ganhou\n");
        } 

    }
    
    return 0;
}