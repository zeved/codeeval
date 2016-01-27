#include <stdio.h>
#include <string.h>
unsigned int rev(unsigned int n)
{
    unsigned int r = 0, _rev = 0;
    while(n != 0)
    {
     r = n % 10;
     _rev = _rev * 10 + r;
     n /= 10;
  }
  return _rev;
}
// have to use small tricks like this because stdlib's atoi is not so fast
int fast_atoi(const char * str)
{
    int val = 0;
    while(*str) {
        val = val * 10 + (*str++ - '0');
    }
    return val;
}
int main(int argc, const char * argv[]) {
    
    FILE *file = fopen(argv[1], "r");
    char line[1024];
    
    unsigned int n, k, i, x;
    
    while(fgets(line, 1024, file))
    {
      line[strlen(line) - 1] = '\0';  // better than strtok
      n = fast_atoi(line);
      x = rev(n);
        i = 0;
        do
        {
           x += rev(x);
           i++;
        }
        while(x != rev(x));        // faster than for(i = 0; i < 100; i++) apparently ?
        printf("%d %d\n", i, x);
    }
    fclose(file);
    return 0;
}
