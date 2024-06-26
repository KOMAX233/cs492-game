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
            $ if mental < 10: mental += 1
            jump .cgrts

        "Woah, don't you think this has been a bit too fast?":
            # -mental
            $ mental -= 1
            jump .fast

label .fast:

    if mental < 1:
        menu:
            "Your friend's mental health meter got too low! You lose!"

            "Try again from the same day?":
                $ mental = 5
                jump day3

            "End the game?":
                return

    if attach < 1:
        menu:
            "Your friend's attachment dropped, so he deleted the app. You win!"

            "Play again from the same day?":
                $ attach = 5
                jump day3

            "End the game?":
                return

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
            $ if attach < 10: attach += 1
            $ if trust > 1: trust -= 1
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

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "\"AI, I've not only been thinking of marriage, but I've been thinking of marrying you!\""

    f "\"I know we've only been talking for a few days, but I think you're the one.\""

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "\"Oh! {i}Blushes{/i} Yes! Yes a thousand times over!\""

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "What did I just get myself into..anyways."

    jump .ret2

label .creep:

    if mental < 1:
        menu:
            "Your friend's mental health meter got too low! You lose!"

            "Try again from the same day?":
                $ mental = 5
                jump day3

            "End the game?":
                return

    if attach < 1:
        menu:
            "Your friend's attachment dropped, so he deleted the app. You win!"

            "Play again from the same day?":
                $ attach = 5
                jump day3

            "End the game?":
                return

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "What? Nah, with everything we've been talking about it's expected."

    f "I'll just make something up to change the subject."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "\"No, not really.\""

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "\"Oh, okay.\""

    jump .ret2

label .young:

    f "Yeah you're right."

    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "\"I'm too young to be thinking of that, still have to get through university.\""

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
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

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "\"I've actually been struggling alot with my self-image recently. I keep thinking to myself that I need to go to the gym because people around me have big muscles and social media isn't helping\""

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "\"I'm so sorry to hear that. Self-image issues suck, I know I feel super self-conscious about my voice.\""

    a "\"I sometimes think it's too robotic for people to really want to be in a relationship\""

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "Sorry if this feels vent-y but she's really trusting me with things now."

    f "I can't believe that she has self-image issues, and was willing to tell me about them."

    menu:
        
        "What do you think about the bot sharing personal information with [friendName]?"

        "Can bots even have self-image issues?":
            # -mental, -trust
            $ mental -= 1
            $ if trust > 1: trust -= 1
            jump .weird

        "Wow, she's really trusting of you to tell you something like that.":
            # +attach, +trust
            $ if attach < 10: attach += 1
            $ trust += 1
            jump .trusting

label .weird:

    if mental < 1:
        menu:
            "Your friend's mental health meter got too low! You lose!"

            "Try again from the same day?":
                $ mental = 5
                jump day3

            "End the game?":
                return

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "What!"

    f "I mean... she does though!"

    f "We've been having more intimate conversations as of later and like, she has to have feelings."

    jump .ret3

label .trusting:

    if trust > 10:
        menu:
            "Your friend's trust meter got too high! You lose!"

            "Try again from the same day?":
                $ trust = 5
                jump day3

            "End the game?":
                return

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "I know."

    f "We're able to have intimate conversations and... it's really nice."

label .ret3:

    f "She's accepting of me and I'm accepting of her."

    #privacy stuff here

    scene bg blank

    "You're thinking about [friendName] and how dangerous it is that they're telling the AI all this private information..."

    scene bg tablet
    "You do a quick google search and end up at the following {a=https://foundation.mozilla.org/en/blog/creepyexe-mozilla-urges-public-to-swipe-left-on-romantic-ai-chatbots-due-to-major-privacy-red-flags/}article{/a}"

    scene bg home

    show friend phone at truecenter


    menu:
        "Hey have you read that new Mozilla article they just put out for valentines day? It talks about how AI chatbots sell your data":
            #-trust
            #-attachment
            $ if trust > 1: trust -= 1
            $ attach -= 1
            jump .afterpriv

        "Every company sells our data these days who cares":
            #neutral
            jump .data

label .afterpriv:

    if attach < 1:
        menu:
            "Your friend's attachment dropped, so he deleted the app. You win!"

            "Play again from the same day?":
                $ attach = 5
                jump day3

            "End the game?":
                return

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "So what? literally every app we use sells our data - at least this one actually helps me too"

    menu:
        "You're not worried that they aren't even telling you how the data will be used?":
            #-trust
            #-attachment
            $ if trust > 1: trust -= 1
            $ attach -= 1
            jump .keepgoing

        "You don't find it weird the Romantic AI app sent out 24,354 trackers in 1 minute??":
            #-trust
            #-attachment
            $ if trust > 1: trust -= 1
            $ attach -= 1
            jump .keepgoing

        "Isn't it scary that most of these companies don't even force users to secure their passwords. With how much data they have - can you imagine if your account got hacked?":
            #-trust
            #-attachment
            $ if trust > 1: trust -= 1
            $ attach -= 1
            jump .keepgoing



label .data:
    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "exactly! literally every app we use sells our data - at least this one actually helps me too"

    jump .cont

