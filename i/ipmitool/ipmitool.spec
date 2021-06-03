Name: ipmitool
Summary: ipmitool - Utility for IPMI control
Version: 1.8.18
Release: alt4
License: BSD
URL: http://ipmitool.sourceforge.net/
Group: System/Kernel and hardware
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: libssl-devel readline-devel ncurses-devel libfreeipmi-devel

%description
This package contains a utility for interfacing with devices that support
the Intelligent Platform Management Interface specification.  IPMI is
an open standard for machine health, inventory, and remote power control.

This utility can communicate with IPMI-enabled devices through either a
kernel driver such as OpenIPMI or over the RMCP LAN protocol defined in
the IPMI specification.  IPMIv2 adds support for encrypted LAN
communications and remote Serial-over-LAN functionality.

It provides commands for reading the Sensor Data Repository (SDR) and
displaying sensor values, displaying the contents of the System Event
Log (SEL), printing Field Replaceable Unit (FRU) information, reading and
setting LAN configuration, and chassis power control.

%prep
%setup
%patch0 -p1

%build
touch NEWS

%autoreconf
# --disable-dependency-tracking speeds up the build
# --enable-file-security adds some security checks
%configure --disable-dependency-tracking --enable-file-security

%make_build

%install
make DESTDIR=%buildroot install
install -pD -m755 contrib/bmclanconf %buildroot%_sbindir/

