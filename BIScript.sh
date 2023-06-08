#!/bin/bash

#Stylish header message
echo "      *********************000 of 000******************"                                
echo "             ____ ___ ____            _       _   "
echo "            | __ )_ _/ ___|  ___ _ __(_)_ __ | |_ "
echo "            |  _ \| |\___ \ / __| '__| | '_ \| __|"
echo "            | |_) | | ___) | (__| |  | | |_) | |_ "
echo "            |____/___|____/ \___|_|  |_| .__/ \__|"
echo "                                       |_|        "   
sleep 0.5
echo ""
echo "𝔸 𝕓𝕠𝕠𝕥 𝕚𝕞𝕒𝕘𝕖 𝕤𝕚𝕘𝕟𝕚𝕟𝕘 𝕤𝕔𝕣𝕚𝕡𝕥 𝕗𝕠𝕣 𝕦𝕟𝕚𝕤𝕠𝕔 𝕔𝕙𝕚𝕡𝕤𝕖𝕥 𝕓𝕒𝕤𝕖𝕕 𝕡𝕙𝕠𝕟𝕖𝕤"
sleep 0.5
echo ""
echo "                      - 𝙼𝚊𝚍𝚎 𝚋𝚢 𝙰𝚋𝚑𝚒𝚓𝚎𝚎𝚝"
echo "      *************************************************"

# Function to display error message in red color
print_error() {
  printf "\033[31m%s\033[0m\n" "$1"
}

# Function to display success message in green color.
function successful_message {
    echo -e "\033[32m$1\033[0m"
}

# Function to display info message in blue color.
function info_message {
    echo -e "\033[34m$1\033[0m"
}


# Update and upgrade termux packages.
if ! apt update && apt upgrade -y; then
    print_error "Package update and upgrade failed. Please check your internet connection and try again."
    exit 1
fi

echo "___________________________________________________________"
echo ""
# Check if Python 2 is installed if not then install it.
if ! command -v python2 &> /dev/null; then
    info_message "Python 2 is not installed. Installing..."
    if ! pkg install python2 -y; then
        print_error "Python 2 installation failed."
        exit 1
    fi
    successful_message "Python 2 installed successfully."
else
    info_message "Python 2 is already installed."
fi
echo "" 
echo "--------------------------------------"
# Check if OpenSSL is installed if not then install it.
if ! command -v openssl &> /dev/null; then
    info_message "OpenSSL Tool is not installed. Installing..."
    if ! pkg install openssl-tool -y; then
        print_error "OpenSSL Tool installation failed."
        exit 1
    fi
    successful_message "OpenSSL Tool installed successfully."
else
    info_message "OpenSSL Tool is already installed."
fi
echo "--------------------------------------"

info_message "checking Boot image info please wait..."
echo "--------------------------------------"
sleep 3
echo ""
# check boot image info with avbtool and extract and grep fingerprint value.
output=$(python2 avbtool info_image --image boot.img)
if [[ $? -ne 0 ]]; then
    print_error "Failed to check 'boot image info!'.Please make sure the 'boot.img' file is placed in the folder."
    exit 1
fi
fingerprint=$(echo "$output" | grep "com.android.build.boot.fingerprint" | awk -F"'" '{print $2}')

info_message "Signing in progress please wait..."
sleep 10
echo ""
echo "Done ✅"
echo "___________________________________________________________"

# sign the boot image using Python2 and avbtool  with the extracted fingerprint value.
python2 avbtool add_hash_footer --image boot.img --partition_name boot --partition_size 67108864 --key boot.pem --algorithm SHA256_RSA4096 --prop com.android.build.boot.fingerprint:$fingerprint --prop com.android.build.boot.os_version:11
if [ $? -ne 0 ]; then
print_error "Failed to 'sign boot image!'.Please make sure the 'boot.img' file is placed in the folder."
    exit 1
fi

message="Boot image signing done! You can now flash the signed boot Image to your phone."

length=$((${#message} + 0))

printf "\n%s\n" "$(printf '%*s' $length | tr ' ' '-')"
printf "\033[32m%s\033[0m\n" "$(printf ' %s ' "$message")"
printf "%s\n\n" "$(printf '%*s' $length | tr ' ' '-')"