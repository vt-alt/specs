# All LSB releases starting with version 3.0 are compatible with previous releases
%define compat_version 3.0

%ifarch %ix86
%define lsb_arch ia32
%define lib_suffix %nil
%endif
%ifarch x86_64
%define lsb_arch amd64
%define lib_suffix ()(64bit)
%endif
%ifarch %e2k
%define lsb_arch e2k
%define lib_suffix ()(64bit)
%endif
%ifarch aarch64
%define lsb_arch aarch64
%define lib_suffix ()(64bit)
%endif

Name: lsb
Summary: The skeleton package defining packages needed for LSB compliance
Version: 4.0
Release: alt8
License: GPL
Url: http://www.linuxbase.org/
Group: System/Base
Packager: Andriy Stepanov <stanv@altlinux.ru>
Source1: README.alt

# 20.4 Installation and Removal of Init Scripts
Source11: install_initd
Source12: remove_initd

# B.2 Commands And Utilities
# lsbinstall -- installation tool for various types of data
# XXX:
Source21: lsbinstall

Exclusivearch: %ix86 x86_64 %e2k aarch64

Requires: lsb-core = %version
Requires: lsb-cxx = %version
Requires: lsb-desktop = %version
Requires: lsb-languages = %version
Requires: lsb-printing = %version

%description
LSB metapackage. This package provides an implementation of all mandatory
modules of the Linux Standard Base:
Core, C++, Desktop, Interpreted Languages, Printing.

Necessary tools, links, and dependencies for the Linux Standard Base (LSB).

