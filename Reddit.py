from utility import UpdateMailBody


def summoner_school():
    import praw

    reddit = praw.Reddit(client_id='bB7n1Ht1P5lgFA',
                         client_secret='48nLDAE6SQdDJ1hSknA9WJg72ew',
                         user_agent='Simple check bot /u/pihran',
                         )
    key_word = ['ahri', 'amumu', 'kindred', 'kog', 'yorick', 'annie', 'gnar', 'anivia']

    # print(reddit.read_only)

    UpdateMailBody("<br>" + '=== Reddit summonerschool ===' + "<br>")

    for submission in reddit.subreddit('summonerschool').new(limit=255):
        for key in key_word:
            if key in submission.title.lower():
                UpdateMailBody(submission.title + '<br>')
                UpdateMailBody('<a href = "' + submission.url + '" > (Link) </a><br>' + '<br>')
                # print(submission.title + '\n\n')
                # print(submission.url + '\n\n')
