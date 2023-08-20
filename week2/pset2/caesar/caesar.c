#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void entcrypt(string plaintxt, int number);

int main(int argc, string argv[])
{


    // Verify if input is valid
    if (argc != 2)
    {
        printf("Key is not valid\n");
        return 1;
    }

    //Promt user for text
    string plaintxt = get_string("plaintext:  ");

    // number from argv
    int number = atoi(argv[1]);
    printf("ciphertext: ");

    //entcrypt function
    entcrypt(plaintxt, number);

    return 0;
}






void entcrypt(string plaintxt, int number)
{
    int plainn = 0;
    int len = strlen(plaintxt);

    for(int i = 0; i < len; i++)
    {
        int plt = plaintxt[i];
        if ((plt >= 65 && plt <= 90) || (plt >= 97 && plt <= 122))

        {
            plainn = plaintxt[i] + number;

            for (; (plainn >= 90 && plt <= 90) || (plainn >= 122 && plt <= 122);)
            {
                if ((plainn > 90 && plt <=90 && plt >=65) || (plainn > 122 && plt <= 122 && plt >= 97))
                {
                    plainn = plainn - 26;
                }
            }

            char cypher = (char)plainn;
            printf("%c", cypher);
        }
        else
        {
            printf("%c", plaintxt[i]);
        }

    }
    printf("\n");
}