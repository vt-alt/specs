%define _unpackaged_files_terminate_build 1

Name: fsharp
Version: 10.2.1
Release: alt3

Summary:        F# compiler, core library and core tools
License:        MIT
Group:          Development/Other
Url:            http://fsharp.org

ExclusiveArch: x86_64 %ix86 aarch64

# https://github.com/fsharp/fsharp.git
Source: %name-%version.tar

Source1: packages.tar

Patch1: %name-debian-bootstrap.patch

BuildRequires: rpm-build-mono >= 2.0.0
BuildRequires: mono-devel-full
BuildRequires: msbuild
BuildRequires: /proc
BuildRequires: /usr/bin/7z

# Interfaces of slightly older versions are required, upstream corrects it by modifying 'Requires'
%define __find_provides sh -c '/usr/lib/rpm/find-provides | sort | uniq'
%define __find_requires sh -c '/usr/lib/rpm/find-requires | sort | uniq | grep ^... | sed \\\
	-e "s/mono\(System\.Collections\.Immutable\).*/mono\(System.Collections.Immutable\) = 1.2.1.0/" \\\
	-e "s/mono\(System\.ValueTuple\).*/mono\(System.ValueTuple\) = 4.0.3.0/" \\\
	-e "/mono\(System\.Core\) = 2\.0/d" \\\
	-e "/mono\(System\.Net\) = 2\.0/d" \\\
	-e "/mono\(System\.Numerics\) = 2\.0/d"'

%description
F# is a mature, open source, functional-first programming language
which empowers users and organizations to tackle complex computing
problems with simple, maintainable and robust code. It is used in
a wide range of application areas and is available across multiple
platforms.

%prep
%setup -a1
%patch1 -p1

pushd packages
for i in *.nupkg ; do
    name=$(basename ${i%%.nupkg})
    mkdir $name
    pushd $name
    7z x ../$i ||:
    cp ../$i ./
    popd
done

# unzip unpacks filenames with %% sign as is. Convert it. TODO: make a more generic solution when necessary
find . -iname '*%%2B*' | while read file ; do
    mv $file $(echo $file | sed -e 's:%%2B:+:g') ||:
done
popd

%build
%make

%install
%makeinstall_std

%files
%doc LICENSE License.txt README.md
%_bindir/fsharp*
%_monodir/fsharp*
%_monodir/Microsoft*
%_monodir/xbuild/Microsoft/VisualStudio/

%changelog
* Wed Nov 18 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 10.2.1-alt3
- Updated runtime dependencies.

* Fri Aug 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 10.2.1-alt2
- Fixed build.

* Thu Oct 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 10.2.1-alt1
- Updated to upstream version 10.2.1.

* Thu Jul 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.1.34-alt1
- Updated to upstream version 4.1.34.

* Fri Sep 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.4-alt2
- Rebuilt with support of %%ubt macro.

* Mon Jul 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0.4-alt1
- Initial build for ALT
