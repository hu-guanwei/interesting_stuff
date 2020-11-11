#include <stdio.h>



/*

---------    low address
|buffer |
|       |
---------
| main  |
|       |
---------    high address
_____________________________ stack grows towards lower address

*/


void attack() {
	char buffer[10];
	printf("%p\n", buffer);
	printf("%p\n", buffer + 42);
	*(int*)(buffer + 42) = 9999;
	return;
}


int main() {

	int i = 100;
	attack();
	printf("%p\n", &i);
	printf("%d\n", i);
	return 0;
}
