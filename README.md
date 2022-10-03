### face-mask-detector


##A.R.M.D - A Robotics Mask Detector
A robotics mask detector that detects masks and indicate using leds.


A.R.M.D is a AI and Ml based project. It uses a camera to detect faces and further face masks. During this Corona Virus (Covid-19) worldwide pandemic wearing mask could only reduce the chance of getting affected. This robot could find mask and it also has a automated voice feedback system too. Now let's see how to make it !!


## Step 1: Getting Things Ready

First for this project needs access to raspberry pi desktop. So you need a monitor mouse and a keyboard or you can use SSH or VNC.

Boot your Raspberry pi and clone this repository into your pi

git clone https://github.com/sanjus-robotic-studio/ARMD.git
Now install packages required for virtual env:

sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper
We need to edit the.profile file to set 1) the variable WORKON_HOME and VIRTUALENVWRAPPER_PYTHON to the path of the directory.virtualenvs which contains our virtual environments and 2) make known the location of the shell file, virualenvwrapper.sh. In a terminal window type:

sudo nano ~/.profile
Add these lines to the bottom of the file

export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python[YOUR-PYTHON-VERSION]
Now save and exit nano and type

source ~/.profile
Now navigate to your cloned local directory and create a virtual env "requir"

cd YOUR-USERNAME/home/ARMD
mkvirtualenv requir -p /usr/bin/YOUR_PYTHON_VERSION
And activate it

workon requir
Now install the files required for the project

pip3 install -r requirements.txt
This command will automatically install the required files

Now for the Text-To-Speech (TTS). We are going to use picoTTS, to install it follow this guide picoTTS

After installing picotts continue to the connections.

## Step 2: Connection
Turn off you pi's power supply and connect the camera to the pi.

Connection to the leds:

Red Led

Positive - GPIO 17

Negative - Gnd

Green Led

Positive - GPIO 27

Negative - Gnd

Connect the aux cable to 3.5 mm audio jack and another end to the speaker.

