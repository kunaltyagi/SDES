#include <stdio.h>
#include <string.h>
#include "mystrlib.h"

void
reverse(char *s)
{
	int i;
	size_t len = strlen(s);
	for (i = 0; i < (len - 1) / 2; ++i) {
		char temp = s[i];
		s[i] = s[len - i - 1];
		s[len - i - 1] = temp;
	}
}

int
main(int argc, char *argv[])
{
	if (argc > 1) {
		reverse(argv[1]);
		printf("%s\n", argv[1]);
	}
	return 0;
}
	
