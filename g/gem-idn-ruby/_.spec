%define        pkgname idn-ruby

Name:          gem-%pkgname
Version:       0.1.0
Release:       alt2.1
Summary:       LibIDN Ruby Bindings
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/deepfryed/idn-ruby
Vcs:           https://github.com/deepfryed/idn-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libidn-devel

%description
Ruby Bindings for the GNU LibIDN library, an implementation of the Stringprep,
Punycode and IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group. Included are the most important parts of
the Stringprep, Punycode and IDNA APIs like performing Stringprep processings,
encoding to and decoding from Punycode strings and converting entire domain
names to and from the ACE encoded form.


%package       devel
Summary:       Development files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Requires:      libidn-devel

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
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
%ruby_gemextdir

%files         devel
%ruby_includedir/idn*

%changelog
* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2.1
- ! spec tags

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt2
- ! spec according to changelog rules

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.0-alt1
- + packaged gem with usage Ruby Policy 2.0
