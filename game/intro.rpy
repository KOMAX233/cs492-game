# intro

init python:
    mental = 5
    attach = 5
    trust = 5

#replcae all rachel's with e - for girl character
#double check background for all narrator moments
#add actual mental health values up and down for each game metric
#double check friend phone in all talking moments
default is_restarted = False

transform mid_left:
    pos (0.2, 0.2)

transform mid_right:
    pos (0.6, 0.2)

transform t_mental:
    pos (0.025, 0.025)

transform t_trust:
    pos (0.325, 0.025)

transform t_attach:
    pos (0.625, 0.025)

label intro:
    #change to bg narrator black
    scene bg blank

    #need to add game title
    if is_restarted:
        "Welcome back to OUR GAME TITLE"
    else:
        "Hello! Welcome to OUR GAME TITLE"

        "In this visual novel you will be taking on the role of a 20 year old university student"
        
        "The adventure you’ll be going on today will explore how humans interact with AI chatbots. We will learn about the harassment, privacy issues, and human dependence that can occur - while also exploring some of the potential benefits that these bots can have"

        "Throughout the game there will be points where you need to make a decision. Each decision will have a different impact and progress the story in a new direction - so choose carefully! To confirm a decision click the option with your mouse"

        "Before the game can begin let’s set the scene:"

        $ myName = renpy.input("You are a 20-year-old university student named: ")

        "Nice to meet you [myName]"
        define m = Character("[myName]")
        # $ myName = "bob"
        # define m = Character("bob")
        # $ friendName = "joe"
        # define f = Character("joe")


        $ friendName = renpy.input("You have a male friend - let’s call him: ")
        define f = Character("[friendName]")

    scene bg home
    show friend phone at truecenter
    $ renpy.show(f'mental {mental}', at_list=[t_mental])

    f "[myName] I have such a big crush on that new girl Rachel, but I don’t think she even knows who I am"

    menu:

        "Dude you’re 20 and can’t talk to a girl - you’ll be single forever":
            $ mental -= 1
            jump .continue

        "She doesn’t know what she’s missing out on, keep your head up":
            $ mental += 1
            jump .continue

label .continue:
    #change to bg narrator black
    scene bg blank
    $ renpy.show(f'mental {mental}', at_list=[t_mental])

    "You may have noticed that after making this decision [friendName]'s mental health score {b}[mental]{/b}"
    "As you continue to make decisions in the game this bar will go up or down. If the bar gets too low {b}you will lose the game!{/b}"

    "Let’s continue…"

    scene bg home
    show friend phone at truecenter
    $ renpy.show(f'mental {mental}', at_list=[t_mental]) 

    f "I gotta figure out something, watching youtube videos is not helping me at all."

    #change to bg narrator black
    scene bg blank

    "A few days go by…"

    scene bg home

    show friend phone at truecenter
    $ renpy.show(f'mental {mental}', at_list=[t_mental])

    f "Hey [myName]! I got some great ideas cooking, I bet you $20 by this time next month Rachel is my girlfriend."

    menu:

        "Okay bet. That’s free money for me why would I turn it down":
            jump .banter1

        "No thanks I’m not in the mood to hear about more of your silly schemes":
            jump .banter2

label .banter1:
    f "Once you hear my idea you’re going to regret that!"
    jump .backToPlanning

label .banter2:
    f "no I’m serious there’s no way this doesn’t work"
    jump .backToPlanning


label .backToPlanning:
    menu:
        "I’ll bite - what are you planning this time?":
            jump .LLM

label .LLM:
    f "Okay so you know how there’s all these new large language models that can answer questions and stuff?"
    
    menu:
        "Yeah like ChatGPT?":
            f "Exactly!"
            jump .doneChatGPT
        "No what’s that?":
            f "It’s basically a type of artificial intelligence algorithm that uses very large sets of data to understand, summarise, and generate new content"
            f "If you want to read more about them check this link out they’re pretty cool: {a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}techtarget{/a}"
            jump .doneChatGPT

        #fix the link here doesn't work for some reason

label .doneChatGPT:
    menu:
        "Okay i’m with you so far but where are you going with this?":
            jump .categoryBars

