%global provider        github.com
%global project         opencontainers
%global repo            runc

%global provider_prefix %{provider}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          d736ef14f0288d6993a1845745d6756cfc9ddd5a
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

Name:           runc
Version:        1.0.0
Release:        alt14.rc92
Summary:        CLI for running Open Containers
Group:          Development/Other
License:        Apache-2.0
URL:            https://%provider_prefix
ExclusiveArch:  %go_arches

Source0:        %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libseccomp-devel
Provides: docker-runc = %version-%release
Obsoletes: docker-runc <= 1.0.0-alt2.gitb2567b3

%description
The runc command can be used to start containers which are packaged
in accordance with the Open Container Initiative's specifications,
and to manage containers running under runc.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path:$BUILDDIR"

%golang_prepare
# TODO: Looks ugly. Definetly should be fixed.
rm -fr "$BUILDDIR/src/$IMPORT_PATH/vendor"
cp -alv -- vendor/* "$BUILDDIR/src"
make COMMIT=%commit

%install
mkdir -p -- %buildroot/%_bindir
install -p -m 755 runc %buildroot/%_bindir/%name

mkdir -p -- %buildroot/lib/tmpfiles.d
cat > %buildroot/lib/tmpfiles.d/runc.conf <<EOF
d /run/runc 0700 root root -
EOF

%files
%doc MAINTAINERS_GUIDE.md PRINCIPLES.md README.md CONTRIBUTING.md
%_bindir/*
/lib/tmpfiles.d/runc.conf

%changelog
* Tue Sep 29 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt14.rc92
- New version

* Fri Jul 3 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt13.rc91
- New version

* Mon Feb 17 2020 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt12.rc10
- New version
- Fixes CVE-2019-19921

* Tue Dec 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt11.rc9
- Print user friendly error on cgroups v2
- Fix license name

* Thu Oct 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt10.rc9
- New version
- fixes: CVE-2019-16884

* Thu Jul 4 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt9.rc8
- New version

* Wed Apr 10 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt8.rc7
- New version

* Wed Feb 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt7.git0a012df
- snapshot of master branch.
- Fixes CVE-2019-5736.

* Tue Jan 29 2019 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt6.rc6
- New version (for docker 18.09.1-ce).

* Fri Jul 20 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt5.git69663f0
- New version (for docker 18.06.0-ce).

* Thu Mar 22 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt4.rc5
- New version (for docker 18.03.0-ce).

* Mon Feb 5 2018 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt3.git9f9c962
- New version (for docker 18.02.0-ce).

* Mon Jan 23 2017 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt2.gitc91b5be
- New version.
- Fixes CVE-2016-9962.

* Tue Aug 2 2016 Vladimir Didenko <cow@altlinux.ru> 1.0.0-alt1.git04f275d
- New version.

* Thu May 12 2016 Vladimir Didenko <cow@altlinux.ru> 0.1.1-alt1.gitbaf6536
- New version.

* Wed Mar 16 2016 Alexey Gladkov <legion@altlinux.ru> 0.0.9-alt1.git69fe79d
- First build for Altlinux.
