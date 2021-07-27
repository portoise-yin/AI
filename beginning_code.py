# will need to !pip install boxsdk
import "colors.csv"
from io import StringIO
import pandas as pd
from boxsdk import Client, OAuth2

#this function will read in images
def read_in(file_name):
	print("")

def main():
	file_name_str = "images_by_url.txt"
	read_in(file_name_str)
	print("test text")

if __name__ == '__main__':
	main()