Weather Check Script

This script allows you to check the current weather conditions for a specified city. It utilizes the requests library to retrieve weather data from the openweathermap.org API. To use this script, you'll need to obtain an API key from openweathermap.org and replace the placeholder xxxxxxxxxxxxxxxxxxxxx with your actual API key.

Prerequisites:

    Install the requests library using the command pip install requests.

    Create a free account on openweathermap.org and obtain an API key.

    Replace the placeholder xxxxxxxxxxxxxxxxxxxxx in the script with your API key.

Usage:

    Execute the script by running python weather_check.py.

    Enter the name of the city you want to check the weather for.

    The script will display the current temperature and weather description for the specified city.

Code Breakdown:

    Import the requests library to make HTTP requests.

    Define the API key variable.

    Prompt the user to enter the city name.

    Construct the URL for the weather data endpoint using the city name and API key.

    Send a GET request to the API endpoint using the requests library.

    Check the response status code. If it's 200 (OK), proceed to parse the JSON response.

    Extract temperature and weather description from the JSON data.

    Print the temperature and weather description for the user.

    If the response status code is not 200, print an error message.
