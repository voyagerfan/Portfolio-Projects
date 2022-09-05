package CS211_Project1;

import java.util.*;

public class NewRandomTest 
{
	
	static String[] method = new String [6];
	static String[] errorMsg = new String [2];
	
	static int howManyTest = 20;
	static NewRandom nRand = new NewRandom();
	static Scanner input = new Scanner(System.in);
	
	
	
	public static void main(String[] args)
	{
		LoadMenu();
		LoadErrorMsg();
		selectNtest();
		
	}
	
	public static void LoadMenu()
	{
		method[0] = "nextInt(int low, int high)";
		method[1] = "nextIntDigit(int digits)";
		method[2] = "nextChar()";
		method[3] = "nextChar(char from, chart to)";
		method[4] = "nextChar(chart from, int i)";
		method[5] = "nextSpecialChar()";
		
	}
	
	public static void LoadErrorMsg()
	{
		errorMsg[0] = "Must be 0..6";
		errorMsg[1] = "Must be a digit";
		
	}
	
	public static void printErrorMsg(int errNumber)
	{
		System.out.println(errorMsg[errNumber]);
	}
	
	public static void selectNtest()
	{
		System.out.println("\nProject 1. New Random Class. (Spring Quater 2022)");
		boolean run = true;
		while(run)
		{
			System.out.println("\nWhat method would you like to test?");
			for(int i = 0; i<method.length; i++)
			{
				System.out.println(i + ". " + method[i]);
				
			}
			System.out.println(method.length + ": quit");
			
			//try-catch block
			int whichTest;
			while(true)
			{
				
				try
				{
					whichTest = input.nextInt(); //if variable is not of type int, InputMisMatch catch is executed	
					int [] array = new int [7]; //creates an array of 6
					array[whichTest] = 1; //if variable is not 0-6, ArrayIndexOutOfBounds catch is executed
					
					
				}
				catch (InputMismatchException e)
				
				{
					
					printErrorMsg(1);
					
					System.out.println("\nTry again...What method would you like to test?");
					input.nextLine(); // clears scanner object
					continue; //continues back to try until try block is satisfied
				}
				
				catch(ArrayIndexOutOfBoundsException e)
				{
					
					printErrorMsg(0);
					System.out.println("\nTry again...What method would you like to test?");
					input.nextLine(); //clears scanner object
					continue; //continues back to try until try block is satisfied
				}
				
				break; //breaks loop when try has no errors
			}
			
			
			//end try-catch
			
			
			if (whichTest == method.length) //if 6 is entered, program will print "bye" then stop
			{
				run = false;
				System.out.println("Bye!");
				break;
			}
			else
			{
				test(whichTest); //if 6 is not entered, testing will start based on the value of whichTest
			}
		}
	}
	
	public static void test(int index) //test method for all the array indexes. They work similarly.  
	{
		if(index == 0)
		{
			System.out.println("input low"); 
			int low = input.nextInt();			//takes input for the method to be tested
			System.out.println("input high");
			int high = input.nextInt();			//takes input for the method to be tested
			
			System.out.println("\nResults: nextInt(" + low + ", "+ high + ")"); 
			for(int i = 0; i<howManyTest; i++)	//for loop runs method 20 times and prints the result
			{
				int a = nRand.nextInt(low,high); //assigns randomized value to a based on method and arguments
				System.out.print(a + " ");
				
			}
			System.out.println(); //adds space line.
		}
		
		else if(index == 1) 
		{
			System.out.println("input digits");
			int digits = input.nextInt();
			
			System.out.println("\nResults: nextIntDigit(" +digits + ")");
			for(int i = 0; i<howManyTest; i++)
			{
				int a = nRand.nextIntDigit(digits);
				System.out.print(a + " ");
			}
			
			System.out.println();
			
		}
		
		else if(index == 2)
		{
			System.out.println("You have selected nextChar(). No input required.");
			System.out.println("\nResults: nextChar()");
			for(int i = 0; i<howManyTest; i++)
			{
				char a = nRand.nextChar();
				System.out.print(a + " ");
			}
			
			System.out.println();
		}
		
		else if(index == 3) 
		{
			System.out.println("input char from");
			char charFrom = input.next().charAt(0);
			
			System.out.println("input char to");
			char charTo = input.next().charAt(0);
			
			System.out.println("\nResults: nextChar(" + charFrom + ", "+ charTo + ")");
			for(int i = 0; i<howManyTest; i++)
			{
				char a = nRand.nextChar(charFrom, charTo);
				System.out.print(a + " ");
			}
			
			System.out.println();
		}
		
		else if(index == 4)
		{
			System.out.println("input char from");
			char charFrom = input.next().charAt(0);
			
			System.out.println("input int i");
			int intTo = input.nextInt();
			
			System.out.println("\nResults: nextChar(" + charFrom + ", "+ intTo + ")");
			for(int i = 0; i<howManyTest; i++)
			{
				char a = nRand.nextChar(charFrom, intTo);
				System.out.print(a + " ");
			}
			
			System.out.println();
		}
		
		else if(index == 5)
		{
			System.out.println("You have selected nextSpecialChar(). No input required.");
			System.out.println("\nResults: nextSpecialChar()");
			for(int i = 0; i<howManyTest; i++)
			{
				char a = nRand.nextSpecialChar();
				System.out.print(a + " ");
			}
			
			System.out.println();
			
		}

	}
	
}
