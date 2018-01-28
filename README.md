# navigation

This task is to implement a small uWSGI application called GitHub navigator. It should be able to search GitHub repositories by given search term and present them as html page. The following requirements should be fulfilled:

How To Setup navigation project.
Step 1: Clone navigation project.
Step 2: Create virtual env for navigation project.
Step 3: Now activate virtual env and move your navigation directory. ex: 
       a). activate virtual env.
	       source env/bin/activate
	   b). cd /var/www/navigation/
	   c). Install all dependency using below cmd:
	       pip install -r requirements.txt
Step 4: Now run your server using below cmd:
        python manage.py runserver 0.0.0.0:9000

Step 5: Now open browser and type url as given below:
       http://0.0.0.0:9000/index/
Step 6: Now Type repo name whose you want to search in text box.
        and click on search button.
Step 7: Now wait and see top 5 sorted Repository information.
