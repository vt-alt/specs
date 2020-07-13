Name:     control-sshd-permit-root-login
Version:  0.0.1
Release:  alt1

Summary:  Control rules for the OpenSSH server PermitRootLogin option
License:  GPLv2+
Group:    System/Servers
Requires: control

BuildArch: noarch

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

%description
This package contains control rules for OpenSSH server PermitRootLogin option.
See control(8) for details.

%prep
%setup

%install
install -pD -m755 sshd-permit-root-login.control \
    %buildroot%_controldir/sshd-permit-root-login

%pre
%pre_control sshd-permit-root-login

%post
%post_control -s default sshd-permit-root-login

%files
%attr(755,root,root) %_controldir/*

%changelog
* Mon Jul 06 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.0.1-alt1
- Create package
