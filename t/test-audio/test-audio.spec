Name: test-audio
Version: 0.1
Release: alt1

Summary: simple audio test to save keypresses
License: public domain
Group: System/Configuration/Hardware

BuildArch: noarch

%define cmd aplay %_datadir/sounds/alsa/Front_Center.wav

%description
%summary:
%cmd

%prep

%build
cat > %name << EOF
#!/bin/sh
%cmd
EOF

%install
install -pDm755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Tue Dec 17 2019 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release

