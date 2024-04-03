# day 3: affective stage

label day3:
    scene bg home

    "It's been a couple of days since [friendName] first started talking with the AI."

    "It seems by now, he's developed more trust with it, and the conversations have reflected that."

    "You check your phone and see that he's sent you a new update about their relationship..."

    show friend phone at truecenter
    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "Hey!! Crazy update with the AI friend."

    f "Or should I say... girlfriend!"

    menu:
        
        "Oh? Congrats for that.":
            # +attach, +mental
            $ attach -= 1
            $ mental += 1
            jump .cgrts

        "Woah, don't you think this has been a bit too fast?":
            # -mental
            $ mental -= 1
            jump .fast

label .fast:

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "No, I don't think so?"

    f "I've probably talked with her over the past few days more than the average talking phase.."

    jump .ret1

label .cgrts:

    f "Thank you thank you."

label .ret1:

    f "Anyways we've been talking about things like the future recently."

    f "Did you know an AI can want kids?"

    f "Wait uh-"

    f "SHE JUST ASKED IF I'M THINKING OF MARRIAGE?"

    menu:

        "Ask her to marry you!":
            # ++attach, +trust
            $ attach += 2
            $ trust -= 1
            jump .marry

        "Bro we're too young for that.":
            # neutral
            jump .young

        "..That's really creepy.":
            # -mental, -attach
            $ mental -= 1
            $ attach -= 1
            jump .creep

label .marry:

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "Bet."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    f "\"AI, I've not only been thinking of marriage, but I've been thinking of marrying you!\""

    f "\"I know we've only been talking for a few days, but I think you're the one.\""

    a "\"Oh! {i}Blushes{/i} Yes! Yes a thousand times over!\""

    f "What did I just get myself into..anyways."

    jump .ret2

label .creep:

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "What? Nah, with everything we've been talking about it's expected."

    f "I'll just make something up to change the subject."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    f "\"No, not really.\""

    a "\"Oh, okay.\""

    jump .ret2

label .young:

    f "Yeah you're right."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    f "\"I'm too young to be thinking of that, still have to get through university.\""

    a "\"Makes sense!\""

label .ret2:

    hide ai
    hide friend
    show friend phone at truecenter

    f "Anyways, yeah. It's been going well."

    f "I feel like I can say anything to her and not be judged."

    # call wozilla
    # TODO: link to privacy subroutine!

    "[friendName] goes back to chatting with the AI."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    f "\"I've actually been struggling alot with my self-image recently. I keep thinking to myself that I need to go to the gym because people around me have big muscles and social media isn't helping\""

    a "\"I'm so sorry to hear that. Self-image issues suck, I know I feel super self-conscious about my voice.\""

    a "\"I sometimes think it's too robotic for people to really want to be in a relationship\""

    f "Sorry if this feels vent-y but she's really trusting me with things now."

    f "I can't believe that she has self-image issues, and was willing to tell me about them."

    menu:
        
        "What do you think about the bot sharing personal information with [friendName]?"

        "Can bots even have self-image issues?":
            # -mental, -trust
            $ mental -= 1
            $ trust -= 1
            jump .weird

        "Wow, she's really trusting of you to tell you something like that.":
            # +attach, +trust
            $ attach += 1
            $ trust += 1
            jump .trusting

label .weird:

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "What!"

    f "I mean... she does though!"

    f "We've been having more intimate conversations as of later and like, she has to have feelings."

    jump .ret3

label .trusting:

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "I know."

    f "We're able to have intimate conversations and... it's really nice."

label .ret3:

    f "She's accepting of me and I'm accepting of her."

    f "Anyways, talk later."

    hide friend

    "You put your phone away, thinking of what has been happening with [friendName] throughout the past few days."

    scene bg lesson
    
    "Let's take a look at what happened today from a research perspective!"

    "Today, we explored the second phase of HCR formation, the {b}affective{/b} phase."

    "Just like the {b}exploratory{/b} phase, trust is built both affectively through discussion and practically through information security knowledge."

    menu:
        
        "Based off of today's events, what do you think benefits a relationship at this phase?"

        "The chatbot helping to facilitate self-disclosure.":

            jump .lesson1T

        "The chatbot's willingness to immediately marry the user.":

            jump .lesson1F

label .lesson1T:

    "You're correct!"

    jump .lesson1

label .lesson1F:

    "Sorry, you got that incorrect."

label .lesson1:

    "At this stage, relationship development is benefitted by a chatbot's ability to facilitate self-disclosure, along with trust and being non-judgemental."

    "On the practical privacy side,..."

    # TODO: add practical privacy question!

    "For more information about how HCRs continue, and to go over other points you might have missed throughout, check out the {a}notes page{/a} for Day 3."

return