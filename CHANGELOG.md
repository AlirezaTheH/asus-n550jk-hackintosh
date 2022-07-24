# Changelog
All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
OpenCore `0.8.0`
macOS Monterey `12.3`
BIOS `N550JKAS.208`

### Added
- Added `ForceAquantiaEthernet` to `Kernel` > `Quirks` for Aquantia AQtion
  AQC-107s based 10GbE network cards support
- Added `Misc` > `Serial` section to customise serial port properties
- Added `CustomPciSerialDevice` to `Kernel` > `Quirks` for XNU to correctly
  recognise customised external serial devices
All according to OpenCore `0.8.0` release notes

### Changed
- OpecCore to `0.8.0`
- macOS to `12.3`
- AppleALC to `1.7.1`
- CPUFriend to `1.2.5`


## [2.4.0] - 2022-03-09
OpenCore `0.7.9`
macOS Monterey `12.2`
BIOS `N550JKAS.208`

### Added
- Added `LogModules` to `Misc` > `Debug` according to OpenCore `0.7.9` release
  notes

### Changed
- OpecCore to `0.7.9`
- macOS to `12.2`
- AppleALC to `1.7.0`
- VirtualSMC to `1.2.9`
- VoodooPS2 to `2.2.8`
- WhateverGreen to `1.5.8`
- VoodooI2C to `2.7`


## [2.3.0] - 2022-03-09
OpenCore `0.7.8`
macOS Monterey `12.2`
BIOS `N550JKAS.208`

### Changed
- OpecCore to `0.7.8`
- macOS to `12.2`
- Lilu to `1.6.0`
- AppleALC to `1.6.9`
- WhateverGreen to `1.5.7`
- itlwm to `2.1.0`


## [2.2.0] - 2022-01-26
OpenCore `0.7.7`
macOS Monterey `12.1`
BIOS `N550JKAS.208`

### Added
- Added pointer polling period tuning setting in `UEFI` > `AppleInput`
  according to OpenCore `0.7.7` release notes

### Changed
- Replaced `AudioOut` with `AudioOutMask` in `UEFI` > `Audio`
- Separated settings for minimum audio assist volume and minimum audible volume
  in `UEFI` > `Audio` according to OpenCore `0.7.7` release notes
- OpecCore to `0.7.7`
- Lilu to `1.5.9`
- AppleALC to `1.6.8`
- WhateverGreen to `1.5.6`


## [2.1.0] - 2021-12-07
OpenCore `0.7.6`
macOS Monterey `12.0.1`
BIOS `N550JKAS.208`

### Added
- Added `ReconnectGraphicsOnConnect` to `UEFI` > `Output`
- Added `EnableVmx` to `UEFI` > `Quirks`
  All according to OpenCore `0.7.6` release notes

### Changed
- OpecCore to `0.7.6`
- Lilu to `1.5.8`
- AppleALC to `1.6.7`
- VirtualSMC to `1.2.8`


## [2.0.1] - 2021-11-18
OpenCore `0.7.5`
macOS Monterey `12.0.1`
BIOS `N550JKAS.208`

### Changed
RealtekRTL8111 to `2.4.2`


## [2.0.0] - 2021-11-02
OpenCore `0.7.5`
macOS Monterey `12.0.1`
BIOS `N550JKAS.208`

### Changed
- Replaced Qualcomm Atheros AR9485 with Intel(R) Dual Band Wireless N 7260
  because Atheros cards are no longer supported in Monterey
- Changed SMBIOS to `MacBookPro11,4`, because only `MacBookPro11,4` and newer
  MacBookPros are supported in Monterey
- macOS to `12.0.1`
- OpecCore to `0.7.5`
- Lilu to `1.5.7`
- AppleALC to `1.6.6`
- VirtualSMC to `1.2.7`
- VoodooPS2 to `2.2.7`
- WhateverGreen to `1.5.5`

### Removed
- Removed FakePCIID kexts due to a shutdown bug in Monterey


## [1.8.0] - 2021-10-06
OpenCore `0.7.4`
macOS Big Sur `11.6`
BIOS `N550JKAS.208`

### Changed
- OpecCore to `0.7.4`
- AppleALC to `1.6.5`
- VoodooPS2 to `2.2.6`
- WhateverGreen to `1.5.4`


## [1.7.1] - 2021-09-15
OpenCore `0.7.3`
macOS Big Sur `11.6`
BIOS `N550JKAS.208`

### Added
- Added Light Sensor support

### Changed
- macOS to `11.6`

### Fixed
- Fixed keyboard backlight


## [1.7.0] - 2021-09-07
OpenCore `0.7.3`
macOS Big Sur `11.5.2`
BIOS `N550JKAS.208`

### Added
- Added `ForceOcWriteFlash` to `UEFI` > `Quirks` according to OpenCore `0.7.3`
  release notes

### Changed
- Improved SSDT-PNLF compatibility with CFL+ graphics according to OpenCore
  `0.7.3` release notes
- Updated config.plist structure to support Driver arguments according to
  OpenCore `0.7.3` release notes
