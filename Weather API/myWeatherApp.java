

/* Description:
 * myWeatherApp.java contains main method and static methods inputCityName() and getWeatherInfo()
 * main method calls inputCityName() first then calls getWeatherInfo.
 * 
 * inputCityName():
 * has while loop for with boolean validCityName as a condition. If an exception is caught in cityWeather, 
 * the catch clause makes validCityName false and impacts the while loop
 * Inside this while loop, console input is assigned to String city.
 * city is passed to "boolean valid = weather211.CityWeather(city)". If the city is valid, IF statements
 * will execute. mapType and zoom levels are collected in the IF statements
 * 
 * If city is invalid, the else the statement executes ("try again") and loops to the top of the while loop.
 * 
 * getWeatherInfo()
 * weather211.getCityWeatherNow() is passed into the weatherInfo arraylist
 * arraylist weatherInfo is printed.
 * map211 is called which accepts weatherInfo, mapType, zoom. This method writes the HTML and creates 
 * myMap.Html
*/

package project_2;

import java.util.ArrayList;
import java.util.Scanner;

public class myWeatherApp
{
	
	static Scanner consol = new Scanner(System.in);
	private static ArrayList<String> weatherInfo = new ArrayList<>();
	static String mapType;
	static int zoom;

	public static void main(String[] args) throws Exception
	{
		System.out.println("Welcome to Weather 211 - Summer 2022");
		System.out.println();
		
		inputCityName();
		getWeatherInfo();
	}

	public static void inputCityName() throws Exception
	{
		boolean validCityName = false;
		while(!validCityName)
		{
			System.out.println("Input a city name: ");
			//stores console input into city
			String city = consol.nextLine();
			System.out.println();
			//city is passed into cityweather method
			boolean valid = weather211.CityWeather(city);
			
			if(valid)
			{
				System.out.println("Select a map type: " + "  " + "1) roadmap" + "  " + "2) satellite");
				//consol.nextInt is assigned to scanner variable "input"
				int input = consol.nextInt();
				//Variable mapType is of type String. If statements correlate to the map type specified.
				if (input == 1)
				{
					mapType = "roadmap";
				}
				if(input == 2)
				{
					mapType = "satellite";
				}
				System.out.println();
				System.out.println("Select a zoom level of the map: " + " " + "0 ~ 21 " + "(default = 14)");
				//console input is passed to zoom.
				zoom = consol.nextInt();
				break;
			}
			//executes if city is invalid
			else
			{
				System.out.println("invalid city name. Try again. \n");
				continue;
			}
		}
	}
	
	public static void getWeatherInfo() throws Exception 
	{
			//array elements are passed into weatherInfo
		   weatherInfo=weather211.getCityWeatherNow();
		 
		   // print text version
		   for (int i=0; i<weatherInfo.size(); i++) {
		      System.out.println(weatherInfo.get(i));
		   }
		 
		  // call Map211
		  new map211(weatherInfo, mapType, zoom);
	}
	
	
	
}
