# Url Shortener

This is a simple Django app, that consist of two parts: api and service for making your urls shorter.   

As I mentioned, you can use API, to cut your url, and get special token. Send POST request to /translate/ url with "short_url=[token]" as data , and you will be redirected to your destination.
        
        API endpoints: 
            - /api/<str:token> - for GET requests:
                    to get the real url of <token>  
                returns {'real_url': <real_url>}

            - /api/ - for POST requests:
                    you have to pass {'real_url': <url>} as a request data
                returns {'short_url': <token>}
----------------------

You may also use shortener service instead of API:  <br/>

In order to cut the link: <br/>
<img src="https://github.com/kinfi4/UrlShortener/blob/main/docs/screenshots/2.png?raw=true"  alt="main window" width="49%"/>
<img src="https://github.com/kinfi4/UrlShortener/blob/main/docs/screenshots/3.png?raw=true"  alt="main window" width="49%"/>
<br/>

If you want to translate the link: <br/>
<img src="https://github.com/kinfi4/UrlShortener/blob/main/docs/screenshots/1.png?raw=true"  alt="main window" width="49%"/>
<br/>
It also checks if this token exists