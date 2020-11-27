Name:     perl-Zabbix-Sender
Version:  0.07
Release:  alt1

Summary:  A pure-perl implementation of zabbix-sender
License:  GPL-2.0+ or Artistic-1.0
Group:    Development/Perl
Url:      https://github.com/dominikschulz/Zabbix-Sender

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   Zabbix-Sender-%version.tar
Source1:  Makefile.PL

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
BuildRequires: perl-devel
BuildRequires: perl-Moo
BuildRequires: perl-namespace-autoclean
BuildRequires: perl-JSON
BuildRequires: perl(Types/Standard.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Output.pm)

%description
%summary

%prep
%setup -n Zabbix-Sender-%version
install %SOURCE1 Makefile.PL

%build
%perl_vendor_build

%install
%makeinstall_std

%check
make test

%files
%doc README.md
%_bindir/zabbix-sender
%perl_vendorlib/Zabbix/Sender.pm
%_man1dir/zabbix-sender.1*

%changelog
* Wed Nov 25 2020 Andrey Cherepanov <cas@altlinux.org> 0.07-alt1
- Initial build for Sisyphus
