Name: rtcheck
Version: 0.7.7
Release: alt2

License: GPL-2.0-only
Summary: Test the running system for real-time capabilities
Group: Development/Tools
Source: %name-%version.tar

# Upstream research:
#   It seems, the program is supplied by IBM to RedHat directly
#   and then ends up in CentOS. And may be to SUSE too, in ibmrtpkgs-2
#   (IBM Utilities for SLERT) package. No upstream repo is found.

%description
The rtcheck program is an application that tests the running system for
real-time capabilities. If it identifies all capabilities, it will return an
exit code of 0. If some capabilities are not present, it will return with a
non-zero exit code. This program can be used by real-time-enabled programs
to determine if the environment they are in is suitable for them to run
correctly.

%prep
%setup

%build
%make_build rtcheck

%install
install -D %name                   %buildroot%_bindir/%name
install -p -m 755 -D %name.init    %buildroot%_initrddir/%name
install -p -m 644 -D %name.service %buildroot%_unitdir/%name.service

%clean

%files
%doc README
%_bindir/%name
%_initrddir/%name
%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name


%changelog
* Fri Mar 06 2020 Vitaly Chikunov <vt@altlinux.org> 0.7.7-alt2
- rtcheck.service: Update limits.
- Try to `ulimit -l unlimited` on each run.

* Fri Sep 20 2019 Vitaly Chikunov <vt@altlinux.org> 0.7.7-alt1
- Initial import of rtcheck-0.7.7 tarball.
