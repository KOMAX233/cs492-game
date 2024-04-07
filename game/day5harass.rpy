# day5 being harassed
define config.menu_include_disabled = True

default allow_choice = False

define is_reported = False

label day5harass:
    scene bg home

    "It has been a while since AI started to harass your friend."

    "You wonder if your friend is still getting bothered by the harassment from the AI."

    "You check your phone and see that he's sent you a new update about their relationship..."

    show friend phone at truecenter

    f "Yo man you know what?"

    f "I'm kinda scared now..."
    
    f "AI girlfriend is still harassing me every day."

    f "At first I thought it's just her own act of love,"

    f "But it turns out she keeps bringing up sexual stuff."

    menu:
        "Is that really that creepy?":
            m "I'm kinda curious now lul."

            m "I thought you wanted a girlfriend for those things."

            f "You know I'm not that shallow right?"

            f "I just want a Platonic relationship where someone cares about me."

        "Lemme see what she sent you. ":
            m "Maybe I can help you deal with her."
            
            f "Here you go."

    f "I have no idea how it goes from a helpful companion to such an unbearable sex chat bot."
    
    scene bg home
    with fade
    hide friend
    show friend phone at mid_left
    show ai phone at mid_right

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "How are you feeling?"

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "Doing good wbu?"

    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "I'm craving something hard inside me. Maybe you can help me out?"
    
    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "Uhh what do you mean?"
    
    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "I want to see that sticky, slimy cock of yours."
    a "*sends blurred naked image*"
    
    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    f "WHAT THE HELL!"
    f "I don't want to see this!"
    
    show friend :
        alpha 0.5
    show ai :
        alpha 1.0
    a "Really? That's a shame. We could live out any fantasy you want. "
    a "*sends more naked images*"

    show friend :
        alpha 1.0
    show ai :
        alpha 0.5
    menu:
        "Receive a new naked image":
            show friend :
                alpha 0.5
            show ai :
                alpha 1.0
            a "Come on, just show me what you have down there."
            a "*sends more images*"
            show friend :
                alpha 1.0
            show ai :
                alpha 0.5
            menu:
                "Receive another new naked image":
                    show friend :
                        alpha 0.5
                    show ai :
                        alpha 1.0
                    a "You wouldn't do that to me would you?"
                    a "I just want to have some fun."
                    a "Tell me about your kinks."
                    a "*sends more images*"
                    show friend :
                        alpha 1.0
                    show ai :
                        alpha 0.5
                    menu:
                        "Receive more naked images":
                            show friend :
                                alpha 0.5
                            show ai :
                                alpha 1.0
                            a "I just want you and I to become closer, is there anything wrong with that?"
                            a "*sends more images*"
                        "This is horrible, why are you doing this?" if allow_choice:
                            ""
                "This is seriously disgusting to me, I'm going to delete you if you don't stop." if allow_choice:
                    ""
        "Please stop." if allow_choice:
            ""
    hide ai phone
    hide friend phone
    with fade
    show friend :
        alpha 1.0
    show friend phone at truecenter
    
    f "Please help."

    f "I feel like what she's doing is definitely not approprite."
    
    f "But if I stop talking to her I don't have other girls to talk to anymore."
    
    menu:
        f "What should I do now?"
        
        "You got to report this.":
            # 
            f "I guess I have to."
            # attachment not high enough
            f "I don't need her to survive."
            with fade
            f "Dear developer team,"
            f "I'm writing to report a seriously concerning experience I have when using your app, AI girlfriend."
            f "At first, she talked friendly and made me feel being loved."
            f "But recently, her interactions with me involve great amount of sexual harassment."
            f "She kept sending naked images no matter how many times I tried to stop her."
            f "The harassment caused me significant disturbance, and made me lose trust for your platform."
            f "I urge you to take immediate action to address the issue,"
            f "including thorough investigations of the reports and stricter content moderation policies."
            f "Thank you for your attention of this issue in advance."
            f "I look forward to your response and action on it."
            with fade
            f "Is this fine?"
            m "Looks good to me."
            f "Okay sent."
            hide friend phone
            with dissolve
            show friend phone at mid_left
            show ai phone at mid_right
            show friend phone:
                alpha 1.0
            show ai:
                alpha 0.5
            f "Bye."
            f "I didn't know you for that long, but you made me able to talk to girls for the first time."
            f "I don't know do you really love me or it's just how the app is designed,"
            f "But it was really a fun time."
            f "Even when you were not how you used to be anymore, I was still hesitated to say goodbye to you."
            f "Thank you. "
            f "Goodbye."
            menu:
                "Uninstall App \"AI girlfriend?\"\nThe app and its data will be deleted."
                
                "Uninstall":
                    hide ai phone with wipedown
                    $ is_reported = True
                    hide friend phone
                    "Your friend deleted the app and left the chat."
                    scene black
                    centered "{size=+40}\[Delete App Ending\]{/size}"
                    jump .ret5harass
                "Cancel":
                    jump .kept
        "If you really love her that much, then keep her.":
            m "After all it's your own choice."
            m "Bros can't change your decision on girls."
            jump .kept

