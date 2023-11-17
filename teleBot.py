import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6490104255:AAEFLWTwrlfgUUe3IxvzBydkjbrN4sVI4bg')

# Variables 

NesoAcademy = "Neso Academy \nis a renowned YouTube channel recognized for its high-quality educational content.  Neso Academy provides comprehensive video lectures, tutorials, and explanations to help students grasp complex concepts with ease. The channel's founder and instructor, Vineet Khatri, has garnered praise for his clear teaching style and ability to break down intricate topics into understandable segments."


ApnaCollage = "Apna college\nThe Apna College YouTube channel is a popular online platform dedicated to providing educational content to students and learners across various subjects. With engaging videos and tutorials, the channel aims to simplify complex topics and make learning more accessible and enjoyable."

DineshVaryani = 'Dinesh Varyani \nmake free programming tutorials from beginner to advanced level. That includes Java for beginners, who is known for his excellent teachings. who is also a full stack developer and has 10 year of experience '

MoshHamedani = "Mosh Hamedani, \nbetter known online as Programming with Mosh, is an Australian educational YouTuber and software engineer specializing in web application development with ASP.NET MVC, Web API, Entity Framework, Angular, Backbone, HTML5, and CSS. He is based in Melbourne, Australia."

CalebCurry = "Caleb Curry \nis a popular programming educator on YouTube. His tutorials are well-structured and beginner-friendly, making them a great resource for learning C." 

CodeWithHarry = "Code With Harry \nis a widely recognized and popular YouTube channel  created by Harry Singh , the channel focuses on a diverse range of programming languages, web development, app development, and other coding-related topics. Harry's engaging teaching style, real-world examples, and step-by-step explanations have made CodeWithHarry a go-to resource for beginners and intermediate learners in the programming world."

Campus_x = 'Campus X \nis a budding YouTube channel that offers  a detailed knowledge on programming and technology-related tutorials with good explanation. The channel focuses on a diverse range of programming languages, web development, app development, and other coding-related topics'

TheCodingNinjas = 'The Coding Ninjas \nYouTube channel is a popular destination for programming enthusiasts and aspiring software developers. Known for its comprehensive coding tutorials and tech-related content.the Coding Ninjas channel has gained a substantial following, making it a valuable resource for those looking to sharpen their coding abilities and stay updated with the latest developments in the tech world. '

Telusko = "Telusko started with the aim not just to teach but to educate to in Navin's words 'Aliens'. On Telusko platform we provide industry level quality content on technologies like Java, Blockchain, Python, JavaScript and their implementations."

Kunal_Kushawaha = "He is a developer relations manager at Civo, CNCF Ambassador, TEDx speaker and a GitHub Star. He is the founder of WeMakeDevs and also started the official Cloud Native Student Community group joined by thousands of folks, focussed on getting more young people involved in the ecosystem."

freeCodeCamp = 'freeCodeCamp \n(also referred to as Free Code Camp) is a non-profit organization that consists of an interactive learning web platform, an online community forum, chat rooms, online publications and local organizations that intend to make learning software development accessible to anyone.'

TheNetNinja = "The Net Ninja (Shaun Pelling)\nCurrent owner of The Net Ninja, with over 1 million active subscribers & over 85,000 students on Udemy. Experienced Content Creator with a history rich in the e-learning & programming industry. Skilled in JavaScript, Firebase, Vue.js, React, Node.js, PHP & python. Master's Degree focused in Astrophysics from The University of Manchester."

    # Create a reply keyboard
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
button_program = KeyboardButton('Programming--Languages')
button_dev = KeyboardButton('Dev-Domains')
button_dsa = KeyboardButton('DSA')
reply_keyboard.add(button_program, button_dev, button_dsa)

# Reply Keyboard or start keyboard for domain
domainKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Frontend","Backend","Full-stack","Android","UI/UX-Design","DevOps")


# Reply Keyboard or start keyboard for frontend english
frontendKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👩‍🏫","Internet🌐","HTML📝","CSS🌈","Javascript🀄","Version-control⬆","CSS-Framework🏢","JS-Framework⚒","Server-side-rendering⬇","Typescript📜")


# Reply Keyboard or start keyboard for frontend Hindi
frontendHKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👨‍🏫","Internet🔌","HTML✍","CSS🍡","Javascript📜","Version-control🔼","CSS-Framework⚒","JS-Framework🏢","Server-side-rendering🔽","Typescript📄")


# Reply Keyboard or start keyboard for backend english
backendEKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👩‍🏫","Internet🌐","Choose a language🔠","Version-control⬆","Relational-Database📤","NoSQl-Database🗳","APIs🦅","Caching🗑","Testing🔍","Containerization📦","GraphQL🗃")


# Reply Keyboard or start keyboard for backend hindi 
backendHKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👨‍🏫","Internet🔌","Choose a language🔠","Version-control🔼","Relational-Database📥","NoSQl-Database🥡","APIs🕊","Caching🗑","Testing🔍","Containerization📦","GraphQL🍱")

# Reply Keyboard or start keyboard for fullStack english
fullEKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👨‍🏫","HTML📝","CSS🌈","Javascript🀄","Version-control⬆","Tailwind🏳‍🌈","React⚛","Nodejs🔰","PostgreSQL🥡","Restful-APIs🦅","JWT-auth🔐","Redis🧧","Linux-basics🐧","AWS-Services🧰","Github-actions😸","Ansible⚓","Terraform🔹")

# Reply Keyboard or start keyboard for fullStack hindi
fullHKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👨‍🏫","HTML✍","CSS🍡","Javascript📜","Version-control🔼","Tailwind🏁","React🕸","Nodejs✅","PostgreSQL📦","Restful-APIs🕊","JWT-auth🔐","Redis🧧","Linux-basics🐥","AWS-Services🗳","Github-actions😸","Ansible🔱","Terraform🔷")

# Reply Keyboard or start keyboard for mobile application language
mobileKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("English📱","Hindi📲")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi!\nI'm CAREER CRAFTER Bot!\nI will help you through your career.\n Choose your Domain below", reply_markup=reply_keyboard)

    

# Create an inline keyboard
language_markup =  InlineKeyboardMarkup()
lngBtn1 = InlineKeyboardButton('Python',callback_data="Python")
lngBtn2 = InlineKeyboardButton('Java',callback_data="Java")
lngBtn3 = InlineKeyboardButton('CLanguage',callback_data="CLanguage")
language_markup.add(lngBtn1, lngBtn2, lngBtn3)

# Inline keyboard for Python languages
pyChooseKeyboard_inline =  InlineKeyboardMarkup()
pyLngHindi = InlineKeyboardButton('Hindi',callback_data="PythonHindi")
pyLngEnglish = InlineKeyboardButton('English',callback_data="PythonEnglish")
pyChooseKeyboard_inline.add(pyLngHindi, pyLngEnglish)

# Inline keyboard for choosing languages for java
javaChooseKeyboard_inline = InlineKeyboardMarkup()
javaHindi = InlineKeyboardButton("Hindi", callback_data="javaHindi")
javaEnglish = InlineKeyboardButton("English", callback_data="javaEnglish")
javaChooseKeyboard_inline.add(javaEnglish, javaHindi)

# Inline keyboard for choosing languages for c
ClangChooseKeyboard_inline = InlineKeyboardMarkup()
CLHindi = InlineKeyboardButton("Hindi", callback_data="CLHindi")
CLEnglish = InlineKeyboardButton("English", callback_data="CLEnglish")
ClangChooseKeyboard_inline.add(CLEnglish, CLHindi)

# Inline keyboard for Languages in DSA
LangDSAkeyboard_inline = InlineKeyboardMarkup()
DSAPython = InlineKeyboardButton("Python", callback_data="DPython")
DSAJava = InlineKeyboardButton("Java", callback_data="DJava")
DSALanguage = InlineKeyboardButton("C Language", callback_data="DCLanguage")
LangDSAkeyboard_inline.add(DSAPython, DSAJava,DSALanguage)

# Inline keyboard for choosing DSA languages for python
DSApHindi = InlineKeyboardButton("Hindi", callback_data="pythonHindi")
DSApEnglish = InlineKeyboardButton("English", callback_data="pythonEnglish")
pythonChooseKeyboard_inline = InlineKeyboardMarkup().add(DSApEnglish, DSApHindi)

