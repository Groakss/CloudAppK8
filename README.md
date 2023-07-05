# CloudAppK8
**Cloud Native app on K8s**

Monitoring app which is going to get cpu and memory utilization metric
In python we got several modules to do tasks so we will use Psutil is the module needs to be imported in app.py

##Run it in bash if psutil module not found
python -m pip install psutil
From <https://stackoverflow.com/questions/50316358/error-no-module-named-psutil> 
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/67fb24f6-3255-4ba9-80d9-526857897569)

89
You put your template in the wrong place. From the Flask docs:
Flask will look for templates in the templates folder

From <https://stackoverflow.com/questions/15053790/jinja2-exceptions-templatenotfound-error> 

NOTE: If error comes 
ERROR: failed to solve: failed to read dockerfile: open /var/lib/docker/tmp/buildkit-mount386140250/Dockerfile: no such file or 
Directory

check whether you have correct name for dockerfile and you are in right directory

Install boto3 if required

Create ecr.py


import boto3
ecr_client = boto3.client('ecr')
repository_name = "cloud-native-repo"
response = ecr_client.create_repository(repositoryName=repository_name)
repository_uri = response['repository']['repositoryUri']
print(repository_uri)


Python ecr.py

Uri will be created for ecr in aws (aws should be configured before hand)



After all commands -> wait for image to be pushed 

Cluster created now go to compute -> Node group

IAM role won't appear until below steps are done
![image](https://github.com/Groakss/CloudAppK8/assets/113557766/3f0e7a23-7e56-4188-9f88-d7f96131758f)
