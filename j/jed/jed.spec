Name: jed
Version: 0.99.19
Release: alt2.qa2.2
Serial: 2

%define srcname %name-0.99-19

Summary: A fast, compact editor based on the slang screen library
Summary(ru_RU.KOI8-R): Небольшой, быстрый текстовый редактор для программистов.
License: GPLv2
Group: Editors
Url: http://www.jedsoft.org/jed/

Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: ftp://ftp.jedsoft.org/pub/davis/jed/v0.99/%srcname.tar.bz2
Source1: %name.conf

# old
#Patch: %name-info.patch
#Patch1: jed-0.99-16-alt-xft.patch

Patch1: jed-0.99.12-xkeys.patch
Patch2: jed-etc.patch
Patch3: jed-multilib-newauto.patch
#Patch4: jed-selinux.patch
Patch5: jed-newauto.patch
Patch6: jed-0.99-18-slutf8.patch

#Patch5: jed-0.99-18-recipe.patch



Requires: %name-common = %{?serial:%serial:}%version-%release

# Automatically added by buildreq on Wed Mar 20 2013
# optimized out: fontconfig fontconfig-devel gnu-config libICE-devel libX11-devel libXrender-devel libfreetype-devel pkg-config xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXft-devel libXt-devel libgpm-devel libncurses-devel libslang2-devel

BuildRequires: /proc
# explicitly added texinfo for info files
BuildRequires: texinfo

%package common
Summary: Files needed by any Jed editor
Summary(ru_RU.KOI8-R): Файлы необходимые для работы текстового редактора JED 
Group: Editors

%package xjed
Summary: The X Window System version of the Jed text editor
Summary(ru_RU.KOI8-R): Редактор JED c поддержкой X Window System
Group: Editors
Requires: %name-common = %{?serial:%serial:}%version-%release

%package -n rgrep
Summary: A grep utility which can recursively descend through directories
Summary(ru_RU.KOI8-R): Рекурсивный вариант утилиты grep
Group: File tools

%description
Jed is a fast, compact editor based on the slang screen library.  Jed
features include emulation of the Emacs, EDT, WordStar and Brief editors;
support for extensive customization with slang macros, colors,
keybindings, etc.; and a variety of programming modes with syntax
highlighting.

%description -l ru_RU.KOI8-R
Быстрый и компактный текстовый редактор для программистов, созданный на основе
библиотеки slang. JED способен эмулировать поведение других популярных
редакторов, таких как Emacs, EDT, WordStar и Brief; с помощью встроеного
скриптового языка реализованны различные дополнительный возможности:
 - синтаксическая подсветка
 - комбинации "горячих" клавиш
 - поддержка различных языков программирования.

%description common
The %name-common package contains files (such as .sl files) that are
needed by any %name binary in order to run.

%description -l ru_RU.KOI8-R common
Пакет %name-common -- платформо-независимая (скриптовая) часть
текстового редактора %name. Содержит исходные тексты и компилированный
байт-код, необходымые для запуска %name.

%description xjed
X%name is a version of the Jed text editor that will work with the X Window
System.

You should install xjed if you like Jed and you'd like to use it with X.
You'll also need to have the X Window System installed.

%description -l ru_RU.KOI8-R xjed
X%name -- версия %name, предназначеная для работы в X Window System.

%description -n rgrep
The rgrep utility can recursively descend through directories as
it greps for the specified pattern.  Note that this ability does
take a toll on rgrep's performance, which is somewhat slow.  Rgrep
will also highlight the matching expression.

Install the rgrep package if you need a recursive grep which can
highlight the matching expression.

%description -n rgrep -l ru_RU.KOI8-R
Вариант утилиты grep с возможностью рекурсивной обработки каталогов,
и подсветкой найденых совпадений.

%prep

%setup -q -n %srcname

#patch -p1
#patch1 -p1

%patch1 -p1 -b .xkeys
%patch2 -p1
%if "%{_lib}" == "lib64"
%patch3 -p1
%endif
#patch5 -p1
#patch6 -p1

cd autoconf
autoconf
mv configure ..
cd ..


%build
%configure --prefix=%_datadir -exec-prefix=%prefix --with-x

# enable gmp and Xft support
#XFTCFLAGS=`xft-config --cflags`
#XFTLIBS=`xft-config --libs`
XFTCFLAGS="-I/usr/include/freetype2"
XFTLIBS="-lXft -lX11 -lfreetype -lfontconfig -lXrender -lX11"

