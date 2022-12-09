# Python Script | ISIS Details Report

The code provided in this sample allows uses PyATS genie to parse 'show isis' operations on NXOS for Instance ID, Area, System ID, VRF, Interface, IP address assigned, and Subnet.

# How to install

Download or clone this repository to a system where you can access your remote hosts.  If you have PyATS installed, you can skip to "How to run".  If you do not have PyATS installed, run 'pip install -r requirements' to ensure that you have PyATS installed.  If you are operating on a system without internet access, run the following steps to get PyATS installed on your system.  Run these steps on a linux machine with access to the internet.

* mkdir pyatsDir
* python3 -m pip download pyats'[full]' -d ./pyatsDir 

Copy the pyatsDir to your destation server and run the below command.

* python3 -m pip install pyats'[full]' --no-index --find-links pyatsDir/

# How to run

cd into the repository directory.  Add your genie testbed file to the folder.  If you do not have a testbed file created, run the following commands:

* genie create testbed interactive --output *testbed*.yaml (you can leave the name as testbed.yaml or call it what you want)
* Follow the interactive process to add your hosts
* Once complete you'll need to update the isis_report.py file with the name of your file

From the repository directory, use your favorite editor (vi / nano) and change line 29, testbed = testbed.load('isis_testbed.yaml'), with the testbed file of your system.  Once complete, save the file and run *python isis_report.py*.  After running the file you'll have a report called "isis_routing_details.csv" in your repository directory. 