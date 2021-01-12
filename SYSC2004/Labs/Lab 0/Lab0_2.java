/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package lab0_2;

/**
 *
 * @author nikpaterson
 */
public class Lab0_2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        int numbers[] = {1,3,5,7,9,12};
        
	// NOTE: THIS CODE IS PROVIDED TO YOU FOR A REASON.
        // IT SHOWS HOW TO ITERATE OVER AN ARRAY.
        // NOTICE THAT every ARRAY has a default attribute called "length"
        // THAT TELLS YOU HOW MANY ELEMENTS ARE IN THE ARRAY.

        for (int i = 0; i < numbers.length; i++){
            System.out.print (numbers[i]);
        }
        System.out.println();
        
        // Task 1 - Pretty-print the array.  Put a comma and a space between 
        // each element, except the last!
        int len = numbers.length;
        for(int i = 0; i < len - 1; i++){
            System.out.print(numbers[i] + " , ");
        
        }
        System.out.print(numbers[len - 1]);
        System.out.println();
        
        
        // Task 2 - Calculate the average of all numbers in the array.
        // Print EXACTLY:  Average = x
        // Note: The average should be an integer value (6 and not 6.3)
        int Average = 0;
        for(int i = 0; i < len; i++){
            Average += numbers[i];
        }
        Average = Average / len;
        System.out.println("Average = " + Average);
        
        
        
        // Task 3 -- Calculate the number of odd numbers in the array.
        // Print EXACTLY: There are x odd numbers in the array.
        int numOdd = 0;
        for(int i = 0; i < len; i++){
            if(numbers[i] % 2 != 0){
                numOdd++;
            }
        }
        System.out.println("There are " + numOdd + " odd numbers in the array");
       
        
        
          // Task 4 -- Calculate the percent of numbers in the array that are odd.
          // Print EXACTLY: x % of the numbers in the array are odd.
          // Note: The percentage should be an integer value (83% not 83.33%)
          // TIP: You will need to use floats though in the calculation.
          // Note: This is trickier than you think.  You should see the difference
          //       between a compile-time syntax erro and a runtime error.
          
          float oddPercent = numOdd;
          oddPercent = (oddPercent / len) * 100;
          int i = Math.round(oddPercent);
          System.out.println(i + "% of the number in the array are odd.");
       
        
    }
    
}
