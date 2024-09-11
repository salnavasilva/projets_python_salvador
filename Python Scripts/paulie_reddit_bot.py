# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 15:32:56 2021

@author: navar
"""

import praw
import random
import time

reddit = praw.Reddit(
    client_id="unntb6EcIJAbq_WMNlf2uA",
    client_secret="yKiU-58lPhCOgpNreeWI687zIgLMTg",
    user_agent="<console:PAULIEWALNUTS:1.0>",
    username="Paulie-Walnuts-bot",
    password="$Hava1738"
)

subreddit=reddit.subreddit("thesopranos+CirclejerkSopranos")

paulie_quotes=['The Skip seeing a psychiatrist, how does that sit with your ass?',
               'You didn’t go to hell. You went to purgatory, my friend.',
               "I'll keep this short and sweet. You're weak. You've become an embarrassment to yourself and everybody else.",
               'The Boss of this family told you, you were going to be Santa Claus. You’re Santa Claus, so shut the f*ck up about it!',
               'She’s so fat, she goes campin’, the bears have to hide their food.',
               'I look over and your uncle June’s got lazerbeams shooting out of his eyes',
               'I gotta watch TV to figure out the world?',
               'Ride the painted pony and let the spinnin wheel glide…',
               'I’m here to tell you one thing. You ever go whining to the big man again about shit between you and me, we’ll have a problem, my friend.',
               'Why do pissin, sh*ttin’, and f*ckin’ all happen within’ a two-inch radius?',
               'You’re a little too worried about what I give you. Worry a little more about what you give me.',
               'Word to the wise, rememba Pearl Harbor',
               'I was born, grew up, spent a few years in the army, couple more in the can, and here I am, half a wise guy.',
               'You’re not going to believe this, guy killed 16 Czechoslovakians…he was an interior decorator.',
               'My name’s Clarence.',
               'Sun-Tuh-Zoo. He’s Chinese Prince Matchabelli.',
               'I went over for a bl*wjob. Your mother was working the bonbon concession at the Eiffel Tower.',
               'Kid…Richard Kimble, the Devil’s whatever, those are all make-believe. I got no arc either. ',
               "The guy gives him the works: MRIs, CAT scans, DOG scans, you name it. He says there's not a thing wrong with his back.",
               'That’s different for everybody. You add up all your mortal sins and multiply that number by 50. Then you add up all your venial sins and multiply that by 25. You add that together and that’s your sentence. I figure I’m gonna have to do 6,000 years before I get accepted into heaven and 6,000 years is nothin’ in eternity terms. I can do that standing on my head. It’s like a couple of days here.',
               'You ever go to tie your shoes and you notice the end of your laces are wet? Come on, why would they be wet?',
               'Well, I… leave that. Don’t touch that, my program’s coming on!',
               'They’re all meat eaters!',
               'They ate pootsie before we gave them the gift of our cuisine. But this, this is the worst. This expresso s***.',
               "It's like an ad for a weight loss center. Before, and way before!",
               'You hear what I said, Ton?',
               'Oof, madone! He looks terrible!',
               'Minn! Your door was open! I brought you something from my Ma!']


for post in subreddit.new(limit=20):
    
    # print('\n')
    # print(post.title)
    
    
    for comment in post.comments:
        if hasattr(comment, 'body'):
            comment_lower=comment.body.lower()
            if ' paulie ' in comment_lower:
                
                print('******************')
                print(comment.body)
                random_index=random.randint(0, len(paulie_quotes)-1)
                comment.reply(paulie_quotes[random_index])
                #time.sleep(540)