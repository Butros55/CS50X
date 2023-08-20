#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Useage: ./recover IMAGE\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("File %s not found!\n", argv[1]);
        return 2;
    }


    BYTE buffer[BLOCK_SIZE];
    int jpegc = 0;
    FILE *output = NULL;
    char filename[8];


    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xFF && buffer[1] == 0xD8 && buffer[2] == 0xFF && (buffer[3]&0xF0) == 0xE0)
        {

            // check if output was written before
            if (jpegc == 0)
            {

                sprintf(filename, "%03i.jpg", jpegc);
                output = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                jpegc++;
            }

            else if (jpegc > 0)
            {
                fclose(output);
                sprintf(filename, "%03i.jpg", jpegc);
                output = fopen(filename, "w");
                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                jpegc++;
            }
        }

        else if (jpegc > 0)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
        }
    }

    fclose(output);
    fclose(file);
    return 0;

}
