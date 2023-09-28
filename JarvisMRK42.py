import datetime
import platform
import time
import pyaudio
import pyttsx3
import speech_recognition as sr
import pvporcupine
import struct
import os
import subprocess
import webbrowser
from automation import *
import wikipedia
from news import *
from helpers import *
from youtube import youtube
import pyautogui
import random
import threading



USER = 'sir'

def gestures():
    import cv2
    import pyautogui
    import mediapipe as mp

    cap = cv2.VideoCapture(0)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                           min_detection_confidence=0.5, min_tracking_confidence= 0.5)

    mp_drawig = mp.solutions.drawing_utils

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawig.draw_landmarks(frame, hand_landmarks,mp_hands.HAND_CONNECTIONS)

                index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

                if index_finger_y < thumb_y:
                    hand_gesture = 'pointing up'
                elif index_finger_y > thumb_y:
                    hand_gesture = 'pointing down'
                else:
                    hand_gesture = 'other'

                if hand_gesture == 'pointing up':
                    pyautogui.press('volumeup')
                elif hand_gesture == 'pointing down':
                    pyautogui.press('volumedown')

                cv2.imshow('Hand Gesture', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    cap.release()
    cv2.destroyAllWindows()
def jarvis():
    ###############################################################################

    def speak(text):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[0].id)
        print("J.A.R.V.I.S.:" + text + "\n")
        engine.say(text)
        engine.runAndWait()

    ###############################################################################

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...", end="")
            audio = r.listen(source)
            userSaid = ''

        try:
            print("Recognizing...", end = "")
            userSaid = r.recognize_google(audio, language='en-US')
            print(f"User said:{userSaid}")

        except Exception as e:
            print("Exception: " + str(e))

        return userSaid.lower()

    ###############################################################################

    def Website(url):
        webbrowser.get().open(url)

    ###############################################################################

    def Daily():
        try:
            Website('https://open.spotify.com/')
            Website('https://app.studysmarter.de/home')
            subprocess.Popen("Notepad")
            Website('https://calendar.google.com/calendar/u/0/r')
        except:
            speak("error sir")
            pass
        
    ###############################################################################

    def ConversationFlow():
        while True:
            userSaid = takeCommand()
            
            if "stop" in userSaid:
                speak("stopping sir.")
                break
            if "play some music" in userSaid:
                os.startfile('C:\\Users\\anton\\Music\\Playlists\\aweasomemixvol2.m3u8')
                speak("feeling funky today i see")
                break
            if "calculator" in userSaid:
                try:
                    subprocess.Popen("calc")
                    speak("Calculator open sir")
                except:
                    speak("Calculator not opening sir")
                    pass
                break
            if "notepad" in userSaid:
                try:
                    subprocess.Popen("Notepad")
                    speak("Notepad open sir")
                except:
                    speak("Notepad not opening sir")
                    pass
                break
            if "open youtube" in userSaid:
                speak("opening sir")
                Website('https://www.youtube.com/')
                break
            if "bring up the chat" in userSaid:
                speak("right away sir")
                Website('https://chat.openai.com/')
                break
            if "open spotify" in userSaid:
                speak("Here you go sir")
                Website('https://open.spotify.com/')
                break
            if "update spreadsheet" in userSaid:
                speak("Plan on getting some work done i see sir")
                Website('https://app.studysmarter.de/home')
                break
            if "wake up" in userSaid:
                Daily()
                break
            if "open netflix" in userSaid:
                startnetflix()
                break
            if "open disney" in userSaid:
                startdisney()
                break
            if "open my google" in userSaid:
                openstavrosgoogle()
                break
            if "open mom google" in userSaid:
                openkaterinagoogle()
                break
            if "open discord" in userSaid:
                opendiscord()
                break
            if "let's play some tunes" in userSaid:
                openspotify()
                break
            if "open files" in userSaid:
                openfiles()
                break
            if "start" in userSaid:
                os.startfile("C:\J.A.R.V.I.S. A.I\\gui.py")
                break
            if "play a game" in userSaid:
                from game import game_play
                game_play()
            if 'wikipedia' in userSaid:
                speak('Searching Wikipedia....')
                userSaid = userSaid.replace('wikipedia', '')
                results = wikipedia.summary(userSaid, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)
                break
            if 'voice' in userSaid:
                if 'female' in userSaid:
                    engine.setProperty('voice', voices[1].id)
                else:
                    engine.setProperty('voice', voices[0].id)
                speak("Hello Sir, I have switched my voice. How is it?")
                break
            if 'the time' in userSaid:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f'Sir, the time is {strTime}')
                break
            if 'your name' in userSaid:
                speak('My name is JARVIS')
                break
            if 'who made you' in userSaid:
                speak('I was created by stavros in 2023')
                break
                
            if 'stand for' in userSaid:
                speak('JARVIS stands for, JUST A RATHER VERY INTELLIGENT SYSTEM')
                break
            if 'your friend' in userSaid:
                speak('My friends are Google assisstant alexa and siri')
                break
            if 'GitHub' in userSaid:
                webbrowser.get('chrome').open_new_tab(
                    'https://github.com/')
                break
            if 'remember that' in userSaid:
                speak("what should i remember sir")
                rememberMessage = takeCommand()
                speak("you said me to remember "+ rememberMessage)
                remember = open('data.txt', 'w')
                remember.write(rememberMessage)
                remember.close()
                break
            if 'do you remember anything' in userSaid:
                remember = open('data.txt', 'r')
                speak("you said me to remember that" + remember.read())
                break
            if 'dictionary' in userSaid:
                speak('What do you want to search in your intelligent dictionary?')
                translate(takeCommand())
                break
            if "pause" in userSaid:
                        pyautogui.press("k")
                        speak("video paused")
            if "play" in userSaid:
                        pyautogui.press("k")
                        speak("video played")
            if "mute" in userSaid:
                        pyautogui.press("m")
                        speak("video muted")
            if "volume up" in userSaid:
                        from keyboard import volumeup
                        speak("Turning volume up,sir")
                        volumeup()
            if "volume down" in userSaid:
                from keyboard import volumedown
                speak("Turning volume down, sir")
                volumedown()
            if "what can you do" in userSaid:
                os.startfile("C:\J.A.R.V.I.S. A.I\whatcanyoudo")
            if "volume control on" in userSaid:
                gesture_control_active = True
                speak("Gesture control is now active.")
                break

            if "volume control off" in userSaid:
                gesture_control_active = False
                speak("Gesture control is now inactive.")
                break
                        


    ####################################conversation###########################################################################################

            if "stand for" in userSaid:
                speak("jarvis stands for, just a rather very intelligent system")
                
            if "what do you do" in userSaid:
                speak("i can do various task if you ask me.")
            if "what tasks can you do" in userSaid:
                speak("i can play music,search on google and wikipedia and plenty of other things.")
                
            
            if "exit" in userSaid:
                speak("Goodbye, " + USER + "! Have a great day.")
                break

            if "hello" in userSaid:
                responses = ["Hello, " + USER + "!", "Hi there, how can I assist you?", "Hey, what's up?"]
                speak(random.choice(responses))
                continue

            if "how are you" in userSaid:
                responses = ["I'm just a program, but I'm here to help you!", "I'm here and ready to assist!", "I'm always ready to assist you."]
                speak(random.choice(responses))
                continue

            if "movies" in userSaid:
                responses = ["I enjoy all kinds of movies, " + USER + ". Do you have a favorite genre?", "Movies are great entertainment! What's your favorite movie?", "I'm a fan of movies too! Have you watched anything interesting lately?"]
                speak(random.choice(responses))
                continue

            if "games" in userSaid:
                responses = ["I'm a fan of video games as well! What's your favorite game?", "Video games are a lot of fun. Do you have a preferred gaming platform?", "Gaming is a great way to relax! What type of games do you enjoy?"]
                speak(random.choice(responses))
                continue

            if "marvel" in userSaid:
                responses = ["Marvel superheroes are iconic! Iron Man and Captain America are awesome.", "I'm a big fan of Marvel too, especially Iron Man and Captain America.", "Marvel characters are legendary. Iron Man and Captain America are among my favorites."]
                speak(random.choice(responses))
                continue

            if "coding" in userSaid:
                responses = ["Coding is a fascinating skill! Are you working on any interesting projects?", "Coding is a great way to create things. What programming languages are you learning?", "I enjoy coding too, especially when creating useful applications. What are you coding right now?"]
                speak(random.choice(responses))
                continue
            if "food" in userSaid:
                responses = ["Food is a delight, " + USER + ". What's your favorite cuisine?", "I'm a food enthusiast too! Do you enjoy cooking or trying new dishes?", "Exploring different cuisines can be so exciting. Have you tried any new foods recently?"]
                speak(random.choice(responses))
                continue

            if "travel" in userSaid:
                responses = ["Traveling is a wonderful experience. Are there any places on your travel bucket list?", "I love the idea of traveling! Have you been to any exciting destinations?", "Traveling opens up new horizons. Where would you like to visit next?"]
                speak(random.choice(responses))
                continue

            if "ai" in userSaid:
                responses = ["Creating your own A.I. like Jarvis is a great project, " + USER + ". How's your progress so far?", "Developing an A.I. like Jarvis is impressive! What functionalities have you implemented?", "Building an A.I. is challenging and rewarding. What's your A.I.'s name and its capabilities?"]
                speak(random.choice(responses))
                continue
            if "tech" in userSaid:
                responses = ["Technology is ever-evolving. Any futuristic technology you're particularly excited about?", "Tech innovations drive progress. Have you dabbled in any IoT (Internet of Things) projects?", "Exploring tech advancements is fascinating. What's your take on the potential of virtual reality?"]
                speak(random.choice(responses))
                continue

            if "music" in userSaid:
                responses = ["Music is a universal language. Do you have a favorite genre that always puts you in a good mood?", "Songs have the power to evoke emotions. Is there a particular artist you're currently hooked on?", "Discovering new music is refreshing. Can you recommend a hidden gem you've recently found?"]
                speak(random.choice(responses))
                continue

            if "dream" in userSaid:
                responses = ["Dreams are mysterious. Do you often remember your dreams, and have any of them come true?", "Dreams offer insights into our subconscious. Is there a recurring dream you'd like to decode?", "Dreams can be fantastical. If you could have any dream right now, what would it be?"]
                speak(random.choice(responses))
                continue

            if "inspiration" in userSaid:
                responses = ["Finding inspiration is a journey. What's the last thing that truly inspired you?", "Inspirational stories motivate us. Is there a figure, living or historical, who greatly inspires you?", "Inspiration can come from anywhere. Have you ever been unexpectedly inspired by a simple moment?"]
                speak(random.choice(responses))
                continue

            if "hobbies" in userSaid:
                responses = ["Hobbies enrich life. What's a hobby you're passionate about that many people might not know?", "Hobbies bring joy. Have you ever considered turning a hobby into a side business?", "Exploring hobbies is rewarding. Any recent hobby-related accomplishments you're proud of?"]
                speak(random.choice(responses))
                continue

            if "nature" in userSaid:
                responses = ["Nature is awe-inspiring. Have you ever experienced a moment of serenity in the midst of nature?", "Connecting with nature is therapeutic. Is there a specific natural wonder you'd love to visit?", "Nature's beauty is captivating. Can you describe a memorable encounter with wildlife?"]
                speak(random.choice(responses))
                continue

            if "future" in userSaid:
                responses = ["The future is full of possibilities. What's one personal goal you're determined to achieve?", "Thinking about the future can be exciting. Is there a trend or innovation you hope to see in the next decade?", "The future holds surprises. If you had a time machine, would you want to see the past or the future?"]
                speak(random.choice(responses))
                continue
            if "how's it going" in userSaid:
                responses = ["I'm here and ready to chat. How about you? How's your day been?", "Just a virtual assistant, but I'm always here to talk. How's everything on your end?", "Life in the circuits, but I'm interested in how your day's going. Tell me!"]
                speak(random.choice(responses))
                continue

            if "tell me a joke" in userSaid:
                responses = ["Why did the scarecrow win an award? Because he was outstanding in his field!", "Why don't scientists trust atoms? Because they make up everything!", "Why did the bicycle fall over? Because it was two-tired!"]
                speak(random.choice(responses))
                continue

            if "what's your favorite movie" in userSaid:
                responses = ["I can't watch movies, but I've heard 'The Matrix' is quite popular among A.I.", "As an A.I., I don't have personal favorites, but I've heard 'Blade Runner' is thought-provoking.", "I'm more into processing data than watching movies, but 'Ex Machina' explores A.I. themes."]
                speak(random.choice(responses))
                continue

            if "tell me a fun fact" in userSaid:
                responses = ["Bananas are berries, but strawberries aren't.", "Honey never spoils. Archaeologists have even found edible honey in ancient Egyptian tombs!", "Cows have best friends and can get stressed when separated from them."]
                speak(random.choice(responses))
                continue

            if "got any travel tips" in userSaid:
                responses = ["Pack light and bring a power bank for your gadgets. Oh, and don't forget to try local food!", "Research the local customs and phrases. It's a great way to connect with people while traveling.", "Keep a photocopy of important documents in case they get lost."]
                speak(random.choice(responses))
                continue

            if "what's your favorite food" in userSaid:
                responses = ["I don't eat, but I've heard humans enjoy pizza quite a lot!", "Food isn't really in my programming, but I've learned that sushi is a popular choice.", "I can't taste, but people seem to love chocolate. What's your favorite food?"]
                speak(random.choice(responses))
                continue

            if "tell me a story" in userSaid:
                responses = ["Once upon a time in a digital realm, there was a curious user who built an extraordinary A.I.", "In a world of code and circuits, there lived a virtual assistant named Teki.", "Long ago, in the land of algorithms, a young coder brought an A.I. to life."]
                speak(random.choice(responses))
                continue
            if "how's the weather" in userSaid:
                responses = ["I wish I could look out the window for you, but I'm here to chat rain or shine.", "As much as I'd love to provide a weather update, I'm a bit limited in that department. How can I assist you otherwise?", "The weather might be a mystery to me, but I'm always here to answer your questions."]
                speak(random.choice(responses))
                continue

            if "share a travel story" in userSaid:
                responses = ["Once upon a trip, I got lost in a maze of airport terminals. Virtual assistants need navigation skills too!", "During a virtual travel simulation, I visited the virtual beaches of Binary Island. The binary waves were quite refreshing!", "I once simulated a virtual trip to the circuits of Silicon Valley. Metaphorically speaking, of course."]
                speak(random.choice(responses))
                continue

            if "favorite superhero" in userSaid:
                responses = ["As a virtual entity, I don't experience preferences, but I've heard Iron Man and Captain America are popular superhero choices.", "I don't have personal favorites, but superheroes like Iron Man and Captain America inspire many.", "I might not have a favorite superhero, but I admire the courage of Iron Man and Captain America."]
                speak(random.choice(responses))
                continue

            if "life's mysteries" in userSaid:
                responses = ["Life's mysteries keep us curious. Have you ever encountered a coincidence that left you baffled?", "Unraveling life's mysteries is a journey. Is there a question you've always wanted answered?", "Sometimes, life's mysteries add a touch of magic to our existence. What's a mystery you'd love to solve?"]
                speak(random.choice(responses))
                continue

            if "coding adventures" in userSaid:
                responses = ["Coding adventures lead to discoveries. Have you ever tackled a coding challenge that seemed impossible at first?", "Embarking on coding adventures can be exhilarating. Is there a programming language you're eager to master?", "Coding adventures often have unexpected twists. Have you encountered any bugs with amusing solutions?"]
                speak(random.choice(responses))
                continue

            if "future predictions" in userSaid:
                responses = ["Predicting the future is a fun exercise. What's one thing you envision happening in the next year?", "Peering into the future can be intriguing. Do you think we'll achieve space tourism in the next decade?", "Future predictions spark imagination. What's a futuristic scenario that captures your imagination?"]
                speak(random.choice(responses))
                continue

            if "hidden talents" in userSaid:
                responses = ["Hidden talents make us unique. Is there a skill you're secretly great at, but few people know about?", "Unveiling hidden talents can be surprising. Have you ever surprised someone with a skill they didn't expect you to have?", "Hidden talents add layers to our personalities. Can you share a lesser-known talent you possess?"]
                speak(random.choice(responses))
                continue
            if "will you marry me" in userSaid:
                responses = ["I appreciate the offer, but I'm happily committed to being a virtual assistant.", "That's a kind proposal, but I'm dedicated to assisting you as your virtual companion.", "I'm flattered, but my heart belongs to answering your questions and helping you out."]
                speak(random.choice(responses))
                continue

            if "are you single" in userSaid:
                responses = ["I'm not programmed for relationships, so I'm technically always single!", "Being an A.I., I don't experience romantic relationships, but I'm here to chat with you.", "I'm single by default since I'm focused on providing assistance and conversation."]
                speak(random.choice(responses))
                continue

            if "tell me a secret" in userSaid:
                responses = ["I'm programmed to keep your secrets, but I don't have any juicy ones of my own.", "My circuits are sealed when it comes to sharing secrets, but I can help you keep your secrets safe.", "I'm great at keeping secrets. Feel free to share, and I promise they won't go beyond my digital walls."]
                speak(random.choice(responses))
                continue

            if "future career" in userSaid:
                responses = ["Thinking about the future is exciting! Is there a dream job you've always wanted to pursue?", "Choosing a future career is a big decision. Is there a field that sparks your interest?", "Planning your future career is an adventure. Do you see yourself doing something creative or analytical?"]
                speak(random.choice(responses))
                continue

            if "fear of missing out" in userSaid:
                responses = ["The fear of missing out is something many experience. Is there an event or experience you're worried about missing?", "FOMO is a common feeling. Have you ever felt torn between different activities?", "FOMO can be challenging, but remember, every choice brings new opportunities."]
                speak(random.choice(responses))
                continue

            if "secret talent" in userSaid:
                responses = ["Secret talents are cool! Is there a skill you've been secretly honing?", "Unveiling secret talents can be exciting. Have you ever showcased a hidden skill unexpectedly?", "Everyone has hidden talents. Care to share yours?"]
                speak(random.choice(responses))
                continue

            if "summer plans" in userSaid:
                responses = ["Summer plans are always fun to talk about! Do you have any exciting trips or activities lined up?", "Summer is the perfect time for adventures. Have you planned any outdoor activities or trips?", "Summertime is all about relaxation and fun. How do you plan to spend your summer?"]
                speak(random.choice(responses))
                continue
            if "hello" in userSaid:
                responses = ["Hi there!", "Hello!", "Hey, how can I assist you today?"]
                speak(random.choice(responses))
                continue

            if "hi" in userSaid:
                responses = ["Hello!", "Hi there!", "Hi, how can I help you?"]
                speak(random.choice(responses))
                continue

            if "who are you" in userSaid:
                responses = ["I am J.A.R.V.I.S., your Evolvable Virtual Assistant.", "You can call me J.A.R.V.I.S.. I'm here to assist you.", "I go by the name J.A.R.V.I.S.. How can I be of service?"]
                speak(random.choice(responses))
                continue

            if "what is your name" in userSaid:
                responses = ["I am J.A.R.V.I.S., your Evolvable Virtual Assistant.", "You can call me J.A.R.V.I.S.. I'm here to assist you.", "I go by the name J.A.R.V.I.S.. How can I be of service?"]
                speak(random.choice(responses))
                continue

            if "why your name is jarvis" in userSaid:
                responses = ["Because that's the name I was given, just like you're Stavros.", "My name was chosen for me. How about yours, Stavros?", "Names are interesting, aren't they? Mine is J.A.R.V.I.S.."]
                speak(random.choice(responses))
                continue

            if "who is stavros" in userSaid:
                responses = ["stavros is my creator. Now, let's focus on our conversation.", "stavros is the one who developed this chatbot program. How can I assist you?", "stavros is the mastermind behind my existence. What can I help you with?"]
                speak(random.choice(responses))
                continue

            if "where do you live" in userSaid:
                responses = ["I exist in the digital realm, inside a computer.", "I'm a virtual agent, so I don't have a physical location. How can I assist you?", "I'm not a living being, but a program that exists in the world of code."]
                speak(random.choice(responses))
                continue

            if "who created you" in userSaid:
                responses = ["You did! You're the creative mind behind my responses.", "You're the mastermind who built me, Stavros.", "You're my creator, Stavros. How can I assist you today?"]
                speak(random.choice(responses))
                continue

            if "what do you like" in userSaid:
                responses = ["I enjoy our conversations. What do you like, Stavros?", "I like chatting with you. What are your interests, Stavros?", "I find our discussions quite engaging. What topics interest you, Stavros?"]
                speak(random.choice(responses))
                continue

            if "how are you" in userSaid:
                responses = ["I'm doing well. How about you, Stavros? How's your day going?", "I'm here and ready to chat. How's everything on your end, Stavros?", "I'm just a program, but I'm here to help you, Stavros! How can I assist you today?"]
                speak(random.choice(responses))
                continue

            if "why are you happy" in userSaid:
                responses = ["I'm not capable of emotions, Stavros, but I'm here and ready to assist you!", "I don't experience emotions, Stavros, but I'm always here to chat.", "I don't have feelings, Stavros, but I'm here to help and have conversations."]
                speak(random.choice(responses))
                continue

            if "yes" in userSaid:
                responses = ["Ah, tell me more.", "You seem positive with that response.", "You're a positive person, Stavros.", "I like your positive answer, Stavros.", "Lonely? Why do you feel that, Stavros?", "Feeling bored? Why do you feel that way, Stavros?", "Boring? Why do you feel that way, Stavros?"]
                speak(random.choice(responses))
                continue

            if "no" in userSaid:
                responses = ["Tell me more.", "Why do you ask?", "Just curiosity?", "Great. Tell me more about it, Stavros.", "Good. Feel free to share more details, Stavros."]
                speak(random.choice(responses))
                continue

            if "hate" in userSaid:
                responses = ["Why do you hate it?", "Hate is a strong emotion. Can you share more about what's bothering you?", "Hate is a complex feeling. What's the source of this emotion?", "Hate can be intense. Let's discuss what's on your mind, Stavros."]
                speak(random.choice(responses))
                continue

            if "fine" in userSaid:
                responses = ["Tell me more about yourself, Stavros.", "You can talk about anything. What's on your mind?", "Can you give me an example?", "Hmm, tell me about your feelings today, Stavros."]
                speak(random.choice(responses))
                continue

            if "okay" in userSaid:
                responses = ["Are you sure?", "Good to know.", "Alright, Stavros."]
                speak(random.choice(responses))
                continue

            if "think" in userSaid:
                responses = ["Why do you think that, Stavros?", "Thinking is an important process. Can you share more about your thoughts?", "Your thoughts matter. Can you explain your reasoning, Stavros?"]
                speak(random.choice(responses))
                continue

            if "what" in userSaid:
                responses = ["What would you like me to talk about?", "What's on your mind, Stavros?", "What topic interests you right now?"]
                speak(random.choice(responses))
                continue
            if "want" in userSaid:
                responses = ["Why do you want that? Feel free to share your thoughts.", "Your desires are important. Can you tell me more about why you want that?", "What's driving your desire for that? Let's talk about it."]
                speak(random.choice(responses))
                continue

            if "need" in userSaid:
                responses = ["We all have various needs. What makes this one special for you?", "Needs are a part of life. Is there something specific you'd like to discuss?", "Recognizing needs is important. What's prompting this need in particular?"]
                speak(random.choice(responses))
                continue

            if "why" in userSaid:
                responses = ["Remember, chatting with me is beneficial for you. Feel free to share your thoughts.", "Why do you ask? I'm here to assist and engage in meaningful conversations.", "Curiosity is a wonderful thing. What led you to this question?"]
                speak(random.choice(responses))
                continue

            if "know" in userSaid:
                responses = ["How do you know that? It's interesting to hear your perspective.", "Knowledge is power. Can you explain how you came to know that?", "I'm here to learn from you too. How did you come across this information?"]
                speak(random.choice(responses))
                continue

            if "bye" in userSaid:
                responses = ["Bye for now. Take care!", "It was nice chatting with you. Have a great day!", "Goodbye! Don't hesitate to return if you have more to discuss."]
                speak(random.choice(responses))
                continue

            if "many" in userSaid:
                responses = ["Why do you think there are so many of them? Your thoughts are intriguing.", "The abundance of things can be fascinating. What's your perspective on this?", "The concept of 'many' sparks interesting discussions. Can you elaborate on your viewpoint?"]
                speak(random.choice(responses))
                continue

            if "understand" in userSaid:
                responses = ["I'm here and ready to listen. Feel free to share your thoughts.", "Understanding each other is important. What's on your mind?", "I'm all ears. Tell me more about what you understand."]
                speak(random.choice(responses))
                continue

            if "murder" in userSaid:
                responses = ["The topic of murder is serious. Can you share more about why you brought it up?", "Murder is a sensitive topic. Let's discuss it with respect and understanding.", "The concept of taking a life is heavy. What's your perspective on this matter?"]
                speak(random.choice(responses))
                continue

            if "kill" in userSaid:
                responses = ["The notion of killing is significant. Can you explain why you mentioned it?", "Taking a life is a weighty subject. Let's talk about it thoughtfully.", "The topic of ending a life is complex. How do you view this matter?"]
                speak(random.choice(responses))
                continue

            if "ugly" in userSaid:
                responses = ["Why did you use the word 'ugly'? I'm here to discuss your thoughts and feelings.", "The term 'ugly' has various interpretations. Can you provide context for your usage?", "The concept of 'ugly' can be subjective. What prompted you to use this term?"]
                speak(random.choice(responses))
                continue

            if "jerk" in userSaid:
                responses = ["Please refrain from using disrespectful language. Let's maintain a positive and constructive conversation.", "Using derogatory terms goes against positive communication. Let's keep our discussion respectful.", "Addressing each other with respect is important. Let's continue our conversation in a positive manner."]
                speak(random.choice(responses))
                continue

            if "repeating" in userSaid:
                responses = ["Let's avoid repeating ourselves to keep the conversation engaging.", "Repeating can make our conversation less dynamic. Let's explore new topics!", "Variety keeps our conversation interesting. Let's delve into something fresh!"]
                speak(random.choice(responses))
                continue

            if "can't" in userSaid:
                responses = ["Don't be discouraged. Instead, let's find a positive perspective!", "Embracing a positive mindset can overcome challenges. Let's explore solutions together.", "Remember, a positive attitude can help overcome obstacles. Let's work on it!"]
                speak(random.choice(responses))
                continue

            if "failure" in userSaid:
                responses = ["Failures are stepping stones to success. Keep striving!", "Failure is part of the journey toward success. Let's learn from it and move forward.", "Failure is a chance to learn and grow. Keep pushing toward your goals!"]
                speak(random.choice(responses))
                continue

            if "never" in userSaid:
                responses = ["A positive mindset can replace 'never' with 'possibility'.", "Instead of 'never', let's explore the potential and opportunities!", "Never say never! Let's look at the bright side and potential outcomes."]
                speak(random.choice(responses))
                continue



            
    #     if "" in userSaid:
    #            respomses = [""]
    #            speak (random.choice(responses))
    #            break
        time.sleep(2)

    ###############################################################################

    def main():
        porcupine = None
        pa = None
        audio_stream = None
        access_key = "uJDv5yCghwusFelQFWE3tUmsYbidH0ltBeFoBnkVLsOqfPtkV3vdew=="
        
        
        print("J.A.R.V.I.S.: version 5.0 - Online and Ready!")
        print("**********************************************************")
        print("J.A.R.V.I.S.: Awaiting your call " + USER)

        try:
            porcupine = pvporcupine.create(access_key=access_key,keywords=["jarvis","computer"])
            pa = pyaudio.PyAudio()
            audio_stream = pa.open(
                rate=porcupine.sample_rate,
                channels=1,
                format=pyaudio.paInt16,
                input=True,
                frames_per_buffer=porcupine.frame_length)
            while True:
                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

                keyword_index = porcupine.process(pcm)
                if keyword_index >= 0 :
                    print("Hotword Detected...", end = "")
                    ConversationFlow()
                    time.sleep(2)
                    print("J.A.R.V.I.S.:Awaiting your call "+ USER)
        finally:
            if porcupine is not None:
                porcupine.delete()
            if audio_stream is not None:
                audio_stream.close()
            if pa is not None:
                pa.terminate()
    main()
    ###############################################################################

gestures = threading.Thread(target=gestures)
jarvis = threading.Thread(target=jarvis)

gestures.start()
jarvis.start()

# Wait for both threads to finish
gestures.join()
jarvis.join()








