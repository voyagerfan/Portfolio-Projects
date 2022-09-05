/* 
 * Program description:
 * The program requests a math expression from the user. The user
 * enters the math expression which is stored in a string variable
 * and passed to the expressionEvalation method. expressionEvaluation
 * iterates over the string variable and evaluates each char
 * against conditional if-statements which if met, will assign a boolean
 * "error" to true or false. If true, an error message is printed and the 
 * while loop main re-starts. If there is no error, mathExpression is passed 
 * to InfixtoPostfix and converts it to postfix. The postfix is then passed to
 * postfixEvaluation which computes the value of the expression.
 * 
 * entering 0 for mathExpression will terminate the program.
 * 
 */

package project_3;

import java.util.*;


public class MyExpressionTest {

	static String mathExpression;
	static Scanner input = new Scanner(System.in);
	static HashMap<Integer, String> errorMessage = new HashMap<>();
	
	//initiates boolean run to true.
	static boolean run = true; 
	
	
	
	public static void main(String[] args) 
	{
		
		LoadErrorMessage();
		boolean error = false;
		//executes statements in while loop until run = false
		while (run)
		{
			System.out.println("\nEnter a math expression: ");
			mathExpression = input.nextLine();
			
			if(mathExpression.equals("0"))
			{
				System.out.println("Bye!");
				run = false;
				break; 
				
			}
			else
			
			{
				//creates object ee of Expression evaluation class.
				ExpressionEvaluation ee = new ExpressionEvaluation();
				
				/* passes mathExpression to expressionEvaluation and yield boolean true or false
				 * will boolean error will either send error if found or if no error found, continue
				 * to next if statement
				 */
				error = ee.expressionEvaluation(mathExpression);
				

			}
			//if no error found, execute statements
			if(!error)
			{
				/* creates an object of InfixToPostfix
				 * sends expression
				 * receives postfix 
				 */
				
				InfixToPostfix i2p = new InfixToPostfix();
				String postfix = i2p.infix2postfix(mathExpression);
				
				 /* creates an object of PostfixEvaluation
				 * sends postfix 
				 * receives the result
				 */
				PostfixEvaluation pe = new PostfixEvaluation();
				int result = pe.postfixEvaluation(postfix);
				
				//prints results
				System.out.println("infix: " + mathExpression);
				System.out.println("postfix: " + postfix);
				System.out.println("result: " + result);
			}
			
		}

	}
	
	public static void LoadErrorMessage()
	{
		errorMessage.put(1, "} expected");
		errorMessage.put(2, ") expected");
		errorMessage.put(3, "Incomplete Expression");
	}
	
}
