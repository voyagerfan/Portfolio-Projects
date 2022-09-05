/* 
 * postfixEvaluation:
 * This method accepts the postfix string and converts in into an int result.
 * A new stack is created. Number values in the post fix string exist as chars 
 * and are converted to int using int value = c - '0'
 * A for loop is used to iterate over the postfix string and makes use of the 
 * int converstion code. The int is then pushed to the stack. If an operator is 
 * encountered in the for loop, the stack is popped twice and assigned new value1 
 * and new value2. These are used in tandem with the encountered operator to
 * determine newValue which is then pushed back to the stack. As the loop interates
 * over postfix, the newValue continues to update and the final pop is the result 
 * of the postfix statement. 
 * 
 */


package project_3;

import java.util.*;

public class PostfixEvaluation 
{
	//method that evaluates postfix string and returns a numerical result
	public int postfixEvaluation(String postfix)
	{
		//create new stack
		Stack <Integer> stack = new Stack<>();	
		
		//iterates over the postfix string
		for(int k = 0; k< postfix.length(); k++)
		{
			char c = postfix.charAt(k);
			
			//if c is a number between 0 and 9
			if(c >= '0' && c<='9')
			{
				//converts the char to int
				int value = c - '0';
				//value is pushed to the stack
				stack.push(value);
			}
			//if any operators are ecountered...
			if (c == '+' || c == '-' || c == '*' || c == '/')
			{
				//stack is popped twice and each is assigned to value1 and value2
				int value1 = stack.pop();
				int value2 = stack.pop();
				
				//initiates newValue
				int newValue = 0;
				
				/* Series of if/else statements:
				 * if a specific operator is enountered, 
				 * newValue = value2 "operator" value1. Operator may be +,-,*,/
				 */
				if(c == '+')
				{
					newValue = value2 + value1;
				}
				else if(c == '-')
				{
					newValue = value2 - value1;
				}
				else if(c == '*')
				{
					newValue = value2 * value1;
				}
				else if(c == '/')
				{
					newValue = value2 / value1;
				}
				//newValue is push to stack
				stack.push(newValue);
				
			}
			
			
		}
		/* since stack is being popped, operated and pushed back, 
		 * the result of postfix is being updated through the loop iteration.
		 * The last remaining element of the stack will be result of postfix, 
		 * therefore pop the stack to get the result
		 */
		int result = stack.pop();
		return result;
	}
	
}
