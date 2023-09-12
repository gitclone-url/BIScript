# Script Setup Guide

# Advisory:

Kindly be informed that the initial execution of the script on your Termux may necessitate a certain duration. This is due to the requirement for the script to perform package updates and upgrades as part of the initial setup process. Additionally, the installation of Python 3 is necessary, as it is a prerequisite for running the main BootSigner script.

*************************************************

**Requirements:**

• Ensure an active internet connection is available for the initial setup to update and upgrade packages.
  
---

**Script Running Steps:**

**Step 1:** Download the BIScript.zip file from the [Releases](https://github.com/gitclone-url/BIScript/releases) section.

**Step 2:** Extract the zip file using ZArchiver or any other zip extractor app.

**Step 3:** After extraction, you will see a folder named "BIScript."

<img src="https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/a505a282-149c-4d46-988a-f4744d45d908" alt="Screenshot" width="500" height="auto">

**Step 4:** Copy or move the "BIScript" folder to your device's internal storage.

**Step 5:** Download the [Termux app](https://github.com/HardcodedCat/termux-monet/releases).

**Step 6:** Download Official Magisk or Magisk delta and install it. Patch your boot image.

<img src="https://github.com/gitclone-url/BIScript/assets/98699436/be31a39e-f236-4876-bc5a-51f3aff37cec" alt="Screenshot" width="500" height="auto">

**Step 7:** After patching, copy the patched boot image from the download folder to the "BIScript" folder and rename it to `boot.img`.

<img src="https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/a0d27951-c4cc-4783-9c25-af02395f68ef" alt="Screenshot" width="500" height="auto">

<img src="https://github.com/gitclone-url/BIScript/assets/98699436/8b964223-8f23-4ae9-be4b-23131b0dc088" alt="Screenshot" width="500" height="auto">

**Step 8:** Open the Termux application and grant storage permission.

**Step 9:** After setup, you will see the Termux interface.

**Step 10:** Change the directory to the "BIScript" folder with this command:
```
cd /storage/emulated/0/BIScript
```

**Step 11:** Make the script executable with this command:
```
chmod +x BIScript.sh
```

<img src="https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/ad401010-b3dc-4112-9860-33728eb74219" alt="Screenshot" width="500" height="auto">

**Step 12:** Run the script with this command:
```
bash BIScript.sh
```

Wait for a few minutes for the main script to start.
It will automatically download necessary packages and sign the image. Wait until it finishes; you will see a success message.

<img src="https://github.com/UnknownShakib/BIScript/assets/124501955/cb85fb51-0dec-416e-a1d8-7aa36a598a19" alt="Screenshot" width="500" height="auto">

Now Follow this [guide](https://github.com/gitclone-url/SPD-T610-Phones-Rooting-Tutorial) to flash the signed boot image.
