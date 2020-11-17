Name: openssl-gost-engine
Version: 1.1.0.3.0.255.ge3af41d.p1
Release: alt3

License: BSD-style
Summary: A reference implementation of the Russian GOST crypto algorithms for OpenSSL

Group: System/Libraries

Source: %name-%version.tar
Source1: openssl-gost.control

Patch0: %name-1.1.0.3.0.255.ge3af41d-mac-iv.patch
Patch1: %name-1.1.0.3.0.255.ge3af41d-gost89-ecb.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
# due to gost algorithms identifiers (in headers)
BuildRequires: libssl-devel >= 1.1.0j-alt2

%{?!_without_check:%{?!_disable_check:BuildRequires: ctest perl-devel perl-Test2-Suite openssl}}

# due to gost algorithms identifiers (inside libcrypto)
Requires: libcrypto1.1 >= 1.1.0j-alt2

%description
A reference implementation of the Russian GOST crypto algorithms for OpenSSL.

%package -n gostsum
Summary: GOST file digesting utilites
Group: File tools

%description -n gostsum
GOST file digesting utilites.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%ifarch %e2k
# lcc 1.23.12: test_curves.c: if ((test = (e)))
%add_optflags -Wno-error=assign-where-compare-meant
%endif
%cmake \
	#

%cmake_build

%install
enginesdir="$(pkg-config --variable=enginesdir libcrypto)"
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot$enginesdir

cp BUILD/bin/gost.so %buildroot$enginesdir/
cp BUILD/bin/gost*sum %buildroot%_bindir/
cp gost*sum.1 %buildroot%_man1dir/

# Install the control scripts
install -D -p -m0755 %_sourcedir/openssl-gost.control \
        %buildroot%_controldir/openssl-gost

%check
CTEST_OUTPUT_ON_FAILURE=1 \
	make test -C BUILD ARGS="--verbose"

%files
%_libdir/openssl/engines-1.1/gost.so
%_controldir/openssl-gost

%files -n gostsum
%_bindir/gost*sum*
%_man1dir/gost*sum*

%changelog
* Mon Jun 01 2020 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt3
- Fix for the "openssl-gost' control: Don't override the main section
  (closes: 37922).

* Fri Oct 25 2019 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt2
- Added openssl-gost control script to turn the GOST ciphers on
  and off.

* Fri Aug 16 2019 Michael Shigorin <mike@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt1.1
- E2K: workaround tests ftbfs

* Thu Jul 04 2019 Paul Wolneykien <manowar@altlinux.org> 1.1.0.3.0.255.ge3af41d.p1-alt1
- Allow to set an IV for MAC using EVP_MD_CTRL_SET_IV (patch).
- Added ECB mode GOST28147-89 cipher (patch).

* Mon Mar 04 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.255.ge3af41d-alt1
- Backported new algorithms from upstream master.

* Sat Sep 29 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.0.3.0.21.ga2174a8-alt1
- Initial build (v1.1.0.3-21-ga2174a8).
