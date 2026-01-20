#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char **findWords(char **words, int wordsSize, int *returnSize)
{
    const char *row1 = "qwertyuiopQWERTYUIOP";
    const char *row2 = "asdfghjklASDFGHJKL";
    const char *row3 = "zxcvbnmZXCVBNM";

    char **result = (char **)malloc(wordsSize * sizeof(char *));
    int count = 0;

    for (int i = 0; i < wordsSize; i++)
    {
        char *word = words[i];
        int len = strlen(word);
        if (len == 0)
            continue;

        const char *firstRow = NULL;
        if (strchr(row1, word[0]))
        {
            firstRow = row1;
        }
        else if (strchr(row2, word[0]))
        {
            firstRow = row2;
        }
        else if (strchr(row3, word[0]))
        {
            firstRow = row3;
        }

        int j;
        for (j = 1; j < len; j++)
        {
            if (!strchr(firstRow, word[j]))
            {
                break;
            }
        }

        if (j == len)
        {
            result[count++] = word;
        }
    }

    *returnSize = count;
    return result;
}