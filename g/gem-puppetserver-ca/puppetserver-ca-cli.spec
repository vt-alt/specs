%define        _unpackaged_files_terminate_build 1
%define        pkgname puppetserver-ca

Name:          gem-%pkgname
Version:       1.7.0
Release:       alt1
Summary:       A simple Ruby CLI tool to interact with the Puppet Server's included CA
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppetserver-ca-cli
Vcs:           https://github.com/puppetlabs/puppetserver-ca-cli.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname-cli < %EVR
Provides:      ruby-%pkgname-cli = %EVR

%description
This gem provides the functionality behind the Puppet Server CA interactions.
The actual CLI executable lives within the Puppet Server project.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Obsoletes:     ruby-%pkgname-cli-doc
Provides:      ruby-%pkgname-cli-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.


%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup
find -name "*.rb" | while read f; do sed "s,/etc/puppetlabs,/etc," -i "$f"; done

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

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Tue May 12 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- ^ 1.4.0 -> 1.7.0
- ! spec tags
- ! pupper server paths in sources

* Tue Aug 27 2019 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt2
- > Ruby Policy 2.0

* Mon Aug 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.4.0-alt1
- Version updated to 1.4.0

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt2
- ca and puppet paths fixed

* Tue May 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3.1-alt1
- Version updated to 1.3.1

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.1-alt1
- Version updated to 1.2.1

* Thu Dec 06 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus
