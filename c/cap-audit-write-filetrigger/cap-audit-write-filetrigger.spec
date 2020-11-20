Name: cap-audit-write-filetrigger
Version: 0.1
Release: alt1

Summary: Setcaps password checkers CAP_AUDIT_WRITE
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar

%description
Setcaps password checking binaries CAP_AUDIT_WRITE to
allow audit type=USER_AUTH

%prep
%setup

%install
%define tdir /usr/lib/rpm
mkdir -p %buildroot%tdir
install -pm755 *.filetrigger %buildroot%tdir/

%files
%doc README
%tdir/*

%changelog
* Thu Oct 29 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- initial version
