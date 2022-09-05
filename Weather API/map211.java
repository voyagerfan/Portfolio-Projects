

/*Description:
 * map211 is a constructor that accepts the weatherInfo array, the map type and zoom level as parameters
 * weatherInfo elements are passed into string variables
 * string variables are concatenated into string "weather."
 * String weather, maptype and zoom are passed into the the writeHTML method.
 * lines 51-53 run html file from java code
 * 
 * writeHTML 
 * builds the HTML with the formating
 * creates myMap.html
 */

package project_2;

import java.util.*;
import java.io.*;
import java.awt.*;



public class map211  

{
	
	static String html;
	static String weather;
	static String mapFileName="myMap.html";
	static ArrayList<String> weatherInfo = new ArrayList<>();
	static String MapAPIKey ="Enter API Key here";
	
	map211 (ArrayList<String> weatherInfo, String mapType, int zoom) throws IOException 
	{
		//create string variable and set equal to elemts of the weatherInfo array
		String city = weatherInfo.get(0);
		String description = weatherInfo.get(1);
		String temp_current = weatherInfo.get(2);
		String temp_min = weatherInfo.get(3);
		String temp_high = weatherInfo.get(4);
		String rh_humidity = weatherInfo.get(5);  
		
		//concatenates all the variables and characters into a string.
		String weather = " " + city.toUpperCase() + " | " +  description + " | " + temp_current
		+ " | " + temp_min + " | " + temp_high + " | " + rh_humidity;
		
	    // write a HTML file
	    writeHTML(weather,city, mapType, zoom);

	    // run html file from java code
	    String url = mapFileName;   // you can find this html file in the project folder
	    File htmlFile = new File(url);
	    Desktop.getDesktop().browse(htmlFile.toURI());
	}
	
	public static void writeHTML(String weatherNow, String city, String mapType, int zoom)

	{
		html="<!DOCTYPE html>"
		+ "<html>"
		+ "<body>"
		+ "<h2>"
		+ "<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\" />"
		+ weatherNow
		+ "</h2>"
		+ "<iframe"
		+ "  width=1200"
		+ "  height=900"
		+ "  style=border:0"
		+ "  loading=lazy"
		+ "  allowfullscreen"
		+ "  referrerpolicy=\"no-referrer-when-downgrade\""
		+ "src=\"https://www.google.com/maps/embed/v1/place?key=" + MapAPIKey + "&q="+ city +"&zoom="+ zoom +"&maptype=" + mapType+"\""
		+ "</iframe>"
		+ "</body>"
		+ "</html>";
		
			
		  File f = new File (mapFileName);
		  try 
		  {
		     BufferedWriter bw = new BufferedWriter(new FileWriter(f));
		     bw.write(html);
		     bw.close();
		  } 
		  catch (IOException e) 
		  {
		    e.printStackTrace();
		  }
	}

	

}
