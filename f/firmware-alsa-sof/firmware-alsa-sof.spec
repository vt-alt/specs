%global _firmwarepath  /lib/firmware
Summary: Firmware and topology files for Sound Open Firmware project
Name: firmware-alsa-sof
Version: 1.4.2
Release: alt1
# See later in the spec for a breakdown of licensing
License: BSD
Group: Sound
Url: https://github.com/thesofproject/sof-bin
Source: %name-%version.tar
Provides: alsa-sof-firmware = %EVR
# noarch, since the package is firmware
BuildArch: noarch

%description
This package contains the firmware binaries for the Sound Open Firmware project.

%package debug
Requires: alsa-sof-firmware
Summary: Debug files for Sound Open Firmware project
Group: Sound

%description debug
This package contains the debug files for the Sound Open Firmware project.

%prep
%setup

# add missing symlink
ln -s v1.4.2/intel-signed/sof-cnl-v1.4.2.ri lib/firmware/intel/sof/sof-cml.ri

%build
%install
mkdir -p  %buildroot%_firmwarepath
ROOT=%buildroot ./go.sh
# remove NXP firmware files
rm -rf %buildroot%_firmwarepath/nxp

# gather files and directories
FILEDIR=$(pwd)
pushd %buildroot/%_firmwarepath
find -P . -name "*.ri" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.tplg" | sed -e '/^.$/d' >> $FILEDIR/alsa-sof-firmware.files
find -P . -name "*.ldc" | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.debug-files
find -P . -type d | sed -e '/^.$/d' > $FILEDIR/alsa-sof-firmware.dirs
popd
sed -i -e 's:^./::' alsa-sof-firmware.{files,debug-files,dirs}
sed -i -e 's!^!/lib/firmware/!' alsa-sof-firmware.{files,debug-files,dirs}
sed -e 's/^/%%dir /' alsa-sof-firmware.dirs >> alsa-sof-firmware.files
cat alsa-sof-firmware.files

%files -f alsa-sof-firmware.files
%doc LICENCE*  README*

%dir %_firmwarepath/intel

# Licence: 3-clause BSD
# .. for files with suffix .tplg
%_firmwarepath/intel/sof-tplg

# Licence: SOF (3-clause BSD plus others)
# .. for files with suffix .ri

%files debug -f alsa-sof-firmware.debug-files

%changelog
* Mon Apr 27 2020 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- first build for ALT, based on Fedora package

