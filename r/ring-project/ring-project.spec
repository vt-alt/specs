%define IF_ver_gt() %if "%(rpmvercmp '%1' '%2')" > "0"
%define IF_ver_gteq() %if "%(rpmvercmp '%1' '%2')" >= "0"
%define IF_ver_lt() %if "%(rpmvercmp '%2' '%1')" > "0"
%define IF_ver_lteq() %if "%(rpmvercmp '%2' '%1')" >= "0"
%define IF_ver_eq() %if "%(rpmvercmp '%1' '%2')" == "0"
%define IF_ver_not_gt() %if "%(rpmvercmp '%1' '%2')" <= "0"
%define IF_ver_not_gteq() %if "%(rpmvercmp '%1' '%2')" < "0"
%define IF_ver_not_lt() %if "%(rpmvercmp '%2' '%1')" <= "0"
%define IF_ver_not_lteq() %if "%(rpmvercmp '%2' '%1')" < "0"
%define IF_ver_not_eq() %if "%(rpmvercmp '%1' '%2')" != "0"

%{expand: %(sed 's,^%%,%%global ,' /usr/lib/rpm/macros.d/ubt)}
%define ubt_id %__ubt_branch_id

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif
%ifarch %arm
%set_verify_elf_method textrel=relaxed
%endif

%define rname ring-project
%define _libexecdir %prefix/libexec
%define builddir %_builddir/%name-%version
%define ring_sover 0
%define libring libring%ring_sover
%define ringclient_sover 1.0.0
%define libringclient libringclient%ringclient_sover

Name: ring-project
Version: 20190814
Release: alt1

Group: Networking/Instant messaging
Summary: SIP and IAX2 compatible softphone
Url: http://ring.cx/
License: GPLv3

Requires(post,preun): alternatives >= 0.2
#Conflicts: sflphone sflphone-common
#Requires: %name-common >= %EVR

Source: %name-%version.tar
Patch1: alt-fix-linking.patch
Patch2: alt-pcre-include.patch
Patch3: alt-armh.patch

BuildRequires(pre): rpm-build-ubt
%IF_ver_gteq %ubt_id M90
BuildRequires: asio-devel
%endif
BuildRequires: cmake gcc-c++ glibc-devel autoconf-archive
BuildRequires: doxygen graphviz gtk-doc
BuildRequires: qt5-tools-devel
BuildRequires: chrpath
BuildRequires: libalsa-devel libdbus-c++-devel libgnutls-devel libgsm-devel
BuildRequires: libavutil-devel libavcodec-devel libavformat-devel libavdevice-devel libavfilter-devel libswscale-devel libswresample-devel
BuildRequires: libssl-devel libgpg-error-devel libgcrypt-devel
#BuildRequires: libssl-devel-static
BuildRequires: libnettle-devel libpcre-devel libpulseaudio-devel libsamplerate-devel libsndfile-devel libvpx-devel
BuildRequires: libspeexdsp-devel libswscale-devel libudev-devel libupnp-devel libuuid-devel jsoncpp-devel
BuildRequires: zlib-devel libopus-devel libspeex-devel ilbc-devel libmsgpack-devel libx264-devel libx265-devel libva-devel libvdpau-devel
BuildRequires: libyaml-cpp-devel yasm perl-Pod-Usage cppunit-devel libgmp-devel libexpat-devel
BuildRequires: evolution-data-server-devel libclutter-gtk3-devel libnotify-devel libpixman-devel
BuildRequires: libXdmcp-devel libpng-devel libXxf86vm-devel libappindicator-gtk3-devel libwebkit2gtk-devel libqrencode-devel
BuildRequires: libcanberra-gtk3-devel

%description
Ring is a Voice-over-IP software phone. We want it to be:
- user friendly (fast, sleek, easy to learn interface)
- professional grade (transfers, holds, optimal audio quality)
- fully compatible with Asterisk (SIP and IAX protocols)
- de-centralized call (P2P-DHT)
- customizable

As the SIP/audio daemon and the user interface are separate processes,
it is easy to provide different user interfaces. Ring comes with
various graphical user interfaces and even scripts to control the daemon from
the shell.

