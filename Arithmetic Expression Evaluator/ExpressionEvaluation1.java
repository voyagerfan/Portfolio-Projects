
 
 * Program description:
 * expressionEvaluation receives the string mathExpression and 
 * iterates over the string variable using a for loop. If a left 
 * parenthesis or left bracket is found, it is pushed to the stack.
 * If a right parenthesis or bracket is found, printError is called
 * if the stack is empty or if the char on the stack is not the correct pairing
 * to the current char being iterated over.
 
 * printError method utilizes the for loop position and error number from the
 * errorMessage hashmap.
 * error messages are loaded into a hashmap errorMessage using LoadErrorMesssage method.
 * 
 * 
 * If there is no error, mathExpression is passed 
 * to InfixtoPostfix and converts it to postfix. The postfix is then passed to
 * postfixEvaluation which computes the value of the expression.
 * 
 * 
 * 
 */

package project_3;

import java.util.*;

public class ExpressionEvaluation 
{
	//create hashmap for errormessages.
	static HashMap<Integer, String> errorMessage = new HashMap<>();
	//create hashmap for character pairs.
	static HashMap<Character, Character> pair = new HashMap<>();
	
	//method that accepts mathExpression and yields boolean value
	public boolean expressionEvaluation(String statement)
	{
		//load hashmap pair
		loadPair();
		//load hasmap errormessage
		LoadErrorMessage();
		
		boolean error = false;
		
		//create stack
		Stack<Character> stack = new Stack<>();
		
		
		//loop iterates over all characters of the mathExpression
		for(int j = 0; j<statement.length(); j++)
		{
			char c = statement.charAt(j);
			
			//if left parenthesis and brackets are found, they are pushed to the stack.
			if(c == '(' || c == '{') 
			{
				stack.push(c);
			}
			
			//if right parenthesis is encountered...
			if(c == ')')
			{
				//if the stack is empty, print error message, assign boolean error, break the loop
				if(stack.isEmpty())
				{
					printError(0, 3);
					error = true;
					break;
				}
				//else.. pop the stack. if popped char does match equal expected pair from hashmap...
				//print error, assign boolean error and break loop 
				else
				{
					char PopedChar = stack.pop();
					if(!(PopedChar == pair.get(c)))
					{
						printError(j, 1);
						error = true;
						break;
					}
				}
			}
			//repeats last if statement but replaces parenthesis with bracket.
			if(c == '}')
			{
				if(stack.isEmpty())
				{
					printError(0, 3);
					error = true;
					break;
				}
				else
				{
					char PopedChar = stack.pop();
					if(!(PopedChar == pair.get(c)))
					{
						printError(j, 2);
						error = true;
						break;
					}
				}
			}
			//if the end of the statement has a left bracket or parenthesis, issue error, assign boolean value and break loop
			if(statement.charAt(statement.length()-1) == '{' || statement.charAt(statement.length()-1) == '(')
			{
				printError(statement.length()-1, 3);
				error = true;
				break;
			}
			
		}
		//if the stack IS NOT empty and no error was found, send error for incomplete expression, assign boolean error.
		if(!stack.isEmpty() && error == false)
		{
			printError(statement.length()-1, 3);
			error = true;
		}
		return error;
	}
	
	/*method printError accepts 2 ints. location corresponds to where the error was found.
	 * will print white space up to the location of the error
	 * prints a carrot after the white space to indicate position of the error.
	 * print error message using hashmap with errorNo as a parameter
	 */
	public static void printError(int location, int errorNo)
	{
		for(int i = 0; i<location; i++)
		{
			System.out.print(" ");
		}
		System.out.print("^ ");
		System.out.println(errorMessage.get(errorNo));
		
	}
	//method to load the pair hashamp with brackets. This is used for expected values above if-statements
	public static void loadPair()
	{
		pair.put('}', '{');
		pair.put(')', '(');
	}
	
	//method to load hashmap with error number and corresponding value.
	public static void LoadErrorMessage()
	{
		errorMessage.put(1, "} expected");
		errorMessage.put(2, ") expected");
		errorMessage.put(3, "Incomplete Expression");
	}




}
