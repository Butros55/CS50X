#include <stdio.h>
#include <cs50.h>

int main(void)
{

    int hashv, n, zeile, spacel = 0;
    do
    {
        n = get_int("Wie groß soll die Pyraide sein (1-8)?: ");
    }
    while (n < 1 || n > 8);



    for (zeile = 0; zeile < n; zeile++)
    {

        // Space Zeichen vorne
        for (spacel = 0; n > zeile + spacel + 1; spacel++)
        {
            printf(" ");
        }


        for (hashv = 0; hashv < zeile + 1; hashv++)
        {
            printf("#");
        }
    printf("\n");
    }

}