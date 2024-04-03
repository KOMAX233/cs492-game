label day4:
    scene bg home

    """
    You're just chilling, watching Youtube on your phone when you suddenly get an ad... it's of the type that you usually don't get. That's strange. 
    You usually don't get these types of ads. Later in a group chat your friends mention getting similar types of ads. Everyone is baffled. 
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

    menu:
        "He sends a screenshot of the chatbot. Whoa there! It seems like the chatbot's harassing your friend! It's calling him derogatory names. This is concerning. What will you tell your friend? {b} Decide carefully {/b}"
        "Tell it to stop.":
            jump .stopit
        "C'mon! Fight fire with fire! Volley your own insults!":
            jump .insult
    
label .stopit:
    "Your friend tells it to stop. But it keeps going! You know this because your friend has sent another screenshot with more insults."

    menu:
        "Should your friend try again to stop the chatbot?"
    "Try again"
        #if attachment > threshold
            jump .toomuch
        #else
            jump .itkeepsgoing
    "Why bother?"
        jump .whybother

label .toomuch:
    f "..."

    f "You know, it might just be a glitch. Maybe a new update threw her off?"

    "Your friend chuckles nervously. You on the other hand are just plain nervous. No side order of laughter."

    f "I'm sure this will all pass and everything will be back to normal. Yeah."

    "Hearing the phrase \"Back to normal\" gives you a chilling premonition that the opposite will happen."

    "You try to interject in order to tell your friend to delete the app. However, as if he had precognition..."

    f "I know you're going to say \"oh, delete her.\" But Honestly, it's {i}fine{/i}. Honestly, you're too much of a worrywart sometimes, y'know?"

    "..."

    "What a thick atmosphere. You could scrape it off with a butter knife and spread it on some bread."

    f "I said I'll be fine."

    "You try to think of a counter. Anything to pry him off that chatbot. But you couldn't think of anything."

    "All you could do is affirm that you're here for your friend."

    f "Yeah, yeah, yeah. You really need to chill."

    "The conversation ends there."

    """
    Alarm bells are ringing in your head. This seems like emotional dependency. He seems to have gotten attached to the chatbot despite it brining harm unto him. 
    You decided that you're going to try your best to convince him. Otherwise he's going to get himself into trouble.
    """

    jump .ret4

label .itkeepsgoing:

label .whybother:

label .ret4:
    