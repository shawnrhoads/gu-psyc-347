# Getting Started

We will walk through setting up the course software on the first day of class.

## Download Anaconda 3
[Anaconda](https://www.anaconda.com/products/individual#Downloads) is an open-source distribution of the Python and R programming languages for scientific computing. We will be using it throughout the course.

You can follow [these instructions](https://docs.anaconda.com/anaconda/install/) to install Anaconda for your operating system.

## Clone repository or Download YAML file

**Using Git**</br>
In your terminal, use command: `git clone https://github.com/shawnrhoads/gu-psyc-347`

Once the download completes, change your directory to 'gu-psyc-347' (for example, using the command `cd gu-psyc-347`)

**Using the file explorer / finder**</br>
Alternatively, you can download this [.zip file](https://github.com/shawnrhoads/gu-psyc-347/archive/master.zip) and unzip it in a directory somewhere on your computer. Then, open "Anaconda Prompt" (Windows) or Terminal (MacOS) and change your directory. For example: 
- MacOS: cd ~/Desktop/gu-psyc-347-master
- Windows: cd "C:\Users\USERNAME\Desktop\gu-psyc-347-master"

## Create Anaconda environment
If you previously created an environment called `gu-psyc-347`, then let's remove first using this command: `conda remove --name gu-psyc-347 --all` 

Create the course environment using this command: `conda env create -f course-env.yml`

This will install the packages listed in the [course-env.yml](https://raw.githubusercontent.com/shawnrhoads/gu-psyc-347/master/course-env.yml) file.

## Activate your Anaconda environment
Activate the course environment using this command: `conda activate gu-psyc-347`
