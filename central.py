import subprocess

while True:
    print("""🇧 🇮 🇪 🇳 🇻 🇪 🇳 🇮 🇩 🇴 
🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐🌐

ℙ𝕣𝕖𝕤𝕖𝕟𝕥𝕒𝕞𝕠𝕤 𝕖𝕝 𝕤𝕖𝕣𝕧𝕚𝕔𝕚𝕠 𝕕𝕖 𝕚𝕟𝕤𝕥𝕒𝕝𝕒𝕔𝕚𝕠𝕟 𝕖𝕟 𝕥𝕖𝕣𝕞𝕦𝕩 𝕕𝕖𝕝 𝕤𝕖𝕣𝕧𝕚𝕔𝕚𝕠 𝕕𝕖 𝕕𝕖𝕤𝕔𝕒𝕣𝕘𝕒 𝕘𝕣𝕒𝕥𝕚𝕤 ℂ𝕦𝕓𝕒𝔽𝕝𝕚𝕩𝕄𝕒𝕩.
👾👾👾👾👾👾👾👾👾👾👾👾
A͢ C͢o͢n͢t͢i͢n͢u͢a͢c͢i͢o͢n͢ s͢e p͢r͢e͢s͢e͢n͢t͢a͢ u͢n͢a͢ l͢i͢s͢t͢a͢ d͢e͢ o͢p͢c͢i͢o͢n͢e͢s͢ d͢e͢b͢e͢ e͢j͢e͢c͢u͢t͢a͢r͢ u͢n͢a͢ d͢e͢t͢r͢a͢s͢ d͢e͢ l͢a͢ o͢t͢r͢a͢:

            [1]⇏𝚁𝚎𝚌𝚞𝚛𝚜𝚘𝚜 𝚗𝚎𝚌𝚎𝚜𝚊𝚛𝚒𝚘𝚜
            [2]⇏𝙸𝚗𝚜𝚝𝚊𝚕𝚊𝚛 𝚋𝚒𝚋𝚕𝚘𝚝𝚎𝚌𝚊 3.0.0
            [3]⇏𝙸𝚗𝚜𝚝𝚊𝚕𝚊𝚛 𝚋𝚒𝚋𝚕𝚒𝚘𝚝𝚎𝚌𝚊 4.0.2(𝚎𝚡𝚙𝚎𝚛𝚒𝚖𝚎𝚗𝚝𝚊𝚕)🌐
            [4]⇏𝙲𝚊𝚖𝚋𝚒𝚘 𝚍𝚎 𝚛𝚞𝚝𝚊 𝚊𝚕 𝚖𝚘𝚟𝚒𝚕.""")
    ejecuto = int(input("𝕀𝕟𝕘𝕣𝕖𝕤𝕖 𝕝𝕒 𝕠𝕡𝕔𝕚𝕠𝕟 𝕕𝕖𝕤𝕖𝕒𝕕𝕒 𝕒 𝕔𝕠𝕟𝕥𝕚𝕟𝕦𝕒𝕔𝕚𝕠𝕟👾⇏⇏:"))

    if ejecuto == 1:  # instalacion
        subprocess.run(["pkg", "install", "python3"])
        subprocess.run(["pkg", "upgrade", "python3"])
        subprocess.run(["pip3", "install", "pymongo"])

    # libreria 3.0.0
    elif ejecuto == 2:
        subprocess.run(["pip3", "install", "cubaflixmax==3.0.0"])

    # libreria 4.0.2
    elif ejecuto == 3:
        subprocess.run(["pip3", "install", "cubaflixmax==4.0.2"])

    elif ejecuto == 4:  # nueva ruta
        subprocess.run(["bash", "nuevaruta.sh"])
        break
    