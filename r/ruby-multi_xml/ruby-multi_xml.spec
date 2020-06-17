%define        pkgname multi_xml

Name:          ruby-%pkgname
Version:       0.6.0
Release:       alt2
Summary:       A generic swappable back-end for XML parsing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sferik/multi_xml
%vcs           https://github.com/sferik/multi_xml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
RMagick is an interface between the Ruby programming language and the
ImageMagick image processing library.


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
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2
^ Ruby Policy 2.0

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus
