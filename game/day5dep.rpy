label day5:
    scene bg home
    
    "It's been a week since that incident. You've been worried about your friend, but whenever you brought up any concerns in chat he'd reply something like \"oh, it's fine. Don't worry about it\""

    "You eventually started saying the opposite. But he just ignores your warnings now. Left on read."

    "Whenever you do see him in class he looks anxious and tired. He either avoids you or says hi before trying to leave."

    "At this point, your worry is driving you crazy. You need to check up on him pronto."

    "You knock on the door. No response. You decided to try knocking again only for..."

    f "Oh, heya."

    #if trust < threshold or attach < threshold (not like the latter is going to happen since this path requires attachment be at a threshold but just in case)
        jump .untrust
    # else
        jump .hailmary

label .untrust:
    f "I deleted her"

    "You look somewhat surprised. But you're proud of your friend."

    f """
    I think you've got a point with the whole \"emotional dependence\" thing. I latched onto the AI despite the relationship being dysfunctional. It was draining. 
    I didn't get a lot of sleep until yesterday night when I deleted the app. It was hard, but I slept surprisingly well that night despite the emotional turmoil. I still miss it, 
    but it was for the best. Already I think I'm feeling better, like a huge weight's been lifted off me!
    """

    "Indeed, your friend is looking more refreshed than the tired soul you saw during the past few days."

    f "Anyways, I'm hungry. Let's get burgers!"

    jump .d5dgoodretro

#it's called hail mary since this is the player's last chance to get the good end
label .hailmary:
    "Yep, it's him alright. Looking just as tired as he did whenever you saw him in class."

    f "Good timing. I... need your help. The chatbot hasn't gotten any better, and I don't think we can go on anymore. Should I delete her?"

    menu optional_name:
        "Should your friend delete the chatbot? {b}Choose wisely.{/b}"
        "Do it.":
            # -attach, -trust (by three points)
            #if attach < threshold or trust < threshold
                jump .goodchoice
            #else
                jump .failedattempt
        "Eh. Wait for a week maybe.":
            #bad choice... but is it a bad end?
            jump .badchoice

label .goodchoice:
    f "..."

    "Your friend hesistates."

    f "Alright."

    "Your friend makes a series of taps. After that he shows you his screen. It's showing the chatbot being deleted. Finally, it's over."

    f "You were right. I did latch onto the chatbot too much. I probably will miss it, but it's for the best that I broke up with it."

    f "Anyways, I'm hungry. Let's get burgers!"

    jump .d5dgoodretro

label .failedattempt:
    f "...I can't go through with this. I need her still. She's the only one that really gets me. I'll stick with her a bit longer."

    "The door closes. You couldn't do anything else. You start ruminating on your previous choices, looking into what went wrong."

    "But none of that can change the present now. If only you could rewind and choose differently..."

    "Bad end."

    jump .d5dbadret

label .badchoice:
    f "...I'm being serious here. Are {i}you{/i} being serious? Arrrgh..."
    #-attach, -trust (by 1 point)

    #if attach < threshold or trust < threshold
        jump .goodchoice2

    #else
        jump .failedattempt

label .goodchoice2:
    "Your friend deletes the chatbot. He shows you proof."

    f "Seriously... what's with you? I was suffering under the abuse of this chatbot and you had to go and say stuff like that. Have some tact."

    "You apologize profusely. You don't know what got into you in the moment. Your friend surprsingly accepts the apology. However..."

    f "You're paying for the burgers! I'm hungry!"

    "Maybe if you chose wisely you could've saved a bit more money..."

    jump .d5dgoodret