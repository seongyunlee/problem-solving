#include <stdio.h>

#include <stdlib.h>

/* You cannot add other libraries */
void print_mountain_info(const int ** mountain, int mountain_size);
const int ** alloc_and_init_mountain(int mountain_size);

void print_mountain_info(const int ** mountain, int mountain_size) {
    for (int i = 0; i < mountain_size; i++) {
        for (int j = 0; j < i + 1; j++) {
            printf("%d", mountain[i][j]);
            if (j == i) printf("\n");
            else printf(" ");
        }

    }
}

const int ** alloc_and_init_mountain(int mountain_size) {
    int ** mountain_org;
    mountain_org = (int ** ) malloc(sizeof(int * ) * mountain_size);
    for (int i = 0; i < mountain_size; i++) {
        mountain_org[i] = (int * ) malloc(sizeof(int) * (i + 1));
    }
    srand(mountain_size);
    for (int i = 0; i < mountain_size; i++) {
        for (int j = 0; j < i + 1; j++) {
            mountain_org[i][j] = (int)(rand() % 9999 + 1);
        }
    }
    return (const int ** ) mountain_org;
}

int solve(const int ** mountain, int mountain_size) {

    int a_dp[mountain_size];
    int b_dp[mountain_size];

    int* now = a_dp;
    int* prev = b_dp;

    prev[0] = mountain[0][0];
    
    for (int i = 1; i < mountain_size; i++) {
        for (int j = 0; j < i + 1; j++) {
            if (j == 0) {
                now[j] = prev[j] + mountain[i][j];
            } else if (j == i) {
                now[j] = prev[j - 1] + mountain[i][j];
            } else {
                now[j] = prev[j - 1] > prev[j] ? prev[j - 1] + mountain[i][j] : prev[j] + mountain[i][j];
            }
        }
        int* temp = now;
        now = prev;
        prev = temp;
    }
    int max = 0;
    for (int i = 0; i < mountain_size; i++) {
        if (prev[i] > max) {
            max = prev[i];
        }
    }
    return max;
}

int main() {
    int mountain_size = 0;

    scanf("%d", & mountain_size);

    const int ** mountain = alloc_and_init_mountain(mountain_size);

    printf("%d\n",solve(mountain, mountain_size));

}