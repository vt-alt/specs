%define  modulename sipsimple
%def_enable bundled_pjsip

Name:    python-module-%modulename
Version: 3.5.0
Release: alt1

Summary: SIP SIMPLE implementation for Python
License: GPLv3
Group:   Development/Python

Url:     https://github.com/AGProjects/python-sipsimple
Source: python-%modulename-%version.tar
Patch: python-module-sipsimple-alt-add-arch-webrtc-defines.patch
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-setuptools_cython
%if_enabled bundled_pjsip
BuildRequires: libavformat-devel
BuildRequires: libswscale-devel
BuildRequires: libvpx-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libv4l-devel
BuildRequires: libalsa-devel
%else
BuildRequires: libpjsip-devel
%endif

%description
SIP SIMPLE client SDK is a Software Development Kit for easy development
of SIP end-points that support rich media like Audio, Video, Instant
Messaging, File Transfers, Desktop Sharing and Presence.  Other media
types can be easily added by using an extensible high-level API.

%prep
%setup -n python-%modulename-%version
%patch -p1
cp -at deps/pjsip/ -- /usr/share/gnu-config/config.*
chmod +x deps/pjsip/*configure
%ifarch %e2k
# more 64-bit little endian arches
sed -i 's,^#elif defined(__aarch64__),& || defined(__e2k__),' \
	deps/pjsip/third_party/webrtc/src/typedefs.h
%endif

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Wed Jun 10 2020 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Sun Sep 01 2019 Michael Shigorin <mike@altlinux.org> 3.4.2-alt2
- Fixed build on %%e2k.

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 3.4.2-alt1
- New version.

* Sat Mar 09 2019 Andrey Cherepanov <cas@altlinux.org> 3.4.1-alt1
- New version.

* Mon Feb 18 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.3.0-alt2
- Fixed build on ppc64le.

* Mon Dec 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Wed Jun 13 2018 Anton Farygin <rider@altlinux.ru> 3.1.1-alt2
- rebuilt for ffmpeg-4.0
- fixed built on aarch64

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
