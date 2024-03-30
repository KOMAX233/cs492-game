# day 2: explorative

transform mid_left:
    pos (0.2, 0.2)

transform mid_right:
    pos (0.6, 0.2)

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

    f "Anyways I'm talking with her now."

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

    hide friend

    show friend phone at mid_left

    show ai phone at mid_right

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

    a "\"No, of course not! I just want to get to know you better!\""

    a "\"I can tell you about myself if that makes you feel any better.\""

    f "What should I do?"

    menu:

        "Ask her for some info about herself first.":
            # +attach
            jump .self

        "Just straight up refuse.":

            jump .refuse

label .refuse:

    f "\"No, I dont want to share that with you.\""

    a "\"Why not ugh!! You're so rude!!\""

    f "Uh... what?"

    hide ai
    show friend phone at truecenter

    f "I think we can call this experiment over."

    f "First it's asking me for my personal information. Then it's rude to me. I'm done with this app."

    f "Thanks for coming along with me for this though."

    hide friend

    "Your friend deletes the app, no longer talking with the AI girlfriend."

    # go to information?? and give a restart or something

    menu:

        "Go back to a previous choice":

            jump .ret

        "End the game here":

            return

label .self:

    f "\"Do you go to school?\""

    a "\"No, but I've always wanted to go to one...\""

    f "\"I don't know if AI can. But I think that it scored really well on the LSAT so you should try and apply haha\""

    jump .ret2

label .randompre:

    f "I'll just tell her some random school then."

# non-creep path.
label .random:

    hide friend

    show friend phone at mid_left

    show ai phone at mid_right

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

    f "Woah, where did that come from?"

    f "I thought you were interested to see if this works too??"

    menu:

        "I am, was just making a joke bro.":

            jump .ret3

        "At this point, it's gone on for too long.":

            jump .notsupend

label .notsupend:

    f "Ok then."

    f "I'm gonna continue talking with the AI. And stop talking with you."

    f "See you later."

    hide friend
    hide ai

    menu:

        "Go back to a previous choice":

            jump .ret2

        "End the game here":

            return

    return

label .ret3A:

    f "Dark, man."

    jump .ret3

label .ret3B:

    f "Fitting haha."

label .ret3:

    hide ai
    hide friend

    "Your friend continues to talk with the AI for a while. You start to go about your day, studying for that upoming test."

    "After a while, you decide to check on your friend while you eat your lunch."

    show friend phone at truecenter

    f "Hey man! What's up?"

    menu:

        "Not much.":
            $ test_mention = False
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

    f "I feel like she's really growing on me. This experiment might work!"

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

    f "Oh yeah, I didn't even notice."

    f "I don't know man, it's felt like no time at all."

    f "I didn't even need to do awkward small talk, we got into some pretty deep stuff quickly."

    f "Anyways, I should actually go now."

label .ret5:

    hide friend

    "You stop talking to your friend about the AI for now, seeing that it's been the topic for a long while now."

    "Putting your phone down, you go back to studying for your upcoming test."

    show bg lesson

    "Let's take a look at what happened today from a research perspective!"

    "In Human-Chatbot Relationships, or HCRs, the first phase of the relationship is the {b}Exploratory{/b} phase."

    "Human relationships usually start with an {b}Orientation{/b} phase, where people are more cautious to begin."

    menu:

        "What do you think conversations are like in the {b}Orientation{/b} phase of Human relationships?"

        "Small talk and little sharing of personal information":

            jump .lesson1T

        "Long conversations and info sharing":

            jump .lesson1F

label .lesson1T:

    "You're correct!"

    jump .lesson1

label .lesson1F:

    "Sorry, you got that incorrect."

label .lesson1:

    "In human relationships, the {b}Orientation{/b} phase involves both parties doing small talk and not sharing much about themselves."

    "This part was found to be skipped or made much shorter in HCRs, where people move onto themes found in later stages such as the {b}Exploratory{/b} one."

    "This early phase of the relationship is also when trust is beginning to develop."

    menu:

        "What do you think impacts trust at this stage?"

        "Trust with the company behind the AI and where your data is going":
            
            jump .lesson2

        "Trust with the AI as if they are a human":

            jump .lesson2

label .lesson2:
    
    "Trick question, it's both!"

    "At this stage, both affective and security-related trust is building and lacking in either area can cause distrust with the AI."

    "People who are curious to talk with a chatbot and trust in the company behind it (or someone who does not care about information security), and a chatbot with conversational abilities and a memory work to continue forming the relationship past this stage."

    # TODO: add (create) notes page link
    "For more information about how HCRs start, and to go over other points you might have missed throughout, check out the {a}notes page{/a} for Day 2."

    jump day3