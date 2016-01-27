#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024]; char *part;
    int i, spaces, element;
    
    while (fgets(line, 1024, file)) {
      i = 0; spaces = 0;
        do
        {
           if(line[i++] == ' ')
              spaces++;
        } while(i < strlen(line));
    
        char *parts[spaces + 1]; i = 0;
        part = strtok(line, " ");
        while(part != NULL)
        {
           parts[i++] = part;
           part = strtok(NULL, " ");
        }
        element = atoi(parts[spaces]);
        if(element < spaces + 1)
           printf("%s\n", parts[spaces - element]);
    }
    fclose(file);
    return 0;
}
