Name:		xmrig
Version:	6.12.1
Release:	alt0.p9.1
Summary:	RandomX and CryptoNight CPU miner
Url:		https://github.com/xmrig/xmrig
Group:		Office
License:	GPLv3
Source0:	%name.tar.xz

Patch0:		%name-6.3.0-minimum_donate_0.diff
Patch1:		%name-5.10.0-Wno-class-memaccess_alt_rm.diff
Patch2:		%name-6.8.1-maes_armh.diff

BuildRequires:	cmake gcc-c++ libmicrohttpd-devel libssl-devel-static libstdc++-devel-static libuv-devel libkrb5-devel zlib-devel libcpuid-devel

ExcludeArch:	ppc64le aarch64 armh

%description
XMRig is high performance RandomX and CryptoNight CPU miner, with the official full
Windows support. Originally based on cpuminer-multi with heavy optimizations/rewrites
and removing a lot of legacy code, since version 1.0.0 complete rewritten from scratch
on C++.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1

%ifarch armh
# To fix "unrecognized command-line option '-maes'" for armh
%patch2 -p1
%endif

%build
mkdir ./build && cd ./build
cmake		../. \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_CXX_FLAGS:STRING="%optflags" \
		-DCMAKE_C_FLAGS:STRING="%optflags" \
		-DWITH_HWLOC=OFF \
		-DWITH_EMBEDDED_CONFIG=ON
%make_build

%install
cd ./build
install -Dp -m 0755 ./%name %buildroot%_bindir/%name

%files
%doc LICENSE README.md CHANGELOG.md src/config.json
%_bindir/*

%changelog
* Sun May 09 2021 Motsyo Gennadi <drool@altlinux.ru> 6.12.1-alt0.p9.1
- build for p9

* Sat May 08 2021 Motsyo Gennadi <drool@altlinux.ru> 6.12.1-alt1
- 6.12.1

* Mon Apr 12 2021 Motsyo Gennadi <drool@altlinux.ru> 6.11.2-alt1
- 6.11.2

* Sun Feb 14 2021 Motsyo Gennadi <drool@altlinux.ru> 6.8.2-alt1
- 6.8.2

* Sat Feb 06 2021 Motsyo Gennadi <drool@altlinux.ru> 6.8.1-alt2.1
- fix diff-file name

* Fri Feb 05 2021 Motsyo Gennadi <drool@altlinux.ru> 6.8.1-alt1
- 6.8.1

* Tue Feb 02 2021 Motsyo Gennadi <drool@altlinux.ru> 6.8.0-alt1
- 6.8.0

* Sat Jan 02 2021 Motsyo Gennadi <drool@altlinux.ru> 6.7.0-alt1
- 6.7.0

* Mon Nov 30 2020 Motsyo Gennadi <drool@altlinux.ru> 6.6.1-alt1
- 6.6.1

* Sat Oct 24 2020 Motsyo Gennadi <drool@altlinux.ru> 6.4.0-alt1
- 6.4.0

* Sat Sep 05 2020 Motsyo Gennadi <drool@altlinux.ru> 6.3.3-alt1
- 6.3.3

* Sun Jul 19 2020 Motsyo Gennadi <drool@altlinux.ru> 6.3.0-alt1.1
- add ExcludeArch for armh

* Sun Jul 19 2020 Motsyo Gennadi <drool@altlinux.ru> 6.3.0-alt1
- 6.3.0

* Thu May 07 2020 Motsyo Gennadi <drool@altlinux.ru> 5.11.1-alt1
- 5.11.1

* Sun Apr 12 2020 Motsyo Gennadi <drool@altlinux.ru> 5.10.0-alt1.1
- add ExcludeArch for aarch64

* Thu Apr 09 2020 Motsyo Gennadi <drool@altlinux.ru> 5.10.0-alt1
- 5.10.0

* Wed Mar 11 2020 Motsyo Gennadi <drool@altlinux.ru> 5.9.0-alt1
- 5.9.0

* Sat Aug 24 2019 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1.1
- add ExcludeArch for ppc64le

* Sat Aug 24 2019 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Tue Aug 06 2019 Motsyo Gennadi <drool@altlinux.ru> 2.99.4-alt1
- 2.99.4

* Fri Mar 15 2019 Motsyo Gennadi <drool@altlinux.ru> 2.14.1-alt1
- 2.14.1

* Wed Oct 24 2018 Motsyo Gennadi <drool@altlinux.ru> 2.8.3-alt1
- 2.8.3

* Sat Sep 22 2018 Motsyo Gennadi <drool@altlinux.ru> 2.8.0-alt3
- upstream link fixing

* Sat Sep 22 2018 Motsyo Gennadi <drool@altlinux.ru> 2.8.0-alt2
- fix buildrequires

* Sat Sep 22 2018 Motsyo Gennadi <drool@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Sep 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.6.3-alt2
- rebuild with libmicrohttpd-0.9.59

* Mon Jun 11 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Fri Jun 08 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Sat Apr 21 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.0-alt0.beta3
- 2.6.0-beta3

* Tue Apr 10 2018 Motsyo Gennadi <drool@altlinux.ru> 2.6.0-alt0.beta2
- 2.6.0-beta2

* Thu Apr 05 2018 Motsyo Gennadi <drool@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Tue Jan 30 2018 Motsyo Gennadi <drool@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Tue Nov 07 2017 Motsyo Gennadi <drool@altlinux.ru> 2.4.3-alt2
- added config.json as example

* Mon Nov 06 2017 Motsyo Gennadi <drool@altlinux.ru> 2.4.3-alt1
- initial build for ALT Linux
