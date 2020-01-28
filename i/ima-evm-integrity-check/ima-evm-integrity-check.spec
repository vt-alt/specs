Name: ima-evm-integrity-check
Version: 0.5.0
Release: alt1

Summary: IMA/EVM integrity check
License: %gpl2plus
Group: System/Base

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: make-initrd

Requires: make-initrd-integrity

%define _unpackaged_files_terminate_build 1

%description
This package make use of the IMA and EVM technologies from the Linux integrity
subsystem.
Basically IMA and EVM provide the following functionality:

- measurement (hashing) of file content as it is accessed and keeping track of
  this information in an audit log.
- appraisal of files, which allows to prevent access when a measurement (hash)
  or digital signature does not match the expected value.

This package requires kernel with corresponding config options enabled.

%package -n make-initrd-integrity
Summary: Integrity check feature for make-initrd
Group: System/Base

# For put-file utility
Requires: make-initrd >= 0.7.6-alt1
Requires: keyutils ima-evm-utils
Requires: filesystem >= 2.3.13-alt1.M80C.1

BuildArch: noarch

%description -n make-initrd-integrity
Integrity check feature for make-initrd

%prep
%setup

%build
LIBDIRS="/%_lib %_libdir"
if [ %_lib = lib64 ]; then
	# There is some shared objects too
	LIBDIRS="$LIBDIRS /lib %_usr/lib"
fi
LIBEXECDIRS="%_usr/libexec $LIBDIRS"

sed -r -e "s;@LIBDIRS@;$LIBDIRS;" -e "s;@EXECLIBDIRS@;$LIBEXECDIRS;" integrity-sign.in >integrity-sign
chmod +x integrity-sign

%install
install -pD -m 750 integrity-sign %buildroot%_sbindir/integrity-sign

# make-initrd feature
mkdir -p %buildroot%_sysconfdir/integrity/
mkdir -p %buildroot%_datadir/integrity/
mkdir -p %buildroot%_datadir/make-initrd/features/integrity/
cp -a make-initrd/*.mk %buildroot%_datadir/make-initrd/features/integrity/

MI_VERSION="$(/usr/sbin/make-initrd --version | sed -n -r 's;^make-initrd version ([[:digit:]]+)\..*;\1;p')"
if [ -n "$MI_VERSION" ] && [ "$MI_VERSION" -ge 2 ]; then
	install -pD -m 755 make-initrd/integrity.init %buildroot%_datadir/make-initrd/features/integrity/data/etc/rc.d/init.d/integrity
else
	mkdir -p %buildroot%_datadir/make-initrd/features/integrity/data/lib/initrd/modules/
	cp -a make-initrd/085-integrity %buildroot%_datadir/make-initrd/features/integrity/data/lib/initrd/modules/
fi

%files
%doc policy.example
%_sbindir/integrity-sign

%files -n make-initrd-integrity
%dir %_sysconfdir/integrity/
%dir %_datadir/integrity/
%_datadir/make-initrd/features/integrity

%changelog
* Tue Apr 09 2019 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1
- integrity-sign: Fix chattr tmpdir cleanup.
- integrity-sign: Create new initrd by default.
- integrity-sign: Sign kernel modules.

* Tue Apr 02 2019 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1
- integrity-sign: Fix -i option with spaces in filenames.
- integrity-sign: Handle shared objects in /var/lib too.

* Fri Jan 25 2019 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Package example policy.

* Fri Nov 16 2018 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Determine make-initrd version at build time.
- Add make-initrd-2.x support.

* Thu Nov 15 2018 Mikhail Efremov <sem@altlinux.org> 0.3-alt1.M80C.1
- New version.

* Thu Nov 01 2018 Mikhail Efremov <sem@altlinux.org> 0.2-alt0.M80C.1
- integrity-sign: Make signed files immutable.
- integrity-sign: Use single command to sign files.

* Wed Oct 24 2018 Mikhail Efremov <sem@altlinux.org> 0.1-alt0.M80C.1
- Initial build.
