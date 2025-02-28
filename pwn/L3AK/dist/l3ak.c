#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define LOGIN_USER_MESSAGE "Username: "
#define LOGIN_PASSWORD_MESSAGE "Password: "
#define INVALID_LOGIN_MESSAGE "Couldn't log in as "

void setup(void)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

struct s_login {
    char *username;
    char *password;
    size_t max_size;
};

void read_field(char **field, size_t *max_size)
{
    *field = (char*) malloc(11);
    *max_size = 11;
    getline(field, max_size, stdin);
    fflush(stdin);
}

void write_field(char *field, size_t size)
{
    write(1, field, size);
    fflush(stdout);
}

bool create_login(struct s_login *login)
{
    login->username = (char*) malloc(11);
    login->password = (char*) malloc(11);
    if (login->username == NULL || login->password == NULL)
        return false;

    login->max_size = 11;

    // Read username and password
    write_field(LOGIN_USER_MESSAGE, sizeof(LOGIN_USER_MESSAGE));
    read_field(&login->username, &login->max_size);
    
    write_field(LOGIN_PASSWORD_MESSAGE, sizeof(LOGIN_PASSWORD_MESSAGE));
    read_field(&login->password, &login->max_size);

    return true;
}

void    destroy_login(struct s_login *login)
{
    free(login->username);
    free(login->password);
}

int main(void)
{
    setup();

    struct s_login login;
    char *secret_user = "user";
    char *secret_password = "fakepassword";

    if (create_login(&login) == -1)
        return -1;

    if ((strstr(login.username, secret_user) != NULL) && (strstr(login.password, secret_password) != NULL))
    {
        destroy_login(&login);
        printf("Welcome admin!\n");
    }
    else
    {
        printf(INVALID_LOGIN_MESSAGE);
        printf(login.username);
        destroy_login(&login);
    }
    
    return 0;
}
