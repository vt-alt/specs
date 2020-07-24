%def_with nghttp2

Name: curl
Version: 7.71.0
Release: alt1

Summary: Gets a file from a FTP, GOPHER or HTTP server
Summary(ru_RU.UTF-8): Утилиты и библиотеки для передачи файлов
License: MITX
Group: Networking/File transfer
Url: http://curl.haxx.se

Source: %url/download/%name-%version.tar
Source1: %name.watch
Patch0: curl-%version-alt.patch

Requires: lib%name = %version-%release

BuildRequires: glibc-devel-static groff-base libidn2-devel libssh2-devel libssl-devel libkrb5-devel
BuildRequires: zlib-devel libpsl-devel libldap-devel libbrotli-devel

%{?_with_nghttp2:BuildRequires: libnghttp2-devel}

%package -n lib%name
Summary: The shared library for file transfer
Summary(ru_RU.UTF-8): Библиотеки для передачи файлов
Group: System/Libraries
Provides: %name-lib = %version
Obsoletes: %name-lib < %version
Requires: ca-certificates

%package -n lib%name-devel
Summary: Header files for lib%name
Summary(ru_RU.UTF-8): Заголовочные файлы для lib%name
Group: Development/C
Requires: lib%name = %version-%release bc
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%package -n lib%name-devel-static
Summary: Static libraries for lib%name
Summary(ru_RU.UTF-8): Статические библиотеки для lib%name
Group: Development/C
Requires: lib%name-devel = %version-%release

%description
Curl is a client to get documents/files from servers, using any of the
supported protocols. The command is designed to work without user
interaction or any kind of interactivity.

Curl offers a busload of useful tricks like proxy support, user
authentication, ftp upload, HTTP post, file transfer resume and more.

NOTE: This version is compiled with SSL (https) support.

%description -l ru_RU.UTF-8
Curl - это клиент для получения файлов или документов с серверов,
используя один из поддерживаемых протоколов.  Утилита спроектирована
для работы в неинтерактивном режиме.

Curl позволяет выполнять различные операции над сетевыми файлами,
реализуя поддержку прокси, авторизацию пользователя, докачку файлов и
многое другое.

%description -n lib%name
This package contains lib%name shared library of functions for
sending and receiving files through various protocols, including
http and ftp.

%description -n lib%name -l ru_RU.UTF-8
Этот пакет содержит разделяемую библиотеку функций для отправки или
получения файлов через различные сетевые протоколы, включая http и ftp.

%description -n lib%name-devel
This package contains lib%name development library of functions for
sending and receiving files through various protocols, including
http and ftp.

This package is required for development of applications that
utilize lib%name.

%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит девелоперскую библиотеку функций для отправки или
получения файлов через различные сетевые протоколы, включая http и ftp.

Этот пакет необходим для разработки приложений, использующих lib%name.

%description -n lib%name-devel-static
This package contains lib%name static library of functions for
sending and receiving files through various protocols, including
http and ftp.

This package is required for development of statically linked
applications that utilize lib%name.

%description -n lib%name-devel-static -l ru_RU.UTF-8
Этот пакет содержит статическую библиотеку функций для отправки или
получения файлов через различные сетевые протоколы, включая http и ftp.

Этот пакет необходим для разработки статически слинкованных приложений,
использующих lib%name.

%prep
%setup -q
%patch0 -p1

%build
./maketgz %version only
./buildconf
%configure \
	--with-ssl \
	--with-libidn \
	--enable-ipv6 \
	--disable-rpat \
	--enable-ldap \
	--enable-sspi \
	--enable-threaded-resolver \
	--with-ssl --enable-openssl-auto-load-config \
	--with-gssapi \
	--with-ca-bundle=%_datadir/ca-certificates/ca-bundle.crt

%make_build

%install
%makeinstall_std
%makeinstall_std -C docs/libcurl

%check
%make -k test-full

%files
%_bindir/curl
%_man1dir/curl.1*

