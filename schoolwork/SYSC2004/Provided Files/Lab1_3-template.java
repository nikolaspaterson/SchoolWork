/**
 *
 * @title Lab 3 - Objective 3
 */

import java.util.Random;

public class Lab1_3 {
    
    public static int NUM_RECTANGLES = 10;
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
        Rectangle r1 = new Rectangle(10,20);
        
        System.out.println("Rectangle r1 ("+r1.getLength()+","+r1.getWidth()+")");
        System.out.println("\tArea = " + r1.area());
          // Notice the use of the tab character \t
          
        // Task 1 : On the next line, print out the perimeter, similarly tabbed
        
        
        // Task 2: Create a second rectangle called r2 with length = 20, width=10.
        
                
        
        //  DO NOT CHANGE THE FOLLOWING CODE
        
        Rectangle rectangles[] = new Rectangle[NUM_RECTANGLES];
        Random randomGenerator = new Random();
        int width, length;
        for (int i=0; i< rectangles.length; i++)
        {
            width = randomGenerator.nextInt(49) + 1;
            length = randomGenerator.nextInt(49) + 1;
            rectangles[i] = new Rectangle(length, width);
        }
        
        // Task 3 : Print out all randomly generated rectangles, one per line.
        //   Each line should print EXACTLY: r[i] = (w,l)
        
        // Task 4 : Search and print out the information for the rectangle with
        //   the largest area

        
        
        // Task 5 : Search and print out the information for the rectangle with
        //   the shortest perimeter
        
        
    }
    
}
