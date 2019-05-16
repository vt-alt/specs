Name: firmware-linux
Version: 20190514
Release: alt1

Summary: Firmware files used by the Linux kernel
License: GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
Group: System/Kernel and hardware

Url: git://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch
Provides: linux-firmware
Provides: firmware-iwl1000 
Provides: firmware-iwl3945 firmware-iwl4965 firmware-iwl5000 firmware-iwl5150 
Provides: firmware-iwl6000 firmware-iwl6050 
Obsoletes: firmware-iwl1000 
Obsoletes: firmware-iwl3945 firmware-iwl4965 firmware-iwl5000 firmware-iwl5150 
Obsoletes: firmware-iwl6000 firmware-iwl6050 
Provides:  firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870 firmware-rt3090
Obsoletes: firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870 firmware-rt3090
Provides: firmware-rt61pci firmware-rt73usb
Obsoletes: firmware-rt61pci firmware-rt73usb
Obsoletes: firmware-libertas-sd8686 firmware-libertas-usb8388
Provides: firmware-ql2100 firmware-ql2200 firmware-ql2300 firmware-ql2322 firmware-ql2400 firmware-ql2500
Obsoletes: firmware-ql2100 firmware-ql2200 firmware-ql2300 firmware-ql2322 firmware-ql2400 firmware-ql2500
Provides: firmware-amd-ucode
Obsoletes: firmware-amd-ucode <= 2.0

Requires: udev
AutoReqProv: no