sed -i "
     s!^#\(MOUSEFLAGS.*\)!\1!
     s!^#\(MOUSELIB.*\)!\1!
     s!^#\(GPMMOUSEO.*\)!\1!
     s!^#\(OBJGPMMOUSEO.*\)!\1!
     s!^#\(XRENDERFONTLIBS\).*!\1 = $XFTLIBS!
     s!^\(XINCLUDE = .*\)!\1 $XFTCFLAGS!
     " src/Makefile

sed -i '
     /XJED_HAS_XRENDERFONT/ s!0!1!
     ' src/jed-feat.h

sed -i '
     s/doc\/txt/help/
     ' lib/*.sl

sed -i '
     s!@INFODIR@!%_infodir!g
     s!@DATADIR@!%_datadir!g
     s!@LIBDIR@!%_libdir!g			     
     ' %SOURCE1

touch src/Makefile

%make_build all JED_ROOT=%_datadir/%name
%make_build xjed rgrep getmail JED_ROOT=%_datadir/%name

%set_verify_info_method relaxed

%install
mkdir -p %buildroot%_infodir
mkdir -p %buildroot%_datadir/%name/lib/colors/X%name
mkdir -p %buildroot%_datadir/%name/help
mkdir -p %buildroot%_libdir/%name

install -pD -m755 src/objs/x%name    %buildroot%_x11bindir/x%name
install -pD -m755 src/objs/%name     %buildroot%_bindir/%name
install -pD -m755 src/objs/rgrep     %buildroot%_bindir/rgrep
install -pD -m755 src/objs/getmail   %buildroot%_libdir/%name/getmail

pushd %buildroot%_bindir
	ln -s %name %name-script
popd

install -pD -m644 %SOURCE1           %buildroot%_sysconfdir/%name.conf

install -pD -m644 doc/manual/%name.1 %buildroot%_man1dir/%name.1
install -pD -m644 doc/manual/rgrep.1 %buildroot%_man1dir/rgrep.1

