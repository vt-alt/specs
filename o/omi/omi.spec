# TODO: issue about dash in version: https://github.com/Microsoft/omi/issues/532
Name:     omi
Version:  1.6.2
Release:  alt1

Summary:  Open Management Infrastructure
License:  MIT
Group:    Other
Url:      https://github.com/Microsoft/omi

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Microsoft/omi/archive/v%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Jun 02 2017
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel lsb-release pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ libpam-devel libssl-devel openssl
BuildRequires: libkrb5-devel

ExclusiveArch: aarch64 x86_64

%ifarch aarch64
# no lsb
%else
BuildRequires: lsb-core
%endif

%description
Open Management Infrastructure (OMI) is an open source project
to further the development of a production quality implementation
of the DMTF CIM/WBEM standards.
The OMI CIMOM is also designed to be portable and highly modular.

In order to attain its small footprint, it is coded in C,
which also makes it a much more viable CIM Object Manager for embedded systems
and other infrastructure components that have memory constraints for their management processor.

%package -n lib%name

Summary: Open Management Infrastructure
Group: Development/C

%description -n lib%name
Open Management Infrastructure (OMI) is an open source project
to further the development of a production quality implementation
of the DMTF CIM/WBEM standards.
The OMI CIMOM is also designed to be portable and highly modular.

In order to attain its small footprint, it is coded in C,
which also makes it a much more viable CIM Object Manager for embedded systems
and other infrastructure components that have memory constraints for their management processor.

%package -n lib%name-devel

Summary: Open Management Infrastructure
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name.

%package -n lib%name-internal-devel

Summary: Open Management Infrastructure
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-internal-devel
Internal development files for %name.


%prep
%setup

%__subst "s|.*-rpath.*|true|g" Unix/buildtool
# fix aarch detection
%__subst "s|arm|aarch64|" Unix/buildtool
# instead of lsb_release
%__subst "s|distro=.*|distro=ALT|g" Unix/buildtool
%__subst "s|distro_version=.*|distro_version=Sisyphus|g" Unix/buildtool

%build
# FIXME: version
export OMI_BUILDVERSION_MAJOR=$(echo %version | cut -d. -f1)
export OMI_BUILDVERSION_MINOR=$(echo %version | cut -d. -f2)
export OMI_BUILDVERSION_PATCH=$(echo %version | cut -d. -f3)
# See https://github.com/Microsoft/omi/issues/532
export OMI_BUILDVERSION_BUILDNR=0

cd Unix
./configure --prefix=%prefix --localstatedir=/var/omi --sysconfdir=/etc/omi \
	--libdir=%_libdir --includedir=%_includedir/omi --datadir=%_datadir/%name \
	--certsdir=/etc/omi/ssl
#	 --credsdir=/etc/omi/creds

%make_build || make

%install
cd Unix
%makeinstall_std
for i in pal base provreg sock oi ; do
    mkdir -p %buildroot%_includedir/omi/$i/
    cp $i/*.h %buildroot%_includedir/omi/$i/
done

mkdir -p %buildroot%_includedir/omi/nits/base/
cp nits/base/nits.h %buildroot%_includedir/omi/nits/base/
cp common/common.h %buildroot%_includedir/omi/
cp common/localizestr.h %buildroot%_includedir/omi/
cp output/include/config.h %buildroot%_includedir/omi/

cp -a pal/*.h %buildroot%_includedir/omi/pal/
subst "s|common/linux/sal.h|linux/sal.h|g" %buildroot%_includedir/omi/pal/palcommon.h
rm -f %buildroot%_includedir/omi/pal/{strlcat.h,strlcpy.h}
mkdir -p %buildroot%_includedir/omi/linux/
cp -a common/linux/sal.h %buildroot%_includedir/omi/linux/

mkdir -p %buildroot%_libdir/%name/{bin,lib}/
cp output/bin/{chkshlib,mkdep,oigenc,strhash} %buildroot%_libdir/%name/bin/
ln -sr %buildroot%_bindir/omireg %buildroot%_libdir/%name/bin/omireg
ln -sr %buildroot%_bindir/omigen %buildroot%_libdir/%name/bin/omigen
cp output/lib/*.a %buildroot%_libdir/%name/lib/
#cp output/lib/libnits.so %buildroot%_libdir/%name/lib/

#%check
#%make_build check

%files
%dir %_sysconfdir/omi/
%_sysconfdir/omi/omiregister/
%_sysconfdir/omi/ssl/
%config(noreplace) %_sysconfdir/omi/*.conf
%_bindir/*
#_man1dir/*
%doc LICENSE CONTRIBUTING.md README.md

%files -n lib%name
%_libdir/*.so
%_datadir/%name/

%files -n lib%name-devel
%dir %_includedir/omi/
%_includedir/omi/MI.h
%_includedir/omi/micxx/
%_includedir/omi/omiclient/

%files -n lib%name-internal-devel
%_libdir/%name/
%_includedir/omi/common.h
%_includedir/omi/config.h
%_includedir/omi/localizestr.h
%_includedir/omi/linux/
%_includedir/omi/pal/
%_includedir/omi/base/
%_includedir/omi/provreg/
%_includedir/omi/sock/
%_includedir/omi/oi/
%_includedir/omi/nits/

%changelog
* Sun Dec 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- new version (1.6.2) with rpmgs script

* Thu Sep 20 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt2
- NMU: rebuilt with openssl-1.1.

* Thu Jun 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version (1.4.2) with rpmgs script
- fix build on aarch64

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt2
- add internal pal headers

* Fri Jun 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus
