1. We created a virtual env in our system
	- the "get-ExecutionPolicy" was Restricted
	- we had to make it Unrestricted by going through Powershell (in Administrator mode) with "Set-ExecutionPolicy Unrestricted -Scope Process" command
	- after that use "virtualenv env" command
	- then activate the virtual env with "env\Scripts\activate.ps1" (.bat file did not work)

2. Install required packages into that virtual env
	- pip install flask
	- pip install -U scikit-learn

3. Download Postman to test http calls

4. run flask server
	- python server.py