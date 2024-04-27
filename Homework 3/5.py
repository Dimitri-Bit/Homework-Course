podcast_list = [{'naziv':'Español para principiantes', 'br_pozitivni':1000,'br_negativni':10},
{'naziv':'Philophize This!', 'br_pozitivni':500,'br_negativni': 30}, {'naziv':'Science VS. ',
'br_pozitivni':600,'br_negativni': 45}]

def worst_comment_ratio(list):
    worst_value = 999999
    worst_podcast = ""

    for podcast in list:
        value = podcast.get("br_pozitivni") / podcast.get("br_negativni")
        if value < worst_value:
            worst_value = value
            worst_podcast = podcast

    return (worst_podcast, worst_value)

print(worst_comment_ratio(podcast_list))