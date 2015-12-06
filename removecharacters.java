import java.io.*; 

public class Main {
  
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        
        // this is quite easy ...
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            String[] parts = line.split("\\,");
            String newString = "";
            String[] words = parts[0].split("\\ ");
            int last = words.length;
            int i = 0;
            for(String w : words)
            {
            	newString += w.replaceAll("["+parts[1]+"]", "");
            	if(++i != last)
            		newString += " ";
            }
            System.out.println(newString);
        }
    }
}
