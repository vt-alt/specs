%define _libexecdir %_prefix/libexec

Name:           clufter
Version:        0.77.2
Release:        alt2
Group:          System/Base
Summary:        Tool/library for transforming/analyzing cluster configuration formats
License:        GPLv2+
URL:            https://pagure.io/%name

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel python3-module-setuptools
BuildRequires:  python3-module-lxml python3-module-distro

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pacemaker-schemas)
BuildRequires:  pacemaker-schemas
BuildRequires:  jing
BuildRequires:  libxslt libxml2 xsltproc

# https://releases.pagure.org/clufter/
Source0:         %name-%version.tar
Source1:         %name-tests-%version.tar
Source11:        fix-jing-simplified-rng.xsl
Source12:        pacemaker-borrow-schemas

Patch0:         compat-Python-3.9-no-longer-offers-collections.Mutable-ABCs.patch
Patch1:         compat-Python-3.9-no-longer-raises-ValueError-at-some-bound.patch
Patch2:         plugin_registry-fix-a-problem-with-native-plugins-missing.patch

%description
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.

%package cli
Group:          System/Base
Summary:        Tool for transforming/analyzing cluster configuration formats
Provides:       %name = %version-%release

BuildRequires:  bash-completion

BuildRequires:  help2man

Requires:       python3-module-setuptools python3-module-distro
Requires:       python3-module-%name = %version-%release
Requires:       %_bindir/nano
BuildArch:      noarch

%description cli
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.

This package contains %name command-line interface for the underlying
library (packaged as python3-module-%name).

%package -n python3-module-%name
Group:          System/Libraries
Summary:        Library for transforming/analyzing cluster configuration formats
License:        GPLv2+/GFDL
Provides:       %name-lib = %version-%release

Requires:       %name-bin = %version-%release
Requires:       python3-module-lxml
BuildArch:      noarch

%description -n python3-module-%name
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.

This package contains %name library including built-in plugins.


%package bin
Group:          System/Libraries
Summary:        Common internal compiled files for %name
License:        GPLv2+

Requires:       %name-common = %version-%release

%description bin
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.

This package contains internal, arch-specific files for %name.

%package common
Group:          System/Libraries
Summary:        Common internal data files for %name
License:        GPLv2+
BuildArch:      noarch

%description common
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.

This package contains internal, arch-agnostic files for %name.

%package lib-general
Group:          System/Libraries
Summary:        Extra %name plugins usable for/as generic/auxiliary products
Requires:       %name-lib = %version-%release
BuildArch:      noarch

%description lib-general
This package contains set of additional plugins targeting variety of generic
formats often serving as a byproducts in the intermediate steps of the overall
process arrangement: either experimental commands or internally unused,
reusable formats and filters.

%package lib-ccs
Group:          System/Libraries
Summary:        Extra plugins for transforming/analyzing CMAN configuration
Requires:       %name-lib-general = %version-%release
BuildArch:      noarch

%description lib-ccs
This package contains set of additional plugins targeting CMAN cluster
configuration: either experimental commands or internally unused, reusable
formats and filters.

%package lib-pcs
Group:          System/Libraries
Summary:        Extra plugins for transforming/analyzing Pacemaker configuration
Requires:       %name-lib-general = %version-%release
BuildArch:      noarch

%description lib-pcs
This package contains set of additional plugins targeting Pacemaker cluster
configuration: either experimental commands or internally unused, reusable
formats and filters.

%prep
%setup -b1 -q

pushd clufter
%patch0 -p1
%patch1 -p1
%patch2 -p1
popd

