

/*Description:
 * weather211 class contains 2 methods and a private static array weatherInfo
 * 
 * cityWeather() 
 * Takes cityName as a parameter.
 * Starts with boolean validCityName = false. Boolean is returned false if an exception is found in the 
 * try block. This impacts the while loop in myWeatherApp.java.
 * The try block:
 * - creates the URL for the weather info.
 * - buffered reader object br is created and reads the URL
 * - jsonparser parses object br and data is stored in myObject.
 * 1 - city name is added to array
 * 2 - Adds the weather info to the array using HashMap methods.
 * 3, 4, 5 - adds temp, templow and temphigh to the arraylist array using HashMap methods. 
 *  each is converted to degrees F
 * 6 - adds humidity to the arraylist using hashmap methods.
 * end of the try block contains a boolean validCityName = true which impacts the while loop in myWeatherApp.
 * 
 * getCityWeatherNow()
 * This is an accessor method that returns the weatherInfo array since it is private. The method is used
 * in getWeatherInfo() which is run in main.
 */

package project_2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;


import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.JSONArray;
import java.util.*;




public class weather211 
{
	
	private static ArrayList<String> weatherInfo = new ArrayList<>();
	
	public static boolean CityWeather (String cityName) throws Exception
	{
		boolean validCityName = false;
		
		try 
		{
			
			///create a URL instance
			String firstPartURL = "https://api.openweathermap.org/data/2.5/weather?q=";
			String secondPartURL ="&appid=Enter API Key Here"; 
			String theURL = firstPartURL + cityName + secondPartURL;
			URL url = new URL(theURL); 

			///Reads information from URL    
			BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
			
			//JSON parser object to parse read file
			JSONParser jsonParser = new JSONParser();
			//Read JSON file. All the data for the city is stored in “myObject"
			JSONObject myObject = (JSONObject)jsonParser.parse(br); 
			
			// 1. add city name to the data structure 
			 weatherInfo.add(cityName);

			// 2. Weather 
			JSONArray weatherArray = (JSONArray)myObject.get("weather");
			JSONObject w = (JSONObject) weatherArray.get(0);
			 // get weather info from weatherarray
			String weatherNow =(String) w.get("description");
			 // add weather info to the data structure 
			weatherInfo.add(weatherNow);   
		
			// 3. Temp  
			// get temp from myObject
			double cityTemp = (double)((JSONObject) myObject.get("main")).get("temp");
			cityTemp = ((cityTemp - 273.15)*9)/5 + 32;///convert to Fahrenheit;
			String tempNow="temp: "+ String.format("%.1f", cityTemp)+"\u00B0"; 
			// add temp to the data structure 
			weatherInfo.add(tempNow);    
			
			// 4. Temp_min  
			// get temp_min from myObject 
			double cityTempMin = (double)((JSONObject) myObject.get("main")).get("temp_min");
			cityTempMin = ((cityTempMin - 273.15)*9)/5 + 32;///convert to Fahrenheit;   
			String tempLow="Low: " + String.format("%.1f", cityTempMin) + "\u00B0";
			// add temp to the data structure 
			weatherInfo.add(tempLow); 
			
			// 5. Temp_high   
			// get temp_high from myObject 
			double cityTempHigh = (double)((JSONObject) myObject.get("main")).get("temp_max");
			cityTempHigh = ((cityTempHigh - 273.15)*9)/5 + 32;///convert to Fahrenheit;   
			String tempHigh = "High: " + String.format("%.1f",cityTempHigh) + "\u00B0";
			weatherInfo.add(tempHigh);
			
			
			// 6. Humidity 
			// get humidity from myObject 
			
			long cityHumidity = (long)((JSONObject) myObject.get("main")).get("humidity");
			String humidity = "humidity: "+ Long.toString(cityHumidity)+"%";
			// add humidity to the data structure 
			weatherInfo.add(humidity);
			validCityName = true;
		
		}
		catch(Exception ex)
		{
			validCityName = false;
			
		}
		
		return validCityName;
		
	}
	
	public static ArrayList <String> getCityWeatherNow()
	{
		return weatherInfo;
	}
	
	
		
	

}
