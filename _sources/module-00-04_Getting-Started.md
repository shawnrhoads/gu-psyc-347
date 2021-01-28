# Getting Started

We will walk through setting up the course software on the first day of class.

## Download Anaconda 3
[Anaconda](https://www.anaconda.com/products/individual#Downloads) is an open-source distribution of the Python and R programming languages for scientific computing. We will be using it throughout the course.

## Clone repository or Download YAML file

**Using Git**</br>
In your terminal, use command: `git clone https://github.com/shawnrhoads/gu-psyc-347`

Once the download completes, change your directory to 'gu-psyc-347' (for example, using the command `cd gu-psyc-347`)

**Using the file explorer / finder**</br>
Alternatively, you can create a directory somewhere on your computer called `gu-psyc-347` and just [download this .yml file](https://raw.githubusercontent.com/shawnrhoads/gu-psyc-347/master/course-env.yml) to that directory. Then, open your terminal and change your directory (for example, using the command `cd gu-psyc-347`)

## Create Anaconda environment
Create a new Anaconda environment using the command: `conda env create -f course-env.yml`

## Activate your Anaconda environment
Activate your environment, using the command: `conda activate gu-psyc-347`