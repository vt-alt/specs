Name: qcad-dxf2pdf
Version: 1.1
Release: alt1

Summary: Command-line converter from DXF to PDF using qcad
Group:  Graphics
License: GPL-3.0
Url: https://gist.github.com/slazav/2c617b8e7ba09ec67e1e633b043f89dd
Source: %name-%version.tar
BuildArch: noarch
Requires: qcad

%description
Command-line converter from DXF to PDF using qcad

%prep
%setup

# qcad keeps all *.js scripts in %_libdir/qcad/scripts.
# I'm using %_datadir/qcad/scripts/ to have proper noarch package.
%define scriptdir %_datadir/qcad/scripts

%install
install -D dxf2pdf.js %buildroot%scriptdir/dxf2pdf.js
install -D dxf2pdf.1  %buildroot%_man1dir/dxf2pdf.1
install -D -m 755 dxf2pdf %buildroot%_bindir/dxf2pdf

sed -i -e 's|@SCRIPTDIR@|%scriptdir|'\
   %buildroot%_bindir/dxf2pdf %buildroot%_man1dir/dxf2pdf.1

%files
%scriptdir/dxf2pdf.js
%_bindir/dxf2pdf
%_man1dir/dxf2pdf.*

%changelog
* Fri Jul 03 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- fix error message in case of wrong argument number

* Fri Jul 03 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- initial version

