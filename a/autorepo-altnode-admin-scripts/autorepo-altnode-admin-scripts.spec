Name: autorepo-altnode-admin-scripts
Version: 0.06
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: admin scripts for an automated packaging node
Group: Development/Other
License: GPL2+
#Url: 
Source: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install

mkdir -p $RPM_BUILD_ROOT%_bindir
install -m 755 autorepo-altnode-admin-setup-build-node $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_sbindir
install -m 755 autorepo-altnode-admin-create-*node $RPM_BUILD_ROOT%_sbindir
install -m 755 autorepo-altnode-admin-delete-*node $RPM_BUILD_ROOT%_sbindir

%files
#%doc 
%_bindir/*
%_sbindir/*

%changelog
* Thu May 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- apt config for newer builder

* Mon Jul 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- support for new repocop for tasks

* Fri May 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- adjusted limits

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Sun Oct 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- support for common /space

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build
