# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname rouge

Name:          gem-%pkgname
Version:       3.7.0
Release:       alt1
Summary:       A pure-ruby code highlighter that is compatible with pygments
License:       MIT/Pygment
Group:         Development/Ruby
Url:           http://rouge.jneen.net/
%vcs           https://github.com/jneen/rouge.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Rouge is a pure-ruby syntax highlighter. It can highlight 100 different
languages, and output HTML or ANSI 256-color text. Its HTML output is compatible
with stylesheets designed for pygments.

If you'd like to help out with this project, assign yourself something from
the issues page, and send me a pull request (even if it's not done yet!). Bonus
points for feature branches.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n rougify
Summary:       Executable for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n rougify
Executable for %gemname gem.

%description   -n rougify -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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

%files         -n rougify
%_bindir/rougify


%changelog
* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 3.7.0-alt1
^ Ruby Policy 2.0
^ v3.7.0

* Mon Apr 29 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
