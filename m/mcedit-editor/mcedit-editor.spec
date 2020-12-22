Name: mcedit-editor
Version: 0.1
Release: alt1

Group: System/Configuration/Other
Summary: Set EDITOR environment variable to mcedit by default
License: GPL

BuildArch: noarch

Requires: /usr/bin/mcedit

Source0: mcedit-editor.sh
Source1: mcedit-editor.csh


%description
Set EDITOR environment variable to mcedit by default

%prep

%install
install -D -m 0755 %SOURCE0 %buildroot/%_sysconfdir/profile.d/mcedit-editor.sh
install -D -m 0755 %SOURCE1 %buildroot/%_sysconfdir/profile.d/mcedit-editor.csh

%files
%config(noreplace) %_sysconfdir/profile.d/mcedit-editor.sh
%config(noreplace) %_sysconfdir/profile.d/mcedit-editor.csh

%changelog
* Wed Dec 16 2020 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