%add_verify_elf_skiplist /lib/firmware/*

%description
Kernel-firmware includes firmware files
required for some devices to operate.

%prep
%setup -n %name-%version 
%patch -p1

%build
## *TODO* check these too
rm -rf ess korg sb16 yamaha

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm *spec

%install
mkdir -p %buildroot/lib/firmware
cp -a * %buildroot/lib/firmware
rm %buildroot/lib/firmware/{WHENCE,LICENCE.*,*.py}

%files
%doc WHENCE LICEN?E.*
/lib/firmware/*

%changelog
* Thu May 16 2019 Cronbuild Service <cronbuild@altlinux.org> 20190514-alt1
- upstream changes (GIT 711d329):
  + Update firmware file for Intel Bluetooth 8265 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + amlogic: add video decoder firmwares (thx Maxime Jourdan)
  + iwlwifi: update -46 firmwares for 22260 and 9000 series (thx Luca Coelho)
  + iwlwifi: add firmware for 22260 and update 9000 series -46
    firmwares (thx Luca Coelho)
  + iwlwifi: add -46.ucode firmwares for 9000 series (thx Luca Coelho)

* Wed May 08 2019 Cronbuild Service <cronbuild@altlinux.org> 20190429-alt1
- upstream changes (GIT 92e17d0):
  + amdgpu: update vega20 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update vega12 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update vega10 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update polaris11 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update polaris10 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update raven2 to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update raven to the latest 19.10 firmware (thx Alex Deucher)
  + amdgpu: update picasso to the latest 19.10 firmware (thx Alex Deucher)
  + update fw for qat devices (thx Giovanni Cabiddu)
  + Mellanox: Add new mlxsw_spectrum firmware 13.2000.1122 (thx Ido Schimmel)

* Thu Apr 25 2019 Cronbuild Service <cronbuild@altlinux.org> 20190424-alt1
- upstream changes (GIT 4b6cf2b):
  + drm/i915/firmware: Add ICL HuC v8.4.3238 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add ICL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add GLK HuC v03.01.2893 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add GLK GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add KBL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add SKL GuC v32.0.3 (thx Anusha Srivatsa)
  + drm/i915/firmware: Add BXT GuC v32.0.3 (thx Anusha Srivatsa)

* Wed Apr 10 2019 Cronbuild Service <cronbuild@altlinux.org> 20190409-alt1
- upstream changes (GIT 260cb35):
  + Add firmware file for Intel Bluetooth 22161 (thx Amit K Bag)
  + cxgb4: update firmware to revision 1.23.4.0 (thx Vishal Kulkarni)
  + Update NXP Management Complex firmware to version 10.14.3 (thx Cristian Sovaiala)

* Thu Apr 04 2019 Cronbuild Service <cronbuild@altlinux.org> 20190326-alt1
- upstream changes (GIT 67b7579):
  + add firmware for MT7615E (thx Ryder Lee)
  + mediatek: update MT8173 VPU firmware to v1.1.2 [decoder] Enlarge
    struct vdec_pic_info to support more capture buffer plane and
    capture buffer format change. (thx Yunfei Dong)
  + update Marvell 8797/8997 firmware images (thx Ganapathi Bhat)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.23 (thx Louis Peens)

* Wed Mar 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190314-alt1
- upstream changes (GIT 7bc2464):
  + cxgb4: update firmware to revision 1.23.3.0 (thx Vishal Kulkarni)
  + Update firmware file for Intel Bluetooth 8265 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth 9560 (thx Amit K Bag)

* Tue Mar 12 2019 Cronbuild Service <cronbuild@altlinux.org> 20190308-alt1
- upstream changes (GIT b0d9583):
  + drm/amdgpu: update picasso to latest from 18.50 branch (thx Alex Deucher)
  + drm/amdgpu: update polaris12 to latest from 18.50 branch (thx Alex Deucher)
  + drm/amdgpu: update vega20 to latest from 18.50 branch (thx Alex Deucher)
  + rtw88: RTL8822C: update rtw8822c_fw.bin to v5.0 (thx Yan-Hsuan Chuang)
  + rtl_bt: Update firmware for BT part of RTL8822C (thx Larry Finger)
  + update Marvell 8787/8801/8887 firmware images (thx Ganapathi Bhat)
  + update Marvell 8897/8997 firmware images (thx Ganapathi Bhat)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.16.1 (thx Louis Peens)
  + QCA: Add the fw files for BT Chip QCA6174. (thx Balakrishna Godavarthi)

* Sun Feb 24 2019 Cronbuild Service <cronbuild@altlinux.org> 20190221-alt1
- upstream changes (GIT 54b0a74):
  + WHENCE: Correct errant entries (thx Josh Boyer)
  + amdgpu: update raven2 rlc firmware (thx Alex Deucher)
  + amdgpu: drop raven2_sdma1.bin (thx Alex Deucher)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + qca: Add firmware files for BT chip wcn3990. (thx Balakrishna Godavarthi)

* Mon Feb 18 2019 Cronbuild Service <cronbuild@altlinux.org> 20190213-alt1
- upstream changes (GIT 710963f):
  + nvidia: add TU10x typec controller firmware (thx Ajay Gupta)
  + bnx2x: Add FW 7.13.11.0. (thx Rahul Verma)
  + amdgpu: add firmware for vega20 from 18.50 (thx Alex Deucher)
  + amdgpu: bump year on license (thx Alex Deucher)
  + update Marvell PCIe-USB8997 firmware image (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image (thx Ganapathi Bhat)
  + add Marvell SD8977 firmware image (thx Ganapathi Bhat)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.9.0.2-00021 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00043 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to
    10.4-3.9.0.2-00024 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)

* Sun Jan 20 2019 Cronbuild Service <cronbuild@altlinux.org> 20190118-alt1
- upstream changes (GIT a8b75ca):
  + brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+ (thx Matthias Brugger)
  + brcm: Fix filename for BCM43430 NVRAM for the Raspberry Pi 3
    Model B (thx Matthias Brugger)
  + amdgpu: add raven2 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: add picasso fw for 18.50 release (thx Alex Deucher)
  + Revert "brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+" (thx Josh Boyer)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + brcm: Add BCM43430 NVRAM for the Raspberry Pi 3 Model B (thx Matthias Brugger)
  + brcm: Add BCM43455 NVRAM for Raspberry Pi 3 B+ (thx Matthias Brugger)
  + update Marvell USB8801 B0 firmware image (thx Ganapathi Bhat)
  + iwlwifi: update firmwares for 9000 series (thx Emmanuel Grumbach)
  + cxgb4: update firmware to revision 1.22.9.0 (thx Arjun Vynipadath)

* Sun Dec 23 2018 Cronbuild Service <cronbuild@altlinux.org> 20181218-alt1
- upstream changes (GIT 0f22c85):
  + Revert "amdgpu: update vega10 fw for 18.50 release" (thx Alex Deucher)
  + brcm: Add 4330 NVRAM for the Prowise PT301 tablet (thx Hans de Goede)
  + brcm: Add 43430 NVRAM for the Chuwi Vi8 Plus tablet (thx Hans de Goede)
  + brcm: Add 43340 based AP6234 NVRAM for the Meegopad T08 HDMI
    stick (thx Hans de Goede)
  + brcm: Add 43430a0 based AP6212 NVRAM for the Jumper EZpad mini
    3 tablet (thx Hans de Goede)
  + brcm: Add 43430a0 based AP6212 NVRAM for the Onda V80 Plus tablet (thx Hans de Goede)
  + brcm: Add 4356 based AP6356 NVRAM for the GPD win handheld (thx Hans de Goede)
  + brcm: Add brcmfmac43362-sdio.lemaker,bananapro.txt symlink (thx Hans de Goede)
  + brcm: Add 43362 based AP6210 NVRAM for the Cubietech Cubietruck (thx Hans de Goede)
  + WHENCE: Put quotes around brcmfmac NVRAM filenames (thx Hans de Goede)
  + check_whence.py: Add support for filenames with spaces in them (thx Hans de Goede)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    part of RTL8723BS (thx Hans de Goede)
  + iwlwifi: update firmwares for 8000 series (thx Emmanuel Grumbach)
  + iwlwifi: add -43.ucode for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update -41.ucode for 9000 series (thx Emmanuel Grumbach)
  + firmware/huc/bxt: Add huC Update for BXT (thx Anusha Srivatsa)

* Mon Dec 17 2018 Cronbuild Service <cronbuild@altlinux.org> 20181107-alt1
- upstream changes (GIT 211de16):
  + brcm: provide new firmwares for BCM4366 chipset (thx Arend van Spriel)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1910.622 (thx Shalom Toledo)
  + cavium: Update firmware for CNN55XX crypto driver (thx Nagadheeraj, Rottela)
  + amdgpu: update vega12 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update vega10 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update raven fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update polaris11 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: update polaris10 fw for 18.50 release (thx Alex Deucher)
  + amdgpu: add firmware for vega12 (thx Alex Deucher)
  + amdgpu: Add new polaris MC firmwares (thx Alex Deucher)
  + amdgpu: Add new polaris SMC firmwares (thx Alex Deucher)
  + Update AMD cpu microcode (thx Allen, John)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.13 (thx Louis Peens)
  + microchip: add firmware for VSC8574 and VSC8584 Ethernet PHYs (thx Quentin Schulz)
  + intel: Update Cannonlake audio firmware. (thx Cezary Rojewski)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.16 (thx Ciaran Toal)
  + cxgb4: update firmware to revision 1.21.5.0 (thx Ganesh Goudar)

* Mon Nov 05 2018 Cronbuild Service <cronbuild@altlinux.org> 20181026-alt1
- upstream changes (GIT 1baa348):
  + qed: Add 8.37.7.0 firmware image (thx Mody, Rasesh)
  + add MC firmware for NXP DPAA2 SoCs (thx Cristian Sovaiala)

* Sun Oct 28 2018 Cronbuild Service <cronbuild@altlinux.org> 20181024-alt1
- upstream changes (GIT 1cb4e51):
  + amdgpu: add raven dmcu firmware (thx Alex Deucher)
  + amdgpu: update raven firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update fiji firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update tonga firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update carrizo firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update polaris10 firmware to 18.40 (thx Alex Deucher)
  + amdgpu: update vega10 firmware to 18.40 (thx Alex Deucher)
  + add firmware for mt7650e (thx Stanislaw Gruszka)
  + liquidio: fix GPL compliance issue (thx Manlunas, Felix)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + add firmware for mt7610e (thx Lorenzo Bianconi)
  + ath10k: QCA9984 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to
    10.4-3.6.0.1-00003 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00041 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.6-00140 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00041 (thx Kalle Valo)
  + ath10k: QCA9377 hw1.0: add firmware-6.bin to
    WLAN.TF.2.1-00021-QCARMSWP-1 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    RM.4.4.1.c2-00057-QCARMSWP-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update firmware-5.bin to 10.4-3.6-00140 (thx Kalle Valo)

* Mon Oct 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20181008-alt1
- upstream changes (GIT c6b6265):
  + rtw88: Add firmware file for driver rtw88 (thx Larry Finger)
  + iwlwifi: add -41.ucode firmwares for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update firmwares for 9000 series (thx Emmanuel Grumbach)
  + iwlwifi: update firmwares for 7000, 8000 and 9000 series (thx Luca Coelho)

* Sun Oct 07 2018 Cronbuild Service <cronbuild@altlinux.org> 20180927-alt1
- upstream changes (GIT 68a4930):
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.37 (thx Louis Peens)
  + nfp: update Agilio SmartNIC firmware to rev 2.1.13 (thx Edwin Peer)
  + ti-connectivity: add firmware for CC2560(A) Bluetooth (thx David Lechner)
  + mediatek: add firmware for mt7668u Bluetooth (thx Sean Wang)
  + nvidia: add GV100 signed firmware (thx Gourav Samaiya)
  + firmware/icl/dmc: Add v1.07 of DMC for Icelake (thx Anusha Srivatsa)
  + add Marvell SD8997 firmware image (thx Ganapathi Bhat)
  + qca: update BT firmware files for QCA ROME chip. (thx Balakrishna Godavarthi)

* Sun Sep 16 2018 Cronbuild Service <cronbuild@altlinux.org> 20180913-alt1
- upstream changes (GIT 44d4fca):
  + brcm: update firmware for bcm43362 sdio (thx Chi-Hsien Lin)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1703.4 (thx Petr Machata)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    part of RTL8822CU (thx Larry Finger)
  + Mellanox: Add new mlxsw_spectrum firmware 13.1703.4 (thx Petr Machata)

* Sun Sep 09 2018 Cronbuild Service <cronbuild@altlinux.org> 20180903-alt1
- upstream changes (GIT 85c5d90):
  + nvidia: switch GP10[2467] to newer scrubber/ACR firmware
    (from GP108) (thx Ben Skeggs)

* Sun Aug 26 2018 Cronbuild Service <cronbuild@altlinux.org> 20180822-alt1
- upstream changes (GIT fea76a0):
  + amdgpu: sync up polaris10 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up polaris12 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up tonga firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.30 release (thx Alex Deucher)
  + amdgpu: sync up fiji firmware with 18.30 release (thx Alex Deucher)
  + add firmware for mhdp8546 (thx Damian Kos)
  + qed: Add firmware 8.37.7.0 (thx Rahul Verma)

* Sun Aug 19 2018 Cronbuild Service <cronbuild@altlinux.org> 20180730-alt1
- upstream changes (GIT f1b95fe):
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + add firmware for mt76x0 (thx Stanislaw Gruszka)
  + qcom: update venus firmware files for v5.2 (thx Vikash Garodia)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.31 (thx Louis Peens)

* Sun Aug 05 2018 Cronbuild Service <cronbuild@altlinux.org> 20180728-alt1
- upstream changes (GIT 7b5835f):
  + add firmware for mt76x2u (thx Lorenzo Bianconi)
  + wl18xx: update firmware file 8.9.0.0.79 (thx Guy Mishol)

* Sun Jul 29 2018 Cronbuild Service <cronbuild@altlinux.org> 20180722-alt1
- upstream changes (GIT b01151b):
  + Mellanox: Add new mlxsw_spectrum firmware 13.1702.6 (thx Nir Dotan)
  + WHENCE: Remove reference to amdgpu/vegam_me_2.bin (thx Josh Boyer)
  + mediatek: add MT7622 Bluetooth firmwares and license file (thx Sean Wang)
  + brcm: add 43430 based AP6212 and 1DX NVRAM (thx Ryan Harkin)
  + update Marvell USB8801 B0 firmware image (thx Ganapathi Bhat)

* Mon Jul 23 2018 Cronbuild Service <cronbuild@altlinux.org> 20180710-alt1
- upstream changes (GIT 8d69bab):
  + amdgpu: update copyright date (thx Alex Deucher)
  + amdgpu: add initial VegaM firmware (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris12 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up polaris10 firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up verde firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up pitcairn firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up tahiti firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up oland firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up hainan firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up kaveri firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up mullins firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up kabini firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up hawaii firmware with 18.20 release (thx Alex Deucher)
  + amdgpu: sync up bonaire firmware with 18.20 release (thx Alex Deucher)
  + WHENCE: Fix typo Version (thx Sedat Dilek)

* Sun Jul 15 2018 Cronbuild Service <cronbuild@altlinux.org> 20180706-alt1
- upstream changes (GIT 6213586):
  + cxgb4: update firmware to revision 1.20.8.0 (thx Ganesh Goudar)

* Mon Jun 11 2018 Cronbuild Service <cronbuild@altlinux.org> 20180606-alt1
- upstream changes (GIT d114732):
  + brcm: update firmware for bcm4356 pcie (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm4354 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43362 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43340 sdio (thx Chi-Hsien Lin)
  + brcm: update firmware for bcm43430 sdio (thx Chi-Hsien Lin)
  + amdgpu: update vega10 VCE firmware to version 55.3 (thx Alex Deucher)
  + Update firmware patch for Intel Bluetooth 7265 (D0) (thx Amit K Bag)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + qcom: add venus firmware files for v5.2 (thx Vikash Garodia)

* Sun May 27 2018 Cronbuild Service <cronbuild@altlinux.org> 20180524-alt1
- upstream changes (GIT 7518922):
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + qed: Add firmware 8.37.2.0 (thx Rahul Verma)

* Sun May 20 2018 L.A. Kostis <lakostis@altlinux.ru> 20180518-alt1
- upstream changes (GIT 2a9b2cf):
  + amd-ucode: delete conflicting ucode
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 7260 (B5/B6) (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 7260 (B3/B4) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Update AMD cpu microcode (thx Sherry Hurwitz)
  + amdgpu: sync up polaris12 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up polaris11 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up polaris10 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up vega10 firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up carrizo firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up topaz firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up stoney firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up tonga firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up fiji firmware with 18.10 release (thx Alex Deucher)
  + amdgpu: sync up raven firmware with 18.10 release (thx Alex Deucher)
  + nfp: Add symlink for Agilio CX 1x40GbE flower firmware (thx Louis Peens)
  + nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.9.A.16 (thx Louis Peens)
  + liquidio: update firmware to v1.7.2 (thx Felix Manlunas)
  + update Marvell USB8997 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)

* Sat May 12 2018 Cronbuild Service <cronbuild@altlinux.org> 20180507-alt1
- upstream changes (GIT 8fc2d4e):
  + update Marvell USB8997 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)
  + update Marvell SD8897-B0 firmware image to add WPA2 vulnerability
    fix (thx Ganapathi Bhat)

* Sun May 06 2018 Cronbuild Service <cronbuild@altlinux.org> 20180430-alt1
- upstream changes (GIT 397a604):
  + qed: Add firmware 8.33.12.0 (thx Rasesh Mody)
  + Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + cxgb4: update firmware to revision 1.19.1.0 (thx Ganesh Goudar)
  + nfp: add symlink for mixed mode Agilio CX 2x25GbE cards (thx Louis Peens)
  + nfp: update Agilio SmartNIC flower firmware to rev 5701 (thx Louis Peens)

* Sat Apr 21 2018 Cronbuild Service <cronbuild@altlinux.org> 20180409-alt1
- upstream changes (GIT b562d2f):
  + update wil6210 firmware to 5.2.0.18 (thx Maya Erez)
  + rsi: update firmware images for Redpine 9113 chipset (thx Amitkumar Karwar)
  + iwlwifi: update firmwares for 3160, 3168 and 7265 (thx Luca Coelho)
  + iwlwifi: add some new FW versions and update older ones (thx Luca Coelho)

* Sun Apr 08 2018 L.A. Kostis <lakostis@altlinux.ru> 20180329-alt1
- configuration changes:
  +  fix cronbuild
- upstream changes (GIT 8c1e439):
  + amdgpu: update vce firmware for Polaris (thx Alex Deucher)
  + Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + Update firmware patch for Intel Bluetooth 8260 (thx Amit K Bag)
  + nfp: update Agilio SmartNIC firmware to rev 2.0.7 (thx Edwin Peer)
  + cxgb4: update firmware to revision 1.18.9.0 (thx Ganesh Goudar)
  + intel: Update Geminilake audio firmware (thx Sanyog Kale)
  + intel: Update Kabylake audio firmware (thx Sanyog Kale)
  + intel: Update Broxton audio firmware (thx Sanyog Kale)
  + intel: Update Skylake audio firmware (thx Sanyog Kale)

* Tue Mar 27 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt3
- Fixed obsoleted fw list (tnx to mike@ and vseleznv@).

* Wed Mar 21 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt2
- .spec cleanup:
  + added provides/obsoletes for absorbed fw.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 20180319-alt1
- upstream changes (GIT 44476f2):
  + BCM-0bb4-0306: Update to Cypress license in WHENCE (thx kaihsiu_chen)

* Thu Mar 15 2018 L.A. Kostis <lakostis@altlinux.ru> 20180314-alt1
- upstream changes (GIT 4c0bf11):
  + intel: Update Kabylake audio firmware (thx Sanyog Kale)

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 20180227-alt1
- upstream changes (GIT 9cf0ec0):
  + Mellanox: Add new mlxsw_spectrum firmware 13.1620.192 (thx Tal Bar)
  + qed: Add firmware 8.33.11.0 (thx Rahul Verma)
  + BCM-0bb4-0306: Cypress Bluetooth firmware for HTC Vive (thx Kaihsiu Chen)
  + linux-firmware:Update firmware patch for Intel Bluetooth 7265
    (D1) (thx Amit K Bag)
  + qed: Add firmwares 8.20.0.0 8.18.9.0 and 8.14.6.0 (thx Rasesh Mody)
  + iwlwifi: update firmware version 34 for 9000 series (thx Luca Coelho)

* Sat Feb 24 2018 L.A. Kostis <lakostis@altlinux.ru> 20180222-alt1
- configuration changes:
  +  update changelog rules
- upstream changes (GIT 7344ec9):
  + ath10k: QCA9984 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA988X hw2.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9888 hw2.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + ath10k: QCA9887 hw1.0: update firmware-5.bin to 10.2.4-1.0-00037 (thx Kalle Valo)
  + ath10k: QCA9377 hw1.0: update firmware-5.bin to
    WLAN.TF.1.0-00002-QCATFSWPZ-5 (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA6174 hw3.0: update firmware-6.bin to
    WLAN.RM.4.4.1-00079-QCARMSWPZ-1 (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update board-2.bin (thx Kalle Valo)
  + ath10k: QCA4019 hw1.0: update firmware-5.bin to 10.4-3.5.3-00053 (thx Kalle Valo)
  + rtl_bt: Add firmware and configuration files for the Bluetooth
    parts of RTL8821C and RTL8723D (thx Larry Finger)
  + qed: Add firmwares 8.30.12.0 and 8.10.9.0 (thx Rasesh Mody)
  + nfp: update Agilio SmartNIC firmware to rev 2.0.4 (thx Edwin Peer)

* Fri Feb 02 2018 L.A. Kostis <lakostis@altlinux.ru> 20180201-alt1
- configuration changes:
  + changelog.sh: get pkg name from specfile
  + cronbuild: initial config
- upstream changes (GIT 2aa2ac2):
  + linux-firmware: Add firmware file for Intel Bluetooth,9560 (thx Amit K Bag)
  + linux-firmware: Add firmware file for Intel Bluetooth,9260 (thx Amit K Bag)
  + linux-firmware: Update firmware file for Intel Bluetooth,8265 (thx Amit K Bag)
  + wl127x/wl128x: update PLT firmwares (thx Guy Mishol)
  + linux-firmware: intel: Update Kabylake audio firmware (thx Guneshwor Singh)
  + .gear: simplify cronbuild scripts

* Tue Jan 23 2018 Konstantin A. Lepikhov <lakostis@altlinux.ru> 20180118-alt1
- Update 65b1c68 GIT:
  + amdgpu: update uvd firmware for polaris asics (thx Alex Deucher).
  + amdgpu: update vce firmware for Fiji (thx Alex Deucher).
  + amdgpu: update vcn firmware for raven (thx Alex Deucher).
  + amdgpu: update vce and uvd firmware for Vega10 (thx Alex Deucher).
  + mediatek: update MT8173 VPU firmware to 1.0.8 [decoder h264]
    Fix h264 decoder output delay for some low latency bitstreams
    (thx pochun.lin).
  + cxgb4: update firmware to revision 1.17.14.0 (thx Ganesh Goudar).
  + linux-firmware: update Marvell PCIe-USB8897/8997 firmware image
    to add WPA2 vulnerability fix (thx Xinming Hu).
  + LICENSE.nouveau-firmware: added.
  + linux-firmware: intel: Update Geminilake audio firmware
    (thx Pradeep Tewani).

* Sat Jan 13 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.2
- prepare .spec for cronbuild.

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1.1
- amd-ucode: Add microcode_amd_fam17h.bin (bsc#1068032 CVE-2017-5715)

* Fri Jan 05 2018 L.A. Kostis <lakostis@altlinux.ru> 20180104-alt1
- Updated to 65b1c68 GIT.

* Mon Dec 04 2017 Michael Shigorin <mike@altlinux.org> 20171128-alt1
- updated from git

* Mon Oct 30 2017 Michael Shigorin <mike@altlinux.org> 20171009-alt1
- updated from git

* Mon Sep 11 2017 Michael Shigorin <mike@altlinux.org> 20170901-alt1
- updated from git

* Mon Jun 26 2017 Michael Shigorin <mike@altlinux.org> 20170622-alt1
- updated from git

* Mon Jun 05 2017 Michael Shigorin <mike@altlinux.org> 20170531-alt1
- updated from git

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt2
- disable attempts to find R:/P: or ELF bugs automatically

* Mon May 22 2017 Michael Shigorin <mike@altlinux.org> 20170517-alt1
- updated from git

* Wed Mar 22 2017 Michael Shigorin <mike@altlinux.org> 20170314-alt1
- updated from git

* Mon Jan 23 2017 Michael Shigorin <mike@altlinux.org> 20170113-alt1
- updated from git (closes: #33022)

* Tue Nov 15 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt2
- dropped /lib/firmware/check_whence.py (closes: #32754)

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 20160927-alt1
- updated from git

* Wed Aug 03 2016 Michael Shigorin <mike@altlinux.org> 20160728-alt1
- updated from git

* Wed Jun 15 2016 Michael Shigorin <mike@altlinux.org> 20160608-alt1
- updated from git

* Tue Mar 01 2016 Michael Shigorin <mike@altlinux.org> 20160219-alt1
- updated from git

* Tue Feb 16 2016 Michael Shigorin <mike@altlinux.org> 20160216-alt1
- updated from git

* Sun Nov 29 2015 Michael Shigorin <mike@altlinux.org> 20151129-alt1
- updated from git

* Fri Nov 06 2015 Michael Shigorin <mike@altlinux.org> 20151104-alt1
- updated from git

* Thu Sep 10 2015 Michael Shigorin <mike@altlinux.org> 20150824-alt1
- updated from git
  + NB: amdgpu* have arrived (thx lakostis@ for the notice)

* Thu Aug 13 2015 Michael Shigorin <mike@altlinux.org> 20150811-alt1
- updated from git
- dropped Requires: firmware-ipw* (closes: #30308)

* Mon Jun 01 2015 Michael Shigorin <mike@altlinux.org> 20150506-alt1
- updated from git

* Tue Apr 28 2015 Michael Shigorin <mike@altlinux.org> 20150410-alt1
- updated from git

* Fri Dec 26 2014 Michael Shigorin <mike@altlinux.org> 20141222-alt1
- updated from git

* Tue Nov 11 2014 Michael Shigorin <mike@altlinux.org> 20141009-alt1
- updated from git

* Mon Oct 06 2014 Michael Shigorin <mike@altlinux.org> 20140926-alt1
- updated from git

* Tue Sep 30 2014 Michael Shigorin <mike@altlinux.org> 20140902-alt1
- updated from git

* Wed Sep 10 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt2
- add P:/O: firmware-amd-ucode

* Sat Aug 30 2014 Michael Shigorin <mike@altlinux.org> 20140828-alt1
- updated from git

* Wed May 21 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140521-alt1
- updated from git

* Thu Jan 23 2014 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20140123-alt1
- updated from git

* Wed Nov 06 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20131106-alt1
- updated from git

* Wed Sep 04 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130904-alt1
- updated from git

* Thu Jun 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130613-alt1
- updated from git

* Tue Apr 23 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130423-alt1
- updated from git
- added prov/obs firmware-carl9170-1.9.4 firmware-i2400m firmware-rt2870
  firmware-rt3090 (closes #27624)

* Fri Mar 15 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt2
- sources exluded (closes: #28682)

* Wed Mar 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130313-alt1
- updated from git

* Wed Jan 09 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20130109-alt1
- updated from git

* Wed Sep 05 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120905-alt1
- updated from git

* Wed Apr 04 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20120304-alt1
- updated from g.k.o/pub/scm/linux/kernel/git/firmware/linux-firmware.git

* Wed Dec 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20111228-alt1
- updated from git

* Fri Aug 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110819-alt1
- updated from git

* Tue Jul 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110726-alt1
- updated from git

* Fri May 27 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt3
- requires for firmware-ipw* added

* Thu May 26 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt2
- false ipw* provedes/obsoletes deleted (closes #25669)

* Fri May 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110520-alt1
- updated from git
- iwl* included and provided/obsoleted

* Thu Mar 31 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110331-alt1
- updated from git

* Fri Jan 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20110114-alt1
- updated from git

* Fri Dec 17 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20101217-alt1
- updated from git

* Fri Sep 24 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100924-alt1
- updated from git

* Tue Jun 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100629-alt1
- updated from git
- provides of linux-firmware added

* Fri May 21 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20100521-alt1
- build to Sisyphus
- updated from git
- radeon and nouveau added to tree directly

* Mon Apr 12 2010 Michael Shigorin <mike@altlinux.org> 20100106-alt1
- adapted fedora spec for ALT Linux (thanks lakostis@ for proposal)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
