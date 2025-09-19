class Txt(object):

    PRIVATE_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴅᴏ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ɪɴ ɴᴇɢʟɪɢɪʙʟᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏss ᴏғ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ
"""
    GROUP_START_MSG = """
Hɪ {},

I'ᴍ Fɪʟᴇs Eɴᴄᴏᴅᴇʀ ʙᴏᴛ ᴄᴀɴ ᴄᴏᴍᴘʀᴇss ʏᴏᴜʀ ғɪʟᴇs ᴛᴏ ɴᴇɢʟɪɢɪʙʟᴇ sɪᴢᴇ ᴡɪᴛʜᴏᴜᴛ ʟᴏᴏsɪɴɢ ᴛʜᴇ ǫᴜᴀʟɪᴛɪᴇs ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ᴠɪᴅᴇᴏ

❗**Yᴏᴜ ʜᴀsɴ'ᴛ sᴛᴀʀᴛᴇᴅ ᴍᴇ ʏᴇᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ғɪʀsᴛ sᴛᴀʀᴛ ᴍᴇ sᴏ ɪ ᴄᴀɴ ᴡᴏʀᴋ ғʟᴀᴡʟᴇssʟʏ**
"""
    PROGRESS_BAR = """<b>
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

    SEND_FFMPEG_CODE = """
❪ SET CUSTOM FFMPEG CODE ❫

Send me the correct ffmpeg code for more info.


☛ <a href=https://unix.stackexchange.com/questions/28803/how-can-i-reduce-a-videos-size-with-ffmpeg#:~:text=ffmpeg%20%2Di%20input.mp4%20%2Dvcodec%20libx265%20%2Dcrf%2028%20output.mp4> FOR HELP </a>

⦿ Fᴏʀᴍᴀᴛ Oɴ Hᴏᴡ Tᴏ Sᴇᴛ

☞ ffmpeg -i input.mp4 <code> -c:v libx264 -crf 23 </code> output.mp4

<code> -c:v libx264 -crf 23 </code> Tʜɪs ɪs ʏᴏᴜʀ ғғᴍᴘᴇɢ ᴄᴏᴅᴇ ✅

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @The_TGGuy
"""

    SEND_METADATA ="""
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="My Video" -metadata author="John Doe" -metadata:s:s title="Subtitle Title" -metadata:s:a title="Audio Title" -metadata:s:v title="Video Title" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @The_TGguy
"""

    
    HELP_MSG = """
Available commands:-

➜ /set_ffmpeg - To set custom ffmpeg code
➜ /set_metadata - To set custom metadata code
➜ /set_caption - To set custom caption
➜ /del_ffmpeg - Delete the custom ffmpeg code
➜ /del_caption - Delete caption
➜ /see_ffmpeg - View custom ffmpeg code
➜ /see_metadata - View custom metadata code
➜ /see_caption - View caption 
➜ To Set Thumbnail just send photo

"""

    ABOUT_TXT = f"""◇──◇──◇──◇──◇──◇──◇──◇
<blockquote>‣ Mʏ ᴜsᴇʀɴᴀᴍᴇ: @{} \n\n‣ Cʀᴇᴀᴛᴏʀ ᴏғ ᴍᴇ: <a href='https://t.me/The_TGguy'>𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝙶𝚞𝚢!!</a>\n\n‣ Dᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/'>𝙼𝚘𝚗𝚐𝚘 𝙳𝙱</a>\n\n‣ Pʀᴏɢʀᴀᴍᴍᴇᴅ Lᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>𝙿𝚢𝚝𝚑𝚘𝚗</a>\n\n‣ Hᴏsᴛᴇᴅ Oɴ: <a href='https://www.heroku.com/'>𝙷𝚎𝚛𝚘𝚔𝚞</a></blockquote>
◇──◇──◇──◇──◇──◇──◇──◇"""
