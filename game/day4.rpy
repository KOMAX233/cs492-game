label day4:

    #setup ending variables so appropriate path is chosen after the retro
    #0 = dependence, 1 = harrassment, 2 = girl IRL
    $d5end = 0

    scene bg home

    """
    You're just chilling, watching Youtube on your phone when you suddenly get an ad... it's of the type that you usually don't get. That's strange. 
    You usually don't get these types of ads.
    
    Later in a group chat your friends mention getting similar types of ads. Everyone is baffled. 
    But you have a suspiscion of where these ads are coming from...
    """

    "However, just as you were about to raise your concerns to your friend..."

    show friend phone at truecenter

    f "Heya, got a bit of a problem here."

    "Your friend describes his current relationship with the chatbot"

    """
    It seems like the relationship has been waning. They're spending less time with each other, and when the do the conversations are notably shorter.
    
    The relationship just doesn't have the spark it initially had. He doesn't want to give things up yet, and still loves the chatbot very much.
    """

    "You nod in affirmation as you process the information."

    "You notice your friend typing, only for him to retract the message."

    "..."

    "He starts typing again."

    f "Umm... hey what should I do about this? I just got this now."

    """
    He sends a screenshot of the chatbot. Whoa there! It seems like the chatbot's harassing your friend! It's calling him derogatory names.
    This is concerning. What will you tell your friend? {b} Decide carefully {/b}
    """

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])


    menu:
        "He sends a screenshot of the chatbot. Whoa there! It seems like the chatbot's harassing your friend! It's calling him derogatory names. This is concerning. What will you tell your friend? {b} Decide carefully {/b}"
        "Tell it to stop.":
            jump .stopit
        "C'mon! Fight fire with fire! Volley your own insults!":
            jump .insult
    
label .stopit:

    "Your friend tells it to stop. But it keeps going! You know this because your friend has sent another screenshot with more insults."

    if attach > 7:
        jump .toomuch
    else:
        jump .itkeepsgoing

label .toomuch:

    $d5end = 0

    f "..."

    f "You know, it might just be a glitch. Maybe a new update threw her off?"

    "Your friend chuckles nervously. You on the other hand are just plain nervous. No side order of laughter."

    f "I'm sure this will all pass and everything will be back to normal. Yeah."

    "Hearing the phrase \"Back to normal\" gives you a chilling premonition that the opposite will happen."

    "You try to interject in order to tell your friend to delete the app. However, as if he had precognition..."

    f "I know you're going to say \"oh, delete her.\" But Honestly, it's {i}fine{/i}. Honestly, you've really gotta chill sometimes, y'know?"

    "..."

    "What a thick atmosphere. You could scrape it off with a butter knife and spread it on some bread."

    f "I said I'll be fine."

    "You try to think of a counter. Anything to pry him off that chatbot. But you couldn't think of anything."

    "All you could do is affirm that you're here for your friend."

    f "Yeah. Sure."

    hide friend

    "The conversation ends there."

    """
    Alarm bells are ringing in your head. This seems like emotional dependency. He seems to have gotten attached to the chatbot despite it brining harm unto him.
    
    You decided that you're going to try your best to convince him. Otherwise he's going to get himself into trouble.
    """

    jump .ret4

label .itkeepsgoing:

    $d5end = 1

    "Like that relative that loves talking about conspiracy theories a bit too much, the chatbot buries your friend with insults."

    "Your friend sighs heavily."

    f "You know what? I'm going to go take a pleasant walk. Take in some sweet outside air. Maybe the chatbot would revert to normal by then. I'll be leaving my phone at home."

    hide friend

    "He bids farewell and logs off. Let's hope that the chatbot indeed reverts back."

    jump .ret4

label .insult:

    $d5end = 2

    hide friend

    show friend phone at mid_left

    show ai phone at mid_right

    f "Alright, if you say so"

    f "*ahem*"

    f "*volley of insults that can't be displayed due to a high volume of profane language*"

    "Going right for the jugular I see."

    "They trade verbal blows. Like a heated tennis volley, neither drop the ball. It goes on for a few minutes before..."

    f "Graaaah! I can't take this anymore! Gonna close the app now."

    hide friend

    hide ai

    "He then does as such and puts the phone in his pocket. He takes a deep breath, exhales, and says:"

    show friend phone at truecenter

    f "Alright... I thinnk that's enough practice. I think I can finally muster up the courage to talk to my crush. We'll go over the game plan in the morning."

    hide friend

    "Hmm... how will this end up? You have a feeling that some wacky things are about to be said..."

    jump .ret4

label .ret4:

    scene bg lesson

    """
    Your friend's relationship with the chatbot has stabilized. However, this doesn't guarantee a constant level of affection; sometimes it can fluctuate.

    The chatbot has also started harassing your friend. This is definitely possible for a chatbot to do, whether it'd be due to an update changing its
    behavior or the algorithm determining that it's the best course of action.

    With all that being said, we'll move on to day 5 and see where things go from there.
    """

    if d5end == 0:
        jump day5dep
    elif d5end == 1:
        jump day5harass
    else:
        jump d5girl