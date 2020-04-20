%global _ocfroot %{_exec_prefix}/lib/ocf
%global _tag 2.3.0

Name: resource-agents-paf
Version: 2.3.0
Release: alt1
BuildArch: noarch
Packager: Pavel Vasenkov <pav@altlinux.org>

Summary: PostgreSQL resource agent for Pacemaker
Group: Databases
License: PostgreSQL
Source0: https://github.com/ClusterLabs/PAF/archive/v%{_tag}.tar.gz
Url: http://clusterlabs.github.io/PAF/

BuildRequires: resource-agents perl perl-Module-Build
Requires: perl, resource-agents, pacemaker >= 1.1.13, corosync >= 2.0.0

%description
%summary

# do not build -debuginfo package
%define debug_package %{nil}

%prep
%setup -q -n v%{_tag}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md CHANGELOG.md LICENSE

%attr(755, -, -) %{_ocfroot}/resource.d/heartbeat/pgsqlms
%{_ocfroot}/lib/heartbeat/OCF_ReturnCodes.pm
%{_ocfroot}/lib/heartbeat/OCF_Directories.pm
%{_ocfroot}/lib/heartbeat/OCF_Functions.pm
%{_datadir}/resource-agents/ocft/configs/pgsqlms

%changelog
* Thu Apr 09 2020 Pavel Vasenkov <pav@altlinux.ru> 2.3.0-alt1
- Initial commit in Sisyphus
