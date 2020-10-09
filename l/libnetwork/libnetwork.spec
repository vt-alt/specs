%global provider        github.com
%global project         docker
%global repo            libnetwork

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          026aabaa659832804b01754aaadd2c0f420c68b6
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           libnetwork
Version:        19.03.13
Release:        alt1.git%shortcommit
Summary:        Networking for containers
Group:          Development/Other
License:        Apache-2.0
URL:            https://%provider_prefix
ExclusiveArch:  %go_arches

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libseccomp-devel

%description
libnetwork provides a native Go implementation for connecting containers.
The goal of libnetwork is to deliver a robust Container Network Model that
provides a consistent programming interface and the required network
abstractions for applications.

%package -n docker-proxy
Summary: docker-proxy util
Group: Development/Other

Conflicts: docker-io < 1.13

%description -n docker-proxy
This package provides docker-proxy util.

%prep
%setup -q

%build
export GOPATH="%go_path:$PWD/vendor:$PWD"
# TODO: restore dnet build
go build -o "bin/docker-proxy" ./cmd/proxy

%install
mkdir -p -- %buildroot/%_bindir
install -p -m 755 bin/docker-proxy %buildroot/%_bindir

%files -n docker-proxy
%doc CHANGELOG.md README.md
%_bindir/*

%changelog
* Wed Sep 30 2020 Vladimir Didenko <cow@altlinux.org> 19.03.13-alt1.git026aaba
- New version for docker 19.03.13-ce

* Fri Jun 5 2020 Vladimir Didenko <cow@altlinux.org> 19.03.11-alt1.git153d076
- New version for docker 19.03.11-ce (fixes: CVE-2020-13401)

* Tue Feb 18 2020 Vladimir Didenko <cow@altlinux.org> 19.03.6-alt1.git92cbfe3
- New version (for docker 19.03.6-ce)
- Fix license name

* Fri Nov 15 2019 Vladimir Didenko <cow@altlinux.org> 19.03.5-alt1.git510ec3a
- New version (for docker 19.03.5-ce)

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.org> 19.03.3-alt1.git45c7102
- New version (for docker 19.03.3-ce).

* Thu Jul 25 2019 Vladimir Didenko <cow@altlinux.org> 19.03.0-alt1.gitfc5a7d9
- New version (for docker 19.03.0-ce).

* Thu Jul 5 2019 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt3.gite7933d4
- New version (for docker 18.09.7-ce).

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt2.gitf3d3985
- New version (for docker 18.09.1-ce).

* Thu Nov 22 2018 Vladimir Didenko <cow@altlinux.org> 18.09.0-alt1.git8bc51fd
- New version (for docker 18.09.0-ce).

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt6.git3ac297b
- New version (for docker 18.06.0-ce).

* Mon May 14 2018 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt5.gitc15b372
- define ExclusiveArch as %%go_arches

* Thu May 10 2018 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt4.gitc15b372
- New version (for docker 18.03.1-ce).

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt3.git1b91bc9
- New version (for docker 18.03.0-ce).

* Wed Feb 7 2018 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt2.gitfcf1c3b
- New version.

* Wed Jan 25 2017 Vladimir Didenko <cow@altlinux.org> 0.8.0-alt1.git7b2b1fe
- First build for Altlinux.
