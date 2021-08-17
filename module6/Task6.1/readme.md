# Task 6.1 Report
## 1 Create virtual machine connection according to task
### VM-1 Setup
Netplan
`sudo nano /etc/netplan/00-installer-config.yaml`

![](Screenshots/S1.png)

`sudo netplan apply`

Ifconfig

![](Screenshots/S2.png)

I implied default ufw rules:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
```
### VM-2 Setup
Netplan

![](Screenshots/S3.png)

ifconfig

![](Screenshots/S4.png)

I implied default ufw rules:
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw enable
```
Let's ping VM-1 from VM-2

![](Screenshots/S5.png)

### NAT (MASQUERADE) setup on VM-1
Enable ip-forwarding - `sudo echo 1 > /proc/sys/net/ipv4/ip_forward`
Apply ufw forwarding policy - `sudo ufw default allow forward`
Apply nat table rules and traffic forwarding via NAT interface using /etc/ufw/before.rules file

![](Screenshots/S6.png)

After applying this settings we need to reload firewall - `sudo ufw reload`

Let's try to ping our host machine

![](Screenshots/S7.png)
 
## 2 Check the route from VM2 to host
![](Screenshots/S8.png)
## 3 Check the access to the Internet, (just ping, for example, 8.8.8.8)
![](Screenshots/S9.png)
## 4 Determine, which resource has an IP address 8.8.8.8
![](Screenshots/S10.png)
## 5 Determine, which IP address belongs to resource epam.com
![](Screenshots/S11.png)
## 6 Determine the default gateway for your HOST and display routing table
![](Screenshots/S12.png)
## 7 Trace the route to google.com
![](Screenshots/S13.png)
