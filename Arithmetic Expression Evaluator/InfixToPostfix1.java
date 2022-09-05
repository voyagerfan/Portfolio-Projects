/*
 * 
 * Program Description:
 * 
 * String post is in intialized
 * Hashamp precedence is created to store the key value pairs for operators.
 * 
 * Mehthod infix2postfix:
 * This method will create 'stack' and loads the precedence values from
 * the method "loadPrecendence." infix2postfix method accepts the infix string 
 * where each char is iterated over a loop. The postfix statement is created by 
 * the series of if-else statements which will add the appropriate chars to 'post'.
 * 
 * loadPrecedence method:
 * This method adds key-value pairs for the operator precedence. It is below in the 
 * if-else block  (c == '+' || c == '-' || c == '*' || c == '/'). 
 * See below for more details.
 */



package project_3;

import java.util.*;


public class InfixToPostfix 
{

	static String post = "";
	static HashMap<Character, Integer> precedence = new HashMap<>();
	
	//infix2postfix method accepts string variable from mathExpression in MyExpressionTest.java
	public String infix2postfix (String infix)
	{ 
		//creates an object of the stack class called stack
		Stack<Character> stack = new Stack<Character>();
		
		//calls the precedence method below and hashmap "precedence" with key value pairs
		loadPrecedence();
		
		post = "";
		
		//for loop interates for the infix string
		for (int j = 0; j<infix.length(); j++)
		{
			//creates the variable c which folds the character in the current iteration
			char c = infix.charAt(j);
			
			//if c is a number between 0-9, it is added to the post variable expression
			if(c>='0' && c<='9')
			{
				post += c;
			}
			//pushes the character ( or { onto the stack
			else if (c == '('|| c == '{')
			{
				stack.push(c);
			}
			//if loop encounters right parenthesis...
			else if (c == ')')
			{
				char p = ' ';
				//if top of stack does not equal left parenthesis 
				if(stack.peek() != '(')
				{
					//pop the stack while there is no left parenthesis
					while(!(stack.peek() == '(')) 
					{
						p = stack.pop();
						post += p;
					}
				}
				stack.pop(); // throws away '('
			}
			//if loop encounters right bracket...
			else if(c == '}')
			{
				char p = ' ';
				//if stop of stack does not equal left bracket...
				if(stack.peek() != '{')
				{
					//pop stack while there is no left parenthesis
					while(!(stack.peek() == '('))
					{
						p = stack.pop();
						post += p;
					}
				}
				stack.pop();
			}
			//if an operator is encountered...
			else if(c == '+' || c == '-' || c == '*' || c == '/')
			{
				/*pop the stack and add it to post variable while stack is empty and 
				 * priority of stack is higher than c.
				 */
				while(!stack.isEmpty() && (precedence.get(stack.peek()) >= precedence.get(c)))
				{
					char p = stack.pop();
					post += p;
					
				}
				//pushes operator to the stack
				stack.push(c);
			}	
		}
		//adds all elements of the stack to post variable
		while(!stack.isEmpty())
		{
			char p = stack.pop();
			post +=p;
		}
		
		return post;
		
	}
	//method to load hashmap with operator and key value pairs for precendence.
	public static void loadPrecedence()
	{
		precedence.put('+', 1);
		precedence.put('-', 1);
		precedence.put('*', 2);
		precedence.put('/', 2);
		precedence.put('(', 0);
		precedence.put('{', 0);
	}
}
