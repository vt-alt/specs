%define pkg nodejs
Name: rpm-build-%pkg
Version: 0.20.4
Release: alt2

Summary: RPM helper scripts for building %pkg packages

License: GPLv2+
Group: Development/Other
Url: http://www.altlinux.org/Node.JS_Policy
BuildArch: noarch

Source: %name-%version.tar
Source1: macros.nodejs-tap
Source2: %pkg.prov.files
Source3: %pkg.env

Patch0: macros.nodejs-alt.patch
Patch1: nodejs.req-alt.patch
Patch2: nodejs.req-alt-rpmbuild404.patch
Patch3: nodejs.req-alt-utf8.patch

Provides:      nodejs-packaging = %version
Requires:      npm
Requires:      node-devel
Requires:      node-gyp

Requires:      rpm-macros-%pkg

%description
RPM helper scripts and build environment
for building %pkg packages.

See %url for detailed %pkg packaging policy.

%package -n rpm-macros-%pkg
Summary: RPM helper macros for building %pkg packages

License: GPLv2+
Group: Development/Other


%description -n rpm-macros-%pkg
RPM macros for building %pkg packages.

See %url for detailed %pkg packaging policy.

%prep
%setup
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2

%install
mkdir -p %buildroot/%_rpmmacrosdir/
cat >> %buildroot/%_rpmmacrosdir/%pkg << 'EOF'
%%_rpm_build_nodejsdir	%%_datadir/%name
%%nodejs_arches	%%ix86 x86_64 %%arm
EOF
sed -e s,_rpmconfigdir,_rpm_build_nodejsdir,g macros.nodejs >> %buildroot/%_rpmmacrosdir/%pkg

# TMP:
cat %{SOURCE1} >> %buildroot%_rpmmacrosdir/%pkg

install -D -m755 %pkg.prov %buildroot/usr/lib/rpm/%pkg.prov
install -D -m755 %{SOURCE2} %buildroot/usr/lib/rpm/%pkg.prov.files
install -D -m644 %{SOURCE3} %buildroot%_rpmmacrosdir/%pkg.env
install -D -m755 %pkg.req %buildroot/usr/lib/rpm/%pkg.req
ln -s %pkg.prov.files %buildroot/usr/lib/rpm/%pkg.req.files
install -D -m755 nodejs-fixdep  %buildroot%_datadir/%name/%pkg-fixdep
install -D -m755 nodejs-symlink-deps  %buildroot%_datadir/%name/%pkg-symlink-deps
install -D -m755 nodejs-setversion %{buildroot}%_datadir/%name/%pkg-setversion
install -Dpm0644 multiver_modules %{buildroot}%{_datadir}/node/multiver_modules

%files
%_datadir/%name
%{_datadir}/node/multiver_modules
/usr/lib/rpm/%pkg.prov
/usr/lib/rpm/%pkg.prov.files
/usr/lib/rpm/%pkg.req
/usr/lib/rpm/%pkg.req.files
# unused now
%exclude %_rpmmacrosdir/%pkg.env

%files -n rpm-macros-%pkg
%_rpmmacrosdir/%pkg

%changelog
* Thu Feb 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt2
- don't need rpm-build-python3 for node-gyp
- require rpm-macros-nodejs from rpm-build-nodejs

* Mon Jan 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.20.4-alt1
- node-gyp: drop --tarball

* Fri Jan 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.20.3-alt1
- added (+) short npm build and install macros scripts
- fixed (*) license
- fixed (*) dependencies

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 0.20.2-alt1
- utf-8 patch (closes: #36427)

* Sat Mar 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.20.1-alt1
- bugfix for rpmbuild 4.04

* Fri Mar 22 2019 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- sync with nodejs-packaging 20-2

* Mon Aug 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1
- fixed warning in nodejs.req

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- provides nodejs-packaging

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- temporarily added nodejs-tap macros

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1
- sync with nodejs-packaging 3-1

* Tue Jun 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1
- bugfixes

* Sun Jun 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- bugfixes
- TODO: sync with nodejs-0.10.12-1 after node update

* Sat Jun 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
