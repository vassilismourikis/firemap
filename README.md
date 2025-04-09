#---------------------------------------------USEFUL LINKS---------------------------------------------

https://github.com/moabukar/CKA-Exercises

#---------------------------------------------Prerequisites ---------------------------------------------

#Install kubectl on Linux

curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client

#To install the latest minikube stable release on x86-64 Linux using Debian package:

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb

#---------------------------------------------To start your local cluster---------------------------------------------

minikube start

#---------------------------------------------sync registry with your local docker---------------------------------------------

# Start minikube
minikube start

# Set docker env
eval $(minikube docker-env)             # Unix shells
minikube docker-env | Invoke-Expression # PowerShell

# Build image
docker build -t foo:0.0.1 .

# Run in Minikube
#For yaml:
You always have to set imagePullPolicy: IfNotPresent. This tells Kubernetes: "Use the local image if available, don’t try pulling it from Docker Hub." 
#With command:
kubectl run hello-foo --image=foo:0.0.1 --image-pull-policy=IfNotPresent

# Check that it's running
kubectl get pods

#after that your docker wont work locally so you have to unset all env vars set by minikube: 

unset DOCKER_TLS_VERIFY
unset MINIKUBE_ACTIVE_DOCKERD
unset DOCKER_CERT_PATH
unset DOCKER_HOST

#---------------------------------------------NOTES---------------------------------------------

#Since Minikube doesn’t run on real cloud infrastructure, it doesn’t automatically provision cloud load balancers. But minikube tunnel acts like one by:
Creating a routable IP on your machine
Mapping that IP to your LoadBalancer service

minikube tunnel
