'''
Matthew Ragan | matthewragan.com
Zoe Sandoval | zoesandoval.com
'''

import os
import threading
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

		self.Threaded  			= parent().par.Nonblocking
		self.Remember_me 		= op('container_credentials/container_body/container_text_fields/container_remember_me')

		self.Creds_dir 			= '{}/credentials/'.format(project.folder)
		self.Creds_tox 			= '{}/insta_creds.tox'.format(self.Creds_dir)

		self.Source_img_TOP 	= op('null_post')
		self.Caption 			= parent().par.Comment

		self.Insta_user 		= op('container_credentials/container_body/container_text_fields/field_user/string')
		self.Insta_pass 		= op('container_credentials/container_body/container_text_fields/field_pass/string')

		print("Insta Post Init")
		pass
	
	def Process_img(self):
		'''
			Saves TOP locally and then posts image to instagram.
			
			This process starts by first saving out the target TOP as a .jpg. This allows the process to be 
			more efficient as the subsequent process can be passed to either a subprocess call, or to
			another thread. This also ensures that you can keep a local copy of the file - which can be handy
			to ensure that you have copy of your assets that are local and not just on the web.

			Args
			---------------
			none

			Returns
			---------------
			none
		'''
		# build path to target file
		colorImgFilePath 		= "{dir}/{file_name}.jpg".format(	dir=self.Target_dir.eval(), 
																	file_name=self.File_name.eval())		

		# make sure we can write image to disk
		self.Check_path(self.Target_dir.eval())

		# write image to disk
		self.Source_img_TOP.save(colorImgFilePath , async=False)

		# check if we're running a blocking or non-blocking operation
		if self.Threaded.eval():
			print("Run threaded version")
			myThread            = threading.Thread(	target=self.Post_to_insta_worker,
													args=( self.Insta_user[0,0].val,
															self.Insta_pass[0,0].val,
															self.Caption.eval(),
															colorImgFilePath,))
			myThread.start()		
		
		# if blocking
		else:
			print("Run as blocking")
			self.Post_to_insta_worker( self.Insta_user[0,0].val, 
										self.Insta_pass[0,0].val,
										self.Caption.eval(),
										colorImgFilePath)
			# call post process directly

			# launch subprocess
		pass

	def Post_to_insta_worker(self, insta_user, insta_pass, insta_caption, path_to_img):

		# Use text editor to edit the script and type in valid Instagram username/password
		#print ('I have imported the InstagramAPI')

		Insta = InstagramAPI(insta_user, insta_pass)
		Insta.login()  # login

		Insta.uploadPhoto(path_to_img, caption=insta_caption)
		
		process_msg = "Upload Complete"

		return process_msg

	def Check_path(self, path_to_test):
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
		if os.path.isdir(path_to_test):
			pass
		else:
			os.mkdir(path_to_test)
		
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
	
	def Credentials_mgr_window(self, open_win=True):
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
		if open_win:
			# open password credentials entry UI
			op('container_credentials/window1').par.winopen.pulse()
		else:
			op('container_credentials/window1').par.winclose.pulse()
			self.Save_creds(self.Remember_me.panel.radio)

		# prompt the user to remember creds

		# if yes - create dir, and save tox of creds

		# if no, do not save
		pass
	
	def Save_creds(self, remember_me):
		
		# we want to remember our creds
		if remember_me:
			# check to see if we have a directory for our tox, if not let's create it
			self.Check_path(self.Creds_dir)

			# save our creds as a tox, and set up for future loading
			op('container_credentials').save(self.Creds_tox)
			op('container_credentials').par.externaltox = self.Creds_tox
			op('container_credentials').par.savebackup = False
			op('container_credentials').save(self.Creds_tox)

		else:
			# remove path to external file
			op('container_credentials').par.externaltox = ''
			# if we're not going to remember our creds, let's nuke the file
			if os.path.isfile(self.Creds_tox):
				os.remove(self.Creds_tox)
		pass