%files
%_bindir/*
%_sbindir/*
%doc %_mandir/man1/*
%doc %_mandir/man8/*
%doc %_datadir/doc/ipmitool/*
%_datadir/%name

%changelog
* Sat Feb 27 2021 Anton Farygin <rider@altlinux.org> 1.8.18-alt4
- applied patches from upstream git to fix security issue (Fixes: CVE-2020-5208)
  see https://github.com/ipmitool/ipmitool/security/advisories/GHSA-g659-9qxw-p7cp
- added upstream fix FTBFS with gcc-10

* Thu Nov 22 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.18-alt3
- revisit openssl-1.1 support

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.8.18-alt2
- fixed build with openssl-1.1

* Tue Oct 18 2016 Anton Farygin <rider@altlinux.ru> 1.8.18-alt1
- new version

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 1.8.17-alt2
- rebuild with new freeipmi

* Tue Jun 14 2016 Anton Farygin <rider@altlinux.ru> 1.8.17-alt1
- new version

* Wed Apr 29 2015 Anton Farygin <rider@altlinux.ru> 1.8.15-alt1
- new version

* Tue Mar 25 2014 Anton Farygin <rider@altlinux.ru> 1.8.13-alt3
- rebuild with new freeipmi

* Thu Oct 24 2013 Anton Farygin <rider@altlinux.ru> 1.8.13-alt2
- add patch from upstream bugzilla for fix sdr list on some HP servers (closes: #29491)

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.8.13-alt1
- new version

* Mon Jul 15 2013 Anton Farygin <rider@altlinux.ru> 1.8.12-alt2
- rebuild with new freeipmi

* Mon Jul 15 2013 Anton Farygin <rider@altlinux.ru> 1.8.12-alt1
- new version

* Sat Dec 31 2011 Michael Shigorin <mike@altlinux.org> 1.8.11-alt4
- applied debian patch to fix CVE-2011-4339 (pidfile had too wide
  permissions allowing users to kill arbitrary processes at times)

* Tue Sep 13 2011 Anton Farygin <rider@altlinux.ru> 1.8.11-alt3
- bmclanconf added to package (closes: #26140)

* Tue Dec 07 2010 Anton Farygin <rider@altlinux.ru> 1.8.11-alt2
- rebuild with new openssl

* Thu Dec 24 2009 Anton Farygin <rider@altlinux.ru> 1.8.11-alt1
- 1.8.11

* Fri Dec 12 2008 Stanislav Ievlev <inger@altlinux.org> 1.8.10-alt1
- 1.8.10

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.8.9-alt2
- Added URL.

* Tue Jul 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.8.9-alt1
- 1.8.9 release.
- HUGE spec cleanup.
- Changed builddeps:
  * removed gcc-c++
  * changed kernel headers to std
  * added libfreeipmi-devel
- repack.
- Pack bmclanconf as well.

* Mon Jan 01 2007 Michail Yakushin <silicium@altlinux.ru> 1.8.8-alt1
- first build for altlinux

* Tue May 02 2006 <duncan@iceblink.org>  1.8.8-1
 - Fix segfaults in sensor data repository list
 - Fix ipmievd to open interface before daemonizing
 - Fix IPMIv1.5 authtype NONE to ignore supplied password
 - Fix cipher suite display bug in lan print
 - Fix typo in IPMIv2 SOL output when sending break
 - Fix improper LUN handling with Tyan SOL
 - Add LUN support to OpenIPMI interface
 - Add support for Kontron OEM commands
 - Update to Kontron Firmware Update command

* Sun Mar 19 2006 <duncan@iceblink.org>  1.8.7-1
 - Add Sun OEM command for blades
 - Increase argument size for raw commands in shell/exec
 - Fix handling of LUNs for LAN interfaces
 - Add IPMIv2 SOL loopback test
 - Add support for IBM OEM SEL messages
 - Disable file paranoia checks on read files by default
 - Support IPMIv2 SOL on older Intel boxes
 - Display message and exit if keepalive fails during SOL
 - Add support for setting VLAN id and priority
 - Add support for FreeBSD OpenIPMI-compatible driver
 - Add support for IPMIv2 Firmware Firewall
 - Fix gcc4 compile warnings
 - Make ipmievd generate pidfile
 - Add initscripts for ipmievd

* Mon Jan 17 2006 <duncan@iceblink.org>  1.8.6-1
 - Fix memory corruption when sending encrypted SOL traffic
 - Add keepalive timer to IPMIv2 SOL sessions

* Sat Jan 14 2006 <duncan@iceblink.org>  1.8.5-1
 - Raise privilege level after creating IPMIv2 session
 - Add support for settable SOL escape character with -e option
 - Add support for Kg BMC key for IPMIv2 authentication with -k option
 - Add support for Tyan IPMIv1.5 SOL with tsol command
 - Add support for PICMG devices
 - Add support for OEM SEL event parsing
 - Add support for command bridging over lan and lanplus interfaces
 - New 'chassis selftest' command
 - Many bufxies and patches from contributors

* Wed May 18 2005 <duncan@iceblink.org>  1.8.2-1
 - Fix FRU reading for large (>255 bytes) areas.
 - Overhaul to ipmievd to support SEL polling in addition to OpenIPMI.
 - Fix LAN parameter segfault when no Ciphers supported by BMC.
 - Fix IPMIv2 support on Intel v2 BMCs (use -o intelplus).
 - Separate option parsing code from main ipmitool source file.
 - Add raw I2C support with IPMI Master Read-Write command.
 - Add support for new 'sdr elist' extended output format.
 - Add support for listing sensors by type with 'sdr type' command.
 - Add support for new 'sel elist' extended output format that
   cross-references events with sensors.
 - Add support for sending dynamically generated platform events
   based on existing sensor information.
 - New '-S' argument to read local SDR cache created with 'sdr dump'.
 - Updated manpage for ipmitool and ipmievd.

* Wed Apr 06 2005 <duncan@iceblink.org>  1.8.1-1
 - Install ipmievd into /usr/sbin

* Wed Mar 16 2005 <duncan@iceblink.org>  1.8.0-1
 - Fix IPMIv2.0 issues
 - Fix chassis boot parameter support
 - Add support for linear sensors
 - Update bmc plugin to work with new Solaris bmc driver (new ioctl
   for interface detection and new STREAMS message-based interface)

* Tue Jan 18 2005 <duncan@iceblink.org>  1.7.0-1
 - Propogate errors correctly so exit status will be useful
 - More consistent display of errors including completion code text
 - Errors and debug is send to stderr now
 - New "sel get" command that will print details about SEL entry
   and corresponding SDR records as well as FRUs via entity association
 - Improved event generator, now supports reading events from text file
 - New "-o oemtype" option for specifying OEM boards
   exsting types are "supermicro" and "intelwv2"
 - New PEF subsystem from Tim Murphy at Dell
 - New "bmc" plugin for Solaris 10 x86
 - Many bugfixes and contributed patches
 - Support for Supermicro BMC OEM authentication method
 - Fix minor problem with LAN parameter setting

* Wed Aug 18 2004 <duncan@iceblink.org>  1.6.0-1
 - Add a README
 - Add support for IPMIv2 and Serial-over-LAN from Newisys
 - Add Solaris x86 lipmi interface
 - Add support for building Solaris packages
 - Add support for building RPMs as non-root user
 - Fix segfault when doing "sel list" (from Matthew Braithwaite)
 - Fix "chassis identify" on some BMCs (from ebrower@sourceforge)
 - Add "bmc info" and related output (from ebrower@sourceforge)
 - new "shell" and "exec" commands
 - lots of other contributed patches

* Sat May 27 2004 <duncan@iceblink.org>  1.5.9-1
 - Add ability to get a particular sensor by name
 - Add ability to set a particular sensor threshold
 - Add support for displaying V2 channel authentication levels
 - Add README for rrdtool scripts in contrib directory
 - Improve lan interface retry handling
 - Support prompting for password or reading from environment
 - Move chaninfo command into channel subcommand
 - Fix reservation ID handling when two sessions open to BMC
 - Fix reading of large FRU data
 - Add configure option for changing binary to ipmiadm for Solaris
 - Fix compile problem on Solaris 8

* Tue Jan 27 2004 <duncan@iceblink.org>  1.5.8-1
 - Enable static compilation of interfaces
 - Fix types to be 64-bit safe
 - Fix compilation problems on Solaris
 - Fix multiple big-endian problems for Solaris/SPARC
 - Fix channel access to save settings to NVRAM
 - Set channel privilege limit to ADMIN during "access on"
 - Enable gratuitous ARP in bmcautoconf.sh
 - Add support for Linux kernel panic messages in SEL output
 - Add support for type 3 SDR records

* Mon Jan  5 2004 <duncan@iceblink.org>  1.5.7-1
 - add IPMIv1.5 eratta fixes
 - additions to FRU printing and FRU multirecords
 - better handling of SDR printing
 - contrib scripts for creating rrdtool graphs

* Thu Dec  4 2003 <duncan@iceblink.org>  1.5.6-1
 - Fix SEL event decoding for generic events
 - Handle empty SEL gracefully when doing "sel list"
 - Fix sdr handling of sensors that do not return a reading
 - Fix for CSV display of sensor readings/units from Fredrik Öhrn

* Tue Nov 25 2003 <duncan@iceblink.org>  1.5.5-1
 - Add -U option for setting LAN username
 - Fix -v usage for plugin interfaces

* Fri Nov 14 2003 <duncan@iceblink.org>  1.5.4-1
 - pull interface plugin api into library
 - fix ipmievd

* Fri Oct 31 2003 <duncan@iceblink.org>  1.5.3-1
 - add -g optin for pedantic ipmi-over-lan communication

* Fri Oct 24 2003 <duncan@iceblink.org>  1.5.2-1
 - add gratuitous arp interval setting

* Wed Oct  8 2003 <duncan@iceblink.org>  1.5.1-1
 - better SEL support
 - fix display bug in SDR list

* Fri Sep  5 2003 <duncan@iceblink.org>  1.5.0-1
 - use automake/autoconf/libtool
 - dynamic loading interface plugins

* Wed May 28 2003 <duncan@iceblink.org>  1.4.0-1
 - make UDP packet handling more robust
 - fix imb driver support

* Thu May 22 2003 <duncan@iceblink.org>  1.3-1
 - update manpage
 - rework of low-level network handling
 - add basic imb driver support

* Wed Apr  2 2003 <duncan@iceblink.org>  1.2-1
 - change command line option parsing
 - support for more chassis commands

* Tue Apr  1 2003 <duncan@iceblink.org>  1.1-1
 - minor fixes.

* Sun Mar 30 2003 <duncan@iceblink.org>  1.0-1
 - Initial release.

