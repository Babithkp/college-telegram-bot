import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('TOKEN')

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


MongoDB = 'MongoDB is a non-relational document database that provides support for JSON-like storage. The MongoDB database has a flexible data model that enables you to store unstructured data, and it provides full indexing support, and replication with rich and intuitive APIs.'


authentications = 'What is the difference between JWT and OAuth2?\n\nJWT is suitable for stateless applications, as it allows the application to authenticate users and authorize access to resources without maintaining a session state on the server. OAuth, on the other hand, maintains a session state on the server and uses a unique token to grant access to the user"s resources.'

redis = 'Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine. Redis provides data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes, and streams. Redis has built-in replication, Lua scripting, LRU eviction, transactions, and different levels of on-disk persistence, and provides high availability via Redis Sentinel and automatic partitioning with Redis Cluster.'

Campus_x = 'Campus X \nis a budding YouTube channel that offers  a detailed knowledge onprogramming and technology-related tutorials with good explaination. The channel focuses on a diverse range of programming languages, web development, app development, and other coding-related topics'

TheCodingNinjas = 'The Coding Ninjas \nYouTube channel is a popular destination for programming enthusiasts and aspiring software developers. Known for its comprehensive coding tutorials and tech-related content.the Coding Ninjas channel has gained a substantial following, making it a valuable resource for those looking to sharpen their coding abilities and stay updated with the latest developments in the tech world. '

DineshVaryani = 'Dinesh Varyani \nmake free programming tutorials from beginner to advanced level. That includes Java for beginners, who is known for his excellent teachings. who is also a full stack developer and has 10 year of experience '

NesoAcademy = "Neso Academy \nis a renowned YouTube channel recognized for its high-quality educational content.  Neso Academy provides comprehensive video lectures, tutorials, and explanations to help students grasp complex concepts with ease. The channel's founder and instructor, Vineet Khatri, has garnered praise for his clear teaching style and ability to break down intricate topics into understandable segments."

CalebCurry = "Caleb Curry \nis a popular programming educator on YouTube. His tutorials are well-structured and beginner-friendly, making them a great resource for learning C." 

INTELLIPAT = 'Intellipaat is an online education platform that offers a wide range of courses and training programs in various fields, with a primary focus on technology, data science, artificial intelligence, and programming. It provides learners with the opportunity to enhance their skills and knowledge through comprehensive, self-paced, and instructor-led courses. '

GRAPHICSGURUJI = 'Graphics Guruji courses are designed to cater to both beginners and experienced professionals, aiming to bridge the gap between theoretical concepts and practical application. The platform often includes hands-on projects, real-world examples, and interactive exercises to ensure a holistic learning experience. '

EduRekha = "EduRekha is an online learning platform that offers a diverse range of courses and training programs across various domains, with a primary focus on technology, programming, data science, and business skills. It aims to provide learners with the opportunity to acquire new skills, advance their careers, and stay competitive in today's fast-paced digital world."


    # Create a reply keyboard
reply_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
button_program = KeyboardButton('Programming--Languages')
button_dev = KeyboardButton('Development')
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
backendHKeyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True).add("About_authors👨‍🏫","Internet🔌","Choose a language🔡","Version-control🔼","Relational-Database📥","NoSQl-Database🥡","APIs🕊","Caching🗑","Testing🔍","Containerization📦","GraphQL🍱")

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
mobileEChooseKeyboard_inline = InlineKeyboardMarkup().add(reactNative,flutter)

# Inline keyboard for choosing CSS framework English
Bootstrap = InlineKeyboardButton(text="Bootstrap", callback_data="Hbootstrap")
Tailwind = InlineKeyboardButton(text="Tailwind", callback_data="Htailwind")
CSShChooseKeyboard_inline = InlineKeyboardMarkup().add(Tailwind, Bootstrap)