The Linux Standard Base (http://www.linuxbase.org/) is a standard core
system that third-party applications written for Linux can depend
upon.

##############################
##############################
# LSB 4.0 defines next modules
# MODULE      ARCHITUCTURE DEPENDENT/INDEPENDENT
# * Core      dependent
# * CXX       dependent
# * Desktop   dependent
# * Languages independent
# * Printing  independent
# * TrialUse  independent
# http://www.linuxfoundation.org/en/Specifications
# http://dev.linuxfoundation.org/navigator/browse/module.php
# define for each separate package
##############################
##############################

#############
# Module Core
# ###########
%package core
Summary: Linux Standard Base %version core support package
Group: System/Base

# 22.6 Package Dependencies
#
# lsb-core-arch
#      This dependency is used to indicate that the application is dependent on
#      features contained in the LSB-Core specification.
#
# lsb-core-noarch
#      This dependency is used to indicate that the application is dependent on
#      features contained in the LSB-Core specification and that the package does
#      not contain any architecture specific files.
#
#      These dependencies shall have a version of 4.0.

Provides: lsb-core-noarch = %version
Provides: lsb-core-%lsb_arch = %version
Provides: lsb-core-noarch = %compat_version
Provides: lsb-core-%lsb_arch = %compat_version

Requires: lsb-init = %version

# 15.1. Commands and Utilities
# http://refspecs.linux-foundation.org/LSB_4.0.0/LSB-Core-generic/LSB-Core-generic/command.html
# http://dev.linuxfoundation.org/navigator/browse/command.php?changever=3.2&changearch=1
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Core
# Commands (139 entries)
# Commands with predefined path
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /bin/cpio
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/ed
Requires: /bin/false
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /bin/gunzip
Requires: /bin/gzip
Requires: /bin/hostname
# Requires:       /usr/lib/lsb/install_initd supplied by lsb-core package
Requires: /bin/kill
Requires: /bin/ln
Requires: /bin/ls
Requires: /usr/bin/lsb_release
Requires: /bin/mkdir
Requires: /bin/mknod
Requires: /bin/more
Requires: /bin/mount
Requires: /bin/mv
Requires: /bin/ps
Requires: /bin/pwd
# Requires:       /usr/lib/lsb/remove_initd supplied by lsb-core package
Requires: /bin/rm
Requires: /bin/rmdir
Requires: /bin/sed
Requires: /usr/sbin/sendmail
Requires: /bin/sh
Requires: /sbin/shutdown
Requires: /bin/su
Requires: /bin/sync
Requires: /bin/tar
Requires: /bin/true
Requires: /bin/umount
Requires: /bin/uname
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod
Requires: /bin/zcat
# Commands without predefined path
# search path in ALTLinux with: cmd="ar at..."; for i in $cmd; do which "$i"; done
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /bin/awk
Requires: /bin/basename
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/chfn
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /bin/cut
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /bin/du
Requires: /bin/egrep
Requires: /usr/bin/env
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /bin/fgrep
Requires: /usr/bin/file
Requires: /bin/find
Requires: /usr/bin/fold
Requires: /sbin/fuser
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/gettext
Requires: /bin/grep
Requires: /usr/bin/groups
Requires: /bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/lp
Requires: /usr/bin/lpr
Requires: /usr/bin/m4
Requires: /usr/bin/mailx
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /bin/mkfifo
Requires: /bin/mktemp
Requires: /usr/bin/msgfmt
Requires: /usr/bin/newgrp
Requires: /bin/nice
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
Requires: /usr/bin/pax
Requires: /bin/pidof
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/renice
Requires: /bin/sleep
Requires: /bin/sort
Requires: /usr/bin/split
Requires: /usr/bin/strip
Requires: /bin/stty
Requires: /bin/tail
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /bin/touch
Requires: /usr/bin/tr
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /bin/wc
Requires: /bin/xargs
Requires: /usr/bin/seq
# Table 15-2. Built In Utilities
# http://refspecs.linux-foundation.org/LSB_4.0.0/LSB-Core-generic/LSB-Core-generic/command.html
# cd getopts type umask
# command read ulimit wait

# Required libs for LSB_Core:
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Core
# Common for %ix86 x86_64
Requires: libm.so.6%lib_suffix
Requires: libdl.so.2%lib_suffix
Requires: libcrypt.so.1%lib_suffix
Requires: libz.so.1%lib_suffix
Requires: libncurses.so.5%lib_suffix
Requires: libutil.so.1%lib_suffix
Requires: libc.so.6%lib_suffix
Requires: libpthread.so.0%lib_suffix
Requires: librt.so.1%lib_suffix
Requires: libpam.so.0%lib_suffix
Requires: libgcc_s.so.1%lib_suffix
# Special libs
# http://dev.linuxfoundation.org/navigator/browse/lib_single.php?cmd=list-by-name&Section=ABI&Lname=proginterp
%ifarch %ix86
# see %install section Requires: /lib/ld-lsb.so.3
Requires: ld-linux.so.2%lib_suffix
%endif
%ifarch x86_64
# see %install section Requires: /lib64/ld-lsb-x86-64.so.3
Requires: ld-linux-x86-64.so.2%lib_suffix
%endif
%ifarch %e2k
# see %install section Requires: /lib64/ld-lsb.so.3
Requires: ld-linux.so.2%lib_suffix
%endif

%description core
This is the Core module of the Linux Standard Base (LSB), ISO/IEC 23360
Part 1. This module provides the fundamental system interfaces,
libraries, and runtime environment upon which all conforming
applications and libraries depend.
Core interfaces may be supplemented by other modules; all modules are
built upon the core.
#################
# END Module Core
#################

############
# Module CXX
############
%package cxx
Summary: Linux Standard Base %version cxx support package
Group: System/Base
Requires: %name-core = %version

Provides: lsb-cxx-noarch = %version
Provides: lsb-cxx-%lsb_arch = %version
Provides: lsb-cxx-noarch = %compat_version
Provides: lsb-cxx-%lsb_arch = %compat_version

# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Cpp
Requires: libstdc++.so.6%lib_suffix

%description cxx
The cxx requirements for LSB compliance.
################
# END Module CXX
################

################
# Module Desktop
#       Have next submodules:
#       * Graphics
#       * Graphics_Ext
#       * Toolkit_Gtk
#       * Toolkit_Qt
#       * Toolkit_Qt3
#       * XML
################
%package desktop
Summary: Linux Standard Base %version desktop support package
Group: System/Base
Requires: %name-core = %version

Provides: lsb-desktop-noarch = %version
Provides: lsb-desktop-%lsb_arch = %version
Provides: lsb-desktop-noarch = %compat_version
Provides: lsb-desktop-%lsb_arch = %compat_version

# XXX@stanv: graphics is submodule of desktop module:
# http://dev.linuxfoundation.org/navigator/browse/module.php

Provides: lsb-graphics-noarch = %version
Provides: lsb-graphics-%lsb_arch = %version
Provides: lsb-graphics-noarch = %compat_version
Provides: lsb-graphics-%lsb_arch = %compat_version

# Submodule Graphics
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Graphics
Requires: libX11.so.6%lib_suffix
Requires: libXt.so.6%lib_suffix
Requires: libGL.so.1%lib_suffix
Requires: libXext.so.6%lib_suffix
Requires: libICE.so.6%lib_suffix
Requires: libSM.so.6%lib_suffix
Requires: libXi.so.6%lib_suffix
Requires: libGLU.so.1%lib_suffix
Requires: libXtst.so.6%lib_suffix

# XXX@stanv: graphics is submodule of desktop module:
# http://dev.linuxfoundation.org/navigator/browse/module.php
# Another distros provide this sub-module as independent module. Why ???
# AEN@altlinux: "Lets be as all others!".
# https://bugzilla.altlinux.org/show_bug.cgi?id=25877

Provides: lsb-graphics-noarch = %version
Provides: lsb-graphics-%lsb_arch = %version
Provides: lsb-graphics-noarch = %compat_version
Provides: lsb-graphics-%lsb_arch = %compat_version

# Submodule Graphics_Ext
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Graphics_Ext
Requires: libfontconfig.so.1%lib_suffix
Requires: libpng12.so.0%lib_suffix
Requires: libjpeg.so.62%lib_suffix
Requires: libXrender.so.1%lib_suffix
Requires: libfreetype.so.6%lib_suffix
Requires: libXft.so.2%lib_suffix
Requires: libcairo.so.2%lib_suffix
Requires: /usr/bin/fc-cache
Requires: /usr/bin/fc-list
Requires: /usr/bin/fc-match

# Submodule Toolkit_Gtk
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Toolkit_Gtk
Requires: libglib-2.0.so.0%lib_suffix
Requires: libgobject-2.0.so.0%lib_suffix
Requires: libgmodule-2.0.so.0%lib_suffix
Requires: libgthread-2.0.so.0%lib_suffix
Requires: libatk-1.0.so.0%lib_suffix
Requires: libpango-1.0.so.0%lib_suffix
Requires: libpangoxft-1.0.so.0%lib_suffix
Requires: libpangoft2-1.0.so.0%lib_suffix
Requires: libgdk_pixbuf-2.0.so.0%lib_suffix
Requires: libgdk_pixbuf_xlib-2.0.so.0%lib_suffix
Requires: libgdk-x11-2.0.so.0%lib_suffix
Requires: libgtk-x11-2.0.so.0%lib_suffix
Requires: libpangocairo-1.0.so.0%lib_suffix

# Submodule Toolkit_Qt
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Toolkit_Qt
Requires: libQtCore.so.4%lib_suffix
Requires: libQtGui.so.4%lib_suffix
Requires: libQtNetwork.so.4%lib_suffix
Requires: libQtXml.so.4%lib_suffix
Requires: libQtOpenGL.so.4%lib_suffix
Requires: libQtSql.so.4%lib_suffix
Requires: libQtSvg.so.4%lib_suffix

# Submodule Toolkit_Qt3
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Toolkit_Qt3
Requires: libqt-mt.so.3%lib_suffix

# Submodule XML
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_XML
Requires: libxml2.so.2%lib_suffix

%description desktop
The desktop requirements for LSB compliance.
####################
# END Module Desktop
####################

##################
# Module Languages
#       Have next submodules:
#       * Perl
#       * Python
##################
%package languages
Summary: Linux Standard Base %version languages support package
Group: System/Base
Requires: %name-core = %version

Provides: lsb-languages-noarch = %version
Provides: lsb-languages-noarch = %compat_version

# Submodule Perl
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Perl
# http://dev.linuxfoundation.org/navigator/browse/intlang.php?cmd=list-modules&ILid=1
Requires: perl-base >= 5.8.8
Requires: /usr/bin/perl
Requires: perl-DBM
Requires: perl-Attribute-Handlers
Requires: perl-devel
Requires: perl-CGI
Requires: perl-CPAN
Requires: perl-Encode
Requires: perl-Filter
Requires: perl-Filter-Simple
Requires: perl-I18N-LangTags
Requires: perl-Locale-Maketext
Requires: perl-Locale-Codes
Requires: perl-Math-BigRat
Requires: perl-Math-BigInt
Requires: perl-Memoize
Requires: perl-NEXT
Requires: perl-libnet
Requires: perl-PerlIO
Requires: perldoc
Requires: perl-Storable
Requires: perl-Switch
Requires: perl-Term-ReadLine-Gnu
Requires: perl-Text-Balanced
Requires: perl-Text-Soundex
Requires: perl-Unicode-Collate
Requires: perl-Unicode-Normalize
Requires: perl-unicore
Requires: perl4-compat
Requires: perl-bignum

# Submodule Python
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Python
# http://dev.linuxfoundation.org/navigator/browse/intlang.php?cmd=list-modules&ILid=2
Requires: /usr/bin/python
Requires: python-base >= 2.4.2
Requires: python-modules
%description languages
The languages requirements for LSB compliance.
######################
# END Module Languages
######################

#################
# Module Printing
#################
%package printing
Summary: Linux Standard Base %version printing support package
Group: System/Base
Requires: %name-core = %version

Provides: lsb-printing-noarch = %version
Provides: lsb-printing-noarch = %compat_version

# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Printing
Requires: libcups.so.2%lib_suffix
Requires: libcupsimage.so.2%lib_suffix
Requires: /usr/bin/foomatic-rip
Requires: /usr/bin/gs
%description printing
The printing requirements for LSB compliance.
#####################
# END Module Printing
#####################

#################
# Module TrialUse
#       Have next submodules:
#       * Multimedia
#       * TUM
#################
%package trialuse
Summary: Linux Standard Base %version trialuse support package
Group: System/Base
Requires: %name-core = %version

Provides: lsb-trialuse-noarch = %version
Provides: lsb-trialuse-noarch = %compat_version

# Submodule Java
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Java
Requires: /usr/bin/java
Requires: java >= 1.8.0

# Submodule Multimedia
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Multimedia
Requires: libasound.so.2%lib_suffix

# Submodule Security
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_Security
Requires: libnss3.so%lib_suffix
Requires: libssl3.so%lib_suffix
Requires: libnspr4.so%lib_suffix

# Submodule TUM
# http://dev.linuxfoundation.org/navigator/browse/module.php?cmd=display_module&module=LSB_TUM
Requires: /usr/bin/xdg-desktop-icon
Requires: /usr/bin/xdg-desktop-menu
Requires: /usr/bin/xdg-email
Requires: /usr/bin/xdg-icon-resource
Requires: /usr/bin/xdg-mime
Requires: /usr/bin/xdg-open
Requires: /usr/bin/xdg-screensaver

%description trialuse
The trialuse requirements for LSB compliance.
#####################
# END Module TrialUse
#####################

%prep
%build
%install
%define docdir %_docdir/%name-%version
install -d -pm 755 %buildroot%docdir
install -m644 %SOURCE1 %buildroot%docdir

install -d -pm 755 %buildroot%_sysconfdir/lsb-release.d

%define lsbrel %buildroot%_sysconfdir/lsb-release

install -d -pm755 %buildroot/usr/lib/lsb
install -m755 %SOURCE11 %buildroot/usr/lib/lsb
install -m755 %SOURCE12 %buildroot/usr/lib/lsb
install -m755 %SOURCE21 %buildroot/usr/lib/lsb

echo -n "LSB_VERSION=\"core-%compat_version-noarch:core-%version-noarch:" > %lsbrel
echo "core-%compat_version-%lsb_arch:core-%version-%lsb_arch\"" >>  %lsbrel

# ALT Linux Sisyphus (20081222)
# ALT Linux 1.0.0 Server Light r1 (Lycoris Radiata)

cat <<EOF >>%lsbrel
DISTRIB_ID="ALT"
LSB_VERSION="%version"
#
# Examples:
#
# DISTRIB_ID - single word, ID of DISTRIBUTOR
# DISTRIB_RELEASE="5.0.0"
# DISTRIB_CODENAME="Lycoris Radiata"
# DISTRIB_DESCRIPTION="ALT Linux Sisyphus (20081222)"
# DISTRIB_DESCRIPTION="ALT Linux 1.0.0 Server Light r1 (Lycoris Radiata)"
EOF

# Required libs for LSB_Core:
# 11.1 Program Interpreter/Dynamic Linker
# The Program Interpreter shall be ......
mkdir -p "%buildroot/%_lib"
%ifarch %ix86
ln -sf "/lib/ld-linux.so.2" "%buildroot/lib/ld-lsb.so.3"
%endif
%ifarch x86_64
ln -sf "/lib64/ld-linux-x86-64.so.2" "%buildroot/lib64/ld-lsb-x86-64.so.3"
%endif
%ifarch %e2k
ln -sf "/lib64/ld-linux.so.2" "%buildroot/lib64/ld-lsb.so.3"
%endif

touch %buildroot%_sysconfdir/lsb-release.d/core-%compat_version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/core-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/core-%version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/core-%version-noarch

touch %buildroot%_sysconfdir/lsb-release.d/cxx-%compat_version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/cxx-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/cxx-%version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/cxx-%version-noarch

touch %buildroot%_sysconfdir/lsb-release.d/desktop-%compat_version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/desktop-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/desktop-%version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/desktop-%version-noarch

# XXX@stanv see above note about lsb-graphics:
touch %buildroot%_sysconfdir/lsb-release.d/graphics-%compat_version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/graphics-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/graphics-%version-%lsb_arch
touch %buildroot%_sysconfdir/lsb-release.d/graphics-%version-noarch

touch %buildroot%_sysconfdir/lsb-release.d/languages-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/languages-%version-noarch

touch %buildroot%_sysconfdir/lsb-release.d/printing-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/printing-%version-noarch

touch %buildroot%_sysconfdir/lsb-release.d/trialuse-%compat_version-noarch
touch %buildroot%_sysconfdir/lsb-release.d/trialuse-%version-noarch

%files
%files core
%docdir
%dir %_sysconfdir/lsb-release.d/
%_sysconfdir/lsb-release.d/core-%compat_version-%lsb_arch
%_sysconfdir/lsb-release.d/core-%compat_version-noarch
%_sysconfdir/lsb-release.d/core-%version-%lsb_arch
%_sysconfdir/lsb-release.d/core-%version-noarch
%ifarch %ix86
/lib/ld-lsb.so.3
%endif
%ifarch x86_64
/lib64/ld-lsb-x86-64.so.3
%endif
%ifarch %e2k
/lib64/ld-lsb.so.3
%endif
%prefix/lib/lsb/install_initd
%prefix/lib/lsb/remove_initd
%prefix/lib/lsb/lsbinstall
%_sysconfdir/lsb-release

%files cxx
%_sysconfdir/lsb-release.d/cxx-%compat_version-%lsb_arch
%_sysconfdir/lsb-release.d/cxx-%compat_version-noarch
%_sysconfdir/lsb-release.d/cxx-%version-%lsb_arch
%_sysconfdir/lsb-release.d/cxx-%version-noarch

%files desktop
%_sysconfdir/lsb-release.d/desktop-%compat_version-%lsb_arch
%_sysconfdir/lsb-release.d/desktop-%compat_version-noarch
%_sysconfdir/lsb-release.d/desktop-%version-%lsb_arch
%_sysconfdir/lsb-release.d/desktop-%version-noarch

# XXX@stanv see above note about lsb-graphics:
%_sysconfdir/lsb-release.d/graphics-%compat_version-%lsb_arch
%_sysconfdir/lsb-release.d/graphics-%compat_version-noarch
%_sysconfdir/lsb-release.d/graphics-%version-%lsb_arch
%_sysconfdir/lsb-release.d/graphics-%version-noarch

%files languages
%_sysconfdir/lsb-release.d/languages-%compat_version-noarch
%_sysconfdir/lsb-release.d/languages-%version-noarch

%files printing
%_sysconfdir/lsb-release.d/printing-%compat_version-noarch
%_sysconfdir/lsb-release.d/printing-%version-noarch

%files trialuse
%_sysconfdir/lsb-release.d/trialuse-%compat_version-noarch
%_sysconfdir/lsb-release.d/trialuse-%version-noarch

%changelog
* Mon Sep 30 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 4.0-alt8
- added aarch64

* Fri Jun 22 2018 Michael Shigorin <mike@altlinux.org> 4.0-alt7
- E2K: initial support

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 4.0-alt6
- NMU: bumped java version to 1.8

* Tue Jul 12 2011 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt5
- #25877

* Fri Apr 16 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt4
- Require lsb-init

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt3
- Correct /etc/lsb-release

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt2
- Add suffix for x86_64 libs, correnct java package name.

* Tue Apr 13 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt1
- Switch to new version.

* Wed Jan 14 2009 Andriy Stepanov <stanv@altlinux.ru> 3.2-alt3
- Update Requires tags using lib_suffix, ex: libc.so.6()(64bit)

* Tue Jan 13 2009 Andriy Stepanov <stanv@altlinux.ru> 3.2-alt2
- Add metapackage lsb (ALT#18501)

* Mon Nov 10 2008 Andriy Stepanov <stanv@altlinux.ru> 3.2-alt1
- Init package for LSB 3.2

* Fri Feb 24 2006 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt0.1
- initial build for ALT Linux Sisyphus (thanks SuSE and Debian)
- remove per arch links to ld.so
- do not require X client dir
- adopted paths to nice, basename, fuser
- fix lsb_release to detect Sisyphus version
