Name:      rpm-build-golang
Version:   1.0.7
Release:   alt1
Summary:   RPM build enviroment to build GO packages
Group:     Development/Other
License:   GPL
BuildArch: noarch
Packager:  Alexey Gladkov <legion@altlinux.ru>

Source0:   golang.macros

Source1:   golang-build
Source2:   golang-install
Source3:   golang-prepare

Source4:   golang-prov
Source5:   golang-prov.files

Source6:   golang-req
Source7:   golang-req.files

Requires:  golang
Requires:  rpm-macros-golang >= %EVR

#lav@: Ещё у меня предложение по rpm-build-golang
#Каждое изменение в подобном пакете должно вести к увеличению версии.
#Релиз отражает лишь изменение способа упаковки пакета.
#Суть в том, что на релиз сложно ставить зависимость, если пакет потом бэкпортируется.

%description
RPM build enviroment to build GO packages

%package -n rpm-macros-golang
Summary: RPM helper macros to build GO packages
Group: Development/Other
BuildArch:      noarch

%description -n rpm-macros-golang
These helper macros provide possibility to create GO packages.

%install
mkdir -p \
	%buildroot/%_rpmlibdir \
	%buildroot/%_rpmmacrosdir \
	%buildroot/%_datadir/golang

cp %SOURCE0 %buildroot%_rpmmacrosdir/golang
cp %SOURCE1 %SOURCE2 %SOURCE3 %buildroot/%_datadir/golang
cp %SOURCE4 %buildroot%_rpmlibdir/golang.prov
cp %SOURCE5 %buildroot%_rpmlibdir/golang.prov.files
cp %SOURCE6 %buildroot%_rpmlibdir/golang.req
cp %SOURCE7 %buildroot%_rpmlibdir/golang.req.files

%files
%_datadir/golang
%_rpmlibdir/*
%exclude %{_rpmmacrosdir}*

%files -n rpm-macros-golang
%_rpmmacrosdir/golang

%changelog
* Thu Feb 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.7-alt1
- Added riscv64 to %%go_arches.

* Mon Sep 23 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.6-alt1
- golang-build: prefer usage of vendor dir instead of internet to get sources
- golang-build: fix previously disabled GO111MODULE (needed by some packages)

* Mon Sep 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.5-alt1
- golang-build: use GO111MODULE to disable go use internet at build stage.

* Sun Feb 10 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.4-alt1
- Added ppc64le to %%go_arches.

* Thu Jan 31 2019 Ivan A. Melnikov <iv@altlinux.org> 1.0.3-alt1
- added mipsel to %%go_arches

* Fri Feb 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.2-alt1
- added aarch64 to %%go_arches

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- NMU: bumped version by request of lav@

* Wed Dec 13 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt7
- NMU: added %%gobuild

* Mon Dec 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt6
- NMU: added %%gotest

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt5
- NMU: moved macros to %%_rpmmacrosdir/
- added rpm-macros-golang

* Tue Aug 08 2017 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- golang-build: Add more arguments.

* Sun Jul 23 2017 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- golang-prepare: copy all sources.

* Mon Jan 25 2016 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2
- Move go_path to _datadir/gocode.

* Tue Oct 20 2015 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First build.
