# CloudAppK8
**Cloud Monitoring app on K8s with solution to problems/ hickups**

Monitoring app deploying locally which is going to get cpu and memory utilization metric {app.py}
In python we got several modules to do tasks, so we will use Psutil, it is the module needs to be imported in app.py

From <https://stackoverflow.com/questions/50316358/error-no-module-named-psutil> 
**##Run it in bash if psutil module not found**
$  python -m pip install psutil

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/67fb24f6-3255-4ba9-80d9-526857897569)



$  pip3 install -r requirements.txt (It will install dependencies required to be used overall locally)

$  python3 app.py (Run the app)

In browser move to localhost:5000 as port number used is 5000

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/2039c61a-e1a5-4168-babd-47b9f90c0740)

**Dockerizing app** {Dockerfile}
Creation of Dockerfile, Use the official Python image as the base image, Set the working directory in the container 
Copy the requirements file to the working directory, install requirements, Copy the application code to the working directory, Set the environment variables for the Flask app, Expose the port on which the Flask app will run, Start the Flask app when the container is run


$  docker build -t <image_name> .
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/ee845bb9-cead-44e8-bff8-c3f067b23c72)

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/b39b0a3c-5dfa-433f-ade3-eeafc89a1afe)


$  docker run -p 5000:5000 <image_name>
Now reload localhost:5000, app will run in browser via Docker container

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/ce970886-50c2-41f1-8eab-548460dc78c9)


NOTE: If error comes as below 
ERROR: failed to solve: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount386140250/Dockerfile: no such file or 
Directory
##check whether you have correct name for **Dockerfile** and you are in right directory while running the command

Use index.html from templates folder but it will require value change as per naming you are adding 
You put your template in the wrong place. From the Flask docs: Flask will look for templates in the **templates** folder
From <https://stackoverflow.com/questions/15053790/jinja2-exceptions-templatenotfound-error> 

**Pushing the Docker image to amazon Repository**
Create an ECR repository using Python code below, import boto3 {ecr.py}

$ pip install boto3 ##via terminal(if required)

**Create ecr.py**

import boto3
ecr_client = boto3.client('ecr')
**repository_name** = "cloud-native-repo"
response = ecr_client.create_repository(repositoryName=**repository_name**)
repository_uri = response['repository']['repositoryUri']
print(repository_uri)

$ Python ecr.py (via terminal run it to create ECR in AWS)
Uri will be created for ecr in aws (aws should be configured before hand)
Check AWS console search ECR there you have the URI

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/9837073b-85e0-4245-83bc-5647212ce8b1)

After all above commands -> wait for image to be pushed  (above commands can be checked in AWS console itself on created ECR page)

IAM Roles required for cluster and second one for node group

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/36874637-2ceb-4abb-a9ac-aa5ea22a965a)

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/3011f41b-102e-466f-89f1-5e5bb7d6c7ca)


Creating an EKS cluster in AWS console via GUI based mode and deploying the app using Python
Create an EKS cluster and add node group (it will require worker node IAM role so need to create it, you can click on right side in overview pane to know how and have the link to create directly while selecting IAM role in node group)
Create a node group in the EKS cluster. (Cluster created, now -> compute -> Node group -> Add nodegroup)
Create deployment and service {eks.py} Make sure to edit the image on line 25 with your image Uri.
IAM role won't appear until below steps are done

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/dc8fbd30-f9c4-41cc-b378-192bfa9ebf50)


$ kubectl get deployment -n default (check deployments)
$ kubectl get service -n default (check service)
$ kubectl get pods -n default (to check the pods) (it will take some time to be live as per system performance)

Once your pod is up and running, run the port-forward to expose the service
kubectl port-forward service/<service_name> 5000:5000

Check again your performance gauge is running on localhost:5000

![image](https://github.com/Groakss/CloudAppK8/assets/113557766/ad7ab61e-335a-4c3a-ae83-1b714ffcef0c)

