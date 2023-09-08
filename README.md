# BIScript 🚀

**𝘼 𝙗𝙤𝙤𝙩 𝙞𝙢𝙖𝙜𝙚 𝙨𝙞𝙜𝙣𝙞𝙣𝙜 𝙨𝙘𝙧𝙞𝙥𝙩 𝙛𝙤𝙧 𝙪𝙣𝙞𝙨𝙤𝙘 𝙘𝙝𝙞𝙥𝙨𝙚𝙩 𝙗𝙖𝙨𝙚𝙙 𝙥𝙝𝙤𝙣𝙚𝙨** 

### What is this script for ❓
This script is for automatically signing Unisoc / Spreadtrum (SPD) boot images using a private key and AVBTool based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32674.html) from hovatek.

Also, a custom-signed vbmeta image based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32664.html) and an OpenSSL-generated custom boot signing (.pem) key based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32662.html) are already provided in the BIScript zip.

In newer Unisoc chip-based phones, if you don't sign and flash the Magisk-patched boot image directly, the device will go into a bootloop. This is because for devices that come with vbmeta-sign, you must flash a customized but signed vbmeta before you can tamper with checked partitions. So, I have made this script to help other people who want to root their phone without any hassle. I have also created a [boot-image-flasher](https://github.com/gitclone-url/Boot-img-flasher) script that can directly flash the signed boot image.

**Note📜**: You must have a rooted environment to use the boot-image-flasher script.

This BIScript has been tested on the following 4 devices:

- Micromax in 2b / Micromax in 2c (Indian brand)
- Symphony z33 / Symphony z45 (Bangladeshi brand)

All of these devices are based on the Unisoc Tiger T610 chip and share many similarities. They all come with svbmeta-sign.img in their firmware because these devices will only accept images signed with keys that match what's contained in the device's vbmeta partition.

### How to use this script ❓

**Please follow this [Script Setup Guide](https://github.com/gitclone-url/BIScript/blob/Master/Script%20Setup%20Guide.md) for detailed instructions on how to set up and use the script.**

## Additional Info 📜

My main purpose behind making this script was to support only those 4 devices I mentioned earlier. I cannot guarantee that this script will work on other Unisoc chipset-based phones because some OEMs use a private (.pem) key to sign partitions, and you'll need that key even for unlocking the bootloader. If you want to use this script on your phone, you need to modify the commands in the script. Here's how you can do it:

1. Modify the `cmd` command as follows:
   
   ```python
   cmd = [
       "python2", "avbtool", "add_hash_footer", "--image", "boot.img", "--partition_name", "boot",
       "--partition_size", "67108864", "--key", "boot.pem", "--algorithm", "SHA256_RSA4096",
       "--prop", f"com.android.build.boot.fingerprint:{fingerprint}",
       "--prop", "com.android.build.boot.os_version:11"
   ]
   ```

2. Replace `Partition size` and `Algorithm` values in the `cmd` command according to your boot image information.

3. Create a custom-signed vbmeta according to this [Tutorial](https://www.hovatek.com/forum/thread-32664.html). You can use [Vbmeta Keys Extractor](https://github.com/Fijxu/VBMetaKeysExtractor-Linux) for this work.

4. If you don't have a private key to sign images, you can use the vbmeta-sign image provided in the zip. Most Unisoc OEMs use the same keys to sign the vbmeta. If my vbmeta works on your phone, you can use the `boot.pem` key provided in the zip to sign your boot image too.

**Acknowledgment 📚:**

If you decide to use or modify my script and those files for your own purposes, it is appreciated if you give credit to me by mentioning my name or providing a link to my GitHub profile. Acknowledging the work of others promotes collaboration and supports the open-source community.

**Special thanks ♥️ go to hovatek forum and their members, particularly the contributors to the following threads:**

- [Thread 1](https://www.hovatek.com/forum/thread-32664.html)
- [Thread 2](https://www.hovatek.com/forum/thread-32674.html)
- [Thread 3](https://www.hovatek.com/forum/thread-32662.html)

The tutorials and information shared in these threads were instrumental in the development of this script.

## Disclaimer❗

This script is provided as-is, without any warranties or guarantees of any kind. The author of this script, Abhijeet, cannot be held responsible for any damages or issues that may arise from flashing the signed boot image by using this script. Use this script at your own risk, and make sure to fully understand the implications and consequences of flashing a boot image. The author and contributors of this script cannot be held liable for any negative outcomes resulting from the use of this script or the flashing of a boot image. It is recommended to thoroughly understand and review the script before using it.
