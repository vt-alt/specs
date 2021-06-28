Name: mesaflash
Version: 3.4.0
Release: alt1.20210527
Summary: Configuration and diagnostic tool for Mesa Electronics boards
License: GPLv2+
Group: Engineering
Url: https://github.com/LinuxCNC/mesaflash
Source0: %name-%version.tar

# Not available sys/io.h
ExcludeArch: armh ppc64le

BuildRequires: pkgconfig(libpci)

%description
Configuration and diagnostic tool for Mesa Electronics
PCI(E)/ETH/EPP/USB/SPI boards.

%prep
%setup
# Remove binary files
rm -rf *.dll *.sys libpci

%build
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%make_build OWNERSHIP=""

%install
%ifarch i386 x86_64
  export USE_STUBS=0
%else
  export USE_STUBS=1
%endif
%makeinstall DESTDIR="%buildroot%_prefix" OWNERSHIP=""

%files
%doc README.md
%_bindir/%name
%_mandir/man1/*.1*

%changelog
* Sun Jun 13 2021 Anton Midyukov <antohami@altlinux.org> 3.4.0-alt1.20210527
- Initial build
