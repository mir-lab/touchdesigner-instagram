import time
import os
import sys
import random
from argparse import ArgumentParser

# ensures correct handling for dependency InstagramAPI 
sys.path.append('dep')

from InstagramAPI import InstagramAPI

def Auto_poster(inputDir, destDir, interval, postIntervalMin, postIntervalMax, instaHandle, instaPass):

    # helper vars
    source          = inputDir
    dest            = destDir
    insta_handle    = instaHandle
    insta_pass      = instaPass

    # ensure vals for time.sleep are ints
    sleep_interval  = int(interval)
    post_interval   = (int(postIntervalMin), int(postIntervalMax))

    while True:
        # create a list of all subdirectories in our source directory
        dir_list    = [os.path.join(source, inst_dir) for inst_dir in os.listdir(inputDir) if os.path.isdir(os.path.join(source, inst_dir))]

        for each_sub_dir in dir_list:
            # generate a sorted list of files in each sub-dir
            file_list           = sorted([each_file for each_file in os.listdir(each_sub_dir) if os.path.isfile(os.path.join(each_sub_dir, each_file))])
            
            # advance to insta_triplet
            Insta_triplet(file_list, each_sub_dir, dest, post_interval, insta_handle, insta_pass)

            print('- '* 10)            
            print("Waiting before checking for new directories")
            print('- '* 10)

            # wait before we repeat this process
            time.sleep(sleep_interval)
        
    pass

def Insta_triplet(fileList, source, dest, postInterval, instaHandle, instaPass):
    for each_file in fileList:
        
        source_path         = os.path.join(source, each_file)
        sub_dir             = os.path.split(source)[-1]
        dest_sub_dir        = os.path.join(dest, sub_dir)
        dest_path           = os.path.join(dest, sub_dir, each_file)
        # move files dest

        # check to ensure target dir exists
        try:
            os.mkdir(dest_sub_dir)
        except:
            pass

        # move file to destination path
        os.rename(source_path, dest_path)

        # Post_to_insta(each_file)
        Post_to_insta(dest_path, instaHandle, instaPass)

        # delay before next post
        sleep_interval = random.randint(postInterval[0], postInterval[1])
        time.sleep(sleep_interval)

    # delete old direcotry
    os.rmdir(source)
 
    pass

def Post_to_insta(inputFile, instaHandle, instaPass):
    # Start Login and Uploading Photo
    insta = InstagramAPI(instaHandle, instaPass)
    # login
    insta.login()
    
    # log progress
    print("Uploading instagram: " + inputFile)

    # post to insta
    insta.uploadPhoto(inputFile, caption=None, upload_id=None)

    pass

# execution order matters -this puppy has to be at the bottom as our functions are defined above
if __name__ == '__main__':
    parser = ArgumentParser(description='Set up a file watcher to stylize files that are added to the specified folder')
    parser.add_argument("-i", "--input", dest="input", help="the directory containing source images", required=True)
    parser.add_argument("-d", "--dest", dest="dest", help="the directory images will be moved to", required=True)    
    parser.add_argument("-c", "--check", dest="check", help="the interval between directory checks", required=False, default=10)
    parser.add_argument("-piMin", "--postIntervalMin", dest="postIntervalMin", help="the minimum interval between instagram posts", required=False, default=60)
    parser.add_argument("-piMax", "--postIntervalMax", dest="postIntervalMax", help="the maximum interval between instagram posts", required=False, default=120)
    parser.add_argument("-ih", "--instaHandle", dest="instaHandle", help="your instagram handle", required=True)
    parser.add_argument("-ip", "--instaPass", dest="instaPass", help="your instagram password", required=True)
    args = parser.parse_args()
    Auto_poster(args.input, args.dest, args.check, args.postIntervalMin, args.postIntervalMax, args.instaHandle, args.instaPass)
    pass

# example
# python .\auto-poster.py -i="E:\auto-post-image-tests\source" -d="E:\auto-post-image-tests\dest" -c=10 -piMin=60 -piMax=120 -ih="helloWorld" -ip="123456"