# Inline keyboard for choosing JS framework English
react = InlineKeyboardButton(text="React", callback_data="Hreact")
angular = InlineKeyboardButton(text="Angular", callback_data="Hangular")
vue = InlineKeyboardButton(text="Vue", callback_data="Hvue")
JSHChooseKeyboard_inline = InlineKeyboardMarkup().add(react,angular,vue)


# Inline keyboard for choosing rending Hindi
NextJS = InlineKeyboardButton(text="NextJS", callback_data="HNextJS")
angular_universal = InlineKeyboardButton(text="angular universal", callback_data="angular_universal")
rendingHChooseKeyboard_inline = InlineKeyboardMarkup().add(NextJS,angular_universal)

# Inline keyboard for choosing mobile Hindi
reactNative = InlineKeyboardButton(text="React Native", callback_data="HreactNative")
flutter = InlineKeyboardButton(text="Flutter", callback_data="Hflutter")
mobileHChooseKeyboard_inline = InlineKeyboardMarkup().add(reactNative,flutter)


# Inline keyboard for choosing languages for backend lang
python = InlineKeyboardButton(text="Python", callback_data="PyhtonEnglish")
java = InlineKeyboardButton(text="Java", callback_data="javaEnglish")
javaScript = InlineKeyboardButton(text="JavaScript", callback_data="javaSEnglish")
backendEChooseKeyboard_inline = InlineKeyboardMarkup().add(python,java,javaScript)

# Inline keyboard for choosing languages for backend lang
python = InlineKeyboardButton(text="Python", callback_data="PyhtonHindi")
java = InlineKeyboardButton(text="Java", callback_data="javaHindi")
javaScript = InlineKeyboardButton(text="JavaScript", callback_data="javaSHindi")
backendHChooseKeyboard_inline = InlineKeyboardMarkup().add(python,java,javaScript)

# Inline keyboard for selecting backend APIs English
authentication = InlineKeyboardButton(text="authentication", callback_data="authentication")
Rest_API = InlineKeyboardButton(text="Rest-API", callback_data="Rest-API")
backAPIeKeyboard_inline = InlineKeyboardMarkup().add(authentication,Rest_API)

# Inline keyboard for selecting backend APIs English
authentication = InlineKeyboardButton(text="authentication", callback_data="authentication")
Rest_API = InlineKeyboardButton(text="Rest-API", callback_data="HRest-API")
backAPIhKeyboard_inline = InlineKeyboardMarkup().add(authentication,Rest_API)


# Inline keyboard for selecting backend container English
kubernetes = InlineKeyboardButton(text="Kubernetes", callback_data="kubernetes")
docker = InlineKeyboardButton(text="Docker", callback_data="docker")
backConKeyboard_inline = InlineKeyboardMarkup().add(kubernetes,docker)


# Inline keyboard for choosing Backend languages
Hindi = InlineKeyboardButton(text="Hindi", callback_data="backendHindi")
English = InlineKeyboardButton(text="English", callback_data="backendEnglish")
backendChooseKeyboard_inline = InlineKeyboardMarkup().add(English, Hindi)

# Inline keyboard for choosing full full stack 
Hindi = InlineKeyboardButton(text="Hindi", callback_data="fullHindi")
English = InlineKeyboardButton(text="English", callback_data="fullEnglish")
fullChooseKeyboard_inline = InlineKeyboardMarkup().add(English, Hindi)


# Inline keyboard for choosing ui/ux-design
Hindi = InlineKeyboardButton(text="Hindi", callback_data="ULHindi")
English = InlineKeyboardButton(text="English", callback_data="ULEnglish")
ULChooseKeyboard_inline = InlineKeyboardMarkup().add(English, Hindi)


# Inline keyboard for choosing ui/ux-design
Hindi = InlineKeyboardButton(text="Hindi", callback_data="DeHindi")
English = InlineKeyboardButton(text="English", callback_data="DeEnglish")
DevChooseKeyboard_inline = InlineKeyboardMarkup().add(English, Hindi)

# back button
menu = InlineKeyboardButton("Menu🔙", callback_data="menu")
menuChooseKeyboard_inline = InlineKeyboardMarkup().add(menu)

# back button
menu = InlineKeyboardButton("Menu🔙", callback_data="menu")
about = InlineKeyboardButton("About us👨‍💻", callback_data="about")
menu2ChooseKeyboard_inline = InlineKeyboardMarkup().add(menu,about)


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"https://i.ibb.co/FWGbKqf/Whats-App-Image-2023-09-04-at-7-12-22-AM.jpg")
    bot.reply_to(message,"Hi!\n/start gives you three options-> Programming Languages,Development-Domains and DSA\n\n1.Programming Languages --> \nJava / Python / C --> English / Hindi \n--> Video links\n\n2.dev-Domains --> \nFrontendBackend / Full-stack / Android / UI/UX-Design / DevOps \n--> English / Hindi --> Video links\n\n3.DSA --> \nJava / Python / C --> English / Hindi \n--> Video links",reply_markup=menu2ChooseKeyboard_inline)
    
    
    
    
    
# This is for ReplyKeyboardMarkup
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    remove_keyboard = ReplyKeyboardRemove()
    if message.text == 'Backend':
        bot.reply_to(message,"Back-end development means working on server-side software, which focuses on everything you can't see on a website. Back-end developers ensure the website performs correctly, focusing on databases, back-end logic, application programming interface (APIs), architecture, and servers.\nChoose Which Language you familiar with",reply_markup=backendChooseKeyboard_inline)
    elif message.text == 'Full-stack':
        bot.reply_to(message," Full stack development is the end-to-end development of applications. It includes both the front end and back end of an application. The front end is usually accessed by a client, and the back end forms the core of the application where all the business logic is applied.\nChoose Which Language you familiar with",reply_markup=fullChooseKeyboard_inline)
    elif message.text == 'Programming--Languages':
        bot.reply_to(message, "A programming language is a way for programmers (developers) to communicate with computers.\n Choose which you want to start with",reply_markup=language_markup)
    elif message.text == 'DSA':
        bot.reply_to(message,"Road map for DSA")
        bot.send_message(message.chat.id,"https://i.ibb.co/ZdLrF3S/Whats-App-Image-2023-08-19-at-11-24-19-PM.jpg")
        bot.send_message(message.chat.id,"Data structure and Algorithm (DSA) is applied in all disciplines of software development.\n DSA is the building block of the software development process.\nChoose which you want to start with", reply_markup=LangDSAkeyboard_inline)
    elif message.text == 'Development':
        bot.reply_to(message,"A domain just for developers. From tools to platforms, languages to blogs.\nChoose which you want to start with", reply_markup=domainKeyboard_reply)
    elif message.text == 'Frontend':
        bot.reply_to(message,"A Front-End Developer is someone who creates websites and web applications.\nFront-end web development is the development of the graphical user interface of a website.\nChoose Which Language you familiar with", reply_markup=frontChooseKeyboard_inline)
    elif message.text == 'UI/UX-Design':
        bot.reply_to(message,"UI UX designers create the user interface for an app, website, or other interactive media. Their work includes collaborating with product managers and engineers to gather requirements from users before designing ideas that can be communicated using storyboards. They also process flows or sitemaps.\nChoose Which Language you familiar with",reply_markup=ULChooseKeyboard_inline)
    elif message.text == 'DevOps':
        bot.reply_to(message,"DevOps is a set of practices, tools, and a cultural philosophy that automate and integrate the processes between software development and IT teams. It emphasizes team empowerment, cross-team communication and collaboration, and technology automation.",reply_markup=DevChooseKeyboard_inline)
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
        bot.send_message(message.chat.id,"Choose one",reply_markup=CSShChooseKeyboard_inline)
    elif message.text == 'JS-Framework🏢':
        bot.reply_to(message,"From, Tanay Pratap")
        bot.send_message(message.chat.id,"https://youtu.be/JcTf22FOfJI")
        bot.send_message(message.chat.id,"Choose one",reply_markup=JSHChooseKeyboard_inline)
    elif message.text == 'Server-side-rendering🔽':
        bot.reply_to(message,"If you choosen React, NextJS👇\nIf you choosen angular, \nangular universal 👇",reply_markup=rendingHChooseKeyboard_inline)
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
        bot.send_message(message.chat.id,"Choose one",reply_markup=mobileEChooseKeyboard_inline)
    elif message.text == 'Hindi📲':
        bot.reply_to(message,"From, Apna college")
        bot.send_message(message.chat.id,"https://youtu.be/5-V0-y1iP3Q")
        bot.send_message(message.chat.id,"Choose one",reply_markup=mobileHChooseKeyboard_inline)
    elif message.text == 'Typescript📄':
        bot.reply_to(message,"From, hitesh choudhary")
        bot.send_message(message.chat.id,"https://youtu.be/j89BvWz8Eag")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLRAV69dS1uWRPSfKzwZsIm-Axxq-LxqhW",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Choose a language🔠':
        bot.reply_to(message,"Choose Which Language you familiar with and learn advance",reply_markup=backendEChooseKeyboard_inline)
    elif message.text == 'Choose a language🔡':
        bot.reply_to(message,"Choose Which Language you familiar with and learn advance",reply_markup=backendHChooseKeyboard_inline)
    elif message.text == 'Relational-Database📤':
        bot.reply_to(message,"Choose has ur language🔡equirements")
        bot.send_message(message.chat.id,"from, Airbyte")
        bot.send_message(message.chat.id,"https://youtu.be/vAv5lks4gzA")
        bot.send_message(message.chat.id,"For PostgreSQL")
        bot.send_message(message.chat.id,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/qw--VYLpxG4")
        bot.send_message(message.chat.id,"For Mysql")
        bot.send_message(message.chat.id,"from, Bro code")
        bot.send_message(message.chat.id,"https://youtu.be/5OdVJbNCSso",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Relational-Database📥':
        bot.reply_to(message,"Choose has ur requirements")
        bot.send_message(message.chat.id,"from, Great learning")
        bot.send_message(message.chat.id,"https://youtu.be/FasR2rdQRd8")
        bot.send_message(message.chat.id,"For PostgreSQL")
        bot.send_message(message.chat.id,"from, Online Study CS")
        bot.send_message(message.chat.id,"https://youtu.be/4G7JkF_e5LM")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLzAy3QBHoWZdxPXkD7UVymWm_Do3IdzwQ")
        bot.send_message(message.chat.id,"For Mysql")
        bot.send_message(message.chat.id,"from, yahoo Baba")
        bot.send_message(message.chat.id,"https://youtu.be/KlWOr2RwqM4")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL0b6OzIxLPbzf12lu5etX_vjN-eUxgxnr",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'NoSQl-Database🗳':
        bot.reply_to(message,MongoDB)
        bot.send_message(message.chat.id,"from, The net Ninja")
        bot.send_message(message.chat.id,"https://youtu.be/ExcRbA7fy_A")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL4cUxeGkcC9h77dJ-QJlwGlZlTd4ecZOA",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'NoSQl-Database🥡':
        bot.reply_to(message,MongoDB)
        bot.send_message(message.chat.id,"from, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/J6mDkcqU_ZE",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'APIs🦅':
        bot.reply_to(message,"In APIs you should learn about\n1.authentication\n2.Rest API\nLearn one-by-one",reply_markup=backAPIeKeyboard_inline)
    elif message.text == 'APIs🕊':
        bot.reply_to(message,"In APIs you should learn about\n1.authentication\n2.Rest API\nLearn one-by-one",reply_markup=backAPIhKeyboard_inline)
    elif message.text == 'Caching🗑':
        bot.reply_to(message,redis)
        bot.send_message(message.chat.id,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/XCsS_NVAa1g",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Testing🔍':
        bot.reply_to(message,"step 1: manual testing")
        bot.send_message(message.chat.id,"from, SDET- QA Automation Techie")
        bot.send_message(message.chat.id,"https://youtu.be/oOvURgHcd4w")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLUDwpEzHYYLseflPNg0bUKfLmAbO2JnE9")
        bot.send_message(message.chat.id,"step 2: software testing")
        bot.send_message(message.chat.id,"from, edureda!")
        bot.send_message(message.chat.id,"https://www.youtube.com/live/sO8eGL6SFsA?feature=share",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Containerization📦':
        bot.reply_to(message,"Choose one docker or kubernetes")
        bot.send_message(message.chat.id,"https://youtu.be/tuyq3H4EXL0",reply_markup=backConKeyboard_inline)
    elif message.text == 'GraphQL🗃':
        bot.reply_to(message,"from, The net Ninja")
        bot.send_message(message.chat.id,"https://youtu.be/xMCnDesBggM",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'GraphQL🍱':
        bot.reply_to(message,"from, coders never quit")
        bot.send_message(message.chat.id,"https://youtu.be/NNNcoWZ6Ih0")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLB97yPrFwo5i9zDrWfvkohPec3Q6EEC9J",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Tailwind🏳‍🌈':
        bot.reply_to(message,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/ft30zcMlFao")
        bot.send_message(message.chat.id,"from, The net Ninja")
        bot.send_message(message.chat.id,"https://youtu.be/O_9u1P5YjVc",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Tailwind🏁':
        bot.reply_to(message,"from, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/L4_jarMnB0c")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLu0W_9lII9ahwFDuExCpPFHAK829Wto2O",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'React⚛':
        bot.reply_to(message,"from, freeCodeCamp.orgv")
        bot.send_message(message.chat.id,"https://youtu.be/u6gSSpfsoOQ")
        bot.send_message(message.chat.id,"from, programming with mosh")
        bot.send_message(message.chat.id,"https://youtu.be/SqcY0GlETPk",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'React🕸':
        bot.reply_to(message,'from, Code step by step')
        bot.send_message(message.chat.id,'https://youtu.be/h18hbBNxXac')
        bot.send_message(message.chat.id,'Check below for playlist 👇')
        bot.send_message(message.chat.id,'https://youtube.com/playlist?list=PL8p2I9GklV45e7L_qC_mntM7FhSIV8pqa',reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Nodejs🔰':
        bot.reply_to(message,'from, Programming with Mosh')
        bot.send_message(message.chat.id,'https://youtu.be/TlB_eWDSMt4',reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Nodejs✅':
        bot.reply_to(message,'from, CodeWithHarry')
        bot.send_message(message.chat.id,'https://youtu.be/BLl32FvcdVM',reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'PostgreSQL🥡':
        bot.reply_to(message,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/qw--VYLpxG4",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'PostgreSQL📦':
        bot.reply_to(message,"https://youtu.be/4G7JkF_e5LM")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLzAy3QBHoWZdxPXkD7UVymWm_Do3IdzwQ",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Restful-APIs🦅':
        bot.reply_to(message,"from, Tutorialspoint")
        bot.send_message(message.chat.id,"https://youtu.be/HeXQ98sogs8")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLWPirh4EWFpGRdVZcQCzeTXFBNSTDAdQX",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Restful-APIs🕊':
        bot.reply_to(message,"from, Thapa Technical")
        bot.send_message(message.chat.id,"https://youtu.be/ALrOcDPimWE",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'JWT-auth🔐':
        bot.reply_to(message,"from, Web Dev Simplified")
        bot.send_message(message.chat.id,"https://youtu.be/mbsmsi7l3r4",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Redis🧧':
        bot.reply_to(message,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/XCsS_NVAa1g",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Linux-basics🐧':
        bot.reply_to(message,"from, CodeWithHarry")
        bot.send_message(message.chat.id,"https://youtu.be/_tCY-c-sPZc",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Linux-basics🐥':
        bot.reply_to(message,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/sWbUDq4S6Y8",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'AWS-Services🧰':
        bot.reply_to(message,"from, Simplilearn")
        bot.send_message(message.chat.id,"https://youtu.be/3XFODda6YXo")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLEiEAq2VkUULlNtIFhEQHo8gacvme35rz",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'AWS-Services🗳':
        bot.reply_to(message,"from, Gaurav Sharma")
        bot.send_message(message.chat.id,"https://youtu.be/rKNSc8RrwxA")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL6XT0grm_TfgtwtwUit305qS-HhDvb4du",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Github-actions😸':
        bot.reply_to(message,"from, Glich.Stream")
        bot.send_message(message.chat.id,"https://youtu.be/-hVG9z0fCacv")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Ansible⚓':
        bot.reply_to(message,"from, edureda")
        bot.send_message(message.chat.id,"https://www.youtube.com/live/9Ua2b06oAr4?feature=share",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Ansible🔱':
        bot.reply_to(message,"from, Gaurav Sharma")
        bot.send_message(message.chat.id,"https://youtu.be/GN6eMwsNkds")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL6XT0grm_TfgP3OlZzmGh4Cq_rHtX8z7e",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Terraform🔹':
        bot.reply_to(message,"from, freeCodeCamp.org")
        bot.send_message(message.chat.id,"https://youtu.be/SLB_c_ayRMo",reply_markup=menuChooseKeyboard_inline)
    elif message.text == 'Terraform🔷':
        bot.reply_to(message,"from, Gaurav Sharma")
        bot.send_message(message.chat.id,"https://youtu.be/5FJE9HPS85c")
        bot.send_message(message.chat.id,"Check below for playlist 👇")
        bot.send_message(message.chat.id,"https://youtube.com/playlist?list=PL6XT0grm_TfgdaAjTmLb4QedMCCMQHISm",reply_markup=menuChooseKeyboard_inline)
    else:
        bot.reply_to(message,message.text)





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
    elif call.data == "HreactNative":
        bot.answer_callback_query(call.id, "You Selected React Native",show_alert=False)
        bot.send_message(call.message.chat.id,'from, code step by step')
        bot.send_message(call.message.chat.id,'https://youtu.be/z1qG80Jkzi8')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PL8p2I9GklV468O2wk-n8Q1KmtMhnHHj4C',reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Hflutter":
        bot.answer_callback_query(call.id, "You Selected Flutter",show_alert=False)
        bot.send_message(call.message.chat.id,'from, codeHelp by babbar')
        bot.send_message(call.message.chat.id,'https://youtu.be/9u0Mz-YnQTE')
        bot.send_message(call.message.chat.id,'Check below for playlist 👇')
        bot.send_message(call.message.chat.id,'https://youtube.com/playlist?list=PLDzeHZWIZsTo3Cs115GXkot28i406511Y',reply_markup=menuChooseKeyboard_inline)
    elif call.data == 'PyhtonEnglish': #choosing english in python
        bot.answer_callback_query(call.id, "You Selected Python in English",show_alert=False)
        bot.send_message(call.message.chat.id,"Corey Schafer \nCorey Schafer is a well-known educator in the programming and web development community.Corey has become a go-to resource for beginners and experienced developers ")
        bot.send_message(call.message.chat.id,"https://youtu.be/YYXdXT2l-Gg")
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,"https://youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",reply_markup=menuChooseKeyboard_inline)    
    elif call.data == 'PyhtonHindi': #choosing hindi in python
        bot.answer_callback_query(call.id, "You Selected Python in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id,"Apna college \nApna College is a dynamic YouTube channel dedicated to delivering insightful educational content.")
        bot.send_message(call.message.chat.id,"https://youtu.be/vLqTf2b6GZw",reply_markup=menuChooseKeyboard_inline)        
    elif call.data == "javaHindi": #for java in hindi
        bot.answer_callback_query(call.id, "You Selected Java in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id,"from, Apna college")
        bot.send_message(call.message.chat.id,"https://youtu.be/UmnCZ7-9yDY",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "javaEnglish": #for java in english
        bot.answer_callback_query(call.id, "You Selected Java in English",show_alert=False)
        bot.send_message(call.message.chat.id,"from, programming with mosh")
        bot.send_message(call.message.chat.id,"https://youtu.be/eIrMbAQSU34",reply_markup=menuChooseKeyboard_inline)        
    elif call.data == "javaSEnglish": #for javascript in english
        bot.answer_callback_query(call.id, "You Selected JavaScript in English",show_alert=False)
        bot.send_message(call.message.chat.id,"from, supersimpledev")
        bot.send_message(call.message.chat.id,"https://youtu.be/SBmSRK3feww",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "javaSHindi": #for javascript in hindi
        bot.answer_callback_query(call.id, "You Selected JavaScript in Hindi",show_alert=False)
        bot.send_message(call.message.chat.id,"From, CodeWithHarry")
        bot.send_message(call.message.chat.id,"https://youtu.be/ER9SspLe4Hg")
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,"https://youtube.com/playlist?list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "authentication": #for backend APIs in english
        bot.answer_callback_query(call.id, "You Selected Authentication",show_alert=False)
        bot.send_message(call.message.chat.id,authentications)
        bot.send_message(call.message.chat.id,"https://youtu.be/a9R3Gq1BKxI")
        bot.send_message(call.message.chat.id,"for OAuth")
        bot.send_message(call.message.chat.id,"from, Productioncoder")
        bot.send_message(call.message.chat.id,"https://youtu.be/YqGXbrVGUaU")
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,"https://youtube.com/playlist?list=PL1Nml43UBm6dOj4UuH-7a9e3wO6eL2SCi")
        bot.send_message(call.message.chat.id,"for JWT")
        bot.send_message(call.message.chat.id,"from, Web Dev Simplified")
        bot.send_message(call.message.chat.id,"https://youtu.be/mbsmsi7l3r4",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "Rest-API": #for backend APIs in english
        bot.answer_callback_query(call.id, "You Selected REST API",show_alert=False)
        bot.send_message(call.message.chat.id,"from, Tutorialspoint")
        bot.send_message(call.message.chat.id,"https://youtu.be/HeXQ98sogs8")
        bot.send_message(call.message.chat.id,"Check below for playlist 👇")
        bot.send_message(call.message.chat.id,"https://youtube.com/playlist?list=PLWPirh4EWFpGRdVZcQCzeTXFBNSTDAdQX",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "HRest-API": #for backend APIs in hindi
        bot.answer_callback_query(call.id, "You Selected REST API",show_alert=False)
        bot.send_message(call.message.chat.id,"from, Thapa Technical")
        bot.send_message(call.message.chat.id,"https://youtu.be/ALrOcDPimWE",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "kubernetes": #for backend containers in english
        bot.answer_callback_query(call.id, "You Selected Kubernetes",show_alert=False)
        bot.send_message(call.message.chat.id,"from, TechWorld with Nana")
        bot.send_message(call.message.chat.id,"https://youtu.be/X48VuDVv0do",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "docker": #for backend containers in english
        bot.answer_callback_query(call.id, "You Selected Docker",show_alert=False)
        bot.send_message(call.message.chat.id,"from, TechWorld with Nana")
        bot.send_message(call.message.chat.id,"https://youtu.be/3c-iBn73dDE",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "backendHindi":
        bot.answer_callback_query(call.id, "Backend in Hindi",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/Fntxs9H/Whats-App-Image-2023-08-19-at-8-25-55-PM.jpg")
        bot.send_message(call.message.chat.id,"Select the courses according to given roadmap",reply_markup=backendHKeyboard_reply)
    elif call.data == "backendEnglish":
        bot.answer_callback_query(call.id, "Backend in English",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/Fntxs9H/Whats-App-Image-2023-08-19-at-8-25-55-PM.jpg")
        bot.send_message(call.message.chat.id,"Select the courses according to given roadmap",reply_markup=backendEKeyboard_reply)
    elif call.data == "ULHindi": #for UI/UX-design in Hindi
        bot.answer_callback_query(call.id, "UI/UX in Hindi",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/zGWkwYC/Whats-App-Image-2023-08-20-at-11-55-20-PM.jpg")
        bot.send_message(call.message.chat.id,"from, INTELLIPAT")
        bot.send_message(call.message.chat.id,INTELLIPAT)
        bot.send_message(call.message.chat.id,"https://www.youtube.com/watch?v=Qmhv1_Z7MIA",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "ULEnglish": #for UI/UX-design in English
        bot.answer_callback_query(call.id, "UI/UX in English",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/zGWkwYC/Whats-App-Image-2023-08-20-at-11-55-20-PM.jpg")
        bot.send_message(call.message.chat.id,"from, GRAPHICS GURUJI")
        bot.send_message(call.message.chat.id,GRAPHICSGURUJI)
        bot.send_message(call.message.chat.id,"https://youtu.be/jKntjC1hp_0",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "DeEnglish": #for DevOps in english
        bot.answer_callback_query(call.id, "DEV-OPS in English",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/S5dtPMC/Whats-App-Image-2023-08-20-at-11-55-19-PM-1.jpg")
        bot.send_message(call.message.chat.id,"from, INTELLIPAT")
        bot.send_message(call.message.chat.id,INTELLIPAT)
        bot.send_message(call.message.chat.id,"https://www.youtube.com/watch?v=-Ffuttr7znM",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "DeHindi": #for DevOps in hindi
        bot.answer_callback_query(call.id, "DEV-OPS in Hindi",show_alert=False)
        bot.send_photo(call.message.chat.id,"https://i.ibb.co/S5dtPMC/Whats-App-Image-2023-08-20-at-11-55-19-PM-1.jpg")
        bot.send_message(call.message.chat.id,"from, EduRekha")
        bot.send_message(call.message.chat.id,EduRekha)
        bot.send_message(call.message.chat.id,"https://youtu.be/7Imi2mVkpAg",reply_markup=menuChooseKeyboard_inline)
    elif call.data == "fullHindi": #for fullstack in hindi
        bot.answer_callback_query(call.id, "Full Stack in Hindi",show_alert=False)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/Bts2fYG/Whats-App-Image-2023-08-20-at-11-55-19-PM.jpg")
        bot.send_message(call.message.chat.id,"Select the courses according to given roadmap",reply_markup=fullHKeyboard_reply)
    elif call.data == "fullEnglish": #for fullstack in english
        bot.answer_callback_query(call.id, "Full Stack in English",show_alert=False)
        bot.send_photo(call.message.chat.id, "https://i.ibb.co/Bts2fYG/Whats-App-Image-2023-08-20-at-11-55-19-PM.jpg")
        bot.send_message(call.message.chat.id,"Select the courses according to given roadmap",reply_markup=fullEKeyboard_reply)
    elif call.data == "about":
        bot.answer_callback_query(call.id, "About",show_alert=False)
        bot.send_message(call.message.chat.id,"○ Team: @Babith_dev, @Pallavigowdaaa, @priyanka142004\n○ Language: Python3.11\n○ Library: Telebot 4.12.0\n○ Institution: East Point College of Engineering",reply_markup=menuChooseKeyboard_inline)
# Start the bot
bot.polling()