# Inline keyboard for choosing DSA languages for java
DSAjHindi = InlineKeyboardButton("Hindi", callback_data="javaDHindi")
DSAjEnglish = InlineKeyboardButton("English", callback_data="javaDEnglish")
javaDSAChooseKeyboard_inline = InlineKeyboardMarkup().add(DSAjHindi, DSAjEnglish)

# Inline keyboard for choosing DSA languages for c
DSAcHindi = InlineKeyboardButton("Hindi", callback_data="CHindi")
DSAcEnglish = InlineKeyboardButton("English", callback_data="CEnglish")
CChooseKeyboard_inline = InlineKeyboardMarkup().add(DSAcEnglish,DSAcHindi)

# Inline keyboard for choosing frontend languages
Hindi = InlineKeyboardButton(text="Hindi", callback_data="frontHindi")
English = InlineKeyboardButton(text="English", callback_data="frontEnglish")
frontChooseKeyboard_inline = InlineKeyboardMarkup().add(English, Hindi)

# Inline keyboard for choosing CSS framework English
Bootstrap = InlineKeyboardButton(text="Bootstrap", callback_data="bootstrap")
Tailwind = InlineKeyboardButton(text="Tailwind", callback_data="tailwind")
CSSEChooseKeyboard_inline = InlineKeyboardMarkup().add(Tailwind, Bootstrap)

# Inline keyboard for choosing JS framework English
react = InlineKeyboardButton(text="React", callback_data="react")
angular = InlineKeyboardButton(text="Angular", callback_data="angular")
vue = InlineKeyboardButton(text="Vue", callback_data="vue")
JSEChooseKeyboard_inline = InlineKeyboardMarkup().add(react,angular,vue)

# Inline keyboard for choosing rending English
NextJS = InlineKeyboardButton(text="NextJS", callback_data="NextJS")
angular_universal = InlineKeyboardButton(text="angular universal", callback_data="angular_universal")
rendingEChooseKeyboard_inline = InlineKeyboardMarkup().add(NextJS,angular_universal)

# Inline keyboard for choosing mobile English
reactNative = InlineKeyboardButton(text="React Native", callback_data="reactNative")
flutter = InlineKeyboardButton(text="Flutter", callback_data="flutter")
mobileEChoosekeyboard_inline = InlineKeyboardMarkup().add(reactNative,flutter)

# Inline keyboard for choosing CSS framework English
Bootstrap = InlineKeyboardButton(text="Bootstrap", callback_data="Hbootstrap")
Tailwind = InlineKeyboardButton(text="Tailwind", callback_data="Htailwind")
CSShChoosekeyboard_inline = InlineKeyboardMarkup().add(Tailwind, Bootstrap)


# Inline keyboard for choosing JS framework English
react = InlineKeyboardButton(text="React", callback_data="Hreact")
angular = InlineKeyboardButton(text="Angular", callback_data="Hangular")
vue = InlineKeyboardButton(text="Vue", callback_data="Hvue")
JSHChoosekeyboard_inline = InlineKeyboardMarkup().add(react,angular,vue)


# Inline keyboard for choosing rending Hindi
NextJS = InlineKeyboardButton(text="NextJS", callback_data="HNextJS")
angular_universal = InlineKeyboardButton(text="angular universal", callback_data="angular_universal")
rendingHChoosekeyboard_inline = InlineKeyboardMarkup().add(NextJS,angular_universal)

# back button
menuChooseKeyboard_inline = InlineKeyboardMarkup()
menu = InlineKeyboardButton("Menu🔙", callback_data="menu")
menuChooseKeyboard_inline.add(menu)


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"Choose an option:")
    
    
    
    
    
