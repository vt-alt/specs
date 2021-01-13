%define ext_dir  %{_libdir}/LibreOffice-still/share/extensions/
%define ext_name altcsp

Name: LibreOffice-plugin-altcsp
Version: 0.0.1
Release: alt1

Group: File tools
Summary: LibreOffice plugin for alt-csp-cryptopro
License: GPL-2.0-or-later

Source: %ext_name.tar
Requires: alt-csp-cryptopro

%add_python_req_skip uno unohelper com

%description
LibreOffice plugin for alt-csp-cryptopro

%prep
# noop

%build
# noop

%install
install -dm0755 %buildroot%ext_dir/
cd %buildroot%ext_dir/
tar -xvf %SOURCE0
cp %_licensedir/%license %buildroot%ext_dir/%ext_name/license.txt

%files
%ext_dir/%ext_name/

%changelog
* Wed Dec 09 2020 Oleg Solovyov <mcpain@altlinux.org> 0.0.1-alt1
- initial build

