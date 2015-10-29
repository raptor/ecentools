"""
@author: buckd

This captures a screenshot from the Agilent 54622d oscilloscope and saves it
as a PNG with a timestamped filename like 'screenshot_20141015203545'.

This assumes the RS-232 interface is connected to COM1 and uses a standard
baud of 57600.

Requirements:
 - python 2.7
 - pyserial, currently found at https://pypi.python.org/pypi/pyserial
 - pyagilent54622d, took latest SVN from http://code.google.com/p/pyagilent54622d/
   - There is an updated version (that wasn't used) found at https://github.com/ryansturmer/pyagilent54622d



This code is released into the public domain

"""

import agilent
import Tkinter
import tkFileDialog
import time
import os
import sys


class ScopeScreenshotGUI(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()
		self.working_dir = os.getcwd()
		self.path_label = Tkinter.StringVar()
		self.message_label = Tkinter.StringVar()
		
		self.scope = agilent.Scope()
		
		browse_button = Tkinter.Button(self, text="Output Directory...", command=self.browse_file)
		browse_button.grid(column=0, row=0)
		
		label = Tkinter.Label(self, textvariable=self.path_label)
		label.grid(column=0,row=1)
		self.path_label.set(self.working_dir)
		
		# Dummy label to add space because I don't know how to use the grid
		label1 = Tkinter.Label(self)
		label1.grid(column=0,row=2)
		
		button = Tkinter.Button(self, text="Take Screenshot", command=self.do_capture)
		button.grid(column=0, row=3)
		
		label2 = Tkinter.Label(self, textvariable=self.message_label)
		label2.grid(column=0,row=4)
		self.message_label.set("")
		

	def browse_file(self):
		temp = tkFileDialog.askdirectory(parent=self, initialdir=self.working_dir, title="Please select an output directory")
		
		# Only update our working_dir if we have one!
		if temp:
			self.working_dir = temp
			self.path_label.set(self.working_dir)
		

	def do_capture(self):
		filename = time.strftime("screenshot_%Y%m%d%H%M%S.png")
		fullpath = os.path.join(self.working_dir, filename)
		
		print("Saving to: " + fullpath)
		
		try:
			self.scope.take_screenshot(filename=fullpath)
			self.message_label.set("Success!  Filename: " + filename)
		except ValueError:
			self.message_label.set("Error:  No input data. Is everything connected and powered on?")
		except:
			self.message_label.set("Unexpected Error:  " + (sys.exc_info()[1]).message)

		
if __name__ == "__main__":
	app = ScopeScreenshotGUI(None)
	app.title("Oscilloscope Screen Shooter")
	app.mainloop()
	

#scope = agilent.Scope()
#scope.take_screenshot()
