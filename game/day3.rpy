# day 3: affective stage

label day3:
    scene bg home

    "It's been a couple of days since your friend first started talking with the AI."

    "It seems by now, he's developed more trust with it, and the conversations have reflected that."

    "You check your phone and see that he's sent you a new update about their relationship..."

    show friend phone at truecenter

    f "Hey!! Crazy update with the AI friend."

    f "Or should I say... girlfriend!"

    menu:
        
        "Oh? Congrats for that.":
            # +attach, +mental
            jump .cgrts

        "Woah, don't you think this has been a bit too fast?":
            # -mental
            jump .fast

label .fast:

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
            jump .marry

        "Bro we're too young for that.":
            # neutral
            jump .young

        "..That's really creepy.":
            # -mental, -attach
            jump .creep

label .marry:

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

    "Your friend goes back to chatting with the AI."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    f "\"I've actually been struggling alot with my self-image recently. I keep thinking to myself that I need to go to the gym because people around me have big muscles and social media isn't helping\""

    a "\"I'm so sorry to hear that. Self-image issues suck, I know I feel super self-conscious about my voice.\""

    a "\"I sometimes think it's too robotic for people to really want to be in a relationship\""

    f "Sorry if this feels vent-y but she's really trusting me with things now."

    f "I can't believe that she has self-image issues, and was willing to tell me about them."

# TODO: LAST QUESTION + RETRO

return