- macOS to `11.5.2`
- OpecCore to `0.7.3`
- Lilu to `1.5.6`
- AppleALC to `1.6.4`
- VirtualSMC to `1.2.7`
- VoodooPS2 to `2.2.5`
- WhateverGreen to `1.5.3`


## [1.6.0] - 2021-08-03
OpenCore `0.7.2`
macOS Big Sur `11.5.1`
BIOS `N550JKAS.208`

### Added
- Added `GraphicsInputMirroring` to `UEFI` > `AppleInput` according to OpenCore
  `0.7.2` release notes

### Changed
- Improved SSDT-PNLF compatibility with Windows according to OpenCore `0.7.2`
  release notes
- OpecCore to `0.7.2`
- Lilu to `1.5.5`
- AppleALC to `1.6.3`
- VirtualSMC to `1.2.6`
- WhateverGreen to `1.5.2`


## [1.5.0] - 2021-07-29
OpenCore `0.7.1`
macOS Big Sur `11.5.1`
BIOS `N550JKAS.208`

### Added
- Added `SyncTableIds` to  `ACPI` > `Quirks` according to OpenCore `0.7.1`
  release notes

### Changed
- macOS to `11.5.1`
- OpecCore to `0.7.1`
- Lilu to `1.5.4`
- AppleALC to `1.6.2`
- VirtualSMC to `1.2.5`
- VoodooPS2 to `2.2.4`
- WhateverGreen to `1.5.1`
- CPUFriend to `1.2.4`



## [1.4.0] - 2021-06-09
OpenCore `0.7.0`
macOS Big Sur `11.4`
BIOS `N550JKAS.208`

### Added
- Added `ProvideCurrentCpuInfo` to  `Kernel` > `Quirks`
- Added `Flavour` to `Misc` > `Entries` and `Misc` > `Tools`
- Added `AppleEg2Info` to `UEFI` > `ProtocolOverrides`
- Added `AllowToggleSip` to `Misc` > `Security`
All according to OpenCore `0.7.0` release notes


### Changed
- Replaced `AdviseWindows` with `AdviseFeatures`  in `PlatformInfo` > `Generic`
- macOS to `11.4`
- OpecCore to `0.7.0`
- VirtualSMC to `1.2.4`
- AppleALC to `1.6.1`
- WhateverGreen to `1.5.0`



## [1.3.0] - 2021-05-05
OpenCore `0.6.9`
macOS Big Sur `11.3.1`
BIOS `N550JKAS.208`

### Added
- Added `ForgeUefiSupport` and `ReloadOptionRoms` to `UEFI` > `Quirks`
  according to OpenCore `0.6.9` release notes

### Changed
- macOS to `11.3.1`
- OpecCore to `0.6.9`
- VirtualSMC to `1.2.3`
- AppleALC to `1.6.0`
- VoodooPS2 to `2.2.3`
- Lilu to `1.5.3`


## [1.2.0] - 2021-04-06
OpenCore `0.6.8`
macOS Big Sur `11.2.3`
BIOS `N550JKAS.208`

### Changed
- Moved `AppleEvent`, `KeyInitialDelay` and `KeySubsequentDelay` from
  `UEFI` > `Input` to `UEFI` > `AppleInput` according to OpenCore `0.6.8`
  release notes
- Increased `KeySubsequentDelay` from `1` to `5` according to OpenCore `0.6.8`
  new `Sample.plist`
- macOS to `11.2.3`
- OpenCore to `0.6.8`
- VirtualSMC to `1.2.2`
- AppleALC to `1.5.9`
- WhateverGreen to `1.4.9`
- AthBluetoothFirmware to `1.1.0`


## [1.1.0] - 2021-03-02
OpenCore `0.6.7`
macOS Big Sur `11.2.2`
BIOS `N550JKAS.208`

### Added
- Added new `SSDT-Swap-CommandOption.aml` according to VoodooPS2 `2.1.9`
  release notes

### Changed
- OpenCore to `0.6.7`
- VirtualSMC to `1.2.1`
- AppleALC to `1.5.7`
- VoodooI2C to `2.6.5`
- VoodooPS2 to `2.2.2`
- WhateverGreen to `1.4.8`

### Removed
- Removed `KeyMergeThreshold` according to OpenCore `0.6.7` release notes

### Fixed
- Fixed comments for all ACPI patches.
- Fixed comments for all ACPI SSDTs in `Add` section.


## [1.0.1] - 2021-02-28
OpenCore `0.6.6`
macOS Big Sur `11.2`
BIOS `N550JKAS.208`

### Fixed
- Missing Wi-Fi kexts added


## [1.0.0] - 2021-02-25
OpenCore `0.6.6`
macOS Big Sur `11.2`
BIOS `N550JKAS.208`

[Unreleased]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.4.0...HEAD
[2.4.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.8.0...v2.0.0
[1.8.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.7.1...v1.8.0
[1.7.1]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.7.0...v1.7.1
[1.7.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/alirezatheh/asus-n550jk-hackintosh/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/alirezatheh/asus-n550jk-hackintosh/releases/tag/v1.0.0
