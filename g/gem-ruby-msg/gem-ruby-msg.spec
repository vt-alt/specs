%define        pkgname ruby-msg

Name:          gem-%pkgname
Version:       1.5.2
Release:       alt2
Summary:       A library for reading and converting Outlook msg and pst files (mapi message stores)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/aquasync/ruby-msg
%vcs           https://github.com/aquasync/ruby-msg.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary


%package       -n mapitool
Summary:       Executable file mapitool for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n mapitool
The command line utility, which is allowing to convert individual msg or pst
files to .eml, or to convert a batch to an mbox format file. See mapitool help
for details.


%description   -n mapitool -l ru_RU.UTF8
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

%files         -n mapitool
%_bindir/mapitool

%files         doc
%ruby_gemdocdir


%changelog
* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt2
- Use Ruby Policy 2.0

* Wed Dec 19 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- Initial build for Sisyphus bumped to 1.5.2
