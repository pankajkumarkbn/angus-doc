Smart message box
=================

In this tutorial we will look into how turn a Raspberry Pi, a web cam and a speaker into a smart message box.

The concept
-----------

That concept might be a little obscure!

We were thinking about a funny smart device that a team / a family / flatmates could use collectively.
Then we thought that it would be great if we someone going to the coffee machine could leave a private message (work related or not) to another member of the team who would come to the coffee machine later. Of course, such a function could be filled up with an app running on a tablet. But we wanted something more fun
where no login nor typing on a touch screen is required (cause you are holding your coffee, right!).

The control flow is as follows:

 1. The device wait to see a new person in front
 2. If nobody is there, run a small tagline as "come on"
 3. When a face is detected, find the identity of the person
 4. Play all messages for this person (if any)
 5. When no message left, propose to leave a new message
 6. Record the message until "stop" is said
 7. Ask for confirmation
 8. Ask for the recipient's name
 9. Store the identity, the recipient and the date
 10. Say goodbye
 11. Go back to 1 and repeat.

Hardware
--------

The hardware indicated below is only a suggestion, it is possible to build you assistant using different options (as long as you have a video/audio input and en audio output).


* Raspberry Pi Model B/B+/2
* 4GB SD Card
* USB web cam (with a microphone)
* Powered speakers with a 3.5mm jack input

Installation
------------

OpenCV
++++++

OpenCV will be used to retrieve and format the video stream captured by your web cam.
Please follow the steps detailed on opencv installation `guides`_.

Note that on most operating systems, opencv libraries are available as binaries through package managers.
On Ubuntu, typing this command is enough to have OpenCV installed::

	sudo apt-get install python-opencv

.. _guides: http://docs.opencv.org/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html


PyAudio
+++++++

PyAudio will be used to retrieve audio buffer recorded by your web cam.
As for OpenCV, you can either follow the instructions found `here`_ or look into your operating system package manager.

On Ubuntu, typing this command is enough to have PyAudio installed::

	sudo apt-get install python-pyaudio

.. _here: https://people.csail.mit.edu/hubert/pyaudio/

Angus SDK
+++++++++

We will use Angus API to provide voice and users recognition.
Please refers to these `steps`_ to install the python SDK.

.. _steps: http://angus-doc.readthedocs.org/en/latest/getting-started/python.html#install-the-angus-sdk


Main program
------------

Get the script
++++++++++++++

Retrieve the code of this project on `github <https://github.com/angus-ai/angus-smartmessagebox.git>`_::

  git clone https://github.com/angus-ai/angus-smartmessagebox.git

All the code was commented.

Prepare face directory
++++++++++++++++++++++

The main program looking for a subdirectory "ids" to create the
directory for the message box. Please create a new subsubdirectory for
each person you want include in the system. And for each, put inside
at least one picture (jpg or png) of the face. For example we uploaded
in the repository our 3 faces::

    ids/
    ├── Aurélien
    │   └── face.jpg
    ├── Gwennael
    │   └── face.jpg
    └── Sylvain
        └── face.jpg


Usage
+++++

For run the script just::

    python main.py

After this, the program invite you to select the input and output
devices::

    2 : HDA Intel PCH: ALC283 Analog (hw:1,0)
    3 : HD Pro Webcam C920: USB Audio (hw:2,0)
    5 : pulse
    6 : default
    Select your input: 3
    0 : HDA Intel HDMI: 0 (hw:0,3)
    1 : HDA Intel HDMI: 1 (hw:0,7)
    4 : hdmi
    5 : pulse
    6 : default
    Select your output: 6

You can give the input and output device indices on command line::

    python main.py 3 6


FAQ
---

 * Sound issues:

	When using PyAudio to play sound directly on the audio output
	controlled by the bcm2835 on raspberry-pi, you may have some
	difficulties to get a clean sound. Check this `thread
	<https://github.com/raspberrypi/linux/issues/994>`_ for example.

	You can fix this issue by defining a
	new alsa output by editing a local configuration file ``.asoundrc``
	(check the `doc
	<http://www.alsa-project.org/main/index.php/Asoundrc>`_ for more
	information) in your
	home directory or a global setting in ``/etc/asound.conf``:

	.. code-block:: bash

	    pcm.convert {
	         type plug;
	         slave {
	               pcm default;
	               rate 48000;
	         }
	    }

	This piece of code creates a new output device that resamples to 48Khz before sending the signal to the standard output (by default
	the bcm2835 audio jack output).
	You just have to select "convert" at program startup in output
	selection.

Licence
-------

The codes provided in this project are under an `Apache v2.0 license <http://www.apache.org/licenses/LICENSE-2.0>`_.
