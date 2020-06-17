%define        pkgname radius

Name:          gem-%pkgname
Version:       0.7.5
Release:       alt1
Summary:       Small, but powerful tag-based template language for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jlong/radius
%vcs           https://github.com/jlong/radius.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Radius is a powerful tag-based template language for Ruby inspired by
the template languages used in MovableType and TextPattern. It uses tags
similar to XML, but can be used to generate any form of plain text (HTML,
e-mail, etc).


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.7.5-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
