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

---

### Additional Information 📜

My primary goal in creating this script was to support the four devices I mentioned earlier. I cannot guarantee its compatibility with other Unisoc chipset-based phones, as some OEMs employ a private (.pem) key for signing partitions, even for bootloader unlocking. If you wish to use this script on your phone the follow these steps:

1. Unlock your phone's bootloader.

2. Create a custom-signed vbmeta following this [Tutorial](https://www.hovatek.com/forum/thread-32664.html) and flash it to your phone. You can use [Vbmeta Keys Extractor](https://github.com/Fijxu/VBMetaKeysExtractor-Linux) for this task. Alternatively, you can use the provided custom signed vbmeta, but if it doesn't work for your phone, you must create your own.

3. Extract the BIScript zip and move the folder to your phone's internal storage. Then navigate to the BIScript folder in the terminal using the following command:
   
   ```
   cd /storage/emulated/0/BIScript
   ```

4. Place your boot image in the BIScript folder and execute the following command in the terminal to obtain boot image information:

   ```
   python2 avbtool info_image --image boot.img
   ```

   The output will resemble the following:
   
   ```
   Footer version:           1.0
   Image size:               100663296 bytes
   Original image size:      50671616 bytes
   VBMeta offset:            50671616
   VBMeta size:              704 bytes
   --
   Minimum libavb version:   1.0
   Header Block:             256 bytes
   Authentication Block:     0 bytes
   Auxiliary Block:          448 bytes
   Algorithm:                NONE
   Rollback Index:           0
   Flags:                    0
   Release String:           'avbtool 1.2.0'
   Descriptors:
       Hash descriptor:
         Image Size:            50184192 bytes
         Hash Algorithm:        sha256
         Partition Name:        boot
         Salt:                  54c2a7ea0cce4cdd77f3604f896fce4fe61a188fe2ce849f08ee354cbc8ea7fa
         Digest:                4b5c117599d94f7604bd2b0df50a996d84a00a150cb952f34f63776a0f5e1144
         Flags:                 0
   ```

From the output, take note of the Image size, Algorithm, and Partition Name, as well as the boot OS version.

5. Modify the `cmd` command as follows:

   ```python
   cmd = [
       "python2", "avbtool", "add_hash_footer", "--image", "boot.img", "--partition_name", "boot",
       "--partition_size", "67108864", "--key", "boot.pem", "--algorithm", "SHA256_RSA4096",
       "--prop", f"com.android.build.boot.fingerprint:{fingerprint}",
       "--prop", "com.android.build.boot.os_version:11"
   ]
   ```
   
Replace the `Partition size`, `Algorithm`, `Name`, and `boot.os_version` values in the `cmd` command to match your boot image information. You will also need to replace the private (.pem) key for signing the image. Then run the script to sign your specific image.

**Notes:**

- Some Unisoc OEMs use custom private keys to sign partition images, even for bootloader unlocking you will need it. if this the case then first you've to manage and get the key your OEM used to sign vbmeta.

- If you have successfully used my custom-signed vbmeta image and flashed it on your phone and it worked, then you can also use my private (boot.pem) key to sign your boot image.

- If you haven't used my custom-signed vbmeta and have created your own & replaced the stock public keys for any partition during the creation of your custom-signed vbmeta, you will need the private key used to generate your custom public key for signing the boot image.

- The boot.pem is custom private key that i have provided for boot signing.
Generated with [Puttygen](https://puttygen.com/).


**Acknowledgment 📚:**

If you decide to use or modify my script and files for your own purposes, it would be appreciated if you credited me by mentioning my name or providing a link to my GitHub profile. Acknowledging the work of others fosters collaboration and supports the open-source community.

**Special thanks ♥️ go to the hovatek forum and its members, especially the contributors to the following threads:**

- [Thread 1](https://www.hovatek.com/forum/thread-32664.html)
- [Thread 2](https://www.hovatek.com/forum/thread-32674.html)
- [Thread 3](https://www.hovatek.com/forum/thread-32662.html)

The tutorials and information shared in these threads were instrumental in the development of this script.

## Disclaimer❗

This script is provided as-is, without any warranties or guarantees of any kind. The author of this script, Abhijeet, cannot be held responsible for any damages or issues that may arise from flashing the signed boot image using this script. Use this script at your own risk, and ensure you fully comprehend the implications and consequences of flashing a boot image. The author and contributors of this script cannot be held liable for any adverse outcomes resulting from the use of this script or the flashing of a boot image. It is recommended to thoroughly understand and review the script before using it.
