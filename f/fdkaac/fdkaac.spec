Name: fdkaac
Version: 1.0.1
Release: alt2

Summary: command line encoder frontend for libfdk-aac
License: Zlib
Group: File tools

Url: https://github.com/nu774/fdkaac

# Source-url: https://github.com/nu774/fdkaac/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: libfdk-aac-devel

Provides: fdkacc
Obsoletes: fdkacc

%description
fdkaac - command line frontend for libfdk-aac encoder.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*
%doc README COPYING

%changelog
* Tue Feb 02 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt2
- build with correct package name

* Wed Jan 20 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- initial build for ALT Sisyphus
