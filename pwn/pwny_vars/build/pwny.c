#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

struct frame {
	char buffer[128];
	unsigned long x;
};

void setup(void)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main(int argc, char** argv)
{
    setup();
	struct frame f;
	memset(&f, 0, sizeof(f));

    printf("Welcome to Pwny vars\n");
	printf("> ");
	fflush(stdout);

	read(STDIN_FILENO, &f.buffer[0], 256);

	if (f.x == (unsigned long)0xdeadbabebeefc0deUL) {
		system("cat flag.txt");
	}

	return EXIT_SUCCESS;
}
