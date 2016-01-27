import java.io.*;
public class Main {
  static class Stack
  {
    public int[] theStack;
    public int last;
      
    public Stack(int size)
    {
      this.theStack = new int[size];
      this.last = -1;
    }
    
    public void push(int n)
    {
      theStack[++last] = n;
    }
    
    public int pop()
    {
      return theStack[last--];
    }  
    
    public boolean isEmpty()
    {
      return (last == -1);
    }
  }
  
  public static void main (String[] args) throws IOException {
    File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        
        while ((line = buffer.readLine()) != null) 
        {
            line = line.trim();
            String[] numbers = line.split(" ");
            Stack stack = new Stack(numbers.length);
            for(String num : numbers)
            {
              int n = Integer.parseInt(num);
              stack.push(n);
            }
            String stackOut = "";
            while(!stack.isEmpty())
            {
              stackOut += Integer.toString(stack.pop());
              if(stack.last >= 0)
              {
                stack.pop();
                stackOut += " ";
              }
            }
            System.out.println(stackOut);
        }
  }
}
