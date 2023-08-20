#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("\n");
    printf("Total Coins: %i\n", coins);
    printf("Total Quarters: %i\n", quarters);
    printf("Total Dimes: %i\n", dimes);
    printf("Total Nickels: %i\n", nickels);
    printf("Total Pennies: %i\n", pennies);
    printf("\n");

}

int get_cents(void)
{
    // Ask how many cents
    int cents = get_int("How many cents do you owed?: ");
    return cents;
}

int calculate_quarters(int cents)
{
    // TODO
    int quarters = 25;
    int i = 0;
    for (i = 0; quarters <= cents; i++)
        {
            cents = cents - quarters;
        }
    return i;
}

int calculate_dimes(int cents)
{
    int dimes = 10;
    int i = 0;
    for (i = 0; dimes <= cents; i++)
        {
            cents = cents - dimes;
        }
    return i;
}

int calculate_nickels(int cents)
{
    int nickels = 5;
    int i = 0;
    for (i = 0; nickels <= cents; i++)
        {
            cents = cents - nickels;
        }
    return i;
}

int calculate_pennies(int cents)
{
    int pennies = 1;
    int i = 0;
    for (i = 0; pennies <= cents; i++)
        {
            cents = cents - pennies;
        }
    return i;
}
