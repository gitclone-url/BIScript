# Advisory:

Kindly be informed that the initial execution of the script on your Termux may necessitate a certain duration. This is due to the requirement for the script to perform package updates and upgrades as part of the initial setup process. Additionally, the installation of Python 3 is necessary, as it is a prerequisite for running the main BootSigner script.

*************************************************

**Requirements:**

• Ensure an active internet connection is available for the initial setup to update and upgrade packages.
  
**Script Running Steps:**

1. Copy the entire BIScript folder to the internal storage of your device.

2. Apply the Magisk patch to the boot image.

3. Move the Magisk-patched boot.img to the BIScript folder, and make sure to rename it to 'boot.img'.

4. Open Termux and grant storage permissions.

5. Navigate to the BIScript folder using the following command:
   ```
   cd /storage/emulated/0/BIScript
   ```

6. Make the bash script executable with the following command:
   ```
   chmod +x BIScript.sh
   ```

7. Execute the script using the following command:
   ```
   bash BIScript.sh
   ```

8. Wait for a few minutes to allow the main script to start.

*************************************************
