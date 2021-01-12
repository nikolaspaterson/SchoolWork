package lab1;

/**
 *
 * @author Nik
 */
import java.util.Random;
import java.util.Date;

public class Lab1 {
    
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
        System.out.println("\tPerimeter = " + r1.perimeter());
        
        
        // Task 2: Create a second rectangle called r2 with length = 20, width=10.
        Rectangle r2 = new Rectangle(20,10);
        
                
        
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
        for (int i = 0; i < rectangles.length; i++){
            System.out.println("r[" + i + "] = (" + rectangles[i].getWidth() + ", " + rectangles[i].getLength() + ")");
        }
        
        
        // Task 4 : Search and print out the information for the rectangle with
        //   the largest area
        int largePos = 0;
        for(int i=0; i<rectangles.length; i++){
            if(rectangles[i].area() > rectangles[largePos].area()){
                largePos = i;
            }
        }
        System.out.println("Rectangle r[" + largePos + "] has the largest area");
        System.out.println("\tArea = " + rectangles[largePos].area());

        
        
        // Task 5 : Search and print out the information for the rectangle with
        //   the shortest perimeter
        int shortPos = 0;
        for(int i=0; i<rectangles.length; i++){
            if(rectangles[i].perimeter() < rectangles[shortPos].perimeter())
                shortPos = i;
        }
        System.out.println("Rectangle r[" + shortPos + "] has the shortest perimeter");
        System.out.println("\tPerimeter = " + rectangles[shortPos].perimeter());
        
        //PART B
        //Exercise 1
        Random myRandomGenerator = new Random(11*17*1999);
        int numRandom = 2000;
        int array[];
        array = new int [numRandom];
        int max = 0;
        int min = 0;
        int avg = 0;
        for(int i=0; i<array.length; i++){
            array[i] = myRandomGenerator.nextInt(26) + 65;
            avg += array[i];
            if(array[i] > array[max]){
                max = i;
            }
            if(array[i] < array[min]){
                min = i;
            }
            
        }
        avg = avg / numRandom;
        System.out.println("Array summary");
        System.out.println("\tMinimum = " + array[min] + "\tMaximum = " + array[max] + "\tAverage = " + avg);
        
        //Exercise 2
        int stringLength = myRandomGenerator.nextInt(100) + 1;
        byte myBytes[] = new byte[stringLength];
        for(int i=0; i<myBytes.length; i++){
            //myBytes[i] = myRandomGenerator.nextBytes(myBytes);
        }
        
        //Exercise 3
        Date today = new Date();
        System.out.println(today.getMonth());
        System.out.println(today.getDay());
    }
    
}
