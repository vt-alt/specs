# TODO: build from sources
%define base_name electron

Name: electron4
Version: 4.1.1
Release: alt2

Summary: Build cross platform desktop apps with JavaScript, HTML, and CSS

License: MIT License
Url: https://electronjs.org/
Group: Development/Other

# Source-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-x64.zip
Source: %name-%version.tar
# Source1-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-ia32.zip
Source1: %name-%version-i586.tar
# Source2-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-arm64.zip
Source2: %name-%version-aarch64.tar

Source10: patch_binary.sh

ExclusiveArch: x86_64 i586 aarch64

%set_verify_elf_method skip
#add_findreq_skiplist %_libdir/%name/bin/code
AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

BuildRequires: libgtk+3 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf
# bundled:
# library libnode.so not found
# library libffmpeg.so not found

%description
Build cross platform desktop apps with JavaScript, HTML, and CSS.

%prep
%setup
%ifarch i586
tar xfv %SOURCE1
%endif

%ifarch aarch64
tar xfv %SOURCE2
# hack: we have lib64/ld-linux-aarch64.so.1
sed -E -i -e "s@/lib/ld-linux-aarch64.so.1@/lib64/ld-2.27.so\x0________@" ./%base_name
rm -rf swiftshader
%endif

# drop undefined symbols from binaries
#sh %SOURCE10 ./%name

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/%base_name %buildroot/%_bindir/%name

%files
%_bindir/%name
%_libdir/%name/

%changelog
* Thu Aug 01 2019 Pavel Moseev <mars@altlinux.org> 4.1.1-alt2
- rename to electron4

* Sun Mar 24 2019 Vitaly Lipatov <lav@altlinux.ru> 4.1.1-alt1
- new version 4.1.1 (with rpmrb script)

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.8-alt1
- new version 4.0.8 (with rpmrb script)

* Sat Mar 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.6-alt1
- new version 4.0.6 (with rpmrb script)

* Fri Mar 08 2019 Vitaly Lipatov <lav@altlinux.ru> 3.1.6-alt1
- new version 3.1.6 (with rpmrb script)

* Tue Dec 25 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- new version 2.0.5 (with rpmrb script)

* Thu Jul 12 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt2
- enable build on aarch64

* Thu Jul 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)
- GTK3 now

* Sun May 20 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- new version 1.8.7 (with rpmrb script)

* Sat Jan 06 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- new version 1.7.10 (with rpmrb script)

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.11-alt1
- initial release for ALT Sisyphus (just pack binaries)
