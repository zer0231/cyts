#!/usr/bin/python3
import requests
import json
import sys, getopt
import webbrowser

def search_movie(genre,min_,keyword,quality):
	i=0
	from_api = requests.get("https://yts.mx/api/v2/list_movies.json?minimum_rating="+min_+"&genre="+genre+"&limit=50&order_by=asc&quality="+quality+"&query_term="+keyword)
	re = from_api.text
	yts_json = json.loads(re)
	slugs =[]
	movie_string = yts_json['data']
	movie_json = movie_string['movies']
	for titles_english in movie_json:	
		print( str(i)+' ' + titles_english['title_english'])
		i = i + 1
		slugs.append(titles_english['slug'])
	print('\n'+str(i-1) + 'Movies found')
	slug_no = int(input("\nEnter the number: "))
	webbrowser.open('https://yts.mx/movie/'+slugs[slug_no])

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
    except Exception:
        res = True
    if res:
        print("No")
        exit()


def main(argv):
	li={}
	genre = ''
	keyword = ''
	quality = '720p'
	min_ = ''
	try:		
		opts, args = getopt.getopt(argv,"hg:m:k:q:",["genre=","min_=","keyword=","quality="])
		#print("here")
	except getopt.GetoptError:
		print ('usage:\nyts.py -g <genre> -k <single word keyword> -q <quality 720p,1080p> -m <minimum rating 1-9> -h <show this help>')
	for opt, arg in opts:
		#print("here")
		if opt == '-h':
			print ('usage:\nyts.py -g <genre> -k <single word keyword> -q <quality 720p,1080p> -m <minimum rating 1-9> -h <show this help>')
			sys.exit()
		elif opt in ("-g", "--genre"):
			genre = arg
		elif opt in ("-m","--min_"):
			min_= arg
		elif opt in ("-k","--keyword"):
			keyword = arg
		elif opt in ("-q", "--quality"):
			quality = arg
	checkinternet()
	search_movie(genre,min_,keyword,quality)
   
if __name__ == "__main__":
   main(sys.argv[1:])
