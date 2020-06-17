%define        pkgname deacon

Name:          ruby-%pkgname
Version:       1.0.0
Release:       alt2
Summary:       Human readable name generator plugin
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/lzap/deacon
%vcs           https://github.com/lzap/deacon.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Out of ideas for incoming bare-metal host names in your cluster? This little gem
is a way out! It contains frequently occurring given names and surnames from the
1990 US Census (public domain data):

 * 256 (8 bits) unique male given names
 * 256 (8 bits) unique female given names
 * 65,536 (16 bits) unique surnames

Given names were filtered to be 3-5 characters long, surnames 5-8 characters,
therefore generated names are never longer than 14 characters (5+1+8).

This gives 33,554,432 (25 bits) total of male and female name combinations.
Built-in generator can either generate randomized succession, or generate
combinations based on MAC adresses.

%description   -l ru_RU.UTF8
Модель генератора человекочитаемых имён


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
* Sat Jul 20 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- Use Ruby Policy 2.0

* Fri Sep 21 2018 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- Initial gemified build for Sisyphus
