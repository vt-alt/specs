# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname kramdown

Name:          gem-%pkgname
Version:       2.1.0
Release:       alt1
Summary:       kramdown is a fast, pure Ruby Markdown superset converter
License:       MIT
Group:         Development/Ruby
Url:           http://kramdown.gettalong.org
%vcs           https://github.com/gettalong/kramdown.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
kramdown was originally licensed under the GPL until the 1.0.0 release. However,
due to the many requests it is now released under the MIT license and therefore
can easily be used in commercial projects, too.

kramdown is a fast, pure Ruby Markdown superset converter, using a strict syntax
definition and supporting several common extensions.

The syntax definition for the kramdown syntax can be found in doc/syntax.page
(or online at http://kramdown.gettalong.org/syntax.html) and a quick reference
is available in doc/quickref.page or online at
http://kramdown.gettalong.org/quickref.html.

The kramdown library is mainly written to support the kramdown-to-HTML
conversion chain. However, due to its flexibility (by creating an internal AST)
it supports other input and output formats as well. Here is a list of the
supported formats:

* input formats: kramdown (a Markdown superset), Markdown, GFM, HTML
* output formats: HTML, kramdown, LaTeX (and therefore PDF), PDF via Prawn

All the documentation on the available input and output formats is available in
the doc/ directory and online at http://kramdown.gettalong.org.

Starting from version 1.0.0 kramdown is using a versioning scheme with major,
minor and patch parts in the version number where the major number changes on
backwards-incompatible changes, the minor number on the introduction of new
features and the patch number on everything else.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


#%package       doc
#Summary:       Documentation files for %gemname gem
#Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
#Group:         Development/Documentation
#BuildArch:     noarch
#
#%description   doc
#Documentation files for %gemname gem.
#
#%description   doc -l ru_RU.UTF8
#Файлы сведений для самоцвета %gemname.
#
#
%prep
%setup

%build
%ruby_config

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

#%files         doc
#%ruby_gemdocdir


%changelog
* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
