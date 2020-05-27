# vim: set ft=spec: -*- rpm-spec -*-

%def_with nghttp2

# Wireshark has huge number of plugins that are not linked against most of the external libraries
# as they are loaded into wireshark/tshark processes which guarantee that linkage
%set_verify_elf_method unresolved=relaxed

%define _pluginsdir %_libdir/%name/plugins/3.2

Name: wireshark
Version: 3.2.4
Release: alt1

Summary: The BugTraq Award Winning Network Traffic Analyzer
Group: Monitoring
License: GPLv2
Url: http://www.wireshark.org/

Source: http://www.wireshark.org/download/src/%name-%version.tar
Source2: %name.control
Source3: %name.watch

Patch: %name-%version-alt.patch

# Automatically added by buildreq on Sun Dec 23 2007
BuildRequires: control doxygen flex gcc-c++ libadns-devel libcap-devel libcom_err-devel libgnutls-openssl-devel libgcrypt-devel zlib-devel
BuildRequires: libkrb5-devel libpcap-devel libpcre-devel libportaudio2-devel libssl-devel python3 unzip xml-utils xsltproc perl-Pod-Parser perl-devel
BuildRequires: liblua5.1-compat-devel
BuildRequires: libssh-devel
BuildRequires: libnl-devel
%if_with nghttp2
BuildRequires: libnghttp2-devel
%endif
BuildRequires: liblz4-devel
BuildRequires: libxml2-devel
BuildRequires: libspandsp6-devel
BuildRequires: libsnappy-devel
BuildRequires: libcares-devel
BuildRequires: libsmi-devel
BuildRequires: libGeoIP-devel
BuildRequires: libglib2-devel
BuildRequires: qt5-base-devel qt5-multimedia-devel qt5-tools-devel qt5-svg-devel
BuildRequires: cmake
BuildRequires: libsystemd-devel
BuildRequires: libmaxminddb-devel
BuildRequires: asciidoctor
BuildRequires: libbcg729-devel >= 1.0.4-alt1
BuildRequires: libsbc-devel
BuildRequires: libnettle-devel
BuildRequires: libminizip-devel
BuildRequires: libzstd-devel
BuildRequires: libspeexdsp-devel
BuildRequires: libbrotli-devel
BuildRequires: git
BuildRequires(pre):rpm-build-xdg

%package base
Summary: Wireshark base package
Group: Monitoring
Obsoletes: ethereal-libs < 0.10.10
Obsoletes: libwiretap
Obsoletes: ethereal-base

%package qt5
Summary: QT5 GUI for Wireshark package
Group: Monitoring
Requires: %name-base = %EVR
Provides: %name = %EVR
Requires: url_handler
Obsoletes: ethereal

%package -n tshark
Summary: Console GUI for Wireshark package
Group: Monitoring
Requires: %name-base = %EVR
Obsoletes: tethereal

%package devel
Summary: Development environment for wireshark extensions 
Group: Development/C
Requires: wireshark-base = %EVR
Obsoletes: libwiretap-devel < %EVR

%description
Wireshark (formerly Ethereal) is a network protocol analyzer, or
"packet sniffer", that lets you capture and interactively browse
the contents of network frames. The goal of the project is to
create a commercial-quality packet analyzer for Unix, and the
most useful packet analyzer on any platform.

%description base
Wireshark (formerly Ethereal) is a network protocol analyzer, or
"packet sniffer", that lets you capture and interactively browse
the contents of network frames. The goal of the project is to
create a commercial-quality packet analyzer for Unix, and the
most useful packet analyzer on any platform.

This package lays base for libpcap, a packet capture and filtering
library, contains command-line utilities, plugins and documentation
for wireshark. A graphical user interface is packaged separately to
GTK+/QT5 packages.

%description qt5
This package contains QT5 GUI ie. the wireshark -- application.

%description -n tshark
This package contains console wireshark application.

%description devel
This package contains development files needed to develop wireshark
extensions.

%prep
%setup
%patch -p1

%build
# Some plugins use C++ and need lcxa. It can't be loaded
# dynamically, so all binaries should be linked with it.
%ifarch %e2k
cc --version | grep -q '^lcc:1.21' && export LIBS+=" -lcxa"
%endif
%cmake -DBUILD_sharkd=off
%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot%_libdir/%name/plugins/%version/*.la

mkdir -p %buildroot{%_controldir,%_menudir,%_datadir/applications,%_niconsdir,%_liconsdir,%_miconsdir}
cp -p wireshark.desktop %buildroot%_datadir/applications/%name-qt5.desktop
cp -p image/wsicon16.png %buildroot%_miconsdir/wireshark.png
cp -p image/wsicon32.png %buildroot%_niconsdir/wireshark.png
cp -p image/wsicon48.png %buildroot%_liconsdir/wireshark.png

mkdir -p %buildroot%_includedir/wiretap
install -p -m644 wiretap/wtap.h %buildroot%_includedir/wiretap/wtap.h

install -p -m755 %_sourcedir/%name.control %buildroot%_controldir/%name-capture

# Rename qt5 binary:
mv -v %buildroot%_bindir/%name %buildroot%_bindir/%name-qt5

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name-qt5
%_bindir/%name	%_bindir/%name-qt5	20
_EOF_

%pre base
%pre_control %name-capture

%post base
%post_control -s relaxed %name-capture

%files base
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README* doc/README.*
%config %_controldir/%name-capture
%_bindir/capinfos
%_bindir/captype
%attr(700,root,root) %verify(not mode,group) %_bindir/dumpcap
%_bindir/editcap
%_bindir/mergecap
%_bindir/randpkt
%_bindir/rawshark
%_bindir/text2pcap
%_bindir/reordercap
%_bindir/mmdbresolve
%_man1dir/androiddump.*
%_man1dir/capinfos.*
%_man1dir/captype.*
%_man1dir/ciscodump.*
%_man1dir/dpauxmon.*
%_man1dir/udpdump.*
%_man1dir/sshdump.*
%_man1dir/mmdbresolve.*
%_man1dir/randpkt.*
%_man1dir/randpktdump.*
%_man1dir/sdjournal.*
%_man1dir/dftest.*
%_man1dir/dumpcap.*
%_man1dir/editcap.*
%_man1dir/mergecap.*
%_man1dir/rawshark.*
%_man1dir/text2pcap.*
%_man1dir/reordercap.*
%_man4dir/wireshark-filter.*
%_man4dir/extcap.*
%_datadir/%name
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%dir %_pluginsdir
%dir %_libdir/%name/extcap
%_libdir/%name/extcap/*
%_pluginsdir/*
%_libdir/lib%name.so.*
%_libdir/libwsutil.so.*
%_libdir/libwiretap.so.*
%_man1dir/wireshark.*
%_miconsdir/wireshark.png
%_niconsdir/wireshark.png
%_liconsdir/wireshark.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/*/apps/wireshark.png
%_xdgmimedir/packages/%name.xml
%_datadir/appdata/wireshark.appdata.xml

%files qt5
%_altdir/%name-qt5
%_bindir/wireshark-qt5
%_datadir/applications/%name-qt5.desktop

%files -n tshark
%_bindir/tshark
%_man1dir/tshark.*

%files devel
%_bindir/idl2wrs
%_includedir/wiretap
%_libdir/libwiretap.so
%_includedir/wireshark
%_libdir/libwireshark.so
%_libdir/libwsutil.so
%_pkgconfigdir/wireshark.pc

%changelog
* Mon May 25 2020 Anton Farygin <rider@altlinux.ru> 3.2.4-alt1
- 3.2.4
- fixes:
   * the NFS dissector could crash. CVE-2020-13164

* Tue Apr 14 2020 Anton Farygin <rider@altlinux.ru> 3.2.3-alt1
- 3.2.3
- fixes:
   * the BACapp dissector could crash. CVE-2020-11647

* Wed Apr 01 2020 Anton Farygin <rider@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Thu Mar 12 2020 Anton Farygin <rider@altlinux.ru> 3.0.9-alt1
- 3.0.9
- fixes:
   * LTE RRC dissector could leak memory. CVE-2020-9431
   * WiMax DLMAP dissector could crash. CVE-2020-9430

* Tue Jan 21 2020 Anton Farygin <rider@altlinux.ru> 3.0.8-alt1
- 3.0.8
- disabled sharkd build
- fixes:
   * BT ATT dissector crash. CVE-2020-7045

* Mon Dec 09 2019 Anton Farygin <rider@altlinux.ru> 3.0.7-alt1
- 3.0.7
- fixes:
   * CMS dissector crash. CVE-2019-19553

* Mon Nov 18 2019 Anton Farygin <rider@altlinux.ru> 3.0.6-alt2
- changed BuildRequires from liblua5.1-devel to liblua5.1-compat-devel

* Sun Nov 10 2019 Anton Farygin <rider@altlinux.ru> 3.0.6-alt1
- 3.0.6

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 3.0.5-alt1
- 3.0.5

* Mon Sep 16 2019 Anton Farygin <rider@altlinux.ru> 3.0.4-alt1
- 3.0.4
- fixes:
    * Gryphon dissector infinite loop. CVE-2019-16319

