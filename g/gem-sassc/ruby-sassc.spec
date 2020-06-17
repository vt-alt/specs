%define        pkgname sassc

Name:          gem-%pkgname
Version:       2.2.1
Release:       alt2.1
Summary:       Use libsass with Ruby!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-ruby
Vcs:           https://github.com/sass/sassc-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         patch-2.2.1.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rake-compiler)
BuildRequires: gem(rake-compiler-dock)
BuildRequires: gem-minitest
BuildRequires: libsass-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR
Requires:      libsass

%description
This gem combines the speed of libsass, the Sass C implementation, with
the ease of use of the original Ruby Sass library.


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
%patch -p1
# TODO to upstream
sed "s,Dir.entries(libsass_dir).size <= 3,false,"  -i *.gemspec ext/extconf.rb
sed 's/File.expand_path("libsass.#{dl_ext}", __dir__)/"libsass.so"/'  -i lib/sassc/native.rb

%build
%ruby_build

%install
%ruby_install
mkdir -p %buildroot%ruby_gemextdir
# TODO with setup.rb
ln -s $(realpath $(find %_libdir/ -name libsass.so 2>/dev/null)) %buildroot%ruby_gemextdir/libsass.so

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Apr 01 2020 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2.1
- ! spec tags and syntax, build procedure

* Fri Nov 08 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt2
- changed (*) spec to use build requires
- fixed (!) lost link to system's .so lib (closes #37433)
- fixed (!) requires

* Thu Sep 26 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.1-alt1
- update (^) 2.0.0 -> 2.2.1
- update (^) Ruby Police 2.0

* Wed Sep 26 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.1-alt1
- New version.
- Disable tests.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.12.0-alt1
- New version.
- Package as gem.

* Mon Jun 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.11.4-alt1
- Initial build for Sisyphus
