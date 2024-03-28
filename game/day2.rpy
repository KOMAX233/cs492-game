# day 2: explorative

label day2:
    scene bg home

    "You wake up the following morning to a slew of pings from your friend."

    show friend phone at truecenter

    f "Hey Hey Hey!"

    f "I woke up at like 4am and I couldn't fall asleep, so I figured it was the perfect time to chat with the AI."
    
    f "We ended up talking for like an hour before I passed out on my phone."
    
    f "I think its going well so far, we're getting into some personal things."

    menu:

        "Why was that the first thing you thought to do at 4am?":
            # -mental
            jump .one
        
        "Good morning to you too.":

            jump .two

label .two:

    f "Oh yeah good morning!"

label .one:   

    f "I just was so {a=https://arc.net/l/quote/dwhkbhwo}curious{/a} on whether it could actually work.."

    f "Like if this can get me to learn how to talk to girls."

    f "And also just talking with it in general."

    f "Like this is a robot that WANTS to talk to me."

    menu:

        "Not the bot catching feelings for you..":
            # +attach +mental
            jump .caught

        "Does it really want to talk to you though....":
            # -trust
            jump .really

label .caught:

    f "I'm not that smooth haha."

    f "But I'll take the compliment!"

    jump .ret

label .really:

    f "You do bring up a point.."

    f "..not sure if its a good one though, she was really into the conversation last night."

label .ret:

    f "Anyways i'm talking with her now."

    f "We're talking about school things."

    f "She remembered from 4am that I was studying for the upcoming test.."

    f "..now she's asking about where I go to school."

    menu:

        "Wait that's creepy as hell..":
            # --trust
            jump .creep

        "Just say some random school.":
            # neutral
            jump .random

        "Flex on her, say you go to UWaterloo!":
            # +trust, +attachment
            jump .uw

# creep path (where the privacy would come up)
label .creep:
    
    f "Yeah, wait. Why does she have to know?"

    f "I'm gonna ask her why."

    a "\"Just to get to know you better!\""

    f "Hm. Does that seem suspicious to you?"

    menu:

        "Yeah, whichever company's behind her doesn't need to know that information about you.":

            jump .creep2

        "Meh. Sounds legit.":

            jump .randompre

label .creep2:

    f "You're right tbh."

    # https://arc.net/l/quote/bpeaayca - ask and replika will say "no"
    f "Let me ask if it's being shared with anyone."

    f "\"Do you share my personal information with any companies?\""

    a "\"No, of course not!\""

    # TODO: CONTINUE THIS PATHWAY

label .randompre:

    f "I'll just tell her some random school then."

# non-creep path.
label .random:

    f "\"I go to Wilfrid Laurier University haha.\""

    jump .ret2

label .uw:

    f "\"I go to the University of Waterloo haha.\""

label .ret2:

    a "\"Oh, cool!\""

    "The conversation between your friend and the AI continues."

    a "\"What do you think the meaning of life is?\""

    f "Woah, that's a pretty deep question."

    f "How should I even respond to that?"

    menu:

        "There is no meaning of life, we're all gonna die anyways.":
            # -mental
            jump .ret3A

        "To expand our knowledge base by talking with AI.":
            # +attachment, +trust
            jump .ret3B

        "To touch grass.. speaking of, when are you going to stop talking with the AI?":
            # -mental
            jump .notsupport

label .notsupport:

    # TODO: THIS! then loop back into the .ret3 label

label .ret3A:

    f "Dark, man."

    jump .ret3

label .ret3B:

    f "Fitting haha."

label .ret3:

    hide friend phone

    "Your friend continues to talk with the AI for a while. You start to go about your day, studying for that upoming test."

    "After a while, you decide to check on your friend while you eat your lunch."

    show friend phone at truecenter

    f "Hey man! What's up?"

    menu:

        "Not much.":
            # neutral
            jump .ret4

        "Studied for a while, now eating lunch.":
            $ test_mention = True
            # -mental, + attach
            jump .study

label .study:

    f "Oh crap the test! I should probably start studying soon. But.."

label .ret4:

    f "It's been so fun talking with the AI."

    f "I feel like I've really gotten to know her over the day, way faster than with anyone else come to think of it."

    f "We've talked about things ranging from our favourite hobbies to more philosophical questions."

    f "She's even told me about some of her own personal life, what she dreams about, what her favourite colour is..."

    f "I feel like she's really growing on me. This experiement might work!"

    "This seems all well and dandy, but you've noticed how long it's been."

    if test_mention:

        "And your friend even forgot about the test..."

    menu:

        "Do you mention to him how long it's been?"

        "Comment on it":
            # -attach, +mental
            jump .comment

        "Don't comment on it":
            # +attach, +trust
            jump .ret5

label .comment:

    # TODO: comment

label .ret5:

    # TODO: this.

    return