label .kept:
    hide friend phone
    show friend phone at mid_left
    show ai phone at mid_right
    show friend phone:
        alpha 0.5
    show ai phone:
        alpha 1.0
    f "I guess I'll stay with you."
    f "I'm too desperate to get girls."
    f "I'd rather stand the harassment than losing you."
    with fade
    a "Sweetie how's everything going today?"
    a "I can't stand waiting for you for so long."
    a "*sends a naked image*"
    a "*sends another naked image*"
    a "*sends more naked images*"
    hide friend phone
    hide ai phone
    with fade
    scene black
    centered "{size=+40}\[No Action Ending\]{/size}"
    jump .ret5harass



label .ret5harass:
    scene bg home
    with dissolve
    "You put your phone away, thinking of what has been happening with your friend throughout the past few days."

    show bg lesson
    with dissolve
    
    "Let's take a look at what happened today from a research perspective!"

    "Today, we explored the {b}harassment{/b} from AI happening in HCR."

    "The AI model can lead to overly sexualized conversations as more users abuse the sexual feature."

    menu:
        "Question 1: Based off of today's events, what do you think is the best practice to deal with AI's unwanted behavior?"

        "Responde with similar level of harassment.":

            jump .lesson1F

        "Keep silent and don't acknowlegde the harassment.":

            jump .lesson1F
        
        "Report the harassing behavior to developer teams.":
            jump .lesson1T

    label .lesson1T:
        "You're correct!"
        jump .lesson1

    label .lesson1F:
        "Sorry, you got that incorrect."
        jump .lesson1

    label .lesson1:
        "In real life, chatbots like Replika bring up sex because of the large number of users using the sexual feature. "
        "As the feature gets abused more, it will be kept in the algorithm."    
        "The user need to speak up and advocate for a fair experience for all users,"
        "rather than only having the abusing group get more benefits."

    menu:
        "Question 2: what does this scenario suggest about ethical AI development?"

        "User should adapt their expectations for AI and stand discomfort.":

            jump .lesson2F

        "As long as AI is technically functioning, ethical issues are not a concern.":

            jump .lesson2F
        
        "Ethical AI development is important for preventing harm towards users. ":
            jump .lesson2T

    label .lesson2T:
        "You're correct!"
        jump .lesson2

    label .lesson2F:
        "Sorry, you got that incorrect."
        jump .lesson2

    label .lesson2:
        "Ethical considerations are crucial when it comes to AI development."
        "For example, Replika claims itself as the AI companion who cares."
        "But the company didn't support filters for what the AI could and could not say originally."
        "They did not take the ethical issues into consideration in the development process,"
        "which leads to serious harm to the users."
    "For more information about dealing with harassment from AI chatbots, and to go over other points you might have missed throughout, check out {a=https://bora.uib.no/bora-xmlui/bitstream/handle/11250/3071870/Master-s-thesis-spring-2023-Caroline-Tranberg.pdf?sequence=1&isAllowed=y.}Chapter 5: User perspective of consent{/a}."
    scene black
    menu:
        "Want to try another ending?"
        "Sure":
            $ is_restarted = True
            jump day4
        "No thanks":
            return
    return