# This is for ReplyKeyboardMarkup
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    remove_keyboard = ReplyKeyboardRemove()
    if message.text == 'Programming--Languages':
        bot.reply_to(message, "A programming language is a way for programmers (developers) to communicate with computers.\n Choose which you want to start with",reply_markup=language_markup)
    elif message.text == 'DSA':
        bot.reply_to(message,"Road map for DSA")
        bot.send_message(message.chat.id,"https://i.ibb.co/ZdLrF3S/Whats-App-Image-2023-08-19-at-11-24-19-PM.jpg")
        bot.send_message(message.chat.id,"Data structure and Algorithm (DSA) is applied in all disciplines of software development.\n DSA is the building block of the software development process.\nChoose which you want to start with", reply_markup=LangDSAkeyboard_inline)
    elif message.text == 'Dev-Domains':
        bot.reply_to(message,"A domain just for developers. From tools to platforms, languages to blogs.\nChoose which you want to start with", reply_markup=domainKeyboard_reply)
    elif message.text == 'Frontend':
        bot.reply_to(message,"A Front-End Developer is someone who creates websites and web applications.\nFront-end web development is the development of the graphical user interface of a website.\nChoose Which Language you familiar with", reply_markup=frontChooseKeyboard_inline)
    elif message.text == 'About_authors👩‍🏫':
        bot.reply_to(message,"Some best authors from youtube")
        bot.send_message(message.chat.id, freeCodeCamp)
        bot.send_message(message.chat.id, MoshHamedani)
        bot.send_message(message.chat.id, TheNetNinja)
        bot.send_message(message.chat.id, "And so on",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Internet🌐':
        bot.reply_to(message,"HOW internet works ?")
        bot.send_message(message.chat.id,"https://youtu.be/zN8YNNHcaZc",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'HTML📝':
        bot.reply_to(message, "Choose anyone has you prefer")
        bot.send_message(message.chat.id, "From, freeCodeCamp")
        bot.send_message(message.chat.id, "https://youtu.be/kUMe1FH4CHE")
        bot.send_message(message.chat.id, "From, The Net Ninja")
        bot.send_message(message.chat.id, "https://youtu.be/qz0aGYrrlhU",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'CSS🌈':
        bot.reply_to(message,"From, freeCodeCamp")
        bot.send_message(message.chat.id, "https://youtu.be/OXGznpKZ_sA",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Javascript🀄':
        bot.reply_to(message,"From, programming with mosh")
        bot.send_message(message.chat.id, "https://youtu.be/W6NZfCO5SIk",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Version-control⬆':
        bot.reply_to(message,"From, kunal kushwaha(Git and Github)")
        bot.send_message(message.chat.id, "https://youtu.be/apGV9Kg7ics",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'CSS-Framework🏢':
        bot.reply_to(message, "From, codedamm")
        bot.send_message(message.chat.id, "https://youtu.be/zgXW-xwTUQo",reply_markup=menuChooseKeyboard_inline)
        bot.send_message(message.chat.id, "Choose one",reply_markup=CSSEChooseKeyboard_inline)
    elif message.text == 'JS-Framework⚒':
        bot.reply_to(message, "From, Scrimba")
        bot.send_message(message.chat.id, "https://youtu.be/T2uKprwHHXU",reply_markup=menuChooseKeyboard_inline)
        bot.send_message(message.chat.id, "Choose one",reply_markup=JSEChooseKeyboard_inline)
    elif message.text == 'Server-side-rendering⬇':
        bot.reply_to(message, "Choose one")
        bot.send_message(message.chat.id, "If you choosen React, NextJS👇\nIf you choosen angular, \nangular universal 👇",reply_markup=rendingEChooseKeyboard_inline)
    elif message.text == 'Typescript📜':
        bot.reply_to(message,"From, freeCodeCamp")
        bot.send_message(message.chat.id,"https://youtu.be/30LWjhZzg50")
        bot.send_message(message.chat.id,"From, programming with mosh")
        bot.send_message(message.chat.id,"https://youtu.be/d56mG7DezGs")
        bot.send_message(message.chat.id,"From, The net Ninja")
        bot.send_message(message.chat.id,"https://youtu.be/2pZmKW9-I_k")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'About_authors👨‍🏫':
        bot.reply_to(message, "Some best authors from youtube")
        bot.send_message(message.chat.id,ApnaCollage)
        bot.send_message(message.chat.id,CodeWithHarry)
        bot.send_message(message.chat.id,"And so on",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Internet🔌':
        bot.reply_to(message, "From, Apna college")
        bot.send_message(message.chat.id,"https://youtu.be/YtxLexm-9pI")
        bot.send_message(message.chat.id,"From, Tanay Pratap")
        bot.send_message(message.chat.id,"https://youtu.be/YE-dA5ZXCs0",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'HTML✍':
        bot.reply_to(message, "From, Apna college")
        bot.send_message(message.chat.id,"https://youtu.be/HcOc7P5BMi4")
        bot.send_message(message.chat.id,"From, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/BsDoLVMnmZs",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'CSS🍡':
        bot.reply_to(message, "From, Apna college")
        bot.send_message(message.chat.id,"https://youtu.be/ESnrn1kAD4E")
        bot.send_message(message.chat.id,"From, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/Edsxf_NBFrw",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Javascript📜':
        bot.reply_to(message,"From, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/ER9SspLe4Hg")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Version-control🔼':
        bot.reply_to(message,"From, Apna college")
        bot.send_message(message.chat.id,"https://youtube.com/watch?v=Ez8F0nW6S-w&si=VsozleEXIx-pixyW",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'CSS-Framework⚒':
        bot.reply_to(message,"From, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/TAP5B_XlVa0")
        bot.send_message(message.chat.id,"Choose one",reply_markup=CSShChoosekeyboard_inline)
    elif message.text == 'JS-Framework🏢':
        bot.reply_to(message,"From, Tanay Pratap")
        bot.send_message(message.chat.id,"https://youtu.be/JcTf22FOfJI")
        bot.send_message(message.chat.id,"Choose one",reply_markup=JSHChoosekeyboard_inline)
    elif message.text == 'Server-side-rendering🔽':
        bot.reply_to(message,"If you choosen React, NextJS👇\nIf you choosen angular, \nangular universal 👇",reply_markup=rendingHChoosekeyboard_inline)
    elif message.text == 'Typescript📄':
        bot.reply_to(message,"From, hitesh choudhary")
        bot.send_message(message.chat.id,"https://youtu.be/j89BvWz8Eag")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLRAV69dS1uWRPSfKzwZsIm-Axxq-LxqhW",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Android':
        bot.reply_to(message,"Mobile application development is the process of creating software applications that run on a mobile device, and a typical mobile application utilizes a network connection to work with remote computing resources. Hence, the mobile development process involves creating installable software bundles (code, binaries, assets, etc.) , implementing backend services such as data access with an API, and testing the application on target devices.\nChoose Which Language you familiar with",reply_markup=mobileKeyboard_reply)
    elif message.text == 'English📱':
        bot.reply_to(message,"From, fireship")
        bot.send_message(message.chat.id,"https://youtu.be/X8ipUgXH6jw",reply_markup=menuChooseKeyboard_inline)
        bot.send_message(message.chat.id,"Choose one",reply_markup=mobileEChoosekeyboard_inline)
    elif message.text == 'Hindi📲':
        bot.reply_to(message,"From, Apna college")
        bot.send_message(message.chat.id,"https://youtu.be/5-V0-y1iP3Q")
        bot.send_message(message.chat.id,"Choose one",reply_markup=mobileHChoosekeyboard_inline)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'menu':
        bot.answer_callback_query(call.id, "Service Center",show_alert=False)
        bot.send_message(call.message.chat.id, "Hi!\nI'm CAREER CRAFTER Bot!\nWelcome again,Are you lost? or give your feedback here /help, Thank you\n Choose your Domain below",reply_markup=reply_keyboard)  
    elif call.data == 'Python':
        bot.answer_callback_query(call.id, "RoadMap for Python",show_alert=False)
        bot.send_message(call.message.chat.id, "RoadMap for Python",)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/k2YMZ1t/Python-Roadmap.jpg")
        bot.send_message(call.message.chat.id, "Choose the Language your familiar with",reply_markup=pyChooseKeyboard_inline)
    elif call.data == 'PythonHindi':
        bot.answer_callback_query(call.id, "Python",show_alert=False)
        bot.send_message(call.message.chat.id, "Apna college \nApna College is a dynamic YouTube channel dedicated to delivering insightful educational content.")
        bot.send_message(call.message.chat.id, "https://youtu.be/vLqTf2b6GZw",reply_markup=menuChooseKeyboard_inline)
    elif call.data == 'PythonEnglish':
        bot.answer_callback_query(call.id, "Python",show_alert=False)
        bot.send_message(call.message.chat.id, "Corey Schafer \nCorey Schafer is a well-known educator in the programming and web development community.Corey has become a go-to resource for beginners and experienced developers")
        bot.send_message(call.message.chat.id, "https://youtu.be/YYXdXT2l-Gg")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PL4cUxeGkcC9joIM91nLzd_qaH_AimmdAR",reply_markup=menuChooseKeyboard_inline)
    elif call.data == 'Java':
        bot.answer_callback_query(call.id, "Java is Selected",show_alert=False)
        bot.send_message(call.message.chat.id, "RoadMap for Java")
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/Ln9scTh/Whats-App-Image-2023-08-20-at-12-49-14-AM.jpg")
        bot.send_message(call.message.chat.id,"Choose Which Language you familiar with",reply_markup=javaChooseKeyboard_inline)
    elif call.data == 'javaEnglish':
        bot.answer_callback_query(call.id, "Java in English is Selected",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Programming with Mosh")
        bot.send_message(call.message.chat.id, MoshHamedani)
        bot.send_message(call.message.chat.id, "https://youtu.be/eIrMbAQSU34?si=InP7GxbGnshkRa3O",reply_markup=menuChooseKeyboard_inline)
    elif call.data == 'javaHindi':
        bot.answer_callback_query(call.id, "Java in English is Selected",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Apna college")
        bot.send_message(call.message.chat.id, ApnaCollage)
        bot.send_message(call.message.chat.id, "https://youtu.be/yRpLlJmRo2w")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop",reply_markup=menuChooseKeyboard_inline)
    elif call.data == 'CLanguage':
        bot.answer_callback_query(call.id, "Roadmap for C Language",show_alert=False)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/HYhZtVm/Whats-App-Image-2023-08-20-at-12-49-13-AM.jpg")
        bot.send_message(call.message.chat.id, "Choose Which Language you familiar with",reply_markup=ClangChooseKeyboard_inline)
    elif call.data == "CLEnglish": #for C language in english
        bot.answer_callback_query(call.id, "C Language is selected",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Caleb Curry")
        bot.send_message(call.message.chat.id, CalebCurry)
        bot.send_message(call.message.chat.id, "https://youtu.be/Bz4MxDeEM6k",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "CLHindi": #for C language in hindi
        bot.answer_callback_query(call.id, "C Language is selected",show_alert=False)
        bot.send_message(call.message.chat.id, "from, CodeWithHarry")
        bot.send_message(call.message.chat.id, CodeWithHarry)
        bot.send_message(call.message.chat.id, "https://youtu.be/7Dh73z3icd8")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "DPython": #for DSA in python
        bot.answer_callback_query(call.id, "DSA in Python",show_alert=False)
        bot.send_message(call.message.chat.id,"Choose Which Language you familiar with",reply_markup=pythonChooseKeyboard_inline)
    elif call.data == "DJava": #for DSA in java
        bot.answer_callback_query(call.id, "DSA in Java",show_alert=False)
        bot.send_message(call.message.chat.id,"Choose Which Language you familiar with",reply_markup=javaDSAChooseKeyboard_inline)
    elif call.data == "DCLanguage": #for DSA in C language
        bot.answer_callback_query(call.id, "DSA in C",show_alert=False)
        bot.send_message(call.message.chat.id,"Choose Which Language you familiar with",reply_markup=CChooseKeyboard_inline)
    elif call.data == "pythonHindi": #for DSA in python language in hindi
        bot.answer_callback_query(call.id, "DSA on Python in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Campus X")
        bot.send_message(call.message.chat.id, Campus_x)
        bot.send_message(call.message.chat.id, "https://youtu.be/f9Aje_cN_CY",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "pythonEnglish": #for DSA in python language in english
        bot.answer_callback_query(call.id, "DSA on python in English",show_alert=False)
        bot.send_message(call.message.chat.id, "from, The Coding Ninjas")
        bot.send_message(call.message.chat.id, TheCodingNinjas)
        bot.send_message(call.message.chat.id, "https://youtu.be/UljGkm2ikdY")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PLrk5tgtnMN6TYBW0-U4YhIRyYEVpqVEnJ",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "javaDHindi": #for DSA in java language in hindi
        bot.answer_callback_query(call.id, "DSA on Java in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id, "from, kunal kushwaha")
        bot.send_message(call.message.chat.id, Kunal_Kushawaha)
        bot.send_message(call.message.chat.id, "https://youtu.be/rZ41y93P2Qo?si=4rSWDoDrXZKd9k8j")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&si=ByrjoSlkQSZUq_en",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "javaDEnglish": #for DSA in java language in english
        bot.answer_callback_query(call.id, "DSA on Java in English",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Telusko")
        bot.send_message(call.message.chat.id, Telusko)
        bot.send_message(call.message.chat.id, "https://youtu.be/xWLxhF3b5P8?si=CoucqQWGTKTjl6L3",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "CEnglish": #for DSA in C language in english
        bot.answer_callback_query(call.id, "DSA on C in English",show_alert=False)
        bot.send_message(call.message.chat.id, "from, Neso Academy")
        bot.send_message(call.message.chat.id, NesoAcademy)
        bot.send_message(call.message.chat.id, "https://youtu.be/4OGMB4Fhh50")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PLBlnK6fEyqRhX6r2uhhlubuF5QextdCSM",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "CHindi": #for DSA in C language in hindi
        bot.answer_callback_query(call.id, "DSA on C in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id, "from, CodeWithHarry")
        bot.send_message(call.message.chat.id, CodeWithHarry)
        bot.send_message(call.message.chat.id, "https://youtu.be/5_5oE5lgrhw")
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, "https://youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "frontEnglish":
        bot.answer_callback_query(call.id, "RoadMap for Frontend",show_alert=False)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/51tF1FY/Whats-App-Image-2023-08-19-at-8-22-38-PM-1.jpg")
        bot.send_message(call.message.chat.id, "Select the courses according to given roadmap",reply_markup=frontendKeyboard_reply)
    elif call.data == "frontHindi":
        bot.answer_callback_query(call.id, "RoadMap for Frontend",show_alert=False)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/51tF1FY/Whats-App-Image-2023-08-19-at-8-22-38-PM-1.jpg")
        bot.send_message(call.message.chat.id, "Select the courses according to given roadmap",reply_markup=frontendHKeyboard_reply)
    elif call.data == "bootstrap":
        bot.answer_callback_query(call.id, "You Selected Bootstrap",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/-qfEOE4vtxE')
        bot.send_message(call.message.chat.id,'from, The net Ninja')
        bot.send_message(call.message.chat.id,'https://youtu.be/bxmDnn7lrnk')
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL4cUxeGkcC9joIM91nLzd_qaH_AimmdAR',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "tailwind":
        bot.answer_callback_query(call.id, "You Selected Tailwind",show_alert=False)
        bot.send_message(call.message.chat.id, 'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id, 'https://youtu.be/ft30zcMlFao')
        bot.send_message(call.message.chat.id, 'from, The net Ninja')
        bot.send_message(call.message.chat.id, 'https://youtu.be/O_9u1P5YjVc')
        bot.send_message(call.message.chat.id, 'from, hitesh choudhary')
        bot.send_message(call.message.chat.id, 'https://youtu.be/_9mTJ84uL1Q')
        bot.send_message(call.message.chat.id, "Check below for playlist 👇")
        bot.send_message(call.message.chat.id, 'https://youtube.com/playlist?list=PL4cUxeGkcC9gpXORlEHjc5bgnIi5HEGhw',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "react":
        bot.answer_callback_query(call.id, "You Selected React",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/u6gSSpfsoOQ')
        bot.send_message(call.message.chat.id,'from, programming with mosh')
        bot.send_message(call.message.chat.id,'https://youtu.be/SqcY0GlETPk',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "angular":
        bot.answer_callback_query(call.id, "You Selected Angular",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/3qBXWUpoPHo')
        bot.send_message(call.message.chat.id,'from, programming with mosh')
        bot.send_message(call.message.chat.id,'https://youtu.be/k5E2AVpwsko',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "vue":
        bot.answer_callback_query(call.id, "You Selected Vue",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/FXpIoQ_rT_c')
        bot.send_message(call.message.chat.id,'from, The net Ninja')
        bot.send_message(call.message.chat.id,'https://youtu.be/YrxBCBibVo0')
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL4cUxeGkcC9hYYGbV60Vq3IXYNfDk8At1',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "NextJS":
        bot.answer_callback_query(call.id, "You Selected NextJS",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/ETV17M4SauU')
        bot.send_message(call.message.chat.id,'from, programming with mosh')
        bot.send_message(call.message.chat.id,'https://youtu.be/TlB_eWDSMt4')
        bot.send_message(call.message.chat.id,'from, The net Ninja')
        bot.send_message(call.message.chat.id,'https://youtu.be/A63UxsQsEbU')
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL4cUxeGkcC9g9gP2onazU5-2M-AzA8eBw',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "angular_universal":
        bot.answer_callback_query(call.id, "You Selected Angular Universal",show_alert=False)
        bot.send_message(call.message.chat.id,'from, blackBox Tech')
        bot.send_message(call.message.chat.id,'https://youtu.be/5bOtSAQYo8Q')
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PLBiJ_OHa1m2ZoFXXJxOnqsIFOBW-A856p',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "reactNative":
        bot.answer_callback_query(call.id, "You Selected React Native",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/obH0Po_RdWk')
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/0-S5a0eXPoc')
        bot.send_message(call.message.chat.id,'from, The net Ninja')
        bot.send_message(call.message.chat.id,'https://youtu.be/ur6I5m2nTvk')
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL4cUxeGkcC9ixPU-QkScoRBVxtPPzVjrQ',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "flutter":
        bot.answer_callback_query(call.id, "You Selected Flutter",show_alert=False)
        bot.send_message(call.message.chat.id,'from, freeCodeCamp.org')
        bot.send_message(call.message.chat.id,'https://youtu.be/VPvVD8t02U8')
        bot.send_message(call.message.chat.id,'from, The net Ninja')
        bot.send_message(call.message.chat.id,"https://youtu.be/1ukSR1GRtMU")
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Hbootstrap":
        bot.answer_callback_query(call.id,'from, Apna college')
        bot.send_message(call.message.chat.id,'https://youtu.be/wjskiR81EjY')
        bot.send_message(call.message.chat.id,'from, CodeWithHarry')
        bot.send_message(call.message.chat.id,'https://youtu.be/vpAJ0s5S2t0',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Htailwind":
        bot.answer_callback_query(call.id,'from, CodeWithHarry')
        bot.send_message(call.message.chat.id,'https://youtu.be/L4_jarMnB0c')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PLu0W_9lII9ahwFDuExCpPFHAK829Wto2O',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Hangular":
        bot.answer_callback_query(call.id,'from, CodeWithHarry')
        bot.send_message(call.message.chat.id,'https://youtu.be/0LhBvp8qpro',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Hreact":
        bot.answer_callback_query(call.id,'from, CodeWithHarry')
        bot.send_message(call.message.chat.id,'https://youtu.be/-mJFZp84TIY')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Hvue":
        bot.answer_callback_query(call.id,'from, Code step by step')
        bot.send_message(call.message.chat.id,'https://youtu.be/h18hbBNxXac')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL8p2I9GklV45e7L_qC_mntM7FhSIV8pqa',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "HNextJS":
        bot.answer_callback_query(call.id,'from, CodeWithHarry')
        bot.send_message(call.message.chat.id,'https://youtu.be/DZKOunP-WLQ')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PLu0W_9lII9agtWvR_TZdb_r0dNI8-lDwG',reply_markup=menuChooseKeyboard_inline)
    
    elif call.data == "about":
        bot.answer_callback_query(call.id, "About",show_alert=False)
        bot.send_message("○ Team: @Babith_dev, @Pallavigowdaaa, @priyanka142004\n○ Language: Python3.11\n○ Library: Telebot 4.12.0\n○ Institution: East Point College of Engineering",reply_markup=menuChooseKeyboard_inline)
# Start the bot
bot.polling()
