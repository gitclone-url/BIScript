# BIScript 🚀

**Automated Boot Image Signing Script for Unisoc Chipset-Based Phones** 

## What is this script for ❓
This script automates the process of signing Unisoc/Spreadtrum (SPD) boot images using a private key and AVBTool, following the instructions in this [**Tutorial**](https://www.hovatek.com/forum/thread-32674.html) from hovatek.

Included in the BIScript zip are a custom-signed vbmeta image based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32664.html) and an OpenSSL-generated custom boot signing (.pem) key based on this [**Tutorial**](https://www.hovatek.com/forum/thread-32662.html).

Newer Unisoc chip-based phones require you to sign and flash the Magisk-patched boot image directly; otherwise, the device may enter a bootloop. This is because devices equipped with vbmeta-sign demand a customized signed vbmeta before tampering with protected partitions. Thus, I've created this script to simplify the rooting process and aid others in need. Additionally, I've developed a [boot-image-flasher](https://github.com/gitclone-url/Boot-img-flasher) script for directly flashing the signed boot image.

**Note📜**: You must have a rooted environment to use the boot-image-flasher script.

This BIScript has been tested on the following four devices:

- Micromax in 2b / Micromax in 2c (Indian brand)
- Symphony z33 / Symphony z45 (Bangladeshi brand)

All these devices rely on the Unisoc Tiger T610 chip and share many similarities. They all include vbmeta-sign.img in their firmware, as these devices exclusively accept images signed with keys matching the contents of the device's vbmeta partition.

## How to use this script ❓

**For detailed instructions on setting up and using the script, please follow this [Script Setup Guide](https://github.com/gitclone-url/BIScript/blob/Master/Script%20Setup%20Guide.md).**

## Additional Info 📜

My primary goal in creating this script was to support the four devices I mentioned earlier. I cannot guarantee its compatibility with other Unisoc chipset-based phones, as some OEMs employ a private (.pem) key for signing partitions, even for bootloader unlocking. If you wish to use this script on your phone, you'll need to make these modifications:

1. Modify the `cmd` command as follows:
   
   ```python
   cmd = [
       "python2", "avbtool", "add_hash_footer", "--image", "boot.img", "--partition_name", "boot",
       "--partition_size", "67108864", "--key", "boot.pem", "--algorithm", "SHA256_RSA4096",
       "--prop", f"com.android.build.boot.fingerprint:{fingerprint}",
       "--prop", "com.android.build.boot.os_version:11"
   ]
   ```

2. Adapt the `Partition size` and `Algorithm` values in the `cmd` command to match your boot image information.

3. Create a custom-signed vbmeta using this [Tutorial](https://www.hovatek.com/forum/thread-32664.html). You can use [Vbmeta Keys Extractor](https://github.com/Fijxu/VBMetaKeysExtractor-Linux) for this task.

4. If you lack a private key to sign images, you can use the vbmeta-sign image provided in the zip. Most Unisoc OEMs employ the same keys for vbmeta signing. If my vbmeta works on your phone, you can use the `boot.pem` key from the zip to sign your boot image as well.

**Acknowledgment 📚:**

If you decide to use or modify my script and files for your own purposes, it would be appreciated if you credited me by mentioning my name or providing a link to my GitHub profile. Acknowledging the work of others fosters collaboration and supports the open-source community.

**Special thanks ♥️ go to the hovatek forum and its members, especially the contributors to the following threads:**

- [Thread 1](https://www.hovatek.com/forum/thread-32664.html)
- [Thread 2](https://www.hovatek.com/forum/thread-32674.html)
- [Thread 3](https://www.hovatek.com/forum/thread-32662.html)

The tutorials and information shared in these threads were instrumental in the development of this script.

## Disclaimer❗

This script is provided as-is, without any warranties or guarantees of any kind. The author of this script, Abhijeet, cannot be held responsible for any damages or issues that may arise from flashing the signed boot image using this script. Use this script at your own risk, and ensure you fully comprehend the implications and consequences of flashing a boot image. The author and contributors of this script cannot be held liable for any adverse outcomes resulting from the use of this script or the flashing of a boot image. It is recommended to thoroughly understand and review the script before using it.
