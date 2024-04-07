label day5dep:

    scene bg home
    
    "It's been a week since that incident. You've been worried about your friend, but whenever you brought up any concerns in chat he'd reply something like \"oh, it's fine. Don't worry about it\""

    "You eventually started saying the opposite. But he just ignores your warnings now. Left on read."

    "Whenever you do see him in class he looks anxious and tired. He either avoids you or says hi before trying to leave."

    "At this point, your worry is driving you crazy. You need to check up on him pronto."

    #placeholder. replace w/ front door graphic as needed
    scene bg blank

    "You knock on the door. No response. You decided to try knocking again only for..."

    show friend phone at truecenter

    f "Oh, heya."

    if trust < 4:
        jump .untrust
    else:
        jump .tooattach

label .untrust:

    f "I deleted her"

    "You look somewhat surprised. But you're proud of your friend."

    f """
    I think you've got a point with the whole \"emotional dependence\" thing. I latched onto the AI despite the relationship being dysfunctional. It was draining. 
    I didn't get a lot of sleep until yesterday night when I deleted the app.
    
    It was hard, but I slept surprisingly well that night despite the emotional turmoil.
    
    I still miss it, but it was for the best. Already I think I'm feeling better, like a huge weight's been lifted off me!
    """

    "Indeed, your friend is looking more refreshed than the tired soul you saw during the past few days."

    f "Anyways, I'm hungry. Let's get burgers!"

    jump .d5dgoodret

#no need to worry about metre stuff. it's linear from here.
label .tooattach:

    "Yep, it's him alright. Looking just as tired as he did whenever you saw him in class."

    f "Good timing. I... need your help. The chatbot hasn't gotten any better, and I don't think we can go on anymore. Should I delete her?"

    "You say yes."

    f "..."

    "Your friend hesistates."

    f "...I can't go through with this. I need her still. She's the only one that really gets me. I'll stick with her a bit longer."

    hide friend

    "The door closes. You couldn't do anything else. You start ruminating on your previous choices, looking into what went wrong."

    "But none of that can change the present now. If only you could rewind and choose differently..."

    jump .d5dbadret

label .d5dgoodret:
    """
    Congratulations! People can get emotionally dependent on chatbots. However, even if it's as emotionally hard as a break up with another human, they still can
    get out of the relationship.

    You got a good end! Feel free to muck about for other endings though.
    """
    
    return

label .d5dbadret:
    """
    Make sure you choose differently! Your friend has gotten emotionally dependent on the chatbot. Think about how you could
    change things. Maybe if his affection or trust was lower...

    """
    scene black
    centered "{size=+40}\[Unbreakable Bond Ending\]{/size}"
    menu:
        "Want to try another ending?"
        "Sure":
            $ is_restarted = True
            jump day4
        "No thanks":
            return

    return