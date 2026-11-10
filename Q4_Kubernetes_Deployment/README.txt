QUESTION 4 - KUBERNETES DEPLOYMENT WITH 2 REPLICAS

REQUIREMENTS
- kubectl installed
- A running Kubernetes cluster (for a beginner, Docker Desktop Kubernetes is one option)

STEP 1: Open Docker Desktop.
STEP 2: Open Settings > Kubernetes and enable Kubernetes, if this option is available.
    Click Apply / Restart and wait until Kubernetes is running.
    (Alternatively, use a configured Minikube or cloud Kubernetes cluster.)

STEP 3: Open a terminal and verify kubectl:
    kubectl version --client
    kubectl get nodes

If kubectl get nodes shows a Ready node, your cluster is available.

STEP 4: Open this Q4_Kubernetes_Deployment folder in VS Code.
STEP 5: Open Terminal in this folder.
STEP 6: Apply the deployment YAML:
    kubectl apply -f deployment.yaml

EXPECTED RESPONSE:
    deployment.apps/sample-deployment created

STEP 7: Check the deployment:
    kubectl get deployments

STEP 8: Check the pods:
    kubectl get pods

EXPECTED RESULT
You should see two pods with names beginning with sample-deployment-.
Both should eventually show STATUS Running and READY 1/1.

STEP 9: Check details:
    kubectl describe deployment sample-deployment

STEP 10: If pods are still starting, wait a few seconds and run:
    kubectl get pods

STEP 11: Delete the deployment after your practical (optional):
    kubectl delete -f deployment.yaml

IMPORTANT
- replicas: 2 means Kubernetes tries to keep two copies of the application running.
- The YAML uses the public nginx:latest container image.
- Applying the file requires a working Kubernetes cluster. kubectl alone is not a cluster.
- If kubectl get nodes reports connection refused or no context, start/configure
  your cluster and check the selected context with:
    kubectl config current-context
