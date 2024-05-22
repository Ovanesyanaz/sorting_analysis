# import youtube_dl
# youtube_dl_options = {
#     'skip_download': True,
#     'ignoreerrors': True
# }
# with youtube_dl.YoutubeDL(youtube_dl_options) as ydl:
#     videos = ydl.extract_info(f'https://www.youtube.com/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/videos')

# import urllib, json
# author = 'UCX6OQ3DkcsbYNE6H8uQQuVA'
# inp = urllib.urlopen(r'http://gdata.youtube.com/feeds/api/videos?max-results=1&alt=json&orderby=published&author=' + author)
# resp = json.load(inp)
# inp.close()
# first = resp['feed']['entry'][0]
# print (first['title']) # video title
# print (first['link'][0]['href']) #url

import scrapetube

videos = scrapetube.get_channel("UCBDMwVUsdj0tG3WTvMbsDgw")

for video in videos:
    print(video['videoId'])