* Mon Jul 22 2019 Anton Farygin <rider@altlinux.ru> 3.0.3-alt1
- 3.0.3
- fixes:
    * ASN.1 BER and related dissectors crash. CVE-2019-13619

* Fri May 31 2019 Anton Farygin <rider@altlinux.ru> 3.0.2-alt1
- 3.0.2
- fixes:
    * Wireshark dissection engine crash. CVE-2019-12295

* Wed Apr 10 2019 Anton Farygin <rider@altlinux.ru> 3.0.1-alt1
- 3.0.1
- fixes:
    * NetScaler file parser crash. CVE-2019-10895
    * SRVLOC dissector crash. CVE-2019-10899
    * IEEE 802.11 dissector infinite loop. CVE-2019-10897
    * GSUP dissector infinite loop. CVE-2019-10898
    * Rbm dissector infinite loop. CVE-2019-10900
    * GSS-API dissector crash. CVE-2019-10894
    * DOF dissector crash. CVE-2019-10896
    * TSDNS dissector crash. CVE-2019-10902
    * LDSS dissector crash. CVE-2019-10901
    * DCERPC SPOOLSS dissector crash. CVE-2019-10903

* Tue Mar 19 2019 Anton Farygin <rider@altlinux.ru> 3.0.0-alt1
- 3.0.0
- removed package with documentation

* Mon Mar 04 2019 Anton Farygin <rider@altlinux.ru> 2.6.7-alt1
- 2.6.7
- fixes:
     * ASN.1 BER and related dissectors crash. CVE-2019-9209
     * TCAP dissector crash. CVE-2019-9208

* Sat Jan 19 2019 Anton Farygin <rider@altlinux.ru> 2.6.6-alt2
- libwiretap included to wireshark-base package
- libwiretap-devel included to wireshark-devel package

* Sun Jan 13 2019 Anton Farygin <rider@altlinux.ru> 2.6.6-alt1
- 2.6.6
- fixes:
     * The 6LoWPAN dissector could crash. CVE-2019-5716
     * The P_MUL dissector could crash. CVE-2019-5717
     * The RTSE dissector and other dissectors could crash. CVE-2019-5718
     * The ISAKMP dissector could crash. CVE-2019-5719

