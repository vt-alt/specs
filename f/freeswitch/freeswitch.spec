Name: freeswitch
Version: 1.10.2
Release: alt1
Epoch: 1

Summary: FreeSWITCH open source telephony platform
License: MPL
Group: System/Servers
Url: http://www.freeswitch.org/

Source: %name-%version.tar
Patch0: %name-%version-alt.patch
Source1: %name.init
Source2: %name.tmpfiles
Source3: %name.sysconfig
Source4: modules.conf
Source5: fs_cli.conf

BuildRequires: gcc-c++ gsmlib-devel libalsa-devel
BuildRequires: libgnutls-devel libncurses-devel libssl-devel libunixODBC-devel
BuildRequires: gdbm-devel db4-devel libldap-devel libcurl-devel libjpeg-devel
BuildRequires: libspeex-devel libspeexdsp-devel libsqlite3-devel libX11-devel libmp4v2-devel
BuildRequires: libxmlrpc-devel libyaml-devel libiksemel-devel libedit-devel
BuildRequires: libsndfile-devel libpcre-devel liblua5-devel
BuildRequires: libilbc1-devel >= 0.0.2-alt3 libjs-devel flite-devel
BuildRequires: libtiff-devel libldap-devel libsoundtouch-devel libldns-devel
BuildRequires: libpcap-devel perl-devel
BuildRequires: libcelt-devel libmpg123-devel liblame-devel libshout2-devel
BuildRequires: libopenr2.3-devel
BuildRequires: libnet-snmp-devel libnl-devel libsensors3-devel zlib-devel
BuildRequires: libuuid-devel postgresql-devel
BuildRequires: java-common java-1.8.0-openjdk-devel /proc libavformat-devel libavutil-devel libavresample-devel libswscale-devel
BuildRequires: libmemcached-devel libopus-devel libbroadvoice-devel libcodec2-devel libImageMagick-devel 
BuildRequires: flite-devel libyuv-devel libfreetype-devel libvpx-devel libsilk-devel libg7221-devel libvlc-devel libavcodec-devel libx264-devel

%ifarch %ix86 x86_64
BuildRequires: yasm
%endif

%description
FreeSWITCH is an open source telephony platform designed to facilitate
the creation of voice and chat driven products scaling from a soft-phone
up to a soft-switch.  It can be used as a simple switching engine, a media
gateway or a media server to host IVR applications using simple scripts
or XML to control the callflow.
It supports various communication technologies such as SIP, H.323 and 
GoogleTalk making it easy to interface with other open source PBX systems
such as sipX, OpenPBX, Bayonne, YATE or Asterisk.

%package -n lib%name
Summary: FreeSWITCH shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: Development package for FreeSWITCH
Group: Development/C
Requires: lib%name = %version-%release


%package daemon
Summary: FreeSWITCH daemon
Group: System/Servers
Requires: lib%name = %version-%release
Requires: freeswitch-sounds-default


%package lang-de
Summary: German language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-en
Summary: English language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-es
Summary: Spanish language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-fr
Summary: French language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-he
Summary: Hebrew language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-ru
Summary: Russian language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package lang-pt
Summary: Portugal language dependand modules and sounds for the FreeSwitch
Group: System/Servers
Requires: %name-daemon = %version-%release

%package java
Summary: Java support for the FreeSWITCH open source telephony platform
Group: Development/Java
Requires: %name-daemon = %version-%release
Requires: java >= 1.6.0

%package lua
Summary: Lua support for the FreeSWITCH open source telephony platform
Group: Development/Other
Requires: %name-daemon = %version-%release

%package perl
Summary: Perl support for the FreeSWITCH open source telephony platform
Group: Development/Perl
Requires: %name-daemon = %version-%release

%package vlc
Summary: VLC support for the FreeSWITCH open source telephony platform
Group: System/Servers

%package av
Summary: FFMpeg support for the FreeSWITCH open source telephony platform
Group: System/Servers

%package webui
Summary: Web-based UI for FreeSWITCH
Group: System/Servers
Requires: %name-daemon = %version-%release

# {{{ descriptions

%description -n lib%name
FreeSWITCH shared library

%description -n lib%name-devel
FreeSWITCH development files


%description daemon
FreeSWITCH is an open source telephony platform designed to facilitate
the creation of voice and chat driven products scaling from a soft-phone
up to a soft-switch.  It can be used as a simple switching engine,
a media gateway or a media server to host IVR applications using simple
scripts or XML to control the callflow.

%description java
Java support for the FreeSWITCH open source telephony platform

%description lua
Lua support for the FreeSWITCH open source telephony platform

%description perl
Perl support for the FreeSWITCH open source telephony platform

%description vlc
VLC support for the FreeSWITCH open source telephony platform

%description av
FFMpeg support for the FreeSWITCH open source telephony platform

%description lang-de
German language phrases module and directory structure for
say module and voicemail

%description lang-en
English language phrases module and directory structure for
say module and voicemail

%description lang-es
Spanish language phrases module and directory structure for
say module and voicemail

%description lang-fr
French language phrases module and directory structure for
say module and voicemail

%description lang-he
Hebrew language phrases module and directory structure for
say module and voicemail

%description lang-pt
Portugal language phrases module and directory structure for
say module and voicemail

%description lang-ru
Russian language phrases module and directory structure for
say module and voicemail

%description webui
FreeSWITCH is an open source telephony platform designed to facilitate
the creation of voice and chat driven products scaling from a soft-phone
up to a soft-switch.  It can be used as a simple switching engine,
a media gateway or a media server to host IVR applications using simple
scripts or XML to control the callflow.

This package provides simple web-based UI.

# }}}

%prep
%setup
%patch0 -p1

%build
LIBTOOL_M4=/usr/share/libtool/aclocal/libtool.m4 ./bootstrap.sh
autoreconf -fisv
cat %SOURCE4 >modules.conf
# special hack for building libvpx by nasm
export ASFLAGS='-Ox'
%configure \
    --enable-fhs \
    --enable-system-xmlrpc-c \
    --enable-system-lua \
    --localstatedir=%_var \
    --with-modinstdir=%_libdir/freeswitch \
    --with-logfiledir=%_var/log/freeswitch \
    --with-dbdir=%_var/lib/freeswitch/db \
    --with-htdocsdir=%_datadir/freeswitch/htdocs \
    --with-soundsdir=%_datadir/freeswitch/sounds \
    --with-grammardir=%_datadir/freeswitch/grammar \
    --with-scriptdir=%_datadir/freeswitch/scripts \
    --with-recordingsdir=%_var/spool/freeswitch \
    --enable-core-libedit-support \
    --enable-core-pgsql-support \
    --enable-core-odbc-support \
    --enable-zrtp \
    --with-libcurl \
    --with-openssl \
    --disable-static \
    #
make

%install
PERL_ARCHLIB=%perl_vendorarch %make_install sysconfdir=%_sysconfdir/freeswitch DESTDIR=%buildroot install
%make_install sysconfdir=%_sysconfdir/freeswitch DESTDIR=%buildroot config-vanilla
(cd conf && find dialplan directory -type f | cpio -pmd %buildroot%_sysconfdir/%name)

install -pm0755 -D %SOURCE1 %buildroot%_initdir/freeswitch
install -pm0644 -D %SOURCE2 %buildroot%_tmpfilesdir/freeswitch.conf
install -pm0644 -D %SOURCE3 %buildroot%_sysconfdir/sysconfig/freeswitch
install -pm0640 -D %SOURCE5 %buildroot%_sysconfdir/fs_cli.conf

install -pm0644 src/include/switch_version.h %buildroot/%_includedir/freeswitch/switch_version.h

