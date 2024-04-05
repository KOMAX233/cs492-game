# day 5 meet girl in IRL

define said = False

label day5irl:
    scene bg home
    "It has been a while since your friend responded to AI's harassment with similar level of mean words."

    "You wonder if your friend is done with with the AI girlfriend and the girl he likes IRL."

    "You check your phone and see that he's sent you a new update about his relationship with them..."
    show friend phone at truecenter with dissolve
    m "So, you've finally decided to talk to her?"

    f "Yeah, I've thought about it for days."

    f "Based on my prior conversations with AI girlfriend, I should probably get real deep and intimate."
    f "I'll ask her some questions like what the meaning of life is, and about her childhood experiences. "
    f "Oh and of course if she wants to get married or not."
    
    m "Marriage? Don't you think that's a bit too fast?"

    f "Maybe, but I feel like those conversations are really genuine to win someone's heart."
    f "It's how AI girlfriend guided me."

    m "Honestly, these ideas sound kind of ridiculous."
    
    m "I think using AI girlfriend was a mistake."
    
    f "As {a=https://adriancheok.info/category-speech/wit-singapore-2019-finding-love-in-the-arms-of-a-robot/}Adrian Cheok{/a} has discussed, AIs and robots do need to acquire a large amount of knowledge to understand human behaviors and may not truly feel human emotions."
    f "But as long as there is love between the two consenting adults, human-computer relationships should work out."
    f "Just like human-human relationships."
    f "So there should be no problem for me to confess my genuine love to the girl, just like how my AI friend taught me."

    m "AI girlfriend can guide conversations, but it can't replace the human interactions."
    m "The complexity and depth of real-life connections require a personal touch beyond AI's current capabilities."
    m "I think you should think more carefully."

    menu:
        f "Then what do you think I should do?"
        "Should you really be saying that?":
            m "I mean, listen to yourself. Doesn't it sound creepy?"
            
            f "You're right..."
            f "AI girlfriend was a mistake."
            f "I got so caught up in the addiction of talking to a chatbot I lost my common sense and social skills."
            m "Lemme see."
            m "What about starting with a simple \"{i}Hello{/i}\"?"
            m "And see how it goes?"
            f "Sounds much better than the experiences I got from talking to AI girlfriend."
            m "Exactly."
            f "Thanks, I feel a lot better now."
            f "It's weird how I got so dependent on the app."
            f "I'll try talking to her later."
            hide friend phone
            with fade
            show friend phone at mid_left
            # show girl phone
            show ai phone at mid_right
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Hello!"

            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "Oh, hi."

            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "So, how are you doing?"

            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "Um, pretty good I suppose. What about you?"
            
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Pretty good..."
            f "Um, truth is, I've had a crush on you for a long time. "
            f "Do you maybe wanna hang out sometime?"
            
            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "Uh, sure!"
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Great! Can I get your number?"
            scene black
            centered "{size=+40}\[Riajuu Ending\]{/size}"
            jump .ret5irl
        "Yeah, you do you, man.":
            "Considering the implications of being too forward, you decide to support your friend's decision despite personal doubts."
            f "Right? I think deep and intimate conversations will perfectly express my affection to her."
            hide friend phone
            with fade
            show friend phone at mid_left
            # show girl phone
            show ai phone at mid_right
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Have you ever wondered what the meaning of life is?"
            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "..."
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "What's your favorite color?"
            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "..."
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "What's your childhood dream?"
            show friend phone:
                alpha 0.5
            show ai:
                alpha 1.0
            g "..."
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Oh, and... how do you feel about marriage?"
            hide friend
            hide ai
            show friend phone at truecenter
            menu:
                "You've been blocked.":
                    scene black
                    centered "{size=+40}\[Messed UP Ending\]{/size}"
                    jump .ret5irl
            
label .ret5irl:
    scene bg home
    with dissolve
    "You put your phone away, thinking of what has been happening with your friend throughout the past few days."

    show bg lesson
    with dissolve
    
    "Let's take a look at what happened today from a research perspective!"

    "Today, we explored the {b}harassment{/b} to AI happening in HCR and its impact on human interactions."

    "Users may take AI's behaviors and use them in real life social interactions."

    menu:
        "Question 1: After reading about your friend's plan to approach the girl he likes with deep and intimate questions learned from AI girlfriend, what do you learn about AI's influence on human interactions?"

        "AI can perfectly guide human social interactions.":

            jump .lesson1F

        "Conversations with AI can fully replace personal touches.":

            jump .lesson1F
        
        "Relying on AI for social cues can potentially lead to inappropriate behaviors.":
            jump .lesson1T

    label .lesson1T:
        "You're correct!"
        jump .lesson1

    label .lesson1F:
        "Sorry, you got that incorrect."
        jump .lesson1

    label .lesson1:
        "The friend's initial approach used topics learned from AI for human relationship."
        "AI may not be able to fully understand human emotions and interactions,"
        "which can lead to inappropriate conversations the friend sent."

    "For more information about dealing with harassment to AI happening in HCR and its impact on human interactions, "
    "and to go over other points you might have missed throughout, "
    "check out {a=https://www.sciencedirect.com/science/article/abs/pii/S2211695823000144.}“Date me date me”: AI chatbot interactions as a resource for the online construction of masculinity{/a}."
    scene black
    menu:
        "Want to try another ending?"
        "Sure":
            $ is_restarted = True
            jump intro
        "No thanks":
            return
    return