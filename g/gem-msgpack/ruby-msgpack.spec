%define        pkgname msgpack

Name: 	       gem-%pkgname
Version:       1.3.3
Release:       alt1
Summary:       MessagePack implementation for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/msgpack/msgpack-ruby
Vcs:           https://github.com/msgpack/msgpack-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller. For
example, small integers (like flags or error code) are encoded into a single
byte, and typical short strings only require an extra byte in addition to the
strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (binary data, size, speed ...), MessagePack
is a perfect replacement.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-%pkgname-devel
Summary:       Development headers files for %gemname gem
Summary(ru_RU.UTF-8): Файлы заголовков для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Conflicts:     libmsgpack-devel

%description   -n gem-%pkgname-devel
Development headers for %gemname gem.

%description   -n gem-%pkgname-devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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

%files         -n gem-%pkgname-doc
%ruby_gemdocdir

%files         -n gem-%pkgname-devel
%ruby_includedir/*


%changelog
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- updated (^) 1.3.1 -> 1.3.3
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- updated (^) 1.2.9 -> 1.3.1
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.9-alt1
- used (>) Ruby Policy 2.0
- updated (^) 1.1.0 -> 1.2.9

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1.5
- Add rubygem files

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus
