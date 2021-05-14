Name: act
%global lname   AutomaticComponentToolkit
%global goipath github.com/Autodesk/%lname
Version: 1.6.0
Release: alt1
Summary: Automatic Component Toolkit
License: BSD

BuildRequires: %_bindir/go

Group: Development/Other
Url: https://%goipath
Packager: Anton Midyukov <antohami@altlinux.org>

#Source-url: %url/archive/v%version/%lname-%version.tar.gz
Source: %lname-%version.tar

%description
The Automatic Component Toolkit (ACT) is a code generator that takes an
instance of an Interface Description Language file and generates a thin
C89-API, implementation stubs and language bindings of your desired software
component.

%prep
%setup -n %lname-%version

%build
%{?!gobuild:%global gobuild go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x}
%gobuild -o act Source/*.go

%install
mkdir -p %buildroot%_bindir
install -m 0755 -vp act %buildroot%_bindir/

%files
%doc README.md
%doc LICENSE.md
%_bindir/act

%changelog
* Thu May 13 2021 Anton Midyukov <antohami@altlinux.org> 1.6.0-alt1
- initial build for ALT Sisyphus

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6.0-1
- Initial package (#1819148)
