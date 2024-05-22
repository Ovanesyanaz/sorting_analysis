import scrapetube

videos = scrapetube.get_channel("UCJ-9ya7TKouLVEYClugMOBA")

for video in videos:
    print(video['videoId'])