label .categoryBars:
        f "Stop rushing me I’m getting to the good part"
        f "Well since these tools started getting popular, a lot of companies have started training AI chatbots to act as your girlfriend"
        f "You can talk to them, you can ask them questions, they’ll even send you spicy photos if you ask"
        f "It's not like I actually want to date the bot, but I don’t have anything better to do either now do I?"

        #change to bg narrator black
        scene bg blank
        $ renpy.show(f'mental {mental}', at_list=[t_mental])
        $ renpy.show(f'trust {trust}', at_list=[t_trust])
        $ renpy.show(f'attach {attach}', at_list=[t_attach])
        
        "Before continuing in the game it is important to note the 2 new categories alongside [friendName]'s mental health bar"
        "There is now also ‘trust with the AI’ and ‘attachment’"
        "Trust in the system represents how much [friendName] trusts their new AI companion. If you can manage to get trust low enough {b}you will win the game!{/b}"
        "Similarly, attachment represents how attached your friend is to their new AI friend. Who knows what might happen if they get too attached? If this bar gets too high {b}you will lose the game!{/b}"

        "Now back to the story..."

   
        scene bg home
        show friend phone at truecenter
        $ renpy.show(f'mental {mental}', at_list=[t_mental])
        $ renpy.show(f'trust {trust}', at_list=[t_trust])
        $ renpy.show(f'attach {attach}', at_list=[t_attach])

        f "It's not like I actually want to date the bot, but I don’t have anything better to do either now do I?"
        f "It’s lonely out here"

        menu:
            "I think that’s a great idea! It will help you get some practice talking to a girl in a safe environment":
                $ support = "to"
                "You have chosen [support] be supportive..."
                "[friendName] starts telling you about the potential benefits of having an AI girlfriend"
                jump .retroDay1


            "Uhhh I’m not sure that sounds like the best idea. You know how many privacy concerns those apps have right?":
                $ support = "not to"
                "You have chosen to [support] be supportive..."
                "You start telling [friendName] about the privacy concerns you’ve read about online."
                jump .retroDay1

label .retroDay1:
    scene bg lesson
    "Now that you’re reaching the end of the introduction, you’ve arrived at your first retrospective moment!"

    "At the end of each day you will have a retrospective which focuses on the real world implications of the choices you make in the game"
    "Many of the themes and ideas you will interact with today have a significant impact on real people’s day to day lives"

    "Your first retrospective will relate to the potential benefits of AI chatbots"

    jump .q1

label .q1:
    "Question 1: Can having an AI girlfriend genuinely make people feel more supported and less isolated?"

    menu:
        "Yes it would help":
            "Correct!"
            "Some examples of these apps include Replika, and Microsoft Asia-Pacific’s ‘Xiaoice’"
            "These apps have been shown to give users a space for connection and emotional support making them feel less isolated"
            jump .q2

        "No it would not help":
            "Incorrect!"
            "While there is still much more long term research that needs to be done, at face value these apps do help users feel less isolated"
            "They provide a space for connection and emotional support. Some examples of these apps include Replika, and Microsoft Asia-Pacific’s ‘Xiaoice’"
            jump .q2

        "I need a hint":
            "Here are some sources that may be useful:\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}linkedin{/a}\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}health news{/a}\nClick anywhere on the screen to go back to question 1"
            jump .q1

label .q2:
    "Question 2: There is a consensus among popular AI related writers that one of the benefits of having an AI girlfriend is the 24/7 convenience of having a conversation"

    menu:
        "True":
            "Correct!"
            "General consensus is that having 24/7 access to an AI chatbot is beneficial for individuals"
            "Without the constraints of distance and time people are always able to alleviate feelings of loneliness or isolation immediately, which often is not possible in a real relationship."
            jump .endDay1

        "False":
            "Incorrect!"
            "While it is definitely a new idea that will continue to be researched and explored, current sentiment within the AI community shows that having 24/7 access to an AI chatbot is beneficial for individuals"
            "Without the constraints of distance and time people are able to alleviate feelings of loneliness or isolation immediately, which often is not possible in a real relationship"
            jump .endDay1

        "I need a hint":
            "Here are some sources that may be useful:\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}Linkedin{/a}\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}Health News{/a}\nClick anywhere on the screen to go back to question 2"
            jump .q2


label .endDay1:
    "Congrats on finishing the introduction and tutorial. Let the games begin!"
    jump day2