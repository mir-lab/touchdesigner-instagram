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

		self.My_op 						= myOp
		self.Dep_path 					= '{}/dep/python/'.format(project.folder)

		self.Target_dir 				= parent().par.Savedirectory
		self.File_name 					= parent().par.Savephotoname

		self.Threaded  					= parent().par.Nonblocking
		self.Remember_me 				= op('container_credentials/container_body/container_text_fields/container_remember_me')

		self.Creds_dir 					= '{}/credentials/'.format(project.folder)
		self.Creds_tox 					= '{}/insta_creds.tox'.format(self.Creds_dir)

		self.Source_img_TOP 			= op('null_post')
		self.Caption 					= parent().par.Comment

		self.Insta_user 				= op('container_credentials/container_body/container_text_fields/field_user/string')
		self.Insta_pass 				= op('container_credentials/container_body/container_text_fields/field_pass/string')

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
		
		insta_user 				= self.Insta_user[0,0].val
		insta_pass				= self.Insta_pass[0,0].val
		insta_caption 			= self.Caption.eval()

		# make sure we can write image to disk
		self.Check_path(self.Target_dir.eval())

		# write image to disk
		self.Source_img_TOP.save(colorImgFilePath , async=False)

		# check if we're running a blocking or non-blocking operation
		if self.Threaded.eval():
			print("Run threaded version")
			myThread            = threading.Thread(	target=self.Post_to_insta_thread_worker,
													args=( insta_user,
															insta_pass,
															insta_caption,
															colorImgFilePath,))
			myThread.start()		
		
		# if blocking
		else:
			# call post process directly
			print("Run as blocking")
			self.Post_to_insta_worker( insta_user, 
										insta_pass,
										insta_caption,
										colorImgFilePath)

		pass

	def Post_to_insta_worker(self, insta_user, insta_pass, insta_caption, path_to_img):
		'''
			The worker method that does the work of posting the image to instagram.

			Moving this portion of the process into a separate method allows this operation to be
			thread-safe, and allows us to upload to instagram without TouchDesigner freezing. The
			TOX allows for both behaviors - threaded and non-threaded execution. This means that you
			have the flexibility to choose if the application should stop responding while it's posting, or
			if it should continue to run / allow for another instagram post.
			

			Args
			---------------
			insta_user (str):
			> an instagram user name
			
			insta_pass (str):
			> the password for the instagram account

			insta_caption (str):
			> an optional caption to added to the upload

			path_to_img (str):
			> a file path to the image that is going to be uploaded

			Returns
			---------------
			process_msg (str):
			> a string that's delivered when the process is complete
		'''

		# set-up API calls and longin to the webservice
		Insta = InstagramAPI(insta_user, insta_pass)
		Insta.login()  # login

		# upload the image to instagram
		Insta.uploadPhoto(path_to_img, caption=insta_caption)

		# return a process image - this would be a good place to add some error handling		
		process_msg = "Upload Complete"
		return process_msg

	def Check_path(self, path_to_test):
		'''
			Checks to see if a directory exists.

			While this seems out of place as a helper method, this really comes from an existing
			code snippet to solve this problem. If you've gotten this far, and are reading these
			doc strings - steal this method. Use this helper function in your own work to save
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
	
	def Credentials_mgr_window(self, open_win=True):
		'''
			Handles capturing the user's instagram credentials.

			We need a mechanism for capturing a user's credentials for logging into instagram, and this is one
			way to solve the challenge. This leverages the UI elements available in TouchDesigner to hold the user
			credentials, then save them in a binary formate. That allows the user to "Remember Me" between sessions
			and not have to consistently insert credentials. This method both opens floating window for adding
			user creds, and goes through the process of both saving and / or deleting those credentials. 

			The process of saving or deleting the credentials happens when the floating window is closed. 
			

			Args
			---------------
			open_win (bool):
			> a boolean used to issue a command to either open the floating window
			> or to close that window. As a note it's in the close window call that 
			> cached creds are saved or deleted

			Returns
			---------------
			none
		'''

		if open_win:
			# open password credentials entry UI
			op('container_credentials/window1').par.winopen.pulse()
		
		else:
			# when the UI is closed, run the save_creds() method and externalize or delete credentials
			op('container_credentials/window1').par.winclose.pulse()
			self.Save_creds(self.Remember_me.panel.radio)

		pass
	
	def Save_creds(self, remember_me):
		'''
			Handles the process of saving or deleting user credentials.

			To allow the user to save credentials without saving the entire TOE file, this will save
			the credentials entered into the pop up dialogue in a binary format. This still doesn't pass
			security muster, but it's better than saving them in plain text.

			Args
			---------------
			remember_me (bool):
			> a boolean that will indicate if credentials should be saved, or ignored.

			Returns
			---------------
			none
		'''		
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