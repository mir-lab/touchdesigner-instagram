'''
Matthew Ragan | matthewragan.com
Zoe Sandoval | zoesandoval.com
'''

import os
from InstagramAPI import InstagramAPI

class Insta:
	'''
		This is a sample class.

		This sample class has several important features that can be described here.


		Notes
		---------------
		Your notes about the class go here
 	'''

	def __init__(self, myOp):

		self.My_op 				= myOp
		self.Dep_path 			= '{}/dep/python/'.format(project.folder)

		self.Target_dir 		= parent().par.Savedirectory
		self.File_name 			= parent().par.Savephotoname

		self.Source_img_TOP 	= op('null_post')

		print("Insta Post Init")
		pass
	
	def Process_img(self):
		'''
			Checks to see if a directory exists.

			While this seems out of place as a helper method, this really comes from an existing
			code snippet to solve this problem. If you've gotten this far, and are reading these
			doc strings - steal this method. Use this helper fucntion in your own work to save
			yourself the hassle of missing directories and filed file writes.
			

			Args
			---------------
			colrImgDir (str):
			> a file path to check for existing

			Returns
			---------------
			none
		'''		
		colorImgFilePath 		= "{dir}/{file_name}.jpg".format(	dir=self.Target_dir.eval(), 
																	file_name=self.self.File_name.eval())		

		# make sure we can write image to disk
		self.Check_path(self.Target_dir.eval())

		# write image to disk
		self.Source_img_TOP.save(colorImgFilePath , async=False)

		# check if we're running a blocking or non-blocking operation

		# if blocking
		# call post process directly

		# launch subprocess
		
		pass

	def Check_path(self, colorImgDir):
		'''
			Checks to see if a directory exists.

			While this seems out of place as a helper method, this really comes from an existing
			code snippet to solve this problem. If you've gotten this far, and are reading these
			doc strings - steal this method. Use this helper fucntion in your own work to save
			yourself the hassle of missing directories and filed file writes.
			

			Args
			---------------
			colrImgDir (str):
			> a file path to check for existing

			Returns
			---------------
			none
		'''
		if os.path.isdir(colorImgDir):
			pass
		else:
			os.mkdir(colorImgDir)
		
		pass
	
	def Create_external_python(self):
		'''
			Checks to see if a directory exists.

			While this seems out of place as a helper method, this really comes from an existing
			code snippet to solve this problem. If you've gotten this far, and are reading these
			doc strings - steal this method. Use this helper fucntion in your own work to save
			yourself the hassle of missing directories and filed file writes.
			

			Args
			---------------
			colrImgDir (str):
			> a file path to check for existing

			Returns
			---------------
			none
		'''
		# check to see if we have an external python script

		# create script if it's not there

		# otherwise pass and continue

		pass
	
	def Open_credentials_mgr(self):
		'''
			Checks to see if a directory exists.

			While this seems out of place as a helper method, this really comes from an existing
			code snippet to solve this problem. If you've gotten this far, and are reading these
			doc strings - steal this method. Use this helper fucntion in your own work to save
			yourself the hassle of missing directories and filed file writes.
			

			Args
			---------------
			colrImgDir (str):
			> a file path to check for existing

			Returns
			---------------
			none
		'''

		# open password credentials entry UI
		op('container_credentials/window1').par.winopen.pulse()

		# prompt the user to remember creds

		# if yes - create dir, and save tox of creds

		# if no, do not save
		pass