# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:    qps
Version: 2.1.0
Release: alt1
Summary: Visual process status monitor
License: GPLv2+
Group:   Monitoring
URL:     https://github.com/lxqt/qps
Source0: %name-%version.tar
Source1: %name.desktop

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: lxqt-build-tools >= 0.6.0
BuildRequires: liblxqt-devel >= 0.15.0
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: /usr/bin/convert

%description
Qps is a perfect visual process manager, an X11 version of "top" or "ps" that displays processes in a window and lets you sort and manipulate them easily
Qps can
    * change nice value of a process
    * alter the scheduling policy and soft realtime priority of a process
    * display the TCP/UDP sockets used by a process, and names of the connected hosts (Linux only)
    * display the memory mappings of the process (which files and shared libraries are loaded where)
    * display the open files of a process, and the state of unix domain sockets
    * kill or send any other signal to selected processes
    * display the load average as a graph, and use this as its icon when iconified
    * show (as graph or numbers) current CPU, memory and swap usage
    * sort the process table on any attribute (size, cpu usage, owner etc)
    * on SMP systems running Linux 2.1 or later (or Solaris), display cpu usage for each processor, and which CPU a process is running on
    * display the environment variables of any process
    * show the process table in tree form, showing the parent-child relationship
    * execute user-defined commands on selected processes
    * display MOSIX-specific fields and migrate processes to other nodes in a cluster
%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std
install -pD -m 644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 32x32 icon/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 icon/%name.png %buildroot%_miconsdir/%name.png

%files
%dir %_datadir/%name
%doc CHANGELOG COPYING LICENSE.QPL README.md
%_man1dir/*
%_bindir/*
%_datadir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Tue Oct 15 2019 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 1.10.20-alt1
- 1.10.20
- swith to github

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 1.10.19-alt1
- 1.10.19

* Mon Oct 08 2018 Motsyo Gennadi <drool@altlinux.ru> 1.10.18-alt1
- 1.10.18

* Fri Mar 30 2018 Motsyo Gennadi <drool@altlinux.ru> 1.10.17-alt1
- 1.10.17 (altbug #34690)

* Sun Jul 15 2012 Motsyo Gennadi <drool@altlinux.ru> 1.10.16-alt1
- 1.10.16

* Wed Aug 10 2011 Motsyo Gennadi <drool@altlinux.ru> 1.10.15-alt1
- 1.10.15 release

* Sun Jul 03 2011 Motsyo Gennadi <drool@altlinux.ru> 1.10.13-alt1
- 1.10.13 release

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.10.12.1-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for qps
  * postclean-03-private-rpm-macros for the spec file

* Sat Jul 31 2010 Motsyo Gennadi <drool@altlinux.ru> 1.10.12.1-alt1
- 1.10.12.1 release

* Wed Sep 02 2009 Motsyo Gennadi <drool@altlinux.ru> 1.10.11-alt1
- 1.10.11 release

* Tue May 12 2009 Motsyo Gennadi <drool@altlinux.ru> 1.10.8.3-alt1
- 1.10.8.3 release

* Sat May 09 2009 Motsyo Gennadi <drool@altlinux.ru> 1.10.8.1-alt1
- 1.10.8.1 release

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 1.10.5.1-alt1
- 1.10.5.1 release
- delete post/postun scripts (new rpm)

* Sat Sep 06 2008 Motsyo Gennadi <drool@altlinux.ru> 1.10.2-alt1
- 1.10.2 release

* Tue Feb 26 2008 Motsyo Gennadi <drool@altlinux.ru> 1.10.1-alt0.a8
- aplha version (only Qt4)

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 1.9.20-alt2
- add Url for Source

* Tue Nov 20 2007 Motsyo Gennadi <drool@altlinux.ru> 1.9.20-alt1
- new version
- add optflags support for building
- cleanup spec-file
- add icons
- fix and enable desktop-file
- remove old menu-file
- run buildreq -bi script
- fix license

* Fri May 13 2005 Nick S. Grechukh <gns@altlinux.ru> 1.9.9.4-alt1
- initial Sisyphus build
