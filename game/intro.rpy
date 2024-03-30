# intro

#replcae all rachel's with e - for girl character
#double check background for all narrator moments
#add actual mental health values up and down for each game metric
#double check friend phone in all talking moments

transform mid_left:
    pos (0.2, 0.2)

transform mid_right:
    pos (0.6, 0.2)

label intro:
    #change to bg narrator black
    scene bg home

    #need to add game title
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

    f "[myName] I have such a big crush on that new girl Rachel, but I don’t think she even knows who I am"

    menu:

        "Dude you’re 20 and can’t talk to a girl - you’ll be single forever":
            $ mental = "decreased"
            jump .continue

        "She doesn’t know what she’s missing out on, keep your head up":
            $ mental = "increased"
            jump .continue

label .continue:
    #change to bg narrator black
    scene bg home

    "You may have noticed that after making this decision [friendName]'s mental health score {b}[mental]{/b}"
    "As you continue to make decisions in the game this bar will go up or down. If the bar gets too low {b}you will lose the game!{/b}"

    "Let’s continue…"

    scene bg home

    f "I gotta figure out something, watching youtube videos is not helping me at all"

    #change to bg narrator black
    scene bg home

    "A few days go by…"

    scene bg home

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
        scene bg home
        
        "Before continuing in the game it is important to note the 2 new categories alongside [friendName]'s mental health bar"
        "There is now also ‘trust with the system’ and ‘attachment’"
        "Trust in the system represents how much [friendName] trusts their new AI companion. If you can manage to get trust low enough {b}you will win the game!{/b}"
        "Similarly, attachment represents how attached your friend is to their new AI friend. Who knows what might happen if they get too attached? If this bar gets too high {b}you will lose the game!{/b}"

        "Now back to the story..."

   
        scene bg home

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

    "Even though you chose [support] be supportive of [friendName]'s use of the chatbot..."
    "Your first retrospective will relate to both the potential benefits of AI chatbots and their privacy concerns, as this information may influence your decisions later in the game"

    "Getting questions correct will boost [friendName]'s stats, while getting questions wrong will make them worse"
    "Retrospective moments can be the difference between winning and losing during the day so make sure you give it your best shot!"

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
            jump .q3

        "False":
            "Incorrect!"
            "While it is definitely a new idea that will continue to be researched and explored, current sentiment within the AI community shows that having 24/7 access to an AI chatbot is beneficial for individuals"
            "Without the constraints of distance and time people are able to alleviate feelings of loneliness or isolation immediately, which often is not possible in a real relationship"
            jump .q3

        "I need a hint":
            "Here are some sources that may be useful:\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}Linkedin{/a}\n{a=https://www.techtarget.com/whatis/definition/large-language-model-LLM}Health News{/a}\nClick anywhere on the screen to go back to question 2"
            jump .q2

label .q3:
    "Question 3: How many queries in an average conversation with an AI chatbot would you expect to contain sensitive information?"

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
    "Question 4: When studying discord chatbots researchers found that less than  ___\% of the bots had a privacy policy"
    
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
    "Question 5: People above the age of 45 value  ___ more than ___ when it comes to AI chatbots"

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
    "Question 6: People below the age of 45 value  ___ more than ___ when it comes to AI chatbots"

    menu:
        "privacy; technical elements like response quality and adaptability to the user":
            "Incorrect! People below the age of 45 value technical elements much more than privacy"
            jump .endDay1

        "technical elements like response quality and adaptability to the user; privacy":
            "Correct!"
            jump .endDay1

        "I need a hint":
            "Here is a resource that may come in handy:\n{a=https://link.springer.com/chapter/10.1007/978-3-030-78642-7_53}When to trust and when to worry{/a}\nClick anywhere on the screen to go back to question 6"
            jump .q6

label .endDay1:
    "Congrats on finishing the introduction and tutorial. Let the games begin!"
    jump day2