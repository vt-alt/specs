%define        pkgname hiera-eyaml

Name: 	       gem-%pkgname
Version:       3.2.0
Release:       alt1
Summary:       A backend for Hiera that provides per-value asymmetric encryption of sensitive data
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/hiera-eyaml
Vcs:           https://github.com/voxpupuli/hiera-eyaml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version highline ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
hiera-eyaml is a backend for Hiera that provides per-value encryption of
sensitive data within yaml files to be used by Puppet.


%package       -n eyaml
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n eyaml
Executable file for %gemname gem.

%description   -n eyaml -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n eyaml
%_bindir/eyaml

%files         doc
%ruby_gemdocdir


%changelog
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.2.0-alt1
- updated (^) 3.0.0 -> 3.2.0
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 06 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.1.0 -> 3.0.0
- fixed (!) spec

* Wed Apr 10 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.0-alt2
- Use new ruby packaging policy
- Make appropriate require to highline

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build in Sisyphus
