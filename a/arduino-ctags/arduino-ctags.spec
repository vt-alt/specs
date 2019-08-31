Group: Development/C
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global         extraver        arduino11
Name:           arduino-ctags
Version:        5.8
Release:        alt1_9.%{extraver}
Summary:        A mix of ctags and anjuta-tags for the perfect C++ ctags

License:        GPLv2
URL:            http://arduino.cc
Source0:        https://github.com/arduino/ctags/archive/%{version}-%{extraver}.tar.gz#/ctags-%{version}-%{extraver}.tar.gz

# add support for DESTDIR in make install
Patch0:         ctags-5.7-destdir.patch
# https://github.com/arduino/ctags/issues/14
Patch1:         ctags-CVE-2014-7204.patch

BuildRequires:  gcc
Source44: import.info
%description
An Arduino fork of exuberant ctags

%prep
%setup -q -n ctags-%{version}-%{extraver}
%patch0 -p1
%patch1 -p1

# rename executable and man page
sed -i 's/^CTAGS_PROG =.*/CTAGS_PROG = arduino-ctags/' Makefile.in
sed -i 's/^MANPAGE =.*/MANPAGE = arduino-ctags.1/' Makefile.in

# remove glibc regex bundled copy to ensure it's not used
rm -r gnu_regex

%build
%configure
%make_build


%install
%makeinstall_std DESTDIR=%{buildroot}

%files
%doc --no-dereference COPYING
%doc EXTENDING.html FAQ NEWS README
%{_bindir}/arduino-ctags
%{_mandir}/man1/arduino-ctags.1*


%changelog
* Fri Jul 19 2019 Igor Vlasenko <viy@altlinux.ru> 5.8-alt1_9.arduino11
- aarch64 build

* Sat Nov 04 2017 Igor Vlasenko <viy@altlinux.ru> 5.8-alt1_6.arduino11
- new version

