%define        pkgname hashdiff

Name:          gem-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       HashDiff is a ruby library to to compute the smallest difference between two hashes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/liufengyun/hashdiff
%vcs           https://github.com/liufengyun/hashdiff.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Hashdiff is a ruby library to compute the smallest difference between two
hashes.

It also supports comparing two arrays.

Hashdiff does not monkey-patch any existing class. All features are contained
inside the Hashdiff module.


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

%files         doc
%ruby_gemdocdir


%changelog
* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
