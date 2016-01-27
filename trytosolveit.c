#include <stdio.h>
#include <string.h>
char decrypt(char c)
{
  int dec = (int) c;
  switch(dec)
  {
    case 97 ... 102:
      dec += 20;
      break;
    case 103 ... 109:
      dec += 7;
      break;
    case 110 ... 116:
      dec -= 7;
      break;
    case 117 ... 122:
      dec -= 20;
      break;
  
    default: break;
  }
  return (char) dec;
}
int main(int argc, const char * argv[]) {
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    int i;
    
    while (fgets(line, 1024, file)) {
        for(i = 0; i < strlen(line); i++)
          line[i] = decrypt(line[i]);
        printf("%s", line);
    }
    fclose(file);
    return 0;
}
