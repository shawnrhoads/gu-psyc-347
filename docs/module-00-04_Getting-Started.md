# Getting Started



## 1. Downloading Anaconda 3
[Anaconda](https://www.anaconda.com/products/individual#Downloads) is an open-source distribution of the Python and R programming languages for scientific computing. We will be using it throughout the course.

You can follow [these instructions](https://docs.anaconda.com/anaconda/install/) to install Anaconda for your operating system.

## 2. Creating the Anaconda environment

### Downloading YAML file (Option A)
If you would like to download files in a piecewise fashion (i.e., one at a time), then follow these instructions. If you would like to download the entire GitHub repository with all of the files, then follow the instructions for Option B.

**Using the course-env.yml file**</br>
Download this [course-env.yml](https://raw.githubusercontent.com/shawnrhoads/gu-psyc-347/master/course-env.yml) file into any directory on your local computer (i.e., ~/Desktop/gu-psyc-347/course-env.yml).

Once the download completes, change your directory to 'gu-psyc-347' (for example, using the command `cd gu-psyc-347`)

### Cloning GitHub repository (Option B)
If you would like to download the entire GitHub repository with all of the files, then follow these instructions. If you would like to download files in a piecewise fashion (i.e., one at a time), then follow the instructions for Option A.

**Using Git**</br>
In your terminal, use command: `git clone https://github.com/shawnrhoads/gu-psyc-347`

Once the download completes, change your directory to 'gu-psyc-347' (for example, using the command `cd gu-psyc-347`)

**Using the file explorer / finder**</br>
Alternatively, you can download this [.zip file](https://github.com/shawnrhoads/gu-psyc-347/archive/master.zip) and unzip it in a directory somewhere on your computer. Then, open "Anaconda Prompt" (Windows) or Terminal (MacOS) and change your directory. For example: 
- MacOS: cd ~/Desktop/gu-psyc-347-master
- Windows: cd "C:\Users\USERNAME\Desktop\gu-psyc-347-master"

### Creating the gu-psyc-347 environment
If you previously created an environment called `gu-psyc-347`, then let's remove first using this command: `conda remove --name gu-psyc-347 --all`. 

Alternatively, you can just update the environment using the command: `conda env update --file course-env.yml`.

Create the course environment using this command: `conda env create -f course-env.yml`.

This will install the packages listed in the [course-env.yml](https://raw.githubusercontent.com/shawnrhoads/gu-psyc-347/master/course-env.yml) file (please check that you have the most up-to-date version).

## 3. Activating your Anaconda environment
**Before running any notebooks related to this course**, activate the course environment using the command: `conda activate gu-psyc-347`.

## Opening Jupyter Notebook
Once you've completed all of the steps above, you should be able to run Jupyter Notebook with all of the required packages for the course using the command: `jupyter notebook`.

## Troubleshooting
If you followed all of the steps above, but are experiencing issues, then you might have to update the Anaconda environment that we use for the course. To do this, download the most up-to-date version of the [course-env.yml](https://raw.githubusercontent.com/shawnrhoads/gu-psyc-347/master/course-env.yml) file, navigate to the directory that you downloaded this file to, and run the command: `conda env update --file course-env.yml`

If you are still experiencing issues, check that you've first run the command  `conda activate gu-psyc-347` before opening Jupyter Notebook using the command `jupyter notebook`.