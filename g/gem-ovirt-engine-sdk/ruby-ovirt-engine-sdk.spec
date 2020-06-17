%define        pkgname ovirt-engine-sdk

Name:          gem-%pkgname
Version:       4.3.0
Release:       alt2
Summary:       The oVirt Ruby SDK is a Ruby gem that simplyfies access to the oVirt Engine API
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/oVirt/ovirt-engine-sdk-ruby
Vcs:           https://github.com/oVirt/ovirt-engine-sdk-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: xmllint
BuildRequires: libcurl-devel
BuildRequires: libxml2-devel
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rubocop)
BuildRequires: gem(yard)
BuildRequires: gem(rspec-core)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
%summary.

This is a mirror from gerrit.ovirt.org http://www.ovirt.org, for issues use http://bugzilla.redhat.com


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       devel
Summary:       Development files for %gemname gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      xmllint
Requires:      libcurl-devel
Requires:      libxml2-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


%prep
%setup
# NOTE: create version.rb
echo "module OvirtSDK4;VERSION = '$(xmllint pom.xml --xpath "/*[name()='project']/*[name()='version']/text()")';end" > sdk/lib/ovirtsdk4/version.rb

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir

%files         devel
%ruby_includedir/*


%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt2
- ! spec tags and syntax

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.3.0-alt1
- > Ruby Policy 2.0
- ^ 4.2.5 -> 4.3.0

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.5-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.2
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1.1
- Rebuild for aarch64.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.4-alt1
- Initial build for Sisyphus
