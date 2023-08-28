#!/usr/bin/env python3

import subprocess
import sys
import time

def print_error(message):
    print("\033[31m{}\033[0m".format(message))

def print_success(message):
    print("\033[32m{}\033[0m".format(message))

def print_info(title, message=None):
    color_code = "34"
    colored_title = f"\033[{color_code}m{title}\033[0m"
    colored_text = f"{colored_title} {message}" if message else colored_title
    print(colored_text)

def print_colored(text, color_code):
    colored_text = f"\033[{color_code}m{text}\033[0m"
    print(colored_text)

def check_package_installed(package_name):
    try:
        output = subprocess.check_output(["pkg", "list-installed"], stderr=subprocess.DEVNULL, text=True)
        return package_name in output
    except subprocess.CalledProcessError:
        return False

def install_package(package_name):
    print_info(f"{package_name} is not installed. Installing...")
    if subprocess.call(["pkg", "install", package_name, "-y"], stderr=subprocess.STDOUT) != 0:
        print_error(f"{package_name} installation failed.")
        sys.exit(1)
    print_success(f"{package_name} installed successfully.")

def main():
    print("      *********************000 of 000******************")
    print("             ____ ___ ____            _       _   ")
    print("            | __ )_ _/ ___|  ___ _ __(_)_ __ | |_ ")
    print("            |  _ \| |\___ \ / __| '__| | '_ \| __|")
    print("            | |_) | | ___) | (__| |  | | |_) | |_ ")
    print("            |____/___|____/ \___|_|  |_| .__/ \__|")
    print("                                       |_|        ")
    time.sleep(0.5)
    print("")
    print("  𝔸 𝕓𝕠𝕠𝕥 𝕚𝕞𝕒𝕘𝕖 𝕤𝕚𝕘𝕟𝕚𝕟𝕘 𝕤𝕔𝕣𝕚𝕡𝕥 𝕗𝕠𝕣 𝕦𝕟𝕚𝕤𝕠𝕔 𝕔𝕙𝕚𝕡𝕤𝕖𝕥 𝕓𝕒𝕤𝕖𝕕 𝕡𝕙𝕠𝕟𝕖𝕤")
    time.sleep(0.5)
    print("")
    print("                      - 𝙼𝚊𝚍𝚎 𝚋𝚢 𝙰𝚋𝚑𝚒𝚓𝚎𝚎𝚝")
    print("      *************************************************")
    print("________________________________________________________________")

    print_info("Updating and upgrading Termux packages...")
    update_upgrade_cmd = ["apt update && apt upgrade -y"]
    try:
        subprocess.check_call(update_upgrade_cmd, stderr=subprocess.STDOUT, text=True, shell=True)
    except subprocess.CalledProcessError:
        print_error("Package update and upgrade failed. Please check your internet connection and try again.")
        sys.exit(1)
    
    time.sleep(1)
    print("----------------------------------------")
    if not check_package_installed("python2"):
        install_package("python2")
    else:
        python2_version = subprocess.check_output(["python2", "--version"], stderr=subprocess.STDOUT, text=True).strip()
        print_info("Python 2 is already installed.")
        print_colored(f"Python2 version: {python2_version}", "97") 
    print("----------------------------------------")
    
    time.sleep(1)
    
    if not check_package_installed("openssl-tool"):
        install_package("openssl-tool")
    else:
        print_info("OpenSSL Tool is already installed.")
        openssl_version = subprocess.check_output(["openssl", "version"], stderr=subprocess.STDOUT, text=True).strip()
        print_colored(f"OpenSSL version: {openssl_version.split()[1]}", "97")

    print("----------------------------------------")
    time.sleep(1)
    print_info("Checking Boot image info, please wait...")
    print("----------------------------------------")
    time.sleep(5)
    try:
        output = subprocess.check_output(["python2", "avbtool", "info_image", "--image", "boot.img"], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        error_output = e.output
        if "No such file or directory: 'boot.img'" in error_output:
            print_error("Failed to check 'boot image info!'. Please make sure the 'boot.img' file is placed in the folder.")
            sys.exit(1)
        elif "Given image does not look like a vbmeta image" in error_output:
            print_error("Failed to check 'boot image info!'.The image you have provided does not look like a boot image.")
            sys.exit(1)
        else:
            print(error_output)  
            print_error("Failed to check 'boot image info!")
            sys.exit(1)
        
    lines = output.splitlines()
    fingerprint = None
    for line in lines:
        if "com.android.build.boot.fingerprint" in line:
            fingerprint = line.split("'")[1]
            break

    if fingerprint is None:
        print_error("Error: Failed to extract fingerprint value.")
        sys.exit(1)

    fingerprint = fingerprint.replace("'", "").replace('"', '').replace('[', '').replace(']', '')

    print_info("Signing in progress, please wait...")
    print("----------------------------------------")
    time.sleep(10)

    cmd = [
        "python2", "avbtool", "add_hash_footer", "--image", "boot.img", "--partition_name", "boot",
        "--partition_size", "67108864", "--key", "boot.pem", "--algorithm", "SHA256_RSA4096",
        "--prop", f"com.android.build.boot.fingerprint:{fingerprint}",
        "--prop", "com.android.build.boot.os_version:11"
    ]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        error_output = e.output
        if "Traceback (most recent call last)" not in error_output.lower():
            print_error("Failed:", error_output) 
            print("")
            print("Possible reason: corrupted/broken image or incorrect format.")
            sys.exit(1)
        else:
            print("An error occurred:", e)
            print("")
            print_error("Possible reason: corrupted/broken image or incorrect format.")
            sys.exit(1)
    else:
        print("")
        print("Done ✅")
        print("________________________________________________________________")
    
        message = "Boot image signing done! You can now flash the signed boot Image to your phone."
        length = len(message)
        print("-" * length)
        print_success(message)
        print("-" * length)
        sys.exit(0)

if __name__ == "__main__":
    main()