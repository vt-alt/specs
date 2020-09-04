Name: bitcoin
Version: 0.20.1
Release: alt1

Summary: peer-to-peer network based anonymous digital currency
License: MIT
Group: Networking/Other

Url: http://www.bitcoin.org/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Sep 14 2017
# optimized out: boost-devel boost-devel-headers gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libcom_err-devel libdb4-devel libgpg-error libkrb5-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-xml libstdc++-devel llvm perl pkg-config python-base python-modules qt5-base-common
BuildRequires: boost-filesystem-devel boost-interprocess-devel boost-program_options-devel boost-signals-devel
BuildRequires: clang libevent-devel libminiupnpc-devel libprotobuf-devel libqrencode-devel
BuildRequires: libssl-devel protobuf-compiler python-module-mpl_toolkits qt5-base-devel qt5-tools libdb4.8_cxx-devel

%description
Q. What is Bitcoin?
A. Bitcoin is a peer-to-peer currency. Peer-to-peer means that no
central authority issues new money or tracks transactions. These tasks
are managed collectively by the network.

Q. How does Bitcoin work?
A. Bitcoin utilises public-key cryptography. A coin contains the owner's
public key. When a coin is transferred from user A to user B, A adds B's
public key to the coin, and the coin is signed using A's private key. B
now owns the coin and can transfer it further. A is prevented from
transferring the already spent coin to other users because a public list
of all previous transactions is collectively maintained by the network.
Before each transaction the coin's validity will be checked.

%prep
%setup
%patch0 -p1

%build
./autogen.sh
export OBJC=clang
export OBJCXX=clang++
%configure \
	--enable-upnp-default \
	--with-gui=qt5
%make_build V=1

%install
%makeinstall_std
ln -s %name-qt %buildroot%_bindir/%name

%pre
rm -f %_bindir/%name

%files
%_bindir/%{name}*
%_mandir/man1/bitcoin*.1.*
%doc doc/*

%changelog
* Mon Aug 03 2020 Alexei Takaseev <taf@altlinux.org> 0.20.1-alt1
- 0.20.1

* Wed Jun 03 2020 Alexei Takaseev <taf@altlinux.org> 0.20.0-alt1
- 0.20.0

* Thu Mar 05 2020 Alexei Takaseev <taf@altlinux.org> 0.19.1-alt1
- 0.19.1

* Tue Feb 04 2020 Alexei Takaseev <taf@altlinux.org> 0.19.1-alt0.rc1
- 0.19.1rc1
- Fix build with boost-1.72

* Tue Nov 19 2019 Alexei Takaseev <taf@altlinux.org> 0.19.0.1-alt1
- Version 0.19.0.1

* Mon Nov 11 2019 Alexei Takaseev <taf@altlinux.org> 0.19.0-alt1
- Version 0.19.0

* Mon Oct 28 2019 Alexei Takaseev <taf@altlinux.org> 0.18.1-alt2
- Remove BR: lcov

* Sun Aug 04 2019 Alexei Takaseev <taf@altlinux.org> 0.18.1-alt1
- Version 0.18.1

* Fri May 03 2019 Alexei Takaseev <taf@altlinux.org> 0.18.0-alt1
- Version 0.18.0

* Mon Dec 24 2018 Alexei Takaseev <taf@altlinux.org> 0.17.1-alt1
- Version 0.17.1

* Tue Oct 30 2018 Alexei Takaseev <taf@altlinux.org> 0.17.0.1-alt1
- Version 0.17.0.1

* Tue Oct 02 2018 Alexei Takaseev <taf@altlinux.org> 0.17.0-alt1
- Version 0.17.0

* Tue Sep 18 2018 Alexei Takaseev <taf@altlinux.org> 0.16.3-alt1
- Version 0.16.3

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.16.2-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Fri Jul 27 2018 Alexei Takaseev <taf@altlinux.org> 0.16.2-alt1
- Version 0.16.2

* Thu Jun 14 2018 Alexei Takaseev <taf@altlinux.org> 0.16.1-alt1
- Version 0.16.1

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt2.1
- NMU: rebuilt with boost-1.67.0

* Thu Apr 19 2018 Alexei Takaseev <taf@altlinux.org> 0.16.0-alt2
- Rebuild with boost 1.66.0

* Mon Feb 26 2018 Alexei Takaseev <taf@altlinux.org> 0.16.0-alt1
- Version 0.16.0

* Fri Nov 10 2017 Alexei Takaseev <taf@altlinux.org> 0.15.1-alt1
- Version 0.15.1

* Thu Sep 21 2017 Alexei Takaseev <taf@altlinux.org> 0.15.0.1-alt1
- Version 0.15.0.1

* Thu Sep 14 2017 Alexei Takaseev <taf@altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Wed Jun 10 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.3-alt1.rc1.1.1
- Rebuilt with:
 + gcc5 C++11 ABI.
 + boost 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.9.3-alt1.rc1.1
- rebuild with boost 1.57.0

* Thu Sep 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.rc1
- Version 0.9.3rc1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.0-alt1.4.qa1
- NMU: rebuilt for updated dependencies.

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.4
- Rebuilt with Boost 1.53.0

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.3
- Rebuilt with Boost 1.52.0

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.2
- Rebuilt with Boost 1.51.0
- Enabled debuginfo

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.1
- Rebuilt with Boost 1.49.0

* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 0.6.0-alt1
- 0.6.0 (Closes: #26403).

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Rebuilt with Boost 1.48.0

* Tue Oct 04 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.4.0-alt1
- 0.4.0 (Closes: #26403).

* Tue Jul 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.21-alt1.1
- Rebuilt with Boost 1.47.0

* Wed May 04 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 0.3.21-alt1
- Initial build for Sisyphus.