%files -n lib%name
%_libdir/*.so.*

%doc CHANGES README* docs/{FAQ,FEATURES}

%files -n lib%name-devel
%_libdir/*.so
%_libdir/pkgconfig/libcurl.pc
%_bindir/curl-config
%_aclocaldir/libcurl.m4
%_includedir/*
%_man3dir/*
%_man1dir/curl-config.1*
%doc docs/{THANKS,BUGS,RESOURCES,TheArtOfHttpScripting,TODO,examples}

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Wed Jun 24 2020 Anton Farygin <rider@altlinux.ru> 7.71.0-alt1
- 7.71.0
- fixes:
  * CVE-2020-8177: curl overwrite local file with -J
  * CVE-2020-8169: Partial password leak over DNS on HTTP redirect

* Wed Apr 29 2020 Anton Farygin <rider@altlinux.ru> 7.70.0-alt1
- 7.70.0
- removed DEV from version string (with maketgz script)

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 7.69.1-alt1
- 7.69.1

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 7.69.0-alt1
- 7.69.0

* Fri Jan 10 2020 Anton Farygin <rider@altlinux.ru> 7.68.0-alt1
- 7.68.0

* Mon Nov 11 2019 Anton Farygin <rider@altlinux.ru> 7.67.0-alt1
- 7.67.0

* Wed Sep 11 2019 Anton Farygin <rider@altlinux.ru> 7.66.0-alt1
- 7.66.0
- fixes:
 * CVE-2019-5481: FTP-KRB double-free 
 * CVE-2019-5482: TFTP small blocksize heap buffer overflow

* Tue Jul 23 2019 Anton Farygin <rider@altlinux.ru> 7.65.3-alt1
- 7.65.3

* Wed Jun 05 2019 Anton Farygin <rider@altlinux.ru> 7.65.1-alt1
- 7.65.1

* Wed May 22 2019 Anton Farygin <rider@altlinux.ru> 7.65.0-alt1
- 7.65.0
- fixes:
  * CVE-2019-5435: Integer overflows in curl_url_set
  * CVE-2019-5436: tftp: use the current blksize for recvfrom

* Thu Mar 28 2019 Anton Farygin <rider@altlinux.ru> 7.64.1-alt1
- 7.64.1

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 7.64.0-alt2
- increased level of verbosity in make check stage

* Wed Feb 06 2019 Anton Farygin <rider@altlinux.ru> 7.64.0-alt1
- 7.64.0
- fixes:
  * CVE-2018-16890: NTLM type-2 out-of-bounds buffer read
  * CVE-2019-3822: NTLMv2 type-3 header stack buffer overflow
  * CVE-2019-3823: SMTP end-of-response out-of-bounds read

* Wed Dec 12 2018 Anton Farygin <rider@altlinux.ru> 7.63.0-alt1
- 7.63.0

* Wed Nov 14 2018 Anton Farygin <rider@altlinux.ru> 7.62.0-alt3
- enabled idn support (closes: #34103)
- enabled ldap support
- enabled brotli support

* Thu Nov 01 2018 Michael Shigorin <mike@altlinux.org> 7.62.0-alt2
- added nghttp2 knob (on by default)

* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 7.62.0-alt1
- 7.62.0 
- fixes:
  * CVE-2018-16839 - buffer overrun in the SASL authentication code. 
  * CVE-2018-16840 - use-after-free in handle close
  * CVE-2018-16842 - warning message out-of-buffer read

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 7.61.1-alt2
- enabled HTTP/2 support
* Sun Sep 09 2018 Anton Farygin <rider@altlinux.ru> 7.61.1-alt1
- 7.61.1 (fixes: CVE-2018-14618)

* Thu Aug 16 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.61.0-alt2
- Rebuilt with openssl 1.1.
- Added BR: libkrb5-devel.

* Tue Jul 17 2018 Anton Farygin <rider@altlinux.ru> 7.61.0-alt1
- 7.61.0
- fixes:
  * CVE-2018-0500 SMTP send heap buffer overflow

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 7.60.0-alt1
- 7.60.0 
- fixes:
  * CVE-2018-1000300 FTP shutdown response buffer overflow
  * CVE-2018-1000301 RTSP bad headers buffer over-read 

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 7.59.0-alt1
- new version 
- fixes: 
  * CVE-2018-1000120 FTP path trickery leads to NIL byte out of bounds write
  * CVE-2018-1000121 LDAP NULL pointer dereference
  * CVE-2018-1000122  RTSP RTP buffer over-read

* Wed Jan 24 2018 Anton Farygin <rider@altlinux.ru> 7.58.0-alt1
- new version
- fixes:
  * CVE-2018-1000005 HTTP/2 trailer out-of-bounds read
  * CVE-2018-1000007 HTTP authentication leak in redirects

* Fri Dec 01 2017 Anton Farygin <rider@altlinux.ru> 7.57.0-alt1
- new version
- fixes:
  * CVE-2017-8818 SSL out of buffer access
  * CVE-2017-8817 FTP wildcard out of bounds read
  * CVE-2017-8816 NTLM buffer overflow via integer overflow

* Mon Oct 23 2017 Anton Farygin <rider@altlinux.ru> 7.56.1-alt1
- new version
- fixes:
  * CVE-2017-1000257 libcurl contains a buffer overrun flaw in the IMAP handler

* Wed Oct 04 2017 Anton Farygin <rider@altlinux.ru> 7.56.0-alt1
- new version
- fixes:
  * CVE-2017-1000254 libcurl may read outside of a heap allocated buffer when doing FTP.
  
* Mon Aug 14 2017 Anton Farygin <rider@altlinux.ru> 7.55.1-alt1
- new version

* Wed Aug 09 2017 Anton Farygin <rider@altlinux.ru> 7.55.0-alt1
- new version with following security fixes:
   * CVE-2017-1000101 glob: do not parse after a strtoul() overflow range
   * CVE-2017-1000100 tftp: reject file name lengths that don't fit
   * CVE-2017-1000099 file: output the correct buffer to the user

* Wed Jun 14 2017 Anton Farygin <rider@altlinux.ru> 7.54.1-alt1
- new version with security fixes:
  CVE-2017-9502: URL file scheme drive letter buffer overflow 

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 7.54.0-alt1
- new version with security fixes:
  CVE-2016-5419: TLS session resumption client cert bypass (again) 

* Mon Feb 27 2017 Anton Farygin <rider@altlinux.ru> 7.53.1-alt1
- new version

* Wed Feb 22 2017 Anton Farygin <rider@altlinux.ru> 7.53.0-alt1
- new version with security fixes:
  CVE-2017-2629: SSL_VERIFYSTATUS ignored

* Fri Dec 23 2016 Anton Farygin <rider@altlinux.ru> 7.52.1-alt1
- new version with security fixes:
  CVE-2016-9594: uninitialized random

* Wed Dec 21 2016 Anton Farygin <rider@altlinux.ru> 7.52.0-alt1
- new version with security fixes:
  CVE-2016-9586: printf floating point buffer overflow

* Wed Dec 07 2016 Anton Farygin <rider@altlinux.ru> 7.51.0-alt2
- enabled gssapi (closes: #32862)

* Wed Nov 02 2016 Anton Farygin <rider@altlinux.ru> 7.51.0-alt1
- new version with security fixes:
  CVE-2016-8615: cookie injection for other servers 
  CVE-2016-8616: case insensitive password comparison 
  CVE-2016-8617: OOB write via unchecked multiplication 
  CVE-2016-8618: double-free in curl_maprintf 
  CVE-2016-8619: double-free in krb5 code 
  CVE-2016-8620: glob parser write/read out of bounds 
  CVE-2016-8621: curl_getdate read out of bounds 
  CVE-2016-8622: URL unescape heap overflow via integer truncation 
  CVE-2016-8623: Use-after-free via shared cookies 
  CVE-2016-8624: invalid URL parsing with '#'
  CVE-2016-8625: IDNA 2003 makes curl use wrong host


* Thu Oct 27 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 7.50.3-alt2
- libcurl-devel: packaged libcurl.m4

* Wed Sep 14 2016 Anton Farygin <rider@altlinux.ru> 7.50.3-alt1
- new version with security fixes (CVE-2016-7167)

* Fri Sep 09 2016 Anton Farygin <rider@altlinux.ru> 7.50.2-alt1
- new version

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 7.50.1-alt1
- new version

* Thu Jul 21 2016 Anton Farygin <rider@altlinux.ru> 7.50.0-alt1
- new version

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 7.49.1-alt1
- new version

* Mon May 23 2016 Anton Farygin <rider@altlinux.ru> 7.49.0-alt1
- new version

* Thu Mar 24 2016 Anton Farygin <rider@altlinux.ru> 7.48.0-alt1
- new version

* Sat Mar 12 2016 Anton Farygin <rider@altlinux.ru> 7.47.1-alt1
- new version

* Sun Dec 13 2015 Anton Farygin <rider@altlinux.ru> 7.46.0-alt2
- enabled http2 support (closes: #31617)

* Mon Dec 07 2015 Anton Farygin <rider@altlinux.ru> 7.46.0-alt1
- new version

* Sun Oct 18 2015 Anton Farygin <rider@altlinux.ru> 7.45.0-alt1
- new version

* Fri Jun 19 2015 Anton Farygin <rider@altlinux.ru> 7.43.0-alt1
- new version, with fixes for CVE-2015-3236, CVE-2015-3237

* Wed Apr 29 2015 Anton Farygin <rider@altlinux.ru> 7.42.1-alt1
- new version, with fixes for CVE-2015-3153

* Wed Apr 22 2015 Anton Farygin <rider@altlinux.ru> 7.42.0-alt1
- new version, with fixes for CVE-2015-3148, CVE-2015-3143, CVE-2015-3145 
  and CVE-2015-3144

* Wed Feb 25 2015 Anton Farygin <rider@altlinux.ru> 7.41.0-alt1
- new version

* Wed Jan 14 2015 Anton Farygin <rider@altlinux.ru> 7.40.0-alt1
- new version

* Wed Nov 05 2014 Anton Farygin <rider@altlinux.ru> 7.39.0-alt1
- new version

* Thu Oct 30 2014 Anton Farygin <rider@altlinux.ru> 7.38.0-alt2
- threaded-resolver: revert Curl_expire_latest() switch (closes: #30427)

* Wed Sep 10 2014 Anton Farygin <rider@altlinux.ru> 7.38.0-alt1
- new version

* Thu Jul 24 2014 Anton Farygin <rider@altlinux.ru> 7.37.1-alt1
- new version

* Fri Jun 06 2014 Anton Farygin <rider@altlinux.ru> 7.37.0-alt1
- new version

* Wed Mar 26 2014 Anton Farygin <rider@altlinux.ru> 7.36.0-alt1
- new version
- added watch file

* Fri Feb 14 2014 Anton Farygin <rider@altlinux.ru> 7.35.0-alt2
- test172 fixed by upstream

* Wed Jan 29 2014 Anton Farygin <rider@altlinux.ru> 7.35.0-alt1
- new version

* Tue Dec 17 2013 Anton Farygin <rider@altlinux.ru> 7.34.0-alt1
- new version

* Wed Oct 23 2013 Anton Farygin <rider@altlinux.ru> 7.33.0-alt1
- new version

* Fri Aug 16 2013 Anton Farygin <rider@altlinux.ru> 7.32.0-alt1
- new version

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 7.31.0-alt1
- new version

* Tue Apr 16 2013 Anton Farygin <rider@altlinux.ru> 7.30.0-alt1
- new version

* Mon Feb 11 2013 Anton Farygin <rider@altlinux.ru> 7.29.0-alt2
- Fix NULL pointer reference when closing an unused multi handle (closes: #28534)

* Wed Feb 06 2013 Anton Farygin <rider@altlinux.ru> 7.29.0-alt1
- new version

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 7.27.0-alt1
- new version

* Tue May 29 2012 Anton Farygin <rider@altlinux.ru> 7.26.0-alt1
- new version

* Tue Jan 24 2012 Anton Farygin <rider@altlinux.ru> 7.24.0-alt1
- new version (fixes two separate security vulnerabilities)

* Thu Nov 24 2011 Anton Farygin <rider@altlinux.ru> 7.23.1-alt1
- new version

* Fri Sep 16 2011 Anton Farygin <rider@altlinux.ru> 7.22.0-alt1
- new version

* Mon Jun 27 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.21.7-alt1
- new version (CVE-2011-2192)

* Sat Apr 23 2011 Anton Farygin <rider@altlinux.ru> 7.21.6-alt1
- new version

* Mon Apr 18 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.21.5-alt2
- fix curl-config script:
 + version: replace VERSION with CURLVERSION
 + checkfor: add Requires: bc

* Mon Apr 18 2011 Anton Farygin <rider@altlinux.ru> 7.21.5-alt1
- new version

* Tue Mar 15 2011 Alexey Tourbin <at@altlinux.ru> 7.21.4-alt2
- libcurl-devel: removed dependencies on libidn-devel libssl-devel zlib-devel
- applied debug.patch from Fedora to enable -g in CFLAGS

* Sat Feb 26 2011 Anton Farygin <rider@altlinux.ru> 7.21.4-alt1
- new version
- enabled test check

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 7.21.3-alt1
- new version
- test suite temporary disabled (it does not work in hasher)

* Wed Oct 13 2010 Anton Farygin <rider@altlinux.ru> 7.21.2-alt1
- new version

* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 7.21.1-alt3
- Removed unused requirement on libcares.
- Cleaned up package descriptions.
- Enabled test suite.
- Built with libssl.so.10.

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 7.21.1-alt2
- build without libcares (fixed #23891,#23486)

* Thu Aug 12 2010 Anton Farygin <rider@altlinux.ru> 7.21.1-alt1
- new version
- enabled build with libssh2

* Tue Jun 29 2010 Anton Farygin <rider@altlinux.ru> 7.21.0-alt1
- new version

* Thu Apr 15 2010 Anton Farygin <rider@altlinux.ru> 7.20.1-alt1
- new version

* Thu Feb 11 2010 Anton Farygin <rider@altlinux.ru> 7.20.0-alt1
- new version

* Sun Nov 08 2009 Anton Farygin <rider@altlinux.ru> 7.19.7-alt1
- new version

* Thu Aug 13 2009 Anton Farygin <rider@altlinux.ru> 7.19.6-alt1
- new version (CVE-2009-2417)

* Sat Mar 07 2009 Anton Farygin <rider@altlinux.ru> 7.19.4-alt2
- build curl with really external libcares (fixed #19097)

* Tue Mar 03 2009 Anton Farygin <rider@altlinux.ru> 7.19.4-alt1
- new version (CVE-2009-0037)

* Mon Feb 09 2009 Anton Farygin <rider@altlinux.ru> 7.19.3-alt3
- build from cvs

* Mon Feb 09 2009 Anton Farygin <rider@altlinux.ru> 7.19.3-alt2
- curl-config --libs fixed (#18779)

* Wed Jan 28 2009 Anton Farygin <rider@altlinux.ru> 7.19.3-alt1
- new version

* Fri Nov 14 2008 Anton Farygin <rider@altlinux.ru> 7.19.2-alt1
- new version

* Fri Nov 14 2008 Anton Farygin <rider@altlinux.ru> 7.19.1-alt2
- post-ldconfig removed

* Mon Nov 10 2008 Anton Farygin <rider@altlinux.ru> 7.19.1-alt1
- new version

* Mon Sep 15 2008 Anton Farygin <rider@altlinux.ru> 7.19.0-alt2
- enabled c-ares support (#17101)

* Fri Sep 12 2008 Anton Farygin <rider@altlinux.ru> 7.19.0-alt1
- new version

* Thu Jun 05 2008 Anton Farygin <rider@altlinux.ru> 7.18.2-alt1
- new version

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 7.18.1-alt1
- new version

* Thu Jan 31 2008 Anton Farygin <rider@altlinux.ru> 7.18.0-alt1
- new version

* Thu Nov 15 2007 Anton Farygin <rider@altlinux.ru> 7.17.1-alt2
- disabled ldap support

* Tue Nov 06 2007 Anton Farygin <rider@altlinux.ru> 7.17.1-alt1
- new version

* Fri Sep 14 2007 Anton Farygin <rider@altlinux.ru> 7.17.0-alt1
- new version
- removed patch1 (included to mainstream)
- removed unsused patch0

* Tue Sep 11 2007 Anton Farygin <rider@altlinux.ru> 7.16.4-alt2
- added patch to ftp from sbolshakov@. Fixed anonymous login on some non-standart servers

* Wed Jul 11 2007 Anton Farygin <rider@altlinux.ru> 7.16.4-alt1
- new version with security fixes (CVE-2007-3564)
- disabled kerberos support (by requiest from krb5 mantainer)

* Tue Jul 03 2007 Anton Farygin <rider@altlinux.ru> 7.16.3-alt1
- new version

* Thu Apr 12 2007 Anton Farygin <rider@altlinux.ru> 7.16.2-alt1
- new version

* Mon Feb 12 2007 Anton Farygin <rider@altlinux.ru> 7.16.1-alt3
- fixed curl-config --libs and libcurl.pc (unneeded libs removed)

* Fri Feb 09 2007 Anton Farygin <rider@altlinux.ru> 7.16.1-alt2
- use ca-certificates
- build with gssapi support
- updated build requires

* Wed Jan 31 2007 Anton Farygin <rider@altlinux.ru> 7.16.1-alt1
- new version

* Tue Jan 09 2007 Anton Farygin <rider@altlinux.ru> 7.16.0-alt1
- new version (soname changed)

* Wed Sep 13 2006 Anton Farygin <rider@altlinux.ru> 7.15.5-alt1
- new version

* Fri Mar 24 2006 Anton Farygin <rider@altlinux.ru> 7.15.3-alt1
- new version

* Fri Oct 14 2005 Anton Farygin <rider@altlinux.ru> 7.15.0-alt1
- new version

* Fri Sep 02 2005 Anton Farygin <rider@altlinux.ru> 7.14.1-alt1
- new version

* Tue May 17 2005 Anton Farygin <rider@altlinux.ru> 7.14.0-alt1
- new version

* Fri May 06 2005 Anton Farygin <rider@altlinux.ru> 7.13.2-alt1
- new version

* Fri Mar 04 2005 Anton Farygin <rider@altlinux.ru> 7.13.1-alt1
- 7.13.1

* Mon Feb 07 2005 Anton Farygin <rider@altlinux.ru> 7.13.0-alt2
- lib%name-devel: added requires to libidn-devel libssl-devel zlib-devel

* Tue Feb 01 2005 Anton Farygin <rider@altlinux.ru> 7.13.0-alt1
- new version

* Tue Jan 18 2005 Anton Farygin <rider@altlinux.ru> 7.12.3-alt1
- new version

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 7.12.2-alt1
- new version

* Fri Oct 15 2004 Anton Farygin <rider@altlinux.ru> 7.12.1-alt1
- new version

* Mon Apr 26 2004 Anton Farygin <rider@altlinux.ru> 7.11.2-alt1
- new version

* Tue Apr 20 2004 Anton Farygin <rider@altlinux.ru> 7.11.1-alt1
- new version

* Thu Mar 18 2004 Anton Farygin <rider@altlinux.ru> 7.11.0-alt1
- new version

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 7.10.8-alt1
- new version

* Wed Apr 30 2003 Rider <rider@altlinux.ru> 7.10.4-alt1
- 7.10.4

* Mon Mar 31 2003 Rider <rider@altlinux.ru> 7.10.3-alt1
- 7.10.3

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 7.10.2-alt1
- new version

* Fri Oct 04 2002 Rider <rider@altlinux.ru> 7.10-alt1
- 7.10

* Fri Jun 14 2002 Rider <rider@altlinux.ru> 7.9.8-alt1
- 7.9.8

* Sat Jun 01 2002 Rider <rider@altlinux.ru> 7.9.7-alt1
- 7.9.7

* Sat Apr 27 2002 Rider <rider@altlinux.ru> 7.9.6-alt1
- 7.9.6

* Wed Mar 27 2002 Rider <rider@altlinux.ru> 7.9.5-alt1
- 7.9.5

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 7.9.4-alt1
- 7.9.4

* Thu Jan 03 2002 Rider <rider@altlinux.ru> 7.9.2-alt1
- 7.9.2
- russian summary and description

* Tue Oct 09 2001 Rider <rider@altlinux.ru> 7.9-alt1
- 7.9

* Fri Aug 24 2001 Rider <rider@altlinux.ru> 7.8.1-alt1
- 7.8.1

* Tue May 22 2001 Alexander Bokovoy <ab@altlinux.ru> 7.7.3-alt2
- Fixed:
    + curl-config moved to libcurl-devel
    + curl-config(1) moved to libcurl-devel

* Tue May 08 2001 Rider <rider@altlinux.ru> 7.7.3-alt1
- 7.7.3

* Wed Apr 25 2001 Rider <rider@altlinux.ru> 7.7.2-alt1
- 7.7.2

* Thu Apr 05 2001 Rider <rider@altlinux.ru> 7.7.1-alt1
- 7.7.1

* Sun Jan 28 2001 Dmitry V. Levin <ldv@fandra.org> 7.6-ipl1mdk
- 7.6

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 7.5.2-ipl2mdk
- RE adaptions.

* Tue Jan  9 2001 DindinX <odin@mandrakesoft.com> 7.5.2-2mdk
- change lisence, according to the author's will (reported by F. Crozat)
- added some sample codes to the -devel package

* Tue Jan  9 2001 DindinX <odin@mandrakesoft.com> 7.5.2-1mdk
- 7.5.2
- small spec updates

* Mon Dec 18 2000 DindinX <odin@mandrakesoft.com> 7.5.1-2mdk
- corrected URL

* Wed Dec 13 2000 DindinX <odin@mandrakesoft.com> 7.5.1-1mdk
- 7.5.1

* Thu Dec 07 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 7.5-2mdk
- manually include fcntl.h, strangely, it has been left out (sucky!!!).

* Mon Dec 04 2000 Geoffrey lee <snailtalk@mandrakesoft.com> 7.5-1mdk
- new and shiny source.
- requires: curl = %%version

* Wed Nov 15 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 7.4.2-5mdk
- really 7.4.2.
- well we compile with ssl now, so obviously description is wrong (daoudascks)

* Mon Nov 13 2000 Daouda Lo <daouda@mandrakesoft.com> 7.4.2-4mdk
- compiled with ssl (from TitiSux)

* Mon Nov 13 2000 Daouda Lo <daouda@mandrakesoft.com> 7.4.2-3mdk
- relase pre4.

* Fri Nov 10 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.4.2-2mdk
- fiw requires

* Tue Nov 07 2000 Daouda Lo <daouda@mandrakesoft.com> 7.4.2-1mdk
- new release

* Fri Nov 03 2000 DindinX <odin@mandrakesoft.com> 7.4.1-1mdk
- 7.4.1

* Mon Aug 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 7.1-1mdk
- used srpm from Anton Graham <darkimage@bigfoot.com> :
	- new version
	- new -lib and -devel packages

* Mon Aug 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 6.5.2-3mdk
- change description
- clean spec

* Tue Jul 11 2000 Anton Graham <darkimage@bigfoot.com> 6.5.2-2mdk
- Macroification

* Wed May 03 2000 Anton Graham <darkimage@bigfoot.com> 6.5.2-1mdk
- First Mandrake build
