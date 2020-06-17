%define        pkgname license-scout
%define        gemname license_scout

Name: 	       ruby-%pkgname
Version:       1.0.24
Release:       alt1
Summary:       Discovers license information of the dependencies of a project.
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/license_scout
%vcs           https://github.com/chef/license_scout.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
License Scout is a utility that discovers and aggregates the licenses for your
software project's transitive dependencies.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=artifactory,mixlib-install,mixlib-shellout,mixlib-versioning,net-scp,net-ssh,safe_yaml,test-kitchen,thor,bundler_top_level_project,chef-ingredient,data,remote_install,seven_zip,windows-sdk

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir
%_bindir/*

%files         doc
%ruby_gemdocdir


%changelog
* Fri Jul 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.24-alt1
- Bump to 1.0.24
- Use Ruby Policy 2.0

* Fri Sep 28 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.16-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.15-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.10-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.10-alt1
- Initial build for Sisyphus
