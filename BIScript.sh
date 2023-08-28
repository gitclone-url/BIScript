#!/bin/bash

#<< BIScript 'BANNER'
# ______  _  ______             _              
#(____  \| |/ _____)           (_)       _     
# ____)  ) ( (____   ____  ____ _ ____ _| |_   
#|  __  (| |\____ \ / ___)/ ___) |  _ (_   _)  
#| |__)  ) |_____) | (___| |   | | |_| || |_   
#|______/|_(______/ \____)_|   |_|  __/  \__)  
#                                |_|

# Function to display a spinner while waiting
spinner() {
  local pid=$1
  local delay=0.1
  local spinstr='|/-\'
  while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
    local temp=${spinstr#?}
    printf " [%c] " "$spinstr"
    local spinstr=$temp${spinstr%"$temp"}
    sleep $delay
    printf "\b\b\b\b\b\b"
  done
  printf "    \b\b\b\b"
}

# Install Python3
echo "Initializing script. Please wait..."
apt-get update > /dev/null && apt-get install -y python > /dev/null &
spinner $!  # Run the spinner 

# Check if "__bootsigner__.py" file exists
if [ -f "__bootsigner__.py" ]; then
    # Run the Python script
      echo "Done √"
      sleep 0.5
      echo "Running main script..."
      sleep 2
      clear # clear out screen
      python3 __bootsigner__.py
else
    echo "Failed: bootsigner script not found!"
fi