%package -n ring-daemon
Group: System/Servers
Summary: SIP and IAX2 compatible softphone daemon
%description -n ring-daemon
As the SIP/audio daemon and the user interface are separate processes,
it is easy to provide different user interfaces. Ring comes with
various graphical user interfaces and even scripts to control the daemon from
the shell.

%package -n ring-client-gnome
Summary: Ring client written in GTK+
Group: Networking/Instant messaging
Requires: ring-daemon
Provides: jami-client-gnome = %version-%release
%description -n ring-client-gnome
Ring-client-gnome is a Ring client written in GTK+. It uses libRingClient to
communicate with the Ring daemon and for all of the underlying models and their
logic. Ideally ring-client-gnome should only contain UI related code and any
wrappers necessary for interacting with libRingClient.

%package common
BuildArch: noarch
Summary: Common %name files
Group: System/Configuration/Other
Conflicts: ring-daemon < 3
Provides: ring-daemon-common = 4.1
Obsoletes: ring-daemon-common < 4.1
Provides: libringclient-common = 1.1
Obsoletes: libringclient-common < 1.1
%description common
Common %name files

%package -n %libring
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %EVR
%description -n %libring
%name library.

%package -n %libringclient
Group: System/Libraries
Summary: Ring client library
Requires: %name-common >= %EVR
%description -n %libringclient
Client library for GNU Ring.

%package devel
Group: Development/Other
Summary: Development files for %name
Provides: ring-daemon-devel = %version-%release
Provides: libringclient-devel = %version-%release
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Group: Development/Other
Summary: Development files for %name
Requires: %name-devel
Provides: ring-daemon-devel-static = %version-%release
%description devel-static
The %name-devel package contains static libraries for
developing applications that use %name.

%prep
%setup -qn %name-%version
%patch1 -p1
#%patch2 -p1
%patch3 -p1

# don't build internal vpx
rm -rf daemon/contrib/src/vpx
rm -rf daemon/contrib/tarballs/libvpx*.tar.gz
sed -i '/DEPS_ffmpeg/s/vpx//' daemon/contrib/src/ffmpeg/rules.mak

%build
%add_optflags %optflags_shared -Wno-error=return-type
export CXXFLAGS="%optflags"
mkdir -p daemon/contrib/native
pushd daemon/contrib/native
../bootstrap \
    --no-checksums \
    --disable-downloads \
    --disable-ogg \
    --disable-flac \
    --disable-vorbis \
    --disable-vorbisenc \
    --disable-speex \
    --disable-sndfile \
    --disable-speexdsp \
    --disable-gsm \
    --disable-natpmp \
    #
make list
make
popd
pushd daemon
./autogen.sh
%configure \
    --with-libilbc \
    --with-opus \
    --enable-video \
    --enable-ipv6 \
    --without-jack \
    CFLAGS="%optflags" \
    LDFLAGS="-Wl,-z,defs" \
    #
%make_build
popd

pushd lrc
%cmake \
    -DRING_BUILD_DIR=%builddir/daemon/src \
    -DENABLE_VIDEO=ON \
    -DCMAKE_BUILD_TYPE=Release \
    #
[ -e build ] || ln -s BUILD build
pushd BUILD
%make_build
popd
popd

pushd client-gnome
%cmake \
    -DLibRingClient_PROJECT_DIR=%builddir/lrc \
    -DGSETTINGS_LOCALCOMPILE=OFF \
    #
pushd BUILD
%make_build
popd
popd

%install
%makeinstall -C daemon
make install -C lrc/BUILD DESTDIR=%buildroot
make install -C client-gnome/BUILD DESTDIR=%buildroot

chrpath --delete %buildroot/%_libdir/ring/dring

# install alternatives
mkdir -p %buildroot/%_bindir/
rm -rf %buildroot/%_bindir/jami
ln -s /bin/true %buildroot/%_bindir/jami
ln -s jami %buildroot/%_bindir/ring
ln -s jami %buildroot/%_bindir/ring.cx
#
echo >%buildroot/%_bindir/jami-client-dummy <<__EOF__
#!/bin/sh
echo "Jami not found" >&2
exit 1
__EOF__
chmod 0755 %buildroot/%_bindir/jami-client-dummy
#
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/jami       %_bindir/jami-client-dummy      1
__EOF__
cat > %buildroot/%_sysconfdir/alternatives/packages.d/jami-client-gnome <<__EOF__
%_bindir/jami       %_bindir/jami-gnome      10
__EOF__