install -m644 info/%name.*           %buildroot%_infodir
install -m644 doc/txt/*              %buildroot%_datadir/jed/help

cp -r         lib                    %buildroot%_datadir/%name/

# now make .slc files (comment 21042011)
#( 
#    export JED_ROOT=%buildroot%_datadir/%name
#    %buildroot%_bindir/%name -batch -n -l preparse.sl </dev/null
#) || :

JED_ROOT=%buildroot%_datadir/%name %buildroot%_bindir/%name -batch -n -l preparse.sl </dev/null

while ps -C jed > /dev/null; do sleep 1; done

%files
%_bindir/%{name}*

%files common
     %_sysconfdir/%name.conf
     %_man1dir/%name.1*
     %_datadir/%name/*
     %_libdir/%name/*
     %_infodir/%name.*
%dir %_datadir/%name
%dir %_libdir/%name
%doc COPYRIGHT README changes.txt INSTALL.unx

%files xjed
%_x11bindir/x%name

%files -n rgrep
%_bindir/rgrep
%_man1dir/rgrep.1*

%changelog
* Wed Jan 13 2021 Fr. Br. George <george@altlinux.ru> 2:0.99.19-alt2.qa2.2
- Fix parallel build

* Sat Dec 05 2015 Igor Vlasenko <viy@altlinux.ru> 2:0.99.19-alt2.qa2.1
- NMU: added BR: texinfo

* Wed Mar 20 2013 Fr. Br. George <george@altlinux.ru> 2:0.99.19-alt2.qa2
- Renew buildreq

* Thu Aug 30 2012 Repocop Q. A. Robot <repocop@altlinux.org> 2:0.99.19-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * beehive-log-dependency-needs-epoch-x86_64 for jed
  * postclean-03-private-rpm-macros for the spec file

* Thu Apr 21 2011 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.19-alt2
- fix build

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.19-alt1
- new version

* Fri Jul 10 2009 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.18-alt4
- fix build, remove deprecated macros

* Sat Nov 01 2008 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.18-alt3
- rebuild with new toolchain
- update patches

* Mon May 26 2008 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.18-alt2
- build with libslang2 
- spec cleanup

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 2:0.99.18-alt1
- New version with fixes
- old patches removed

* Tue Nov 26 2002 Igor Homyakov <homyakov at altlinux dot ru> 2:0.99.16-alt2
- added patch for xjed anti-aliasing (thanx for voins@ and aen@)
- enable anti-aliasing support in XJed 

* Fri Aug 30 2002 Igor Homyakov <homyakov at altlinux dot ru> 1:0.99.16-alt1
- update URLs
- rewrited jed.spec
- moved info to %_infodir
- moved getmail to %_libdir/jed
- renamed doc/txt/ to help/
- added sistem wide config file (jed.conf)

* Sun Apr 14 2002 Igor Homyakov <homyakov@altlinux.ru> B0.99.15-alt2
- New modes added (javascript, CSS, ruby, manedit)
- Merge with new LaTeX mode scripts.
- spec cleanup

* Tue Nov 6 2001 Igor Homyakov <homyakov@altlinux.ru> B0.99.15-alt
- build B0.99-15 package
- added russian translation for jed.spec file

* Sat Jun 09 2001 Dmitry V. Levin <ldv@altlinux.ru> B0.99.14-alt1
- Specfile cleanup according to packaging policy.

* Wed Jun 06 2001 Igor Homyakov <homyakov@openbsd.ru>
- make package for ALTLinux with minor changes
- added xjed anti-aliased font support patch by
  Charl P. Botha <cpbotha@ieee.org>

* Sat Jun 02 2001 Matt Hyclak <mrh@ling.ohio-state.edu>
- updated to jed 0.99.14
- removed debian specific stuff from the patch

* Wed Feb 21 2001 Matt Hyclak <mrh@penguinpowered.com>
- updated to jed 0.99.13

* Tue Nov 28 2000 Guido Gonzato <ggonza@tin.it>
- added the %post directive for linking the doc directory to JED_ROOT
- removed Perl - sed will do

* Mon Nov 27 2000 Charl P. Botha <cpbotha@ieee.org>
- thanks to Guido Gonzato <ggonza@tin.it> and
  Ric Klaren <klaren@cs.utwente.nl> these use the _mandir macro for placing
  the man pages.  Notice that this only takes effect when the rpm is rebuilt
  on a new distribution.
- minor fixes in install procedure

* Sun Nov 26 2000 Charl P. Botha <cpbotha@ieee.org>
- updated to new upstream revision B0.99-12
- we now simply make use of the debian jed package diff file as single patch.
  i am the debian maintainer, so this makes it easy for me to keep everything
  up to date.
- we're also building on a machine supplied by Ethan Blanton.  Thanks Ethan!

* Mon Aug 21 2000 Charl P. Botha <cpbotha@ieee.org>
- updated jed rpms to require slang >= 1.3.11, as per documentation

* Wed Jun  7 2000 Charl P. Botha <cpbotha@ieee.org>
- added GPM support to RPMs, requested by <guido@ibogeo.df.unibo.it>

* Fri Jun  2 2000 Charl P. Botha <cpbotha@ieee.org>
- integrated patch from mailing list (thanks John) that fixes emacs-style
  locking on filesystems that don't support symlinks.

* Tue May 30 2000 Charl P. Botha <cpbotha@ieee.org>
- updated to JED B0.99-11
- includes getmail, requested by <guido@ibogeo.df.unibo.it>
- moved info to /usr/lib/jed/info (rh default)

* Tue Nov 16 1999 Charl P. Botha <cpbotha@ieee.org>
- changed to JED B0.99-10

* Sun Sep 26 1999 Charl P. Botha <cpbotha@ieee.org>
- fixed up duplication of doc files
- moved info dir to /usr/doc/jed-*/

* Fri Sep 24 1999 Charl P. Botha <cpbotha@ieee.org>
- changed to use more of John's make install and rebuilt

* Thu Sep 23 1999 Charl P. Botha <cpbotha@ieee.org>
- rebuild for jed B0.99.9

* Wed Jul 14 1999 Charl P. Botha <cpbotha@ieee.org>
- rebuild for jed B0.99-8

* Sun Jul 4 1999 Charl P. Botha <cpbotha@ieee.org>
- modified for jed B0.99-7 from Redhat 6.0 spec

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- update to 0.98.7 for Raw Hide
- split off lib stuff into jed-common

* Mon Oct  5 1998 Jeff Johnson <jbj@redhat.com>
- change rgep group tag, same as grep.

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Mon Nov  3 1997 Michael Fulbright <msf@redhat.com>
- added wmconfig entry for xjed

* Tue Oct 21 1997 Michael Fulbright <msf@redhat.com>
- updated to 0.98.4
- included man pages in file lists

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
