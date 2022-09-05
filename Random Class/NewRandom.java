package CS211_Project1;

import java.util.*;

public class NewRandom extends Random
{
	
	//Returns a random number which is an integer value between the range of ‘low’ to ‘high’.
	public int nextInt(int low, int high)
	{
		int n = nextInt(high-low+1);
		return n+low;
	
	}
	//Returns a random integer number with ‘digit’ digits.
	public int nextIntDigit(int digits)
	{
		int n = 0;
		int low = 0;
		int high = 0;
		
			if(digits == 1)
			{
				n = nextInt(0,9); //this is for if digits = 1 only.
			}
			else
			{
				low = (int) Math.pow(10, digits-1);  //lower bound = 10^(digits-1)
				high = (int) Math.pow(10,digits)-1;	//upper bound = (10^digits)-1
				n = nextInt(low,high); // randomizes between upper and lower bounds.
			}
		
			
		return n;

	}
	
	
	public char nextChar()
	{
		int n = nextInt('a', 'z'); //randomizes between a and z
		return (char) n;
	}
	
	public char nextChar(char low, char high)
	{
		int n = 0;
		
		//creating array list to hold the alphabet
		ArrayList <Character> numset = new ArrayList <> ();
		
		//creating second array list to hold a sublist which will then be randomized by index
		ArrayList <Character> numsetFinal = new ArrayList <> ();
		
		//loads array list numset with alphabet
		for(char c = 'a'; c<='z'; c++)
		{
			numset.add(c);
		}
		
		if(low < high)
		{
			n = nextInt(low, high);
		}
		else if (low>high)
		{
			//calculate the distance between integers
			int first = Math.abs(numset.indexOf(low)-26);
			int last = Math.abs(numset.indexOf(high)-0);
			int distance = Math.abs(first+last);
			
			//variable "initial" is used as starting point to build numsetFinal array
			int initial = numset.indexOf(low);
			
			int n1 = numset.size(); //gets the size of the array
			
			for(int i = 0; i<=distance; i++)
			{
				numsetFinal.add(numset.get(initial%n1)); //initial%n1 creates circular arraylist
				initial++;
			}
			int n2 = nextInt(0,numsetFinal.size()-1); // nextInt randomizes the arraylist index
			
			n = numsetFinal.get(n2); // gets the value in the randomized index array index position is passed to "n" which is casted as char.
		}
			
		else
		{
			n = high; 
		}
		
		
		return (char) n;
		//char c = 'a';
		//return c;
		
		
	}
	
	//Rurns etan lowercase letter between the range of ‘from’ to ‘from+i’
	//(assume -26<= i <= +26)
	public char nextChar(char from, int i)
	{
		int n = 0;
		ArrayList <Character> numset = new ArrayList <> (); //creates and array list to store alphabet
		ArrayList <Character> numsetFinal = new ArrayList <> ();
		
		for(char c = 'a'; c<='z'; c++) //loads arraylist with alphabet.
		{
			numset.add(c);
		}
		
		int initial = numset.indexOf(from); // sets the initial variable to index of the char
		int n1 = numset.size();
		
		if(i>0)
		{
		
			for(int j = 0; j<=i; j++) // adds the chars from numset to numsetfinal starting with initial.
			{
				numsetFinal.add(numset.get(initial%n1)); 
				initial++; //counter variable to move the index forward.
			}
			
		
			
			int n2 = nextInt(0,numsetFinal.size()-1);
			
			n = numsetFinal.get(n2);
		}
		
		else if (i<0) 
		{
			for(int k = 0; k<26+i; k++)  //sets counter variable 'initial' backward by the value of 'i'
			{
				numset.get(initial%n1);
				initial++;
			
			}
			
			for(int j = 0; j<=i*-1; j++) //adds chars from numset to numsetfinal using counter variable above
			{
					numsetFinal.add(numset.get(initial%n1));
					initial++;
			}
			int n2 = nextInt(0,numsetFinal.size()-1); //randomizes the array index in numsetfinal
			
			n = numsetFinal.get(n2); //passes the contents in array position to n
		}
		else
		{
			n = from;
		}
		
		return (char) n;
	}
	
	//Returns a special character
	public char nextSpecialChar()
	{
		int low = 33; //!
		int high = 126; //~
		char c =' ';
		boolean special = false;
		
		while(!special) // will run loop while !special
		{
			int n = nextInt(low, high); //randomizes between 33 and 126
			c = (char) n;
			if(!Character.isDigit(c) && !Character.isLetter(c)) //if c is not number AND letter, c is special, therefore, break. 
			{
				break;
			}
		}
		
		return c;
		
	}
}
	

