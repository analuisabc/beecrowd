#include <stdio.h>
#include <stdlib.h>

int main(void){
    int c, i, count = 0;
    int *v;

    scanf("%d", &c);
    v = (int*)calloc(c, sizeof(int));

    for ( i = 0; i < c; i++){
        scanf("%d", &v[i]);
        if(v[i] == 1) count++;
    }
    printf("%d\n", count);

    free(v);

    return 0;
}