%__cp -a ../"%name-tests-%version"/* .

%__python3 setup.py saveopts -f setup.cfg pkg_prepare \
                      --ccs-flatten='%_libexecdir/%name-%version/ccs_flatten' \
                      --editor='%_bindir/nano' \
                      --extplugins-shared='%_datadir/%name/ext-plugins' \
                      --ra-metadata-dir='%_datadir/cluster' \
                      --ra-metadata-ext='metadata' \
                      --shell-posix='%(which sh 2>/dev/null || echo /bin/SHELL-POSIX)' \
                      --shell-bashlike='%(which bash 2>/dev/null || echo /bin/SHELL-BASHLIKE)'
%__python3 setup.py saveopts -f setup.cfg pkg_prepare \
  --report-bugs='https://bugzilla.altlinux.org/enter_bug.cgi?product=Branch p9&component=%name'

%build
%python3_build


%__python3 -I ./run-dev --skip-ext --completion-bash 2>/dev/null \
  | sed 's|run[-_]dev|%name|g' > .bashcomp
%__mkdir_p -- .manpages/man1
{ echo; %__python3 -I ./run-dev -l | sed -n 's|^  \(\S\+\).*|\1|p' \
  | sort; } > .subcmds
sed -e 's:\(.\+\):\\\&\\fIrun_dev-\1\\fR\\\|(1), :' \
  -e '1s|\(.*\)|\[SEE ALSO\]\n|' \
  -e '$s|\(.*\)|\1\nand perhaps more|' \
  .subcmds > .see-also
help2man -N -h -H -i .see-also \
  -n "$(sed -n '2s|[^(]\+(\([^)]\+\))|\1|p' README)" \
  '%__python3 -I ./run-dev' | sed 's|run\\\?[-_]dev|%name|g' \
  > ".manpages/man1/%name.1"
while read cmd; do
  [ -n "${cmd}" ] || continue
  echo -e "#\!/bin/sh\n{ [ \$# -ge 1 ] && [ \"\$1\" = \"--version\" ] \
  && %__python3 -I ./run-dev \"\$@\" \
  || %__python3 -I ./run-dev \"${cmd}\" \"\$@\"; }" > ".tmp-${cmd}"
  chmod +x ".tmp-${cmd}"
  grep -v "^${cmd}\$" .subcmds \
    | grep -e '^$' -e "$(echo ${cmd} | cut -d- -f1)\(-\|\$\)" \
    | sed -e 's:\(.\+\):\\\&\\fIrun_dev-\1\\fR\\\|(1), :' \
      -e '1s|\(.*\)|\[SEE ALSO\]\n\\\&\\fIrun_dev\\fR\\\|(1), \n|' \
      -e '$s|\(.*\)|\1\nand perhaps more|' > .see-also
  case "${cmd}" in
  ccs[2-]*)
    sed -i \
      '1s:\(.*\):\1\n\\\&\\fIcluster.conf\\fR\\\|(5), \\\&\\fIccs\\fR\\\|(7), :' \
    .see-also
    ;;&
  ccs2pcs*)
    sed -i \
      '1s:\(.*\):\1\n\\\&\\fI%_defaultdocdir/%name-%version/rgmanager-pacemaker\\fR\\\|, :' \
    .see-also
    ;;&
  *[2-]pcscmd*)
    sed -i '1s:\(.*\):\1\n\\\&\\fIpcs\\fR\\\|(8), :' .see-also
    ;;&
  esac
  help2man -N -h -H -i .see-also -n "${cmd}" "./.tmp-${cmd}" \
    | sed 's|run\\\?[-_]dev|%name|g' \
  > ".manpages/man1/%name-${cmd}.1"
done < .subcmds

OUTPUTDIR=.schemas POSTPROCESS="%SOURCE11" sh "%SOURCE12" --clobber

%install
%python3_install

%__chmod -- g-w '%buildroot%_libexecdir/%name-%version/ccs_flatten'
test -f '%buildroot%_bindir/%name' \
  || %__install -D -pm 644 -- '%buildroot%_bindir/%name' \
                                '%buildroot%_bindir/%name'

%__mkdir_p -- '%buildroot%_datadir/%name/formats'
for format in cib corosync; do
  %__cp -a -t '%buildroot%_datadir/%name/formats' \
          -- "%buildroot%python3_sitelibdir_noarch/%name/formats/${format}"
  %__rm -f -- "%buildroot%python3_sitelibdir_noarch/%name/formats/${format}"/*
  ln -s -t "%buildroot%python3_sitelibdir_noarch/%name/formats/${format}" \
     -- $(pushd "%buildroot%_datadir/%name/formats/${format}" >/dev/null; \
          ls -1A | sed "s:.*:%_datadir/%name/formats/${format}/\\0:")
done

%__mkdir_p -- '%buildroot%_datadir/%name/ext-plugins'
%__cp -af -t '%buildroot%_datadir/%name/ext-plugins' \
        -- '%buildroot%python3_sitelibdir_noarch/%name'/ext-plugins/*
%__rm -rf -- '%buildroot%python3_sitelibdir_noarch/%name'/ext-plugins/*/

