Server Client Communication
![Alpha Server and Client](https://storage.googleapis.com/awals-bucket/gemi/Screenshot%20(34).png)

In this project, I use Google Cloud Platform as the cloud provider. Main resource that we use is Compute Engine.

Documentation:
1. Creating google cloud project with sufficient permission to use compute engine.
2. Create VM instance with smallest size (f1-micro) both for the server and client.
3. Attach startup script on it's metadata, so that will automatically started when boot the VM.
4. For the alphaServer, there are two startup script (.sh). startupServerGCP.sh is use when creating the VM, and it will put startupServer.sh on /etc/profile.d/ directory, so that everytime it's ssh, it will shows the ssh metrics. The client server is use same mechanism too, script startupClientABC.sh or startupClientXYZ.sh is used when creating the VM.
5. After the VM instance has been created, we have to ssh to alpha-server first, after that, we can ssh to client node, and we can see the metrics in alpha-server window.
All process above can be done using this command in cloud shell:
git clone https://github.com/BangAwal/fintax-intern-test.git
cd fintax-intern-test/
gcloud compute instances create alpha-server --project=awal-deployment --zone=us-central1-a --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=automated-server,image=projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220805,mode=rw,size=10,type=projects/awal-deployment/zones/us-central1-a/diskTypes/pd-balanced --metadata-from-file startup-script=startupServerGCP.sh
gcloud compute instances create client-serverabc --project=awal-deployment --zone=us-central1-a --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=client-serverabc,image=projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220805,mode=rw,size=10,type=projects/awal-deployment/zones/us-central1-a/diskTypes/pd-balanced --metadata-from-file startup-script=startupClientABC.sh
gcloud compute instances create client-serverxyz --project=awal-deployment --zone=us-central1-a --machine-type=f1-micro --network-interface=network-tier=PREMIUM,subnet=default --tags=http-server,https-server --create-disk=auto-delete=yes,boot=yes,device-name=client-serverxyz,image=projects/ubuntu-os-cloud/global/images/ubuntu-1804-bionic-v20220805,mode=rw,size=10,type=projects/awal-deployment/zones/us-central1-a/diskTypes/pd-balanced --metadata-from-file startup-script=startupClientXYZ.sh
