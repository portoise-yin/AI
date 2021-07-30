# will need to !pip install boxsdk
# !pip install pandas
import os
import os.path
from os import path
from io import StringIO
from boxsdk import Client, OAuth2
from boxsdk.network.default_network import DefaultNetwork
from pprint import pformat
import pandas as pd
#import csv with open("colors.csv",)

#globvars
corpus_items = ""

# the function below aids in setting up an SDK client when reading in from a box file
# this code is heavily referenced from : https://opensource.box.com/box-python-sdk/tutorials/intro.html 
class LoggingNetwork(DefaultNetwork):
    def request(self, method, url, access_token, **kwargs):
        """ Base class override. Pretty-prints outgoing requests and incoming responses. """
        print( '\x1b[36m{} {} {}\x1b[0m'.format(method, url, pformat(kwargs)))
        response = super(LoggingNetwork, self).request(
            method, url, access_token, **kwargs
        )
        if response.ok:
            print('\x1b[32m{}\x1b[0m'.format(response.content))
        else:
            print( '\x1b[31m{}\n{}\n{}\x1b[0m'.format(
                response.status_code,
                response.headers,
                pformat(response.content),
            ))
        return response

#this function will create a connection to box 
def read_in_from_box():
	# Online, I have set up an python developer account, linked it to my rpi.box, and manually retrieved the following tokens
	# Define client ID, client secret, and developer token.
	my_client_id = "j322oi8ygcpus5sb13iq2i32ovaqz3do"
	my_client_secret = "UZ9Yig1bqNqt3dc6cgb3yVLHn63q3eJb"
	developer_access_token = "PO4PkeEiqqUujQemhTlSYjGphZwTWoqH"
	'''
	HERE IS THE PROBLEM^: the developer access token automatically expires every 60 minutes and must manually be retrieved. 
	I am under the impression i can build a function that can manually fetch a new code if the string is found to be expired but
	it's been giving me huge problems and progress is very slow to the point it's impeding on work on other parts of the project

	'''
	
	# Create OAuth2 object. It's already authenticated, thanks to the developer token.
	oauth2 = OAuth2(client_id = my_client_id, client_secret = my_client_secret, access_token=developer_access_token)

	# Create the authenticated client
	client = Client(oauth2)

	#We now have a fully authenticated SDK client! 
	#programmer note: hopefully
	#programmer note 2: it worked

	ai_folder_id_name = "141840904947" # manually retrieved

	corpus_items = client.folder(folder_id=ai_folder_id_name).get_items()
	#print(corpus_items.type())
	for item in corpus_items:
		#here I am running a print test that all files are present, normally here would be where I would download the files
		print('{0} {1} is named "{2}"'.format(item.type.capitalize(), item.id, item.name))

	return corpus_items


def import_files_to_pandas(corpus):
	print("panda time")
	for item in corpus:
		print('{0} {1} is named "{2}"'.format(item.type.capitalize(), item.id, item.name))


def main():
	if path.exists('corpus/') is False:
		print("You do not have the folder \"corpus\" downloaded to the same folder this file runs in.")
		print("Normally here would trigger the function to download the corpus with boxSDK,\nbut that portion is buggy right now")
		#read_in_from_box()
	else:
		#start creating pandas database with image files
		corpus_items = os.listdir('corpus/')
		for i in corpus_items:
			print(i)

	#entries = os.listdir('corpus/')
	#isFile = entries.isFile()
	#print(isFile)
	#print(entries)
	#check if corpus exists
	#if "corpus"
	#corpus_items = box_items = read_in_from_box()
	#import_files_to_pandas(corpus_items)


if __name__ == '__main__':
	main()