mkdir -p \
    %buildroot%_datadir/%name/sounds \
    %buildroot%_sysconfdir/freeswitch/ssl \
    %buildroot%_var/lib/freeswitch/recordings \
    %buildroot%_logdir/freeswitch/{cdr-csv,xml_cdr}


find %buildroot%_libdir/%name  -name \*.la -delete

%triggerun daemon -- freeswitch-daemon < 1.6.6-alt2
if [ $2 -gt 0 ]  && [ $1 -gt 0 ] && [ -f %_sysconfdir/%name/freeswitch.xml ];then 
    mv %_sysconfdir/%name %_sysconfdir/%name-update-%version-%release
fi

#---------------------------------------------------------------
%triggerpostun daemon -- freeswitch-daemon < 1.6.6-alt2
if [ -f %_sysconfdir/%name-update-%version-%release/freeswitch.xml ];then
    mv -Tf %_sysconfdir/%name-update-%version-%release %_sysconfdir/%name
fi

%pre daemon
/usr/sbin/groupadd -r -f _pbx &>/dev/null
/usr/sbin/useradd -r -g _pbx -d /dev/null -s /dev/null \
    -c "freeswitch" -M -n _pbx &>/dev/null ||:

%post daemon
%post_service %name
if [ ! -f %_sysconfdir/%name/freeswitch.xml ];then
    cp -aR %_docdir/%name-daemon-%version/conf/vanilla/* %_sysconfdir/%name
fi

%preun daemon
%preun_service %name

#---------------------------------------------------------------
%files -n lib%name
%_libdir/libfreeswitch*.so.*

%files -n lib%name-devel
%_bindir/fsxs
%_includedir/freeswitch
%_libdir/libfreeswitch*.so
%_pkgconfigdir/freeswitch.pc


%files daemon
%doc conf
%_initdir/freeswitch
%_tmpfilesdir/freeswitch.conf

%config(noreplace) %_sysconfdir/sysconfig/freeswitch

%dir %attr(0750, root, _pbx) %_sysconfdir/%name

%dir %_datadir/freeswitch/fonts
%_datadir/freeswitch/fonts/*.ttf
%_datadir/freeswitch/fonts/OFL.txt
%_datadir/freeswitch/fonts/README.fonts

%_sbindir/freeswitch
%_bindir/fs_cli
%_sbindir/fs_ivrd
%_bindir/fs_encode
%_bindir/fs_tts
%_bindir/tone2wav

%dir %_libdir/%name
%_libdir/%name/mod_abstraction.so
%_libdir/%name/mod_alsa.so
%_libdir/%name/mod_amr.so
%_libdir/%name/mod_b64.so
%_libdir/%name/mod_blacklist.so
%_libdir/%name/mod_bv.so
%_libdir/%name/mod_callcenter.so
%_libdir/%name/mod_cidlookup.so
%_libdir/%name/mod_cdr_csv.so
%_libdir/%name/mod_cdr_sqlite.so
%_libdir/%name/mod_cdr_pg_csv.so
%_libdir/%name/mod_cluechoo.so
%_libdir/%name/mod_codec2.so
%_libdir/%name/mod_commands.so
%_libdir/%name/mod_conference.so
%_libdir/%name/mod_console.so
%_libdir/%name/mod_curl.so
%_libdir/%name/mod_db.so
%_libdir/%name/mod_dahdi_codec.so
%_libdir/%name/mod_dialplan_asterisk.so
%_libdir/%name/mod_dialplan_directory.so
%_libdir/%name/mod_dialplan_xml.so
%_libdir/%name/mod_dingaling.so
%_libdir/%name/mod_directory.so
%_libdir/%name/mod_distributor.so
%_libdir/%name/mod_dptools.so
%_libdir/%name/mod_easyroute.so
%_libdir/%name/mod_enum.so
%_libdir/%name/mod_esl.so
%_libdir/%name/mod_esf.so
%_libdir/%name/mod_event_multicast.so
%_libdir/%name/mod_event_socket.so
%_libdir/%name/mod_expr.so
%_libdir/%name/mod_fifo.so
%_libdir/%name/mod_flite.so
%_libdir/%name/mod_format_cdr.so
%_libdir/%name/mod_fsk.so
%_libdir/%name/mod_fsv.so
%_libdir/%name/mod_g723_1.so
%_libdir/%name/mod_g729.so
%_libdir/%name/mod_h26x.so
%_libdir/%name/mod_hash.so
%_libdir/%name/mod_httapi.so
%_libdir/%name/mod_http_cache.so
%_libdir/%name/mod_ilbc.so
%_libdir/%name/mod_json_cdr.so
%_libdir/%name/mod_lcr.so
%_libdir/%name/mod_ldap.so
%_libdir/%name/mod_limit.so
%_libdir/%name/mod_local_stream.so
%_libdir/%name/mod_logfile.so
%_libdir/%name/mod_loopback.so
%_libdir/%name/mod_memcache.so
%_libdir/%name/mod_mp4.so
%_libdir/%name/mod_mp4v.so
%_libdir/%name/mod_native_file.so
%_libdir/%name/mod_nibblebill.so
%_libdir/%name/mod_opus.so
%_libdir/%name/mod_oreka.so
%_libdir/%name/mod_posix_timer.so
%_libdir/%name/mod_random.so
%_libdir/%name/mod_redis.so
%_libdir/%name/mod_reference.so
%_libdir/%name/mod_rss.so
%_libdir/%name/mod_rtc.so
%_libdir/%name/mod_rtmp.so
%_libdir/%name/mod_shell_stream.so
%_libdir/%name/mod_shout.so
%_libdir/%name/mod_silk.so
%_libdir/%name/mod_siren.so
%_libdir/%name/mod_skinny.so
%_libdir/%name/mod_sms.so
%_libdir/%name/mod_snapshot.so
%_libdir/%name/mod_sndfile.so
%_libdir/%name/mod_snmp.so
%_libdir/%name/mod_snom.so
%_libdir/%name/mod_stress.so
%_libdir/%name/mod_sofia.so
%_libdir/%name/mod_sonar.so
%_libdir/%name/mod_soundtouch.so
%_libdir/%name/mod_spandsp.so
%_libdir/%name/mod_spy.so
%_libdir/%name/mod_syslog.so
%_libdir/%name/mod_theora.so
%_libdir/%name/mod_timerfd.so
%_libdir/%name/mod_tone_stream.so
%_libdir/%name/mod_translate.so
%_libdir/%name/mod_tts_commandline.so
%_libdir/%name/mod_unimrcp.so
%_libdir/%name/mod_valet_parking.so
%_libdir/%name/mod_verto.so
%_libdir/%name/mod_vmd.so
%_libdir/%name/mod_voicemail.so
%_libdir/%name/mod_voicemail_ivr.so
%_libdir/%name/mod_xml_cdr.so
%_libdir/%name/mod_xml_curl.so
%_libdir/%name/mod_xml_rpc.so
%_libdir/%name/mod_yaml.so

%dir %_datadir/%name
%dir %_datadir/%name/scripts
%dir %_datadir/%name/sounds
%dir %_datadir/%name/htdocs
%dir %_datadir/%name/grammar

%dir %attr(0770, root, _pbx) %_spooldir/%name

%dir %attr(0770, root, _pbx) %_localstatedir/%name
%dir %attr(0770, root, _pbx) %_localstatedir/%name/db
%dir %attr(0770, root, _pbx) %_localstatedir/%name/images
%_localstatedir/%name/images/*
%dir %attr(0770, root, _pbx) %_logdir/%name
%dir %attr(0770, root, _pbx) %_logdir/%name/cdr-csv
%dir %attr(0770, root, _pbx) %_logdir/%name/xml_cdr

%dir %attr(0770, root, _pbx) %_var/run/%name

%files java
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/java.conf.xml
%_libdir/%name/mod_java.so*
%_datadir/%name/scripts/%name.jar

%files lua
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/lua.conf.xml
%_libdir/%name/mod_lua.so*

%files perl
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/autoload_configs/perl.conf.xml
%_libdir/%name/mod_perl.so*
%perl_vendor_archlib/freeswitch.pm
%perl_vendor_autolib/freeswitch

%files vlc
%_libdir/%name/mod_vlc.so*

%files av
%_libdir/%name/mod_av.so

%files lang-de
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/de/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/de/vm/*.xml
%_libdir/%name/mod_say_de.so*

%files lang-es
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/es
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/es/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/es/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/es/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/es/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/es/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/es/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/es/vm/*.xml
%_libdir/%name/mod_say_es.so*

%files lang-en
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/ivr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/en/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/ivr/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/en/vm/*.xml
%_libdir/%name/mod_say_en.so*

%files lang-fr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/fr/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/fr/vm/*.xml
%_libdir/%name/mod_say_fr.so*

%files lang-he
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/he/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/he/vm/*.xml

%files lang-pt
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/pt
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/pt/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/pt/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/pt/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/pt/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/pt/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/pt/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/pt/vm/*.xml
%_libdir/%name/mod_say_pt.so*

%files lang-ru
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/dir
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/demo
%dir %attr(0750, root, _pbx) %_sysconfdir/%name/lang/ru/vm
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/dir/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/demo/*.xml
%config(noreplace) %attr(0640, root, _pbx) %_sysconfdir/%name/lang/ru/vm/*.xml
%_libdir/%name/mod_say_ru.so*


%files webui
%_datadir/%name/htdocs/portal

%changelog
* Mon Feb 10 2020 Anton Farygin <rider@altlinux.ru> 1:1.10.2-alt1
- 1.10.2
- removed python,freetdm, avmd and mongodb modules

* Tue Oct 08 2019 Michael Shigorin <mike@altlinux.org> 1:1.8.7-alt2
- E2K: fix build (patch proposed upstream)

* Thu Aug 29 2019 Anton Farygin <rider@altlinux.ru> 1:1.8.7-alt1
- 1.8.7
- fixed build on ppc64 (thanks to glebfm@)

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.5-alt2
- NMU: remove rpm-build-ubt from BR:

* Tue Mar 12 2019 Anton Farygin <rider@altlinux.ru> 1:1.8.5-alt1
- 1.8.5

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.8.4-alt1.1
- rebuild with new perl 5.28.1

* Mon Jan 07 2019 Anton Farygin <rider@altlinux.ru> 1:1.8.4-alt1
- 1.8.4

* Tue Dec 18 2018 Anton Farygin <rider@altlinux.ru> 1:1.8.2-alt4
- fixed build with gcc-8
- disabled build libpri and isdn plugins for freetdm

* Thu Nov 01 2018 Anton Farygin <rider@altlinux.ru> 1:1.8.2-alt3
- added switch_version.h to devel package (closes: #25924)

* Tue Oct 16 2018 Anton Farygin <rider@altlinux.ru> 1:1.8.2-alt2
- added fix for build with libav-11

* Fri Sep 28 2018 Anton Farygin <rider@altlinux.ru> 1:1.8.2-alt1
- 1.8.2

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 1:1.6.20-alt3
- rebuilt with libcodec2-0.8

* Tue Jun 19 2018 Anton Farygin <rider@altlinux.ru> 1:1.6.20-alt2
- disabled sagoma support
- rebuilt for ffmpeg-4.0

* Fri May 04 2018 Anton Farygin <rider@altlinux.ru> 1:1.6.20-alt1
- 1.6.20

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.6.19-alt3.1
- rebuild with new perl 5.26.1

* Sun Oct 29 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.19-alt3
- rebuilt for new postgresql 10

* Tue Oct 03 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.19-alt2
- rebuilt for new libcodev2 0.7

* Wed Jul 19 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.19-alt1.S1
- 1.6.19

* Wed Jun 28 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.18-alt1
- 1.6.18
- build without erlang
- disabled javascript support

* Sat Jun 17 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.17-alt3
- build mod_av.so as freeswitch-av subpackage

* Thu Jun 15 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.17-alt2
- enable mod_rtc build and cleanup modules.conf

* Tue Apr 25 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.17-alt1
- new version

* Wed Feb 15 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.15-alt1
- new version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.6.14-alt1.1
- rebuild with new perl 5.24.1

* Thu Jan 19 2017 Anton Farygin <rider@altlinux.ru> 1:1.6.14-alt1
- new version

* Wed Nov 30 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.13-alt1
- new version

* Wed Oct 19 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.12-alt1
- new version

* Wed Oct 12 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.11-alt1
- new version

* Tue Sep 13 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.10-alt2
- fixed unresolved symbols in mod_flite

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.10-alt1
- new version

* Mon Jul 25 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.9-alt1
- new version

* Tue Jun 14 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.8-alt1
- new version

* Fri Mar 18 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.6-alt2
- removed default configuration from freeswitch-daemon package
- added subpackage with mod_vlc 

* Sat Mar 12 2016 Anton Farygin <rider@altlinux.ru> 1:1.6.6-alt1
- new version

* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1:1.4.26-alt1.1
- rebuilt against libSoundTouch.so.1

* Mon Dec 07 2015 Anton Farygin <rider@altlinux.ru> 1:1.4.26-alt1
- new version

* Wed Dec 02 2015 Andrey Cherepanov <cas@altlinux.org> 1:1.4.23-alt2.2
- rebuild with new libmemcached 1.0.18

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.4.23-alt2.1
- rebuild with new perl 5.22.0

* Sun Nov 22 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.4.23-alt2
- fixed build: added libspeexdsp to BR:.

* Tue Oct 13 2015 Anton Farygin <rider@altlinux.ru> 1:1.4.23-alt1
- new version

* Wed Jul 15 2015 Anton Farygin <rider@altlinux.ru> 1:1.4.20-alt1
- build 1.4.20 as new version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.5.13-alt2.1
- rebuild with new perl 5.20.1

* Tue Nov 18 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.13-alt2
- rebuilt with recent libsoundtouch

* Fri Jul 25 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.13-alt1
- 1.5.13 released

* Fri Oct 11 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.5-alt2
- built mod_gsmopen

* Wed Oct 09 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.5-alt1
- 1.5.5 released

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt2
- built for perl 5.18

* Tue Sep 25 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Fri Sep 21 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.7-alt0.6
- rebuilt for perl-5.16

* Thu Nov 24 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.5
- updated from git b9e28f85

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.7-alt0.4.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Alexey Tourbin <at@altlinux.ru> 1.0.7-alt0.4
- rebuilt for perl-5.14

* Wed Aug 10 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.3
- updated from git 6d1d4a9c

* Wed Jun 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.7-alt0.1
- 1.0.7 (rolling) released
- obsolete openzap stuff removed

* Wed Jun 15 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt9
- mod_memcache temporarily dropped

* Tue Apr 26 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt8
- mod_perl again due to perl changes

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt7
- resurrect mod_perl module

* Mon Mar 21 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt6
- rebuilt with recent libmemcached

* Wed Mar 16 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt5
- exclude mod_erlang_event from build

* Wed Dec 01 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt4
- updated from upstream git.2343f685

* Sun Nov 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt3
- rebuilt with recent libcelt

* Sat May 08 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt2
- fixed build with recent libmpg123

* Fri May  7 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt1
- 1.0.6 released

* Mon Apr 12 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt4
- fixed python module packaging

* Sat Sep 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.4-alt2
- 1.0.4 released

* Wed Jul 29 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt3
- rebuilt due spandsp soname change

* Sat May 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.3-alt1
- 1.0.3 released

* Wed Jan 14 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- first build for ALTLinux
