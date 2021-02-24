# Asus N550JK Hackintosh
A collection of all resources needed to run macOS on a Asus N550JK

# Specifications
- **Processor**: Intel i7 4710HQ                    
- **Integrated Graphics**: Intel® HD Graphics 4600
- **Dedicated Graphics**: NVIDIA GeForce GTX 850M (Disabled)
- **Ethernet**: Realtek 8111G
- **Audio**: Realtek ALC668
- **Memory**: 16 GB
- **Wi-Fi and Bluetooth**: Qualcomm Atheros AR9485
- **Touchpad**: Elan
- **BIOS Version**: N550JK.208
- **Bootloader**: [OpenCore](https://github.com/acidanthera/OpenCorePkg)

## Overview
This is more of a compilation of information and configs from various repositories and forums than a place where real development happens. This repository should contain everything needed to get macOS up and running on your specific Asus N550JK configuration.


## Current Status
- [x] Intel® HD Graphics 4600
- [x] HDMI Output (Not tested)
- [x] Mini Display Port Output (Not tested)
- [x] Audio Internal Speakers
- [x] Internal microphone
- [x] ComboJack Headphones
- [x] HDMI Audio Output (Not tested)
- [x] Mini DisplayPort Audio Output (Not tested)
- [x] Sleep / Wake also with lid
- [x] PS2 Touchpad with gesture
- [x] Keyboard (PS2-Internal) with backlight
- [x] F3 and F4 Backlight Keys
- [x] F5 and F6 Brightness Keys
- [x] F10, F11 and F12 Audio Keys
- [x] Wi-Fi and Bluetooth
- [x] Ethernet
- [x] WebCam (USB-Internal)
- [x] Touch Screen
- [x] All Sensors
- [x] ACPI Battery
- [x] NVRAM (Native)
- [x] Recovery (macOS) boot from OpenCore
- [ ] ComboJack Microphone
- [ ] Micro SD Card Reader (USB-Internal)
- [ ] NVIDIA GeForce GTX 850M


## Installation
Follow this guide if you have never set up a Hackintosh before.

### USB Creation
To start you need a USB flash drive with at least 16 GB of available storage. Then you can follow [this](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/) section from [dortania](https://github.com/dortania)'s guide to create your bootable USB.

### Configuring EFI
Clone this repository to get the base EFI folder as well as all additional kexts and patches. If your hardware differs with mine you should modify EFI folder for your exact hardware configuration. Once everything is configured properly, copy the folder into the EFI partition you have mounted in the previous step.

### Before Installation
#### BIOS Setting
- Advanced:
	- Wake On Lid Open **[ENABLED]**
	- Intel Virtualization Technology **[ENABLED]**
	- Intel AES-NI **[ENABLED]**
	- VT-d **[DISABLED]**
	- SATA Configuration:
		- SATA mode selection **[AHCI]**
	- Graphics configuration:
		- DMVT Pre-Allocated **[64M]**
	- USB Configuration:
		- Legacy USB Support **[ENABLED]**
		- XHCI Pre-Boot Mode **[ENABLED]**
- Boot:
	- Launch PXE OpROM policy **[DISABLED]**

### Installation Process
After having created the installer USB flash drive, you are ready to install macOS on your laptop. Then you can follow [this](https://dortania.github.io/OpenCore-Install-Guide/installation/installation-process.html) section from [dortania](https://github.com/dortania)'s guide to install your macOS.

### Post Installation
Congratulations! You have successfully booted and installed macOS. At this point, you just need to follow next final steps to complete your installation.

#### BIOS Setting
- In order to get full screen boot resolution, you must replace CsmVideo with HermitCsmVideo developed by Hermit Crab Labs. for this purpose just follow below steps:
	1. Extract your current BIOS using [AMI Firmware Update (AMU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/) > Save.
	2. Open extracted BIOS.rom from previous step using [UEFITool](https://github.com/LongSoft/UEFITool)
	3. Search for CsmVideo and replace the body with HermitCsmVideo.fbd and save.
	4. Open the new BIOS.rom file with AMU and Flash it to your ROM.
- For fixing CFG lock follow [this](https://dortania.github.io/OpenCore-Post-Install/misc/msr-lock.html) section from [dortania](https://github.com/dortania)'s guide


## Issues
### Audio
The headphone jack is buggy. External microphones aren't detected. I've tried 3, 20, 27, 28 for `layout-id` but none of those works. I might fork [ComboJack](https://github.com/lvs1974/ComboJack) in the future and fix it myself or give a try to [AppleALC-ALCPlugFix](https://github.com/athlonreg/AppleALC-ALCPlugFix) or [ALCPlugFix](https://github.com/Menchen/ALCPlugFix).

### Card Reader
Card reader is not detected. I've tried [Sinetek-rtsx](https://github.com/cholonam/Sinetek-rtsx), but no luck. maybe try [this](https://www.noobsplanet.com/index.php?threads/fix-internal-external-card-reader-hackintosh-guide.32/) later.

### Dedicated Graphics
Will never work because of Nvidia Optimus and Apple completely dropped Nvidia support beginning with Mojave. Thus it's completely disabled to save power.


## Credits
- [Apple](https://www.apple.com) for macOS and Xcode
- [Acidanthera](https://github.com/acidanthera) for [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg), [Lilu](https://github.com/acidanthera/Lilu), [AppleALC](https://github.com/acidanthera/AppleALC), [VirtualSMC](https://github.com/acidanthera/VirtualSMC), [VoodooPS2](https://github.com/acidanthera/VoodooPS2), [WhateverGreen](https://github.com/acidanthera/WhateverGreen), [CPUFriend](https://github.com/acidanthera/CPUFriend) and [MaciASL](https://github.com/acidanthera/MaciASL).
- [Pike R. Alpha](https://github.com/Piker-Alpha), [onemanOSX](https://github.com/onemanosx) and [Acidanthera](https://github.com/acidanthera) for [CPUFriendDataProvider](https://www.olarila.com/topic/5693-guide-ssdt-with-pikes-pm-script-and-use-with-cpufriend/)
- [VoodooI2C Team](https://github.com/VoodooI2C/VoodooI2C/graphs/contributors) for [VoodooI2C](https://github.com/VoodooI2C/VoodooI2C)
- [dortania](https://github.com/dortania) for [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)  
- [RehabMan](https://github.com/RehabMan) for [FakePCIID](https://github.com/RehabMan/OS-X-Fake-PCI-ID) and [CodecCommander](https://bitbucket.org/RehabMan/os-x-eapd-codec-commander/src/master/)
- [LynXNU](https://github.com/lynxnu) for [AthBluetoothFirmware](https://github.com/lynxnu/AthBluetoothFirmware)
- [pico joe](https://www.insanelymac.com/forum/profile/1113740-pico-joe/) for [AthWifi](https://www.insanelymac.com/forum/files/file/1008-io80211family-modif/)
- [Hiep Bao Le](https://github.com/hieplpvip) for [AsusSMC](https://github.com/hieplpvip/AsusSMC)
- [ami](https://www.ami.com) for [AMI Firmware Update (AMU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/)
- [LongSoft](https://github.com/LongSoft) for [UEFITool](https://github.com/LongSoft/UEFITool)
- [CorpNewt](https://github.com/corpnewt) for [ProperTree](https://github.com/corpnewt/ProperTree)
- [headzake](https://github.com/headkaze) for [Hackintool](https://github.com/headkaze/Hackintool)
- [fatcatsoftware](https://www.fatcatsoftware.com) for [Plist Edit Pro](https://www.fatcatsoftware.com/plisteditpro/)
- Hermit Crab Labs for HermitCsmVideo
