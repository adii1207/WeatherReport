# WeatherReport
#HOW TO THE API'S

- Create a virtual environment and activate the virtual environment
- add the required packages with command "pip install python django djangorestframework requests pandas djangorestframework-simplejwt"
- also we need to install few more packages with commands "pip install openmeteo-requests requests-cache retry-requests numpy"
- in the terminal navigate to the folder Weatherdata
- start the django server using the command - "python manage.py runserver"
- api will be accesible at "http://127.0.0.1:8000/"
- register a user using the POST  api "http://127.0.0.1:8000/weather-data/register/" with the payload { "username":"testuser1","password":"1system@"}, add the username and password
- get the jwt token using the POST api "http://127.0.0.1:8000/api/token/" with the payload  { "username":"testuser1","password":"1system@"}, use the username and password as per the given username in above api
- use the "access_token" generated from "http://127.0.0.1:8000/api/token/" and hit the GET api "http://127.0.0.1:8000/weather-data/report/?latitude=52.52&longitude=13.41&past_days=10", You can change the values of latitude , longitude and past_days

  
This Project uses django rest framework because it has several advantages:
Rapid Development: DRF provides a powerful and flexible toolkit for building Web APIs, allowing for rapid development of API endpoints, serialization, authentication, and more.

Serialization: DRF's serialization capabilities make it easy to convert complex data types, such as querysets and model instances, into native Python data types that can be rendered into JSON, XML, or other content types.

Authentication: DRF provides built-in support for various authentication methods, including token-based authentication, session authentication, OAuth, and more. This makes it easy to implement secure authentication for your API endpoints.

Authorization: DRF includes a flexible and customizable permissions system, allowing you to control access to API views based on user roles, groups, or other criteria.

Browsable API: DRF's browsable API functionality provides a web-based interface for exploring API endpoints, making it easy to understand and test the API without additional tools.

Support for Relationships: DRF supports relationships between different data models, allowing for easy representation of related data in API responses.

Throttling: DRF includes a built-in throttling system to prevent abuse of your API by limiting the number of requests that clients can make.

Extensive Documentation: DRF has extensive and clear documentation, making it easy for developers to learn and understand how to use its features.

Community and Ecosystem: DRF has a large and active community, with many third-party packages, tutorials, and resources available to help with common tasks and challenges when building RESTful APIs.
