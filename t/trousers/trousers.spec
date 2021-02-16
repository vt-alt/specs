Name: trousers
Version: 0.3.15
Release: alt1

Summary: Implementation of the TCG's Software Stack
License: BSD-3-Clause
Group: System/Base
Url: http://www.sf.net/projects/trousers

Source: %name-%version-%release.tar

BuildRequires: libssl-devel

Requires: lib%name = %version-%release

%description
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.

%package -n lib%name
Summary: TrouSerS shared library
Group: System/Libraries

%package -n lib%name-devel
Summary: TrouSerS header files and documentation
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name
TrouSerS is an implementation of the Trusted Computing Group's Software Stack
(TSS) specification. You can use TrouSerS to write applications that make use
of your TPM hardware. TPM hardware can create, store and use RSA keys
securely (without ever being exposed in memory), verify a platform's software
state using cryptographic hashes and more.
This package contains TrouSerS shared library.

%description -n lib%name-devel
Header files and man pages for use in creating Trusted Computing enabled
applications.

%prep
%setup

%build
%autoreconf
%configure --with-gui=openssl
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE NEWS README* ChangeLog
%config(noreplace) %_sysconfdir/tcsd.conf
%_sbindir/tcsd
%_man5dir/tcsd.conf.5*
%_man8dir/tcsd.8*
%_localstatedir/tpm

%files -n lib%name
%_libdir/libtspi.so.*

%files -n lib%name-devel
%_libdir/libtspi.so
%_includedir/tss
%_includedir/trousers
%_man3dir/Tspi_*.3*

%changelog
* Tue Jan 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.15-alt1
- 0.3.15 released
- Corrected mutliple security issues in tcsd
  (Fixes: CVE-2020-24332, CVE-2020-24330, CVE-2020-24331)

* Wed Aug 29 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.14-alt1
- 0.3.14 released

* Mon Aug 03 2015 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.13-alt1
- 0.3.13 released

* Sun Dec 22 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.11.2-alt1
- 0.3.11.2 released

* Thu Mar 21 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.3.10-alt1
- initial
