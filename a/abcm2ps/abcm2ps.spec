Name: abcm2ps
Version: 8.14.4
Release: alt1
Summary: a program to typeset abc tunes into Postscript
License: GPL
Url: http://moinejf.free.fr
Group: File tools

Source: v%version.tar.gz

%description
abcm2ps is a package which converts music tunes from ABC format to
PostScript. Based on abc2ps version 1.2.5, it was developped mainly to print
barock organ scores which have independant voices played on one or many
keyboards and a pedal-board. abcm2ps introduces many extensions to the ABC
language that make it suitable for classical music.

%prep
%setup

%build
%configure --enable-a4
%make_build

%install
%makeinstall docdir=%buildroot%_docdir
rm -rf %buildroot%_docdir/%name/

%files
%doc *.md *.abc *.eps *.html
%_bindir/abcm2ps
%_datadir/abcm2ps/
%_man1dir/*

%changelog
* Tue May 28 2019 Fr. Br. George <george@altlinux.ru> 8.14.4-alt1
- Autobuild version bump to 8.14.4

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 7.8.14-alt1
- Autobuild version bump to 7.8.14

* Wed Jan 28 2015 Fr. Br. George <george@altlinux.ru> 7.8.13-alt1
- Autobuild version bump to 7.8.13

* Sat Oct 04 2014 Fr. Br. George <george@altlinux.ru> 7.8.8-alt1
- Autobuild version bump to 7.8.8

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 5.9.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Jan 09 2009 Yuri Fil <yurifil@altlinux.org> 5.9.3-alt1
- new version of abcm2ps

