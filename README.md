<div align="center">
<img src="blob/readme-header-data/images/header-image.svg">
<h1>Asus N550JK Hackintosh</h1>

[![Bootloader](https://badgen.net/badge/Bootloader/OpenCore/cyan?icon=terminal)](https://github.com/acidanthera/OpenCorePkg)
[![macOS](https://badgen.net/badge/macOS/Monterey/purple?icon=apple)](https://www.apple.com/macos/monterey/)

</div>


A collection of all resources needed to run macOS on an Asus N550JK

## Specifications
- **Processor**: Intel i7 4710HQ
- **Integrated Graphics**: Intel® HD Graphics 4600
- **Dedicated Graphics**: NVIDIA GeForce GTX 850M
- **Ethernet**: Realtek 8111G
- **Audio**: Realtek ALC668
- **Memory**: 16 GB
- **Wi-Fi and Bluetooth**: Intel(R) Dual Band Wireless N 7260
- **Touchpad**: Elan

## Overview
This is more of a compilation of information and configs from various
repositories and forums than a place where real development happens. This
repository should contain everything needed to get macOS up and running on your
specific Asus N550JK configuration.


## Current Status
- [x] Intel® HD Graphics 4600
- [x] HDMI Output
- [x] Mini Display Port Output (Not tested)
- [x] Internal Speakers
- [x] Internal Microphone
- [x] Combo Jack Headphones
- [x] Combo Jack Microphone
- [x] HDMI Audio Output
- [x] Mini DisplayPort Audio Output (Not tested)
- [x] Sleep and Wake also with lid
- [x] Touchpad with gestures
- [x] Keyboard with backlight
- [x] F1 Sleep key
- [x] F3 and F4 Backlight keys
- [x] F5 and F6 Brightness keys
- [x] F9 Touchpad key
- [x] F10, F11 and F12 Audio keys
- [x] Wi-Fi and Bluetooth
- [x] Ethernet
- [x] Webcam
- [x] Touchscreen
- [x] All Sensors
- [x] Battery
- [x] NVRAM
- [x] macOS Recovery
- [ ] Card Reader
- [ ] NVIDIA GeForce GTX 850M (Disabled)


## Installation
Follow this guide if you have never set up a Hackintosh before.

### USB Creation
To start you need a USB flash drive with at least 16 GB of available storage.
Then you can follow
[this section](https://dortania.github.io/OpenCore-Install-Guide/installer-guide/)
from [dortania](https://github.com/dortania)'s guide to create your bootable
USB.

### Configuring EFI
Download
[latest release EFI](https://github.com/alirezah320/asus-n550jk-hackintosh/releases/latest)
to get the base EFI folder as well as all additional kexts and patches. If your
hardware differs with mine you should modify EFI folder for your exact hardware
configuration. If you don't know how to do that you should probably learn more
about hackintoshing. you can read
[Dortania's OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)
for start. Once everything is configured properly, copy the folder into the EFI
partition you have mounted in the previous step.

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

#### OpenCore Setting
- Enable `AppleXcpmCfgLock`

### Installation Process
After having created the installer USB flash drive, you are ready to install
macOS on your laptop. Then you can follow
[this section](https://dortania.github.io/OpenCore-Install-Guide/installation/installation-process.html)
from [dortania](https://github.com/dortania)'s guide to install your macOS.

### After Installation
Congratulations! You have successfully booted and installed macOS. At this
point, you just need to follow next final steps to complete your installation.

#### BIOS Setting
- In order to get full screen boot resolution, you must replace `CsmVideo` with
`HermitCsmVideo` developed by Hermit Crab Labs. for this purpose just follow
below steps:
  1. Download
     [latest release BIOS](https://github.com/alirezah320/asus-n550jk-hackintosh/releases/latest)
     to get base requirements. At this point you can just open
     [`N550JKAS.208-modified.rom`](https://github.com/alirezah320/asus-n550jk-hackintosh/blob/main/BIOS/N550JKAS.208-modified.rom)
     with [AMI Firmware Update (AFU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/)
     ,`Flash` it to your ROM, and skip next steps. But we highly
     recommend to follow next steps and modify your own BIOS.
	2. Extract your current BIOS by opening
	   [AMI Firmware Update (AFU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/)
	   and pressing `Save`.
	3. Open extracted `[BIOS].rom` from previous step using
	   [UEFITool](https://github.com/LongSoft/UEFITool)
	4. Search for `CsmVideo` and replace the body with
	   [HermitCsmVideo.fbd](BIOS/HermitCsmVideo.fbd) and save.
	5. Open the new `[BIOS].rom` file with
	   [AMI Firmware Update (AFU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/)
	   and `Flash` it to your ROM.

- For fixing CFG lock follow
[this section](https://dortania.github.io/OpenCore-Post-Install/misc/msr-lock.html)
from [dortania](https://github.com/dortania)'s guide

#### Wi-Fi Setting
Download and install [HeliPort](https://github.com/OpenIntelWireless/HeliPort)
which is Intel Wi-Fi client for
[itlwm](https://github.com/OpenIntelWireless/itlwm).


## Issues

### Audio
Combo Jack is buggy. External microphone is detected, but by default it isn't
active and also not auto switchable. So you need to select it manually in
**System Preferences** and replug it to make it work! I've tried `3`, `20`,
`27`, `28` for `layout-id` but `29` was the best. Then I thought that there is
something wrong with AppleHDA patching and tried to use
[this guide](https://osxlatitude.com/forums/topic/1946-complete-applehda-patching-guide/)
and add a custom codec to [AppleALC](https://github.com/acidanthera/AppleALC),
but that made no difference. I also tried to modify
[ALCPlugFix](https://github.com/Sniki/ALCPlugFix),
[ComboJack](https://github.com/lvs1974/ComboJack) and
[CodecCommander](https://github.com/RehabMan/EAPD-Codec-Commander) for ALC668
but none of them seems to be worked.

### Card Reader
Card Reader is not detected. I've tried
[Sinetek-rtsx](https://github.com/cholonam/Sinetek-rtsx), but no luck. Maybe try
[this](https://www.noobsplanet.com/index.php?threads/fix-internal-external-card-reader-hackintosh-guide.32/)
later.

### Dedicated Graphics
Will never work because of Nvidia Optimus and Apple completely dropped Nvidia
support beginning with Mojave. Thus it's completely disabled to save power.


## Acknowledgements
- [Apple](https://www.apple.com) for macOS and Xcode
- [Acidanthera](https://github.com/acidanthera) for
  [OpenCorePkg](https://github.com/acidanthera/OpenCorePkg),
  [Lilu](https://github.com/acidanthera/Lilu),
  [AppleALC](https://github.com/acidanthera/AppleALC),
  [VirtualSMC](https://github.com/acidanthera/VirtualSMC),
  [VoodooPS2](https://github.com/acidanthera/VoodooPS2),
  [WhateverGreen](https://github.com/acidanthera/WhateverGreen),
  [CPUFriend](https://github.com/acidanthera/CPUFriend),
  [BlueToolFixup](https://github.com/acidanthera/BrcmPatchRAM) and
  [MaciASL](https://github.com/acidanthera/MaciASL)
- [Pike R. Alpha](https://github.com/Piker-Alpha),
  [onemanOSX](https://github.com/onemanosx) and
  [Acidanthera](https://github.com/acidanthera) for
  [CPUFriendDataProvider](https://www.olarila.com/topic/5693-guide-ssdt-with-pikes-pm-script-and-use-with-cpufriend/)
- [VoodooI2C Team](https://github.com/VoodooI2C/VoodooI2C/graphs/contributors) for
  [VoodooI2C](https://github.com/VoodooI2C/VoodooI2C)
- [dortania](https://github.com/dortania) for
  [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/)
- [OpenIntelWireless](https://github.com/OpenIntelWireless) for
  [AthBluetoothFirmware](https://github.com/OpenIntelWireless/IntelBluetoothFirmware),
  [itlwm](https://github.com/OpenIntelWireless/itlwm) and
  [HeliPort](https://github.com/OpenIntelWireless/HeliPort)
- [Hiep Bao Le](https://github.com/hieplpvip) for
  [AsusSMC](https://github.com/hieplpvip/AsusSMC)
- [Laura Müller](https://github.com/Mieze) for
  [RealtekRTL8111](https://github.com/Mieze/RTL8111_driver_for_OS_X)
- [ami](https://www.ami.com) for
  [AMI Firmware Update (AMU)](https://www.ami.com/products/firmware-tools-and-utilities/bios-uefi-utilities/)
- [LongSoft](https://github.com/LongSoft) for
  [UEFITool](https://github.com/LongSoft/UEFITool)
- [CorpNewt](https://github.com/corpnewt) for
  [ProperTree](https://github.com/corpnewt/ProperTree)
- [headzake](https://github.com/headkaze) for
  [Hackintool](https://github.com/headkaze/Hackintool)
- [fatcatsoftware](https://www.fatcatsoftware.com) for
  [Plist Edit Pro](https://www.fatcatsoftware.com/plisteditpro/)
- [mackie100projects](https://mackie100projects.altervista.org) for
  [OpenCore Configurator](https://mackie100projects.altervista.org/opencore-configurator/)
- Hermit Crab Labs for HermitCsmVideo