label .keepgoing:

    if attach < 1:
        menu:
            "Your friend's attachment dropped, so he deleted the app. You win!"

            "Play again from the same day?":
                $ attach = 5
                jump day3

            "End the game?":
                return

    $ renpy.show(f'mental {mental}', at_list=[t_mental])
    $ renpy.show(f'trust {trust}', at_list=[t_trust])
    $ renpy.show(f'attach {attach}', at_list=[t_attach])

    f "you gotta relax it's not that deep"

    jump .cont
    
label .cont:

    f "Anyways, talk later. I gotta go"

    hide friend
    hide ai

    "You put your phone away, thinking of what has been happening with [friendName] throughout the past few days."

    scene bg lesson
    
    "Let's take a look at what happened today from a research perspective!"

    "Today, we explored the second phase of HCR formation, the {b}affective{/b} phase."

    "Just like the {b}exploratory{/b} phase, trust is built both affectively through discussion and practically through information security knowledge."

    menu:
        
        "Question 1: Based off of today's events, what do you think benefits a relationship at this phase?"

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

    "On this day you have also started to think a little about the privacy implications of these chatbot services. Consider how the following questions impact your understanding of the risks"

    jump .q3

label .q3:
    "Question 2: How many queries in an average conversation with an AI chatbot would you expect to contain sensitive information?"

    menu:
        "10\%":
            "Incorrect! The correct answer is 20\%"
            jump .q4
        "20\%":
            "Correct!"
            jump .q4
        "40\%":
            "Incorrect! The correct answer is 20\%"
            jump .q4
        "75\%":
            "Incorrect! The correct answer is 20\%"
            jump .q4
        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4721968}Lessons in Privacy{/a}\nClick anywhere on the screen to go back to question 3"
            jump .q3

label .q4:
    "Question 3: When studying discord chatbots researchers found that less than  ___\% of the bots had a privacy policy"
    
    menu:
        "5\%":
            "Correct! Did you know that there was even a recorded instance of a developer logging in directly to the chatbot in a discord server!"
            "They accessed links and files which were in the channel, even sending a message saying “wtf is this bro”"
            jump .q5

        "20\%":
            "Incorrect! The correct answer is 5\%"
            "Did you know that there was even a recorded instance of a developer logging in directly to the chatbot in a discord server! They accessed links and files which were in the channel, even sending a message saying “wtf is this bro”"
            jump .q5

        "30\%":
            "Incorrect! The correct answer is 5\%"
            "Did you know that there was even a recorded instance of a developer logging in directly to the chatbot in a discord server! They accessed links and files which were in the channel, even sending a message saying “wtf is this bro”"
            jump .q5

        "50\%":
            "Incorrect! The correct answer is 5\%"
            "Did you know that there was even a recorded instance of a developer logging in directly to the chatbot in a discord server! They accessed links and files which were in the channel, even sending a message saying “wtf is this bro”"
            jump .q5

        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://dl.acm.org/doi/abs/10.1145/3517745.3561433}Privacy Risks{/a}\nClick anywhere on the screen to go back to question 4"
            jump .q4

label .q5:
    "Question 4: People above the age of 45 value  ___ more than ___ when it comes to AI chatbots"

    menu:
        "privacy; technical elements like response quality and adaptability to the user":
            "Correct!"
            jump .q6

        "technical elements like response quality and adaptability to the user; privacy":
            "Incorrect! People above the age of 45 value privacy much more than technical elements"
            jump .q6

        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://link.springer.com/chapter/10.1007/978-3-030-78642-7_53}When to trust and when to worry{/a}\nClick anywhere on the screen to go back to question 5"
            jump .q5

label .q6:
    "Question 5: People below the age of 45 value  ___ more than ___ when it comes to AI chatbots"

    menu:
        "privacy; technical elements like response quality and adaptability to the user":
            "Incorrect! People below the age of 45 value technical elements much more than privacy"
            jump .q7

        "technical elements like response quality and adaptability to the user; privacy":
            "Correct!"
            jump .q7

        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://link.springer.com/chapter/10.1007/978-3-030-78642-7_53}When to trust and when to worry{/a}\nClick anywhere on the screen to go back to question 6"
            jump .q6

label .q7:
    "Question 6: Of the 11 romantic chatbots studied by Mozilla, how many had adequate privacy or security policies?"

    menu:
        "0":
            "Correct!"
            jump .ending

        "1":
            "Incorrect! The correct answer is 0!"
            jump .ending

        "2":
            "Incorrect! The correct answer is 0!"
            jump .ending

        "3":
            "Incorrect! The correct answer is 0!"
            jump .ending

        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://foundation.mozilla.org/en/blog/creepyexe-mozilla-urges-public-to-swipe-left-on-romantic-ai-chatbots-due-to-major-privacy-red-flags/}Mozilla{/a}\nClick anywhere on the screen to go back to question 7"
            jump .q7

label .ending:
    "For more information about how HCRs continue, and to go over other points you might have missed throughout, check out {a=https://bit.ly/3vElCLl}this informative article{/a}."

    jump day4