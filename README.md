# Blockchain-Implemnentation
Introduction
The goal of this step in the blockchain implementation process is to identify that the selected blockchain should be capable of operating on a personal computer at home, in the office, or even on a laptop running Windows, macOS, or Linux. Details on how to set up and run Simple Python Terminal-Based Blockchain will be given in this section. We will also describe the required software dependencies and environmental assumptions and discuss possible tips to avoid troubles.
1. Some of the assumptions about the environment are as follows:
Before diving into the setup, let's clarify the assumptions regarding the system environment:
•	Operating System: The blockchain is built to work in Windows 10 or a newer version, macOS (Catalina and above), and primary Linux distributions (Ubuntu 20.04 and newer, for example).
•	Python Version: Python version 3.8 and above is mandatory. This version was chosen because it is one of the most stable and popular. Make sure that you have the option to select Python from the system Path and command option.
•	Internet Connection: Although the blockchain does not have to use the Internet, it is needed to download libraries (if they are not already present).
•	Hardware Requirements: The blockchain implementation will be light, requiring an average and modern PC with at least 4GB RAM and a 1 GHz processor.
2.Pre-Requisites & Dependent Services
To get started, ensure that your system has the following software installed:
•	Python 3.8+: You can download Python from python.org. For instance, Add Python to PATH.’
•	Pip (Python Package Installer): This often forms part of the Python package. To check if pip is installed, run:
 
•	Text Editor or IDE: It can be done with any code editor (for example, VS Code PyCharm or Sublime Text), although it’s not mandatory.
•	Required Python Libraries:The Simple Python Blockchain uses standard Python libraries: hashlib, DateTime, and JSON. Consequently, no other installations are necessary, making it very movable.


Exploring the Blockchain
•	Viewing and Blockchain: The Script causes it to print details of each block: the block index, timestamp, data, previous hash and hash.
•	Adding New Blocks: You configure the Script to automatically add new blocks in sequence. To add new data for each block you can change the blockchain.py file.
Troubleshooting and Common Issues: 
Python Not Recognized: If you are getting an error says python is not recognised as an internal or external command then make sure python is added to your system’s PATH. You can do this by external command, make sure Python and selecting the option to modify the environment variables.
Outdated Python Version: If your system has an outdated version of Python (test your Python version), then using pyenv for (Linux/macOS) or downloading the latest Windows installer.



