# BIScript 🚀

**𝘼 𝙗𝙤𝙤𝙩 𝙞𝙢𝙖𝙜𝙚 𝙨𝙞𝙜𝙣𝙞𝙣𝙜 𝙨𝙘𝙧𝙞𝙥𝙩 𝙛𝙤𝙧 𝙪𝙣𝙞𝙨𝙤𝙘 𝙘𝙝𝙞𝙥𝙨𝙚𝙩 𝙗𝙖𝙨𝙚𝙙 𝙥𝙝𝙤𝙣𝙚𝙨** 

## What is this script for ❓
This script is for automatically signing Unisoc / Spreadtrum (SPD) boot image using a private key and AVBtool based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32674.html) from hovatek.

Also A custom signed vbmeta image based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32664.html) and a openssl generated custom boot signing (.pem) key based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32662.html) is already provided in the BIScript zip.


In newer unisoc chip based phones if you don't sign and flash the magisk patched boot image directly device will go into bootloop.Because for device's that comes with vbmeta-sign, is that you must flash a customised but signed vbmeta before you can tamper with checked partitions..! So I have made this script to help other people who wants to root their phone without any hassle and i also made this [boot-image-flasher](https://github.com/gitclone-url/Boot-img-flasher) script which they can use and can directly flash the signed boot image.

Note📜 :- You must need a root environment for using boot-image-flasher script

This BIScript is tested only on this 4 devices.

- Micromax in 2b / Micromax in 2c (Indian brand)
- symphony z33 / symphony z45 (Bangladeshi brand)

All of them are Based on unisoc tiger t610 chip and share many similarities and All of this phones comes with svbmeta-sign.img in their firmware as this device's will only accept images signed with keys that match what's contained in the device's vbmeta partition..

## How to use this script ❓

First of All Download the BIScript.zip from
[Releases](https://github.com/gitclone-url/BIScript/releases)

- Extract the zip with zarchiver or other zip extractor apps

After extraction you will find a BIScript folder 📁
![Screenshot](https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/a505a282-149c-4d46-988a-f4744d45d908)

Copy or move it to internal storage.

- Download **Termux** app from [**Here**](https://github.com/HardcodedCat/termux-monet/releases) 

Note📜 :- This script can also be used in any linux shell environment

- Now Download Official Magisk or Magisk delta 

- install and open then Patch your boot image

![IMG](https://github.com/gitclone-url/BIScript/assets/98699436/be31a39e-f236-4876-bc5a-51f3aff37cec)


After it's done ✅

You need to copy the Patched boot image from download folder 📁 to BIScript folder
And rename it to `boot.img`

![Screenshot](https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/a0d27951-c4cc-4783-9c25-af02395f68ef)

![Screenshot](https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/5dad0371-e401-47bb-a49e-2e5914391af0)

- Now Open termux application allow storage permission 

 After setup done you will see termux 
 interface 

- Now change directory to BIScript folder by this command :
```
cd /storage/emulated/0/BIScript
```
- Then enter this command to make the **Script** executable

```
chmod +x BIScript.sh
```

![Screenshot](https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/ad401010-b3dc-4112-9860-33728eb74219)

- Now Run the script by this command :

```
bash BIScript.sh
``` 
It will automatically download necessary packagees and sign the images just wait until it finish after it's done you Will see a success message

![Screenshot](https://github.com/gitclone-url/android_device_micromax_E7544/assets/98699436/22e01b6d-635b-41ca-9d26-03f4932da0aa)

- Now just follow this [**Guide**](you and flash it 🙂

## Additional note 📜

My main purpose behind making this script was to support only those 4 devices i mentioned earlier 

I don't guarantees that this script will work on other unisoc chipset based phones because some oems uses private (.pem) key to sign partition and you'll Need that key just even for unlocking bootloader If you want to use this script on your phone than you need to change the commands in the script **line 88** replace`Partition size` `Algorithm` value according to your boot image info and you'll also need to change **(.pem)** key to sign it but first you need to create a custom signed vbmeta according to this [**Tutorial**](https://www.hovatek.com/forum/thread-32664.html) Then you can use the private key to sign images.you can use [**Vbmeta keys Extractor**](https://github.com/Fijxu/VBMetaKeysExtractor-Linux) for this work.Also if somebody wants they can use the vbmeta-sign image that i have provided in the zip because most of the unisoc oem uses the same keys to sign the vbmeta,if my vbmeta works on your phone than you can use my boot.pem key provided in the zip to sign your boot image too.

#### **Acknowledgment 📚:**

If you decide to use or modify my script and those files for your own purposes, it is appreciated if you give credit to me by mentioning my name or providing a link to my GitHub profile. Acknowledging the work of others promotes collaboration and supports the open-source community.

**Special thanks ♥️ goes to hovatek forum and their members particularly the contributors to the following threads:**

- [Thread 1](https://www.hovatek.com/forum/thread-32664.html)
- [Thread 2](https://www.hovatek.com/forum/thread-32674.html)
- [Thread 3](https://www.hovatek.com/forum/thread-32662.html)

The tutorials and information shared in this threads were instrumental in the development of this script.


## Disclaimer❗

This script is provided as-is, without any warranties or guarantees of any kind. The author of this script, Abhijeet, cannot be held responsible for any damages or issues that may arise from flashing the signed boot image by using this script.Use this script at your own risk, and make sure to fully understand the implications and consequences of flashing a boot image. The author and contributors of this script cannot be held liable for any negative outcomes resulting from the use of this script or the flashing of a boot image
It is recommended to thoroughly understand and review the script before using it.