%if "%_lib" == "lib64"
sed -i 's|/usr/lib|/usr/lib64|' %buildroot/usr/lib/cmake/LibRingClient/LibRingClientConfig.cmake
mkdir -p %buildroot/%_libdir
mv %buildroot/usr/lib/* %buildroot/%_libdir/
%endif

%find_lang lrc --with-qt
%find_lang jami-client-gnome

%files common
%_iconsdir/hicolor/*/apps/jami.*

%files -n ring-daemon
%doc daemon/AUTHORS daemon/COPYING daemon/README
%config %_sysconfdir/alternatives/packages.d/%name
%ghost %_bindir/jami
%_bindir/ring
%_bindir/ring.cx
%_bindir/jami-client-dummy
%_libdir/ring/
%_datadir/dbus-1/services/cx.ring.*
%_datadir/ring/

%files -n ring-client-gnome -f jami-client-gnome.lang
%config %_sysconfdir/alternatives/packages.d/jami-client-gnome
%_bindir/jami-gnome
%_datadir/jami-gnome
%_desktopdir/jami-gnome.desktop
%_datadir/sounds/jami-gnome/
%_datadir/glib-2.0/schemas/net.jami.*.gschema.xml
%_datadir/metainfo/jami-gnome.appdata.xml

%files -n %libring
%doc daemon/AUTHORS daemon/COPYING daemon/README
%_libdir/libring.so.%ring_sover
%_libdir/libring.so.*

%files -n %libringclient -f lrc.lang
%doc lrc/COPYING
%_libdir/libringclient.so.%ringclient_sover
%_libdir/libringclient.so.*

%files devel
%_libdir/lib*.so
%_includedir/dring/
%_includedir/libringclient/
%_datadir/dbus-1/interfaces/cx.ring.Ring.*.xml
%_libdir/cmake/LibRingClient/
%_man1dir/dring.*

%files devel-static
#%_libdir/libring.a

%changelog
* Fri Aug 16 2019 Sergey V Turchin <zerg@altlinux.org> 20190814-alt1
- new version

* Mon Jun 24 2019 Sergey V Turchin <zerg@altlinux.org> 20190622-alt1
- new version

* Mon Feb 18 2019 Sergey V Turchin <zerg@altlinux.org> 20190215-alt1
- new version

* Fri Feb 15 2019 Sergey V Turchin <zerg@altlinux.org> 20190214-alt1
- new version

* Tue Feb 12 2019 Sergey V Turchin <zerg@altlinux.org> 20190129-alt1
- new version

* Tue Feb 12 2019 Sergey V Turchin <zerg@altlinux.org> 20180826-alt4
- disable return-type error

* Mon Nov 26 2018 Sergey V Turchin <zerg@altlinux.org> 20180826-alt3
- fix to build on armh (thanks sbolshakov@alt)

* Fri Nov 23 2018 Sergey V Turchin <zerg@altlinux.org> 20180826-alt2
- fix requires (ALT#33594)

* Thu Aug 30 2018 Sergey V Turchin <zerg@altlinux.org> 20180826-alt1
- new version

* Thu Jul 19 2018 Sergey V Turchin <zerg@altlinux.org> 20180712-alt1.1
- fix build requires

* Tue Jul 17 2018 Sergey V Turchin <zerg@altlinux.org> 20180712-alt1
- using all-in-one tarball

* Mon Jul 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt3
- fix build on arm

* Thu Jul 05 2018 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt2
- fix to build with new ffmpeg

* Tue Jul 25 2017 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt1
- new version
- add dummy client alternative

* Wed Feb 22 2017 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt0.1
- new beta

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.3
- fix build requires

* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.2
- update from master branch

* Tue Mar 15 2016 Sergey V Turchin <zerg@altlinux.org> 2.3.0-alt0.1
- initial build
