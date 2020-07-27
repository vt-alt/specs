Summary: Simple wrapper to quickly run systemd-nspawn containers
Name: snr
License: MIT
Group: System/Base
Url: https://github.com/mikhailnov/snr
Version: 1.7
Release: alt1
Source0: %name-%version.tar
BuildArch: noarch
BuildRequires: md2man
Requires: systemd-container
Requires: coreutils iproute2 binutils grep gawk sed

%description
Simple wrapper to quickly run systemd-nspawn containers with support to:
- run graphical applications inside container
- have full access to videocard
- have working sound input and output
- bind to network bridge
- specify any other options for systemd-nspawn

%prep
%setup -q

%build
:

%install
%makeinstall_std

%files
%doc README.md
%_bindir/snr
%_man1dir/snr.1*
%config(noreplace) %_sysconfdir/snr.conf


%changelog

* Wed Jul 15 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.7-alt1
- Version 1.7:
  - Fixed setting environmental variables by scripts in /etc/profile.d/

* Mon Mar 09 2020 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.6-alt1
- Version 1.6:
  - Fixed parsing pactl output
  - Some rafactoring
  - Extended documentation

* Thu Nov 20 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.5-alt2
- Explicitly require binutils and gawk, AutoReq failed to detect them

* Thu Nov 14 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.5-alt1
- Fixed parsing pactl output

* Mon Oct 21 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.4-alt1
- Version 1.4:
  - Workaround white screen in Qt4 GUIs in chroot

* Mon Jun 10 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.3-alt1
- Version 1.3:
  - Explicitly require iproute2 (shell.req does not detect its necessity)
  - Removed hardcoded binding of /mnt/dev (forgot to remove it)
  - Added bind_options and other_options to config
  - Echo help/man when called without arguements or with --help (-h)
  - Parse all CLI arguements earlier to prevent doing unneeded actions
  - Check that target directory looks like an OS tree
  - Append sbin to PATH when ip utility was not found

* Sun Jun 09 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.2-alt1
- Version 1.2:
  - Accept absolute path to rootfs dir

* Sun Jun 09 2019 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.1-alt1
- Initial build for ALT Linux

