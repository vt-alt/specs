%define        pkgname packaging

Name:          gem-%pkgname
Version:       0.99.59
Release:       alt1
Summary:       Packaging automation for Puppet software
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/packaging
Vcs:           https://github.com/puppetlabs/packaging.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname
%gem_replace_version artifactory ~> 3.0

%description
This is a repository for packaging automation for Puppet software. The goal is
to abstract and automate packaging processes beyond individual software
projects to a level where this repo can be cloned inside any project.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%ruby_build --ignore=acceptance --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 0.99.59-alt1
- ^ 0.99.36 -> 0.99.59

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.99.36-alt1
- fixed ! spec
- ^ 0.99.35 -> 0.99.36

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 0.99.35-alt1
- used > Ruby Policy 2.0
- updated ^ 0.99.22 -> 0.99.35

* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.99.22-alt1
- Version updated to 0.99.22

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.99.20-alt1
- Initial build for Sisyphus
