#include <stdio.h>

int main() {
    int numbers[] = {10, 25, 30, 45, 50};
    int key = 30;
    int size = sizeof(numbers) / sizeof(numbers[0]);
    int i;

    for (i = 0; i < size; i++) {
        if (numbers[i] == key) {
            printf("Key found at index %d\n", i);
            return 0;
        }
    }

    printf("Key not found\n");
    return 0;
}
