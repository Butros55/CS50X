#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentence(string text);
int calc_grade(int words, float letters, float sentences);


int main(void)
{
    // Promt and print User input
    string input = get_string("Text: ");

    // calc letters
    int letters = count_letters(input);

    // calc words
    int words = count_words(input);

    // calc sententences
    int sentences = count_sentence(input);

    // print Grade
    int grade = calc_grade(words, letters, sentences);
    if (grade >= 16)
    {
        printf("Grade 16+");
    }

    if (grade < 1)
    {
        printf("Before Grade 1");
    }

    if (grade >= 1 && grade < 16)
    {
        printf("Grade %i", grade);
    }



    printf("\n");

}


int count_letters(string text)
{
    int calcl = 0;
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        int letter = toupper(text[i]);
        if (letter >= 65 && letter <= 90)
        {
            calcl = calcl + 1;
        }
    }
    return calcl;
}


int count_words(string text)
{
    int calcl = 0;
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (text[i] == 32)
        {
            calcl = calcl + 1;
        }
    }
    return calcl + 1;

}

int count_sentence(string text)
{
    int calcl = 0;
    int len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if ((text[i] == 46) || (text[i] == 63) || (text[i] == 33))
        {
            calcl = calcl + 1;
        }
    }
    return calcl;
}

int calc_grade(int words, float letters, float sentences)
{
    float L = letters * 100 / words;
    float S = sentences * 100 / words;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int rounded = round(index);
    return rounded;
}