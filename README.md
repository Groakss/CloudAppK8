# CloudAppK8
**Cloud Native app on K8s with solution to problems or hickups**

Monitoring app deploying locally which is going to get cpu and memory utilization metric {app.py}
In python we got several modules to do tasks so we will use Psutil is the module needs to be imported in app.py

##Run it in bash if psutil module not found
python -m pip install psutil
From <https://stackoverflow.com/questions/50316358/error-no-module-named-psutil> 
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/67fb24f6-3255-4ba9-80d9-526857897569)

In browser move to localhost:5000 as port number used is 5000
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/2039c61a-e1a5-4168-babd-47b9f90c0740)

$ pip3 install -r requirements.txt (It will install dependencies required)
$ python3 app.py (Run the app)

**Dockerizing app**
Creation of Dockerfile, Use the official Python image as the base image, Set the working directory in the container 
Copy the requirements file to the working directory, install requirements
Copy the application code to the working directory, Set the environment variables for the Flask app
Expose the port on which the Flask app will run, Start the Flask app when the container is run

Terminal
$ docker build -t <image_name> .
$ docker run -p 5000:5000 <image_name>
Now same localhost:5000 app will run in browser 

**Pushing the Docker image to amazon Repository**
Create an ECR repository using Python, import boto3 {ecr.py}
pip install boto3 ##via terminal(if required)

Can use index.html from templates folder but it will require value change as per naming you are adding 
You put your template in the wrong place. From the Flask docs: Flask will look for templates in the **templates** folder
From <https://stackoverflow.com/questions/15053790/jinja2-exceptions-templatenotfound-error> 

NOTE: If error comes 
ERROR: failed to solve: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount386140250/Dockerfile: no such file or 
Directory
##check whether you have correct name for dockerfile and you are in right directory while running the command

Create ecr.py

import boto3
ecr_client = boto3.client('ecr')
**repository_name** = "cloud-native-repo"
response = ecr_client.create_repository(repositoryName=**repository_name**)
repository_uri = response['repository']['repositoryUri']
print(repository_uri)


Python ecr.py

Uri will be created for ecr in aws (aws should be configured before hand)



After all commands -> wait for image to be pushed 

Cluster created now go to compute -> Node group

IAM role won't appear until below steps are done
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/3f0e7a23-7e56-4188-9f88-d7f96131758f)
