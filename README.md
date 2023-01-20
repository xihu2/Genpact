# Genpact Pet API project & UI Web project
##**Environment setup:**

* need python 3.11 (run $ python --version)
* need requests, pytest, selenium packages
* to check if pytest, requests, selenium are installed
	* $ pip list 
* to install pytest, requests packages
	* $ pip install pytest
	* $ pip install requests
	* $ pip install selenium




##**Test structures:**
* all test cases and scripts are located under Genpact/python directory
	* testGet.py is testing all the functionalities for Get API
	* testPost.py is testing all the functionalities for Post API
	* testPut.py is testing all the functionalities for Put API
  	* testDelete.py is testing all the functionalities for Delete API
	* petAPITest_script.sh is the shell scripts to run all above tests together
	* testUI.py is testing all UI Web pages
	* UITest_script.sh

* all documentations are under Genpact/document directory
	* TestUseCases.docx contains the test plan and the details about test cases
	* PetAPIBugList.xlsx contains the list of the bugs
	* test_run_Results.txt contains the Terminal run result for all the test cases

	


##**Test case run steps:**
* run python test by category under Genpact/python
	* $ pytest testGet.py -v
 	* $ pytest testPost.py -v
 	* $ pytest testPut.py -v
        * $ pytest testDelete.py -v
	* $ pytest testUI.py -v
 
* run shell script to run all the API test cases under Genpact/python
 	* $ ./petAPITest_script.sh
	
* run shell script to run the UI web test cases under Genpact/python
 	* $ ./UITest_script.sh
 
	
* setup daily test shell script CI run in Jenkins