* Mon Dec 03 2018 Anton Farygin <rider@altlinux.ru> 2.6.5-alt1
- 2.6.5
- added devel package (closes: #29869)
- fixes:
     * The Wireshark dissection engine could crash. CVE-2018-19625
     * The DCOM dissector could crash. CVE-2018-19626
     * The LBMPDM dissector could crash. CVE-2018-19623
     * The MMSE dissector could go into an infinite loop. CVE-2018-19622
     * The IxVeriWave file parser could crash. CVE-2018-19627
     * The PVFS dissector could crash. CVE-2018-19624
     * The ZigBee ZCL dissector could crash. CVE-2018-19628

* Tue Oct 16 2018 Michael Shigorin <mike@altlinux.org> 2.6.4-alt1.1
- introduce nghttp2 knob (on by default)
- E2K: link against -lcxa explicitly with lcc below 1.23

* Sat Oct 13 2018 Anton Farygin <rider@altlinux.ru> 2.6.4-alt1
- 2.6.4 (fixes: CVE-2018-18227, CVE-2018-18225, CVE-2018-18225,  CVE-2018-12086)
- disabled build gtk+ UI

* Mon Sep 03 2018 Anton Farygin <rider@altlinux.ru> 2.6.3-alt1
- 2.6.3 (fixes: CVE-2018-16056, CVE-2018-16057, CVE-2018-16058)

* Sat Jul 21 2018 Anton Farygin <rider@altlinux.ru> 2.6.2-alt1
- 2.6.2  (fixes: CVE-2018-14370, CVE-2018-14367, CVE-2018-14369, CVE-2018-14368, CVE-2018-14341, CVE-2018-14339, CVE-2018-14343, CVE-2018-14340, CVE-2018-14344, CVE-2018-14342)

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt2
- Fix FTBFS (Add missing rpm-build-xdg).

* Thu May 24 2018 Anton Farygin <rider@altlinux.ru> 2.6.1-alt1
- 2.6.1 (fixes: CVE-2018-11359, CVE-2018-11361, CVE-2018-11358, CVE-2018-11360, CVE-2018-11356, CVE-2018-11357, CVE-2018-11355, CVE-2018-11354, CVE-2018-11362)

* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 2.6.0-alt2
- patch for wireshark #14638 l16mono.so issue is applied

* Wed May 02 2018 Anton Farygin <rider@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Apr 03 2018 Anton Farygin <rider@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 2.4.5-alt1
- 2.4.5
- fixes:
     * wnpa-sec-2018-05 The IEEE 802.11 dissector could crash. CVE-2018-7335
     * wnpa-sec-2018-06 Multiple dissectors could go into large infinite loops. All ASN.1
       BER dissectors, along with the DICOM, DMP, LLTD, OpenFlow, RELOAD, RPCoRDMA, RPKI-Router,
       S7COMM, SCCP, Thread, Thrift, USB and WCCP dissectors were susceptible. CVE-2018-7321, CVE-2018-7322, 
       CVE-2018-7323, CVE-2018-7324, CVE-2018-7325, CVE-2018-7326, CVE-2018-7327, CVE-2018-7328, CVE-2018-7329,
       CVE-2018-7330, CVE-2018-7331, CVE-2018-7332, CVE-2018-7333
     * wnpa-sec-2018-07 The UMTS MAC dissector could crash. CVE-2018-7334
     * wnpa-sec-2018-08 The DOCSIS dissector could crash. CVE-2018-7337
     * wnpa-sec-2018-09 The FCP dissector could crash. CVE-2018-7336
     * wnpa-sec-2018-10 The SIGCOMP dissector could crash. CVE-2018-7320
     * wnpa-sec-2018-11 The pcapng file parser could crash. CVE-2018-7420
     * wnpa-sec-2018-12 The IPMI dissector could crash. CVE-2018-7417
     * wnpa-sec-2018-13 The SIGCOMP dissector could crash. CVE-2018-7418
     * wnpa-sec-2018-14 The NBAP disssector could crash. CVE-2018-7419

* Wed Jan 17 2018 Anton Farygin <rider@altlinux.ru> 2.4.4-alt1
- 2.4.4
- fixes:
    * wnpa-sec-2018-01  Multiple dissectors could crash. CVE-2018-5336
    * wnpa-sec-2018-03  The IxVeriWave file parser could crash.  CVE-2018-5334
    * wnpa-sec-2018-04  The WCP dissector could crash. CVE-2018-5335

* Sat Dec 09 2017 Anton Farygin <rider@altlinux.ru> 2.4.3-alt1
- 2.4.3
- fixes:
     * wnpa-sec-2017-49 CIP Safety dissector crash CVE-2017-17085
     * wnpa-sec-2017-48 NetBIOS dissector crash CVE-2017-17083
     * wnpa-sec-2017-47 IWARP_MPA dissector crash CVE-2017-17084

* Sun Oct 15 2017 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- 2.4.2
- fixes:
     * wnpa-sec-2017-42 BT ATT dissector crash CVE-2017-15192
     * wnpa-sec-2017-43 MBIM dissector crash CVE-2017-15193
     * wnpa-sec-2017-44 DMP dissector crash CVE-2017-15191
     * wnpa-sec-2017-45 RTSP dissector crash CVE-2017-15190
     * wnpa-sec-2017-46 DOCSIS infinite loop CVE-2017-15189

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 2.4.1-alt1
- 2.4.1 with following fixes:
     * wnpa-sec-2017-38 MSDP dissector infinite loop CVE-2017-13767
     * wnpa-sec-2017-39 Profinet I/O buffer overrun CVE-2017-13766
     * wnpa-sec-2017-40 Modbus dissector crash CVE-2017-13764
     * wnpa-sec-2017-41 IrCOMM dissector buffer overrun CVE-2017-13765

* Sun Jul 30 2017 Anton Farygin <rider@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Fri Jul 21 2017 Anton Farygin <rider@altlinux.ru> 2.2.8-alt1
- new version:
     * wnpa-sec-2017-13 WBMXL dissector infinite loop CVE-2017-7702, CVE-2017-11410
     * wnpa-sec-2017-28 openSAFETY dissector memory exhaustion CVE-2017-9350, CVE-2017-11411
     * wnpa-sec-2017-34 AMQP dissector crash CVE-2017-11408
     * wnpa-sec-2017-35 MQ dissector crash CVE-2017-11407
     * wnpa-sec-2017-36 DOCSIS infinite loop CVE-2017-11406

* Sun Jun 04 2017 Anton Farygin <rider@altlinux.ru> 2.2.7-alt1
- new version with these security fixes:
     * wnpa-sec-2017-22 Bazaar dissector infinite loop CVE-2017-9352
     * wnpa-sec-2017-23 DOF dissector read overflow CVE-2017-9348
     * wnpa-sec-2017-24 DHCP dissector read overflow CVE-2017-9351
     * wnpa-sec-2017-25 SoulSeek dissector infinite loop CVE-2017-9346
     * wnpa-sec-2017-26 DNS dissector infinite loop CVE-2017-9345
     * wnpa-sec-2017-27 DICOM dissector infinite loop CVE-2017-9349
     * wnpa-sec-2017-28 openSAFETY dissector memory exhaustion CVE-2017-9350
     * wnpa-sec-2017-29 BT L2CAP dissector divide by zero CVE-2017-9344
     * wnpa-sec-2017-30 MSNIP dissector crash CVE-2017-9343
     * wnpa-sec-2017-31 ROS dissector crash CVE-2017-9347
     * wnpa-sec-2017-32 RGMP dissector crash CVE-2017-9354
     * wnpa-sec-2017-30 MSNIP dissector crash CVE-2017-9343
     * wnpa-sec-2017-31 ROS dissector crash CVE-2017-9347
     * wnpa-sec-2017-32 RGMP dissector crash CVE-2017-9354
     * wnpa-sec-2017-33 IPv6 dissector crash CVE-2017-9353

* Fri Apr 14 2017 Anton Farygin <rider@altlinux.ru> 2.2.6-alt1
- new version with these security fixes:
     * wnpa-sec-2017-12 IMAP dissector crash CVE-2017-7703
     * wnpa-sec-2017-13 WBMXL dissector infinite loop CVE-2017-7702
     * wnpa-sec-2017-14 NetScaler file parser infinite loop CVE-2017-7700
     * wnpa-sec-2017-15 RPCoRDMA dissector infinite loop CVE-2017-7705
     * wnpa-sec-2017-16 BGP dissector infinite loop CVE-2017-7701
     * wnpa-sec-2017-17 DOF dissector infinite loop CVE-2017-7704

* Fri Mar 10 2017 Anton Farygin <rider@altlinux.ru> 2.2.5-alt2
- fixed liblua devel requires

* Tue Mar 07 2017 Anton Farygin <rider@altlinux.ru> 2.2.5-alt1
- new version

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.4-alt2
- NMU: new lua 5.1 BR:

* Fri Feb 03 2017 Anton Farygin <rider@altlinux.ru> 2.2.4-alt1
- new version

* Wed Dec 21 2016 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- new version

* Mon Nov 21 2016 Anton Farygin <rider@altlinux.ru> 2.2.2-alt1
- new version, in which following vulnerabilities have been fixed:
     * CVE-2016-9372 Profinet I/O long loop.
     * CVE-2016-9373 DCERPC crash.
     * CVE-2016-9374 AllJoyn crash.
     * CVE-2016-9375 DTN infinite loop.
     * CVE-2016-9376 OpenFlow crash.

* Thu Oct 13 2016 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- new version

* Fri Sep 09 2016 Anton Farygin <rider@altlinux.ru> 2.2.0-alt1
- new version

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- new version

* Thu Jun 16 2016 Anton Farygin <rider@altlinux.ru> 2.0.4-alt1
- new version

* Sun May 22 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.3-alt1
- 2.0.3

* Mon Mar  7 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Jan  1 2016 Terechkov Evgenii <evg@altlinux.org> 2.0.1-alt3
- doc subpackage made noarch (thanks, repocop)
- add alternatives support for gtk+/qt5
- spec cleanup

* Thu Dec 31 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.1-alt2
- Revive gtk+ subpackage

* Thu Dec 31 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.1-alt1
- 2.0.1
- %name-gtk+ obsoleted by %name-qt5

* Sat Oct 17 2015 Anton Farygin <rider@altlinux.ru> 1.12.8-alt1
- new version 1.12.8

* Fri Jun 19 2015 Anton Farygin <rider@altlinux.ru> 1.12.6-alt1
- new version

* Sat May 23 2015 Anton Farygin <rider@altlinux.ru> 1.12.5-alt1
- new version 1.12.5

* Fri Mar 06 2015 Anton Farygin <rider@altlinux.ru> 1.12.4-alt1
- new version 1.12.4

* Mon Jan 12 2015 Anton Farygin <rider@altlinux.ru> 1.12.3-alt1
- new version 1.12.3

* Tue Nov 18 2014 Anton Farygin <rider@altlinux.ru> 1.12.2-alt1
- new version 1.12.2

* Thu Sep 18 2014 Anton Farygin <rider@altlinux.ru> 1.12.1-alt1
- new version 1.12.1

* Tue Sep 02 2014 Anton Farygin <rider@altlinux.ru> 1.12.0-alt1
- new version

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 1.10.8-alt1
- new version 1.10.8

* Tue Apr 29 2014 Anton Farygin <rider@altlinux.ru> 1.10.7-alt1
- new version

* Thu Mar 13 2014 Anton Farygin <rider@altlinux.ru> 1.10.6-alt1
- new version

* Wed Feb 19 2014 Anton Farygin <rider@altlinux.ru> 1.10.5-alt1
- new version

* Thu Nov 07 2013 Anton Farygin <rider@altlinux.ru> 1.10.3-alt1
- new version

* Thu Oct 10 2013 Anton Farygin <rider@altlinux.ru> 1.10.2-alt1
- new version

* Tue Jun 25 2013 Anton Farygin <rider@altlinux.ru> 1.10.0-alt1
- new version

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- new version

* Wed Jun 06 2012 Anton Farygin <rider@altlinux.ru> 1.6.8-alt1
- new version

* Fri Sep 16 2011 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- new version

* Thu Jun 09 2011 Anton Farygin <rider@altlinux.ru> 1.6.0-alt1
- new version

* Thu Mar 24 2011 Anton Farygin <rider@altlinux.ru> 1.4.4-alt2
- add zlib-devel requires

* Wed Mar 09 2011 Anton Farygin <rider@altlinux.ru> 1.4.4-alt1
- new version

* Wed Nov 24 2010 Anton Farygin <rider@altlinux.ru> 1.4.2-alt1
- new version

* Thu Oct 14 2010 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- new version, fixed CVE-2010-3445 (closes: #24297)
- user guide updated

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- new version

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 1.2.10-alt1
- new version

* Mon Jun 28 2010 Anton Farygin <rider@altlinux.ru> 1.2.9-alt1
- new version

* Thu Jan 28 2010 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- new version, multiple vulnerabilities fixed by upstream (closes #20836)

* Fri Jun 19 2009 Alexander Bokovoy <ab@altlinux.org> 1.2.0-alt2
- Add LUA support for internal scripting
  -- Disabled by default, edit %_datadir/%name/init.lua to enable
- Include libwsutil.so.* into build

* Fri Jun 19 2009 Alexander Bokovoy <ab@altlinux.org> 1.2.0-alt1
- [1.2.0]

* Sat May 23 2009 Alexander Bokovoy <ab@altlinux.org> 1.0.8-alt1
- [1.0.8]
 + PCNFSD dissector crashes fixed, no proper CVE number yet

* Sun Apr 26 2009 Alexander Bokovoy <ab@altlinux.org> 1.0.7-alt1
- [1.0.7]
 + CVE-2009-1210
 + CVE-2009-1267
 + CVE-2009-1268
 + CVE-2009-1269

* Fri Oct 24 2008 Sir Raorn <raorn@altlinux.ru> 1.0.4-alt1
- [1.0.4]
 + CVE-2008-4685
 + CVE-2008-4684
 + CVE-2008-4683
 + CVE-2008-4682
 + CVE-2008-4681
 + CVE-2008-4680

* Fri Sep 05 2008 Sir Raorn <raorn@altlinux.ru> 1.0.3-alt1
- [1.0.3]
 + The NCP dissector was susceptible to a number of problems,
   including buffer overflows and an infinite loop.
 + Wireshark could crash while uncompressing zlib-compressed
   packet data.
 + Wireshark could crash while reading a Tektronix .rf5 file.

* Mon Jul 14 2008 Sir Raorn <raorn@altlinux.ru> 1.0.2-alt1
- [1.0.2]
 + Some crashes fixed before they were submitted to CVE list

* Wed Jul 02 2008 Sir Raorn <raorn@altlinux.ru> 1.0.1-alt1
- [1.0.1]
 + CVE-2008-1563
 + CVE-2008-1562  	
 + CVE-2008-1561

* Sun Mar 30 2008 Sir Raorn <raorn@altlinux.ru> 1.0.0-alt1
- [1.0.0] (YAY!)
 + Some crashes fixed before they were submitted to CVE list
- User Guide updated

* Mon Mar 10 2008 Sir Raorn <raorn@altlinux.ru> 0.99.8-alt1
- [0.99.8]
 + CVE-2008-1072
 + CVE-2008-1071
 + CVE-2008-1070
- User Guide updated
- New tool rawshark(1)
- Traffic capture now control(8)led by %name-capture facility

* Sun Dec 23 2007 Sir Raorn <raorn@altlinux.ru> 0.99.7-alt1
- [0.99.7]
 + CVE-2007-6451
 + CVE-2007-6450
 + CVE-2007-6441
 + CVE-2007-6439
 + CVE-2007-6438
 + CVE-2007-6121
 + CVE-2007-6120
 + CVE-2007-6119
 + CVE-2007-6118
 + CVE-2007-6117
 + CVE-2007-6116
 + CVE-2007-6115
 + CVE-2007-6114
 + CVE-2007-6113
 + CVE-2007-6112
 + CVE-2007-6111
- Enabled kerberos, gcrypt and gnutls support
- Enabled RTP player for VoIP captures

* Tue Jul 10 2007 Sir Raorn <raorn@altlinux.ru> 0.99.6-alt2
- Use url_handler for default webbrowser (closes: #11692)

* Fri Jul 06 2007 Sir Raorn <raorn@altlinux.ru> 0.99.6-alt1
- [0.99.6]
 + CVE-2007-3389
 + CVE-2007-3390
 + CVE-2007-3391
 + CVE-2007-3392
 + CVE-2007-3393

* Sun Feb 04 2007 Sir Raorn <raorn@altlinux.ru> 0.99.5-alt1
- [0.99.5]
 + CVE-2007-0459
 + CVE-2007-0458
 + CVE-2007-0457
 + CVE-2007-0456
- User Guide updated

* Sat Nov 04 2006 Sir Raorn <raorn@altlinux.ru> 0.99.4-alt1
- [0.99.4]

* Tue Jul 18 2006 Sir Raorn <raorn@altlinux.ru> 0.99.2-alt1
- [0.99.2]
 + CVE-2006-3627
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3628
 + CVE-2006-3629
 + CVE-2006-3630
 + CVE-2006-3628
 + CVE-2006-3631
 + CVE-2006-3632
- Renaamed from ethereal to wireshark, added Obsoletes
- Rediffed all patches
- Updated buildrequires

* Wed Apr 26 2006 Sir Raorn <raorn@altlinux.ru> 0.99.0-alt1
- [0.99.0]
- User Guide updated

* Sun Mar 19 2006 Sir Raorn <raorn@altlinux.ru> 0.10.14-alt2
- libethereal should be linked with libadns and libm
- %%_iconsdir -> %%_niconsdir

* Wed Dec 28 2005 Sir Raorn <raorn@altlinux.ru> 0.10.14-alt1
- [0.10.14]

* Thu Oct 20 2005 Sir Raorn <raorn@altlinux.ru> 0.10.13-alt1
- [0.10.13]

* Mon Oct 10 2005 Sir Raorn <raorn@altlinux.ru> 0.10.12-alt2
- Fix unexpanded macros
- Changed -doc group to Documentation

* Sat Jul 30 2005 Sir Raorn <raorn@altlinux.ru> 0.10.12-alt1
- [0.10.12]
- Updated EUG
- Added patches from debian:
  + diameter_vendors
  + drop-capabilities
  + giop-buffer

* Tue May 10 2005 Sir Raorn <raorn@altlinux.ru> 0.10.11-alt1
- [0.10.11]

* Tue Mar 15 2005 Sir Raorn <raorn@altlinux.ru> 0.10.10-alt1
- [0.10.10]
- Fixed:
   + CAN-2005-0699
   + CAN-2005-0704
   + CAN-2005-0705
- ethereal-devel and idl2eth are unusable.  Dropped
- libwiretap is back

* Sat Jan 22 2005 Sir Raorn <raorn@altlinux.ru> 0.10.9-alt1
- [0.10.9]
- Fixed:
   + CAN-2004-1139
   + CAN-2004-1140
   + CAN-2004-1141
   + CAN-2004-1142
   + CAN-2005-0006
   + CAN-2005-0007
   + CAN-2005-0008
   + CAN-2005-0009
   + CAN-2005-0010
   + CAN-2005-0084
- Debian fixes:
  * Fixed dissect_cmip_InvokeIDType declaration (FTBFS with gcc-4.0)
  * epan/dissectors/packet-giop.c: fixed segfault with some GIOP packets
  * ethereal_gen.py: fixed some includes
- ALT fixes (based on Debian):
  * epan/prefs.c: changed default font to "Fixed 11"
  * epan/prefs.c: Use url_handler.sh as default browser
- Removed -kde subpackage (obsoleted by -gtk+) (closes: #5859)
- Removed -consolehelper subpackage.  Running ethereal with root privileges
  is insecure, do it at your own risc (closes: #3520)
- Added menu entry and icons (closes: #5006)
- SNMP support disabled due to overbloated dependencies
- Separated -libs and -devel. Header files list borrowed from Debian
- libwiretap-devel is now obsoleted by ethereal-devel
- Packaged idl2eth utility (idl2eth package)

* Fri Sep 03 2004 Sir Raorn <raorn@altlinux.ru> 0.10.6-alt1
- [0.10.6]
- Moved libwiretap to seperate subpackage
- Added libwiretap-devel
- Added EUG (in -doc subpackage)

* Thu Jul 08 2004 Stanislav Ievlev <inger@altlinux.org> 0.10.5-alt1
- 1.10.5

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.4-alt1
- 0.10.4

* Fri Apr 02 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.3-alt2
- Fixed:
   + Some libraries were missing

* Thu Apr 01 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.3-alt1
- 0.10.3
- Removed:
   + %name-gnome subpackage (outdated and non-usable anymore)

* Tue Feb 24 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.2-alt1
- 0.10.2
- Removed:
   + Stock icons (added into the release tarball finally)
   + Makefile patch
- Added:
   + mergecap, idl2eth, text2pcap and their man-pages
   + man page for ethereal-filter

* Fri Feb 20 2004 Alexander Bokovoy <ab@altlinux.ru> 0.10.1-alt1
- 0.10.1 
- Fixed:
   + Wrong dependencies between makefiles
- Added:
   + Missing stock GTK+ 2.2.4 icons used by Ethereal

* Thu Nov 06 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.16-alt1
- 0.9.16
- Fixed:
   + CAN-2003-0925
   + CAN-2003-0926
   + CAN-2003-0927
- Added:
   + --enable Master switch allows to build this package for 
     ALT Linux Master 2.2
   + Build GTK+ 2.x frontend instead of GTK+ 1.x
- Updated:
   + PAM entry to follow current PAM policy in ALT Linux Sisyphus

* Tue Jun 17 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.13-alt1
- Updated to 0.9.13, fixes a number of vulnerabilities.
- Added plugins path to findprov lib path

* Tue Mar 11 2003 Dmitry V. Levin <ldv@altlinux.org> 0.9.11-alt1
- Updated to 0.9.11:
  "This release fixes  the packaging, and adds minor updates
  and fixes for the following protocols:
  AFS, OpenBSD enc(4), RTP, SCSI, SIP, SMPP, SSH
  IA64 support has been improved."

* Mon Mar 10 2003 Alexander Bokovoy <ab@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Mon Dec 09 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Tue Oct 01 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.7-alt1
- New version
- Fixed:
    + Usermode bindings fixed
    + %name-usermode name is changed to %name-consolehelper

* Wed Aug 21 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.6-alt1
- Security update [CAN-2002-0834]
- Group changed to Monitoring

* Thu Apr 18 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.3-alt1
- Security update

* Wed Jan 23 2002 Alexander Bokovoy <ab@altlinux.ru> 0.9.0-alt1
- First build for ALT Linux

* Mon Jan 07 2002 Henri Gomez <hgomez@slib.fr>
- 0.9.0
- built on Redhat 6.2 + updates
- Too many updates to report here, take a look in NEWS

* Tue Oct 23 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.20

* Thu Jul 20 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.19
- RPM built on Redhat 6.2, updates, rpm 3.0.5 and ucd-snmpd 4.2
  against libpcap 0.6.2 (tcpdump 3.6.2) and openssl 0.9.6

* Thu May 17 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.18
- Many improvement, take a look at NEWS in %%doc
- Reduced the changelog history in .spec

* Thu Apr 26 2001 Henri Gomez <hgomez@slib.fr>
- rebuilt under Redhat 6.2 + updates
- reverted from rpm 4.0.2 to 3.0.5 for better compatibility with Redhat 6.x
- thanks Riku for the great refactory of the spec

* Thu Apr 26 2001 Riku Meskanen <mesrik@iki.fi>
- new binary package rearrangement, separated stuff that needs X11
- I changed, and I'm proposing group to Applications/Network for now ... as
  the /usr/share/doc/rpm-*/GROUPS 'official' list does not have appropriate
  group for networking applications and leads them to be scattered around.
  The tcpdump is now at System/Internet and nmap from Applications/System,
  the X11/* group is now on current distros mostly dead ... the X11/* tree
  seems to still live on contrib packages. Well if it's necessary to show X11
  in group-name, I would rather suggest then Applications/Network{,ing}/X11
  would make more sense and keep all applications closer together and all
  it's bits and bobs easier locatable on multiple packages are built from
  one source package.

* Mon Apr 23 2001 Riku Meskanen <mesrik@iki.fi>
- rebuilt for RedHat 7.1
- created support for usermode
- added icons & config files for gnome and kde desktop integration
- added %%dir %%_libdir/ethereal/plugins to get clean uninstall
- further spec file minor cleaning, converted absolute paths to
  macros for better relocatability

* Sun Apr 16 2001  Henri Gomez <hgomez@slib.fr>
- 0.8.17 (grabbed corrected 0.8.17a archive)
- RPM built on Redhat 6.2, updates, rpm 4.0

* Tue Mar 06 2001 Henri Gomez <hgomez@slib.fr>
- 0.8.16
- RPM built on Redhat 6.1, updates, rpm 3.0.5 and libpcap-0.4-19
- ucd-snmp used 0.4.2-5 (added -lcrypto)

