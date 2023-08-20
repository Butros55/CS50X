#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int n, zeile, hashv, hashh, spacel, spacem ,sapcer;
    do
    {
        n = get_int("Wie groß soll die Pyraide sein (1-8)?: ");
    }
    while (n < 1 || n > 8);


    // Vertikale
    for (zeile = 0; zeile < n; zeile++)
    {
        // Space Zeichen vorne
        for (spacel = 0; n > zeile + spacel + 1; spacel++)
        {
            printf(" ");
        }

        // Hash vorne
        for (hashv = 0; hashv < zeile + 1; hashv++)
        {
            printf("#");
        }

        // Space Zeichen mitte
        for (spacem = 0; spacem < 2; spacem++)
        {
            printf(" ");
        }
i
        // Hash hinten
        for (hashh = 0; hashh < zeile + 1; hashh++)
        {
            printf("#");
        }
        printf("\n");
    }

}
