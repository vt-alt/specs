%define        pkgname rabl

Name:          gem-%pkgname
Version:       0.14.3.1
Release:       alt1
Summary:       General ruby templating with json, bson, xml, plist and msgpack support
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nesquena/rabl
Vcs:           https://github.com/nesquena/rabl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         0.14.3.patch
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
RABL (Ruby API Builder Language) is a Rails and Padrino ruby templating system
for generating JSON, XML, MessagePack, PList and BSON. When using the
ActiveRecord 'to_json' method, I find myself wanting a more expressive and
powerful solution for generating APIs. This is especially true when the JSON
representation is complex or doesn't match the exact schema defined within
the database.

In particular, I want to easily:

 * Create arbitrary nodes named based on combining data in an object
 * Pass arguments to methods and store the result as a child node
 * Render partial templates and inherit to reduce code duplication
 * Rename or alias attributes to change the name from the model
 * Append attributes from a child into a parent node
 * Include nodes only if a certain condition has been met

Anyone who has tried the 'to_json' method used in ActiveRecord for generating
a JSON response has felt the pain of this restrictive approach. RABL is
a general templating system created to solve these problems by approaching API
response generation in an entirely new way.

RABL at the core is all about adhering to MVC principles by deferring API data
representations to the view layer of your application. For a breakdown of common
misconceptions about RABL, please check out our guide to understanding RABL,
which can help clear up any confusion about this project.

%description -l ru_RU.UTF8
RABL есть шаблонная система для Рубина и Падрины для генерирования структур в
форматах JSON, XML, MessagePack, PList и BSON. При использовании метода
'to_json' в Рельсах, было обнаружено, что требуется более яркое и мощное
решение для созидания API. Это особенно верно в случае, когда
представленый JSON сложен или не точно отражает схеме определённой внутри базы
данных.


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
%patch

%build
%ruby_build --ignore=padrino_test,rails2,rails3,rails3_2,rails4,rails5,rails5_api,rails6,sinatra_test \
            --use=%gemname --version-replace=%version
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
* Tue Jun 09 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.3.1-alt1
- ^ 0.14.2 -> 0.14.3+
- ! fault to require to active_view explicitly in code by patch

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- updated (^) 0.13.1 -> 0.14.2
- used (>) Ruby Policy 2.0
- fixed (!) spec

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- Initial gemified build for Sisyphus