find %buildroot%python3_sitelibdir_noarch/%name -type f -a -name "*.py" -print0 | xargs -0 %__python3 -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("$RPM_BUILD_ROOT")[2], optimize=opt) for opt in range(2) for f in sys.argv[1:]]' || :
find %buildroot%_datadir/%name/ext-plugins -type f -a -name "*.py" -print0 | xargs -0 %__python3 -O -c 'import py_compile, sys; [py_compile.compile(f, dfile=f.partition("$RPM_BUILD_ROOT")[2], optimize=opt) for opt in range(2) for f in sys.argv[1:]]' || :

declare bashcompdir="$(pkg-config --variable=completionsdir bash-completion \
                       || echo '%_datadir/bash-completion/completions')"
declare bashcomp="${bashcompdir}/%name"
%__install -D -pm 644 -- \
  .bashcomp '%buildroot%_sysconfdir/%name/bash-completion'
%__mkdir_p -- "%buildroot${bashcompdir}"
ln -s '%_sysconfdir/%name/bash-completion' "%buildroot${bashcomp}"

while true; do
  test "$(dirname "${bashcompdir}")" != "/" \
  && test "$(dirname "${bashcompdir}")" != "%_prefix" \
  && test "$(dirname "${bashcompdir}")" != "%_datadir" \
  && test "$(dirname "${bashcompdir}")" != "%_sysconfdir" \
  || break
  bashcompdir="$(dirname "${bashcompdir}")"
done
cat >.bashcomp-files <<-EOF
    ${bashcompdir}
    %%dir %_sysconfdir/%name
    %%verify(not size md5 mtime) %_sysconfdir/%name/bash-completion
EOF
%__mkdir_p -- '%buildroot%_mandir'
%__cp -a -t '%buildroot%_mandir' -- .manpages/*
%__cp -a -f -t '%buildroot%_datadir/%name/formats/cib' \
              -- .schemas/pacemaker-*.*.rng
%__mkdir_p -- '%buildroot%_defaultdocdir/%name-%version'
%__cp -a -t '%buildroot%_defaultdocdir/%name-%version' \
           -- gpl-2.0.txt doc/*.txt doc/rgmanager-pacemaker


%check
declare ret=0 \
        ccs_flatten_dir="$(dirname '%buildroot%_libexecdir/%name-%version/ccs_flatten')"
ln -s '%buildroot%_datadir/cluster'/*.'metadata' \
      "${ccs_flatten_dir}"
export LC_ALL=C.UTF-8 LANG=C.UTF-8
PATH="${PATH:+${PATH}:}${ccs_flatten_dir}" PYTHONEXEC="%__python3 -I" ./run-tests
ret=$?
%__rm -f -- "${ccs_flatten_dir}"/*.'metadata'
[ ${ret} -eq 0 ] || exit ${ret}


%post cli
if [ $1 -gt 1 ]; then
declare bashcomp="%_sysconfdir/%name/bash-completion"
%_bindir/%name --completion-bash > "${bashcomp}" 2>/dev/null || :
fi

%post lib-general
declare bashcomp="%_sysconfdir/%name/bash-completion"
test -x '%_bindir/%name' && test -f "${bashcomp}" \
  && %_bindir/%name --completion-bash > "${bashcomp}" 2>/dev/null || :

%post lib-ccs
declare bashcomp="%_sysconfdir/%name/bash-completion"
test -x '%_bindir/%name' && test -f "${bashcomp}" \
  && %_bindir/%name --completion-bash > "${bashcomp}" 2>/dev/null || :

%post lib-pcs
declare bashcomp="%_sysconfdir/%name/bash-completion"
test -x '%_bindir/%name' && test -f "${bashcomp}" \
  && %_bindir/%name --completion-bash > "${bashcomp}" 2>/dev/null || :

%files cli -f .bashcomp-files
%_mandir/man1/*.1*
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%name-*.egg-info

%files bin
%_libexecdir/%name-%version

%files common
%_datadir/cluster
%_datadir/%name
%dir %_defaultdocdir/%name-%version
%_defaultdocdir/%name-%version/*[^[:digit:]]
%_defaultdocdir/%name-%version/*[[:digit:]].txt

%files lib-general
%_datadir/%name/ext-plugins/lib-general

%files lib-ccs
%_datadir/%name/ext-plugins/lib-ccs

%files lib-pcs
%_datadir/%name/ext-plugins/lib-pcs

%changelog
* Mon Aug 03 2020 Ivan Razzhivin <underwit@altlinux.org> 0.77.2-alt2
- fix dependency (Closes: 38759)

* Thu Jul 09 2020 Ivan Razzhivin <underwit@altlinux.org> 0.77.2-alt1
- initial build

