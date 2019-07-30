Name: picolisp
Version: 19.6
Release: alt1

Summary: Interpreted Lisp
License: MIT
Group: Development/Lisp

Url: http://picolisp.com
Source: http://software-lab.de/picoLisp-%version.tgz
Source100: picolisp.watch

# 64-bit build bootstraps using 32-bit one or Java
BuildRequires: java /proc

# trickery inside
%set_verify_elf_method textrel=none

# pretty much hardwired
%define _libdir %_usr/lib

%description
PicoLisp can be viewed from two different aspects:
        as a general purpose programming language,
     and a dedicated application server framework.

%prep
%setup -n picoLisp

%build
if [ %_lib = lib64 ]; then
	cd src64
else
	cd src
fi
make
cd ..

%install
mkdir -p %buildroot{%_bindir,%_libdir/%name,%_datadir}
cp -a bin/{picolisp,pil} %buildroot%_bindir/
# TODO: emacs subpackage
rm -rf lib/el
# lib/ and lib.l
cp -a lib* %buildroot%_libdir/%name/
# as per INSTALL
ln -s ../lib/%name %buildroot%_datadir/%name

%files
%doc CHANGES CREDITS README
%_bindir/*
%_libdir/%name/
%_datadir/%name/

%changelog
* Mon Jul 01 2019 Michael Shigorin <mike@altlinux.org> 19.6-alt1
- new version (watch file uupdate)

* Sat Jan 19 2019 Michael Shigorin <mike@altlinux.org> 18.12-alt2
- fix 64-bitness test

* Sun Dec 30 2018 Michael Shigorin <mike@altlinux.org> 18.12-alt1
- new version (watch file uupdate)

* Thu Jun 28 2018 Michael Shigorin <mike@altlinux.org> 18.6-alt1
- new version (watch file uupdate)

* Tue Dec 26 2017 Michael Shigorin <mike@altlinux.org> 17.12-alt1
- new version (watch file uupdate)

* Thu Jun 29 2017 Michael Shigorin <mike@altlinux.org> 17.6-alt1
- new version (watch file uupdate)

* Thu Dec 08 2016 Michael Shigorin <mike@altlinux.org> 16.12-alt1
- new version (watch file uupdate)

* Wed Jun 29 2016 Michael Shigorin <mike@altlinux.org> 16.6-alt1
- new version (watch file uupdate)

* Thu Feb 18 2016 Michael Shigorin <mike@altlinux.org> 16.2-alt1
- new version (watch file uupdate)

* Tue Nov 24 2015 Michael Shigorin <mike@altlinux.org> 15.11-alt1
- new version (watch file uupdate)

* Mon Jun 22 2015 Michael Shigorin <mike@altlinux.org> 3.1.11-alt1
- new version (watch file uupdate)

* Sat Apr 18 2015 Michael Shigorin <mike@altlinux.org> 3.1.10-alt1
- new version (watch file uupdate)

* Sun Mar 22 2015 Michael Shigorin <mike@altlinux.org> 3.1.9-alt1
- new version (watch file uupdate)

* Wed Oct 01 2014 Michael Shigorin <mike@altlinux.org> 3.1.8-alt1
- new version (watch file uupdate)

* Mon Jun 30 2014 Michael Shigorin <mike@altlinux.org> 3.1.7-alt1
- new version (watch file uupdate)

* Wed Apr 02 2014 Michael Shigorin <mike@altlinux.org> 3.1.6-alt1
- new version (watch file uupdate)

* Thu Jan 02 2014 Michael Shigorin <mike@altlinux.org> 3.1.5-alt1
- new version (watch file uupdate)

* Fri Dec 06 2013 Michael Shigorin <mike@altlinux.org> 3.1.4-alt1
- added watch file
- new version (watch file uupdate)

* Mon Nov 26 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt2
- actually working package for Sisyphus

* Wed Jun 27 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- 3.1.0
- spec based on fedora proposed one (rhbz#783294) and cleaned up

* Thu Jan 19 2012 Kalpa Welivitigoda <callkalpa@gmail.com> - 3.0.9-1
- initial packaging
