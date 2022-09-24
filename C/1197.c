#include <stdio.h>

int main(void){
    int v, t, S;

    while (scanf("%d%d", &v, &t) != EOF){
        S = v * t * 2;
        printf("%d\n", S);
    }
    

    return 0;
}