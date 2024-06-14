from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

Token = "XYZ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Aaditya! Please type /help to fetch the study material \n\n\n Note: This bot is designed as per IT department course content in WCE😉")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = """
    /start -> Welcome message
    /help -> Show available commands
    /sem3 -> Semester 3 study Material
    /sem4 -> Semester 4 study Material
    /sem5 -> Semester 5 study Material
    /sem6 -> Semester 6 study Material
    """
    await update.message.reply_text(help_message)


async def sem3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sem3_message = """
    /Math -> Probability and Stats
    /DSA -> Data Structures and Algorithms
    /MP -> Microprocessors
    /DC -> Data Communication
    /CPP -> C++
    /PY -> Python Programming
    """
    await update.message.reply_text("Subjects for Semester 3:\n" + sem3_message)

async def sem4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sem4_message = """
    /TOC -> Theory of Computation
    /CA -> Computer Architecture
    /CN -> Computer Networks
    /SE -> Software Engineering
    /JV -> Java Programming
    """
    await update.message.reply_text("Subjects for Semester 4:\n" + sem4_message)

async def sem5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sem5_message = """
    /DBMS -> Database Management Systems
    /OS -> Operating System
    /WB -> Web Tech
    /GT -> Graph Theory
    /SQL -> SQL for DB lab
    """
    await update.message.reply_text("Subjects for Semester 5:\n" + sem5_message)

async def sem6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sem6_message = """
    /AI -> Artificial Intelligence
    /IPPR -> Image Processing
    /UOS -> Unix OS
    /ADB -> Adv. Database Engineering
    """
    await update.message.reply_text("Subjects for Semester 6:\n" + sem6_message)

async def math(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLU6SqdYcYsfLRq3tu-g_hvkHDcorrtcBK&si=nQD9QeBVMtLoVhwo"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Here is the link for the playlist:\nPlaylist: {playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/Sem3/tree/main/Prob%20%26%20Stats  \n\n\n /DSA -> Data Structures and Algorithms\n/MP -> Microprocessors\n/DC -> Data Communication\n/CPP -> C++\n/PY -> Python Programming \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)

async def dsa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi&si=A-eizgweizP4A7zd",
        "https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA&si=mWR5dV_r24psSn3_",
        "https://youtube.com/playlist?list=PLfqMhTWNBTe3LtFWcvwpqTkUSlB32kJop&si=9Uqb7AQlbcPSnkZW"
    ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/Sem3/tree/main/DSA \n\n\n /Math -> Probability and Stats\n/MP -> Microprocessors\n/DC -> Data Communication\n/CPP -> C++\n/PY -> Python Programming \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")

async def microp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLBlnK6fEyqRgyFCCgqdcBowmSp_BTKs4F&si=1l--QdwFHItX3Cza"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url} \n\n\n /Math -> Probability and Stats\n/DSA -> Data Structures and Algorithms\n/DC -> Data Communication\n/CPP -> C++\n/PY -> Python Programming \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)
    
async def dc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f"\n\n For study material, visit 👇👇\n https://github.com/Garrixer47/Sem3/tree/main/DC \n\n\n /Math -> Probability and Stats\n/DSA -> Data Structures and Algorithms\n/MP -> Microprocessors\n/CPP -> C++\n/PY -> Python Programming \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)
        
async def cpp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLLYz8uHU480j37APNXBdPz7YzAi4XlQUF&si=2Ss2ZgJT9zRSfEnJ",
        "https://youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL&si=7Pz7SSnkOgOCCqoZ",
        "https://youtu.be/he_5GXDz83g?si=6J1aQBildQYwzhRi"
    ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/Sem3/tree/main/Cpp \n\n\n /Math -> Probability and Stats\n/DSA -> Data Structures and Algorithms\n/MP -> Microprocessors\n/DC -> Data Communication\n/PY -> Python Programming \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLjVLYmrlmjGcQfNj_SLlLV4Ytf39f8BF7&si=Cwa6wGK_9T_EzYgf",
        "https://youtube.com/playlist?list=PL7ersPsTyYt26II5XjrZiRkxW11BaejOl&si=t1hydPkcv5mTvIeO"
        ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/Sem3/tree/main/Python \n\n\n /Math -> Probability and Stats\n/DSA -> Data Structures and Algorithms\n/MP -> Microprocessors\n/DC -> Data Communication\n/CPP -> C++ \n\n\n/sem4 -> Semester 4\n/sem5 -> Semester 5\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")


async def toc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLmXKhU9FNesSdCsn6YQqu9DmXRMsYdZ2T&si=8wCM0moY4bdXyNhT"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFourIT/tree/main/TOC \n\n\n/CA -> Computer Architecture\n/CN -> Computer Networks\n/SE -> Software Engineering\n/JV -> Java Programming \n\n\n/sem3 -> Semester 3\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)

async def ca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PL3R9-um41JsxDsAsdRtw7XN7MJJ27Icsv&si=t1tB0EC0psTqwmXj"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url}\n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFourIT/tree/main/TOC \n\n\n /TOC -> Theory of Computation\n/CN -> Computer Networks\n/SE -> Software Engineering\n/JV -> Java Programming \n\n\n/sem3 -> Semester 3\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)

async def cn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLxCzCOWd7aiGFBD2-2joCpWOLUrDLvVV_&si=XerTq9PRAwYPd4l-",
        "https://youtube.com/playlist?list=PL3eEXnCBViH-hlNCNwdfV7VrEcTquANGa&si=ez1WUcRJA67llBLh"
        ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url}\n\n\n /TOC -> Theory of Computation\n/CA -> Computer Architecture\n/SE -> Software Engineering\n/JV -> Java Programming \n\n\n/sem3 -> Semester 3\n/sem5 -> Semester 5\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")

async def se(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLxCzCOWd7aiEed7SKZBnC6ypFDWYLRvB2&si=VkRV_2z884JqZS_G"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url}\n\n\n /TOC -> Theory of Computation\n/CA -> Computer Architecture\n/CN -> Computer Networks\n/JV -> Java Programming \n\n\n/sem3 -> Semester 3\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)

async def jv(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://mega.nz/folder/J4UxxI4B#x0hIC-RklQ8cPbzmAT4jIg"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Abdul Bari Java course link:\n{playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFourIT/tree/main/Java%20lab \n\n\n /TOC -> Theory of Computation\n/CA -> Computer Architecture\n/CN -> Computer Networks\n/SE -> Software Engineering \n\n\n/sem3 -> Semester 3\n/sem5 -> Semester 5\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)


async def dbms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLmXKhU9FNesR1rSES7oLdJaNFgmuj0SYV&si=-s73GvtHYjebvGCw",
        "https://youtube.com/playlist?list=PLG9aCp4uE-s0bu-I8fgDXXhVLO4qVROGy&si=PLU5Nlnxp5GVdd5L"
        ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url} \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFiveIT/tree/main/DBMS \n\n\n/OS -> Operating System\n/WB -> Web Tech\n/GT -> Graph Theory\n/SQL -> SQL for DB lab \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")

async def os(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLG9aCp4uE-s17rFjWM8KchGlffXgOzzVP&si=8D2K2YRtuTcdsO2X"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist link:\n{playlist_url}  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFiveIT/tree/main/OS \n\n\n/DBMS -> Database Management Systems\n/WB -> Web Tech\n/GT -> Graph Theory\n/SQL -> SQL for DB lab \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)
    
async def web(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLDzeHZWIZsTo0wSBcg4-NMIbC0L8evLrD&si=PvjfrNG-Hj9lFzhZ"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist link:\n{playlist_url}  \n\n\n/DBMS -> Database Management Systems\n/OS -> Operating System\n/GT -> Graph Theory\n/SQL -> SQL for DB lab \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem6 -> Semester 6"
    await context.bot.send_message(update.effective_chat.id, message)    

async def gt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtube.com/playlist?list=PLU6SqdYcYsfLV24T0XVb3z3mjl8QG0EBN&si=j3V7ueNj2A-bGY4O",
        "https://youtube.com/playlist?list=PLmXKhU9FNesTpQNP_OpXN7WaPwGx7NWsq&si=554fL9GZFa419wFr"
        ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url}  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemFiveIT/tree/main/Graph%20Theory \n\n\n/DBMS -> Database Management Systems\n/OS -> Operating System\n/WB -> Web Tech\n/SQL -> SQL for DB lab \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")

async def sql(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_urls = [
        "https://youtu.be/hlGoQC332VM?si=fMNkBI4mfQFyev8E",
        "https://youtu.be/D_wNQR3LeeM?si=gFPeQ1TK1VuEeCS0"
        ]

    for playlist_url in playlist_urls:
        try:
            await context.bot.send_message(update.effective_chat.id, f"Playlist link: {playlist_url}  \n\n\n/DBMS -> Database Management Systems\n/OS -> Operating System\n/WB -> Web Tech\n/GT -> Graph Theory \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem6 -> Semester 6")
        except Exception as e:
            print(f"Failed to send playlist URL: {e}")
            
async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLxCzCOWd7aiHGhOHV-nwb0HR5US5GFKFI&si=pRMpgeFl6_tLf-p1"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url}  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemSixIT/tree/main/AI \n\n\n/IPPR -> Image Processing\n/UOS -> Unix OS\n/ADB -> Adv. Database Engineering \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem5 -> Semester 5"
    await context.bot.send_message(update.effective_chat.id, message)
    
async def ippr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLbwfaPBgAKFEPBg-OFzmjFWmRKKrYigLi&si=3HJXYkd5yqxu4iR0"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url}  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemSixIT/tree/main/IPPR \n\n\n/AI -> Artificial Intelligence\n/UOS -> Unix OS\n/ADB -> Adv. Database Engineering \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem5 -> Semester 5"
    await context.bot.send_message(update.effective_chat.id, message)    

async def uos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    playlist_url = "https://youtube.com/playlist?list=PLd3UqWTnYXOloH0vWBs4BtSbP84WcC2NY&si=9xHiBH0jXWtE-Sef"  # Replace with actual URL for Subject I Playlist in Semester 3
    message = f"Playlist Link:\n{playlist_url}  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemSixIT/tree/main/UOS \n\n\n/AI -> Artificial Intelligence\n/IPPR -> Image Processing\n/ADB -> Adv. Database Engineering \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem5 -> Semester 5"
    await context.bot.send_message(update.effective_chat.id, message)      
    
    
async def adb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = f"Refer 'Ramakrishnan - Database Management Systems - 2nd Edition' book strictly  \n\n For study material, visit 👇👇\n https://github.com/Garrixer47/SemSixIT/tree/main/ADE \n\n\n/AI -> Artificial Intelligence\n/IPPR -> Image Processing\n/UOS -> Unix OS \n\n\n/sem3 -> Semester 3\n/sem4 -> Semester 4\n/sem5 -> Semester 5"
    await context.bot.send_message(update.effective_chat.id, message)      
    
def main():
    application = Application.builder().token(Token).build()

    # Add handlers for commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('sem3', sem3))
    application.add_handler(CommandHandler('sem4', sem4))
    application.add_handler(CommandHandler('sem5', sem5))
    application.add_handler(CommandHandler('sem6', sem6))

    application.add_handler(CommandHandler('Math', math))
    application.add_handler(CommandHandler('DSA', dsa))
    application.add_handler(CommandHandler('MP', microp))
    application.add_handler(CommandHandler('DC', dc))
    application.add_handler(CommandHandler('CPP', cpp))
    application.add_handler(CommandHandler('PY', python))
    
    application.add_handler(CommandHandler('TOC', toc))
    application.add_handler(CommandHandler('CA', ca))
    application.add_handler(CommandHandler('CN', cn))
    application.add_handler(CommandHandler('SE', se))
    application.add_handler(CommandHandler('JV', jv))
    application.add_handler(CommandHandler('DBMS', dbms))
    application.add_handler(CommandHandler('OS', os))
    application.add_handler(CommandHandler('WB', web))
    application.add_handler(CommandHandler('GT', gt))
    application.add_handler(CommandHandler('SQL', sql))
    application.add_handler(CommandHandler('AI', ai))
    application.add_handler(CommandHandler('IPPR', ippr))
    application.add_handler(CommandHandler('UOS', uos))
    application.add_handler(CommandHandler('ADB', adb))
    
    

    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
