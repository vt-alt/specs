#ifarch %ix86 x86_64
#def_enable botan
#else
%def_disable botan
#endif

Name: qca-qt5
%define major 2
%define minor 3
%define bugfix 1
Version: %major.%minor.%bugfix
Release: alt1

Group: Networking/Instant messaging
Summary: QCA - Qt Cryptographic Architecture
License: LGPL
Url: https://userbase.kde.org/QCA

Requires: lib%name = %version-%release

Source: %name-%version.tar
# ALT
Patch10: qca-2.0.3-alt-paths.patch

BuildRequires: cmake gcc-c++ glibc-devel ca-certificates
BuildRequires: qt5-base-devel
BuildRequires: zlib-devel bzlib-devel libgmp-devel
BuildRequires: libgcrypt-devel libnss-devel libsasl2-devel pkcs11-helper-devel
BuildRequires: kde-common-devel
%if_enabled botan
BuildRequires: libbotan-devel
%endif

%package -n lib%name
Summary: QCA - Qt Cryptographic Architecture library
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: System/Libraries
Requires: ca-certificates

%package -n lib%name-devel
Summary: Header files for developing apps which will use Qt Crytographic Architecture (QCA)
Summary(ru_RU.UTF-8): Файлы, необходимые для разработки приложений с использованием Qt Crytographic Architecture (QCA)
Group: Development/KDE and QT
Requires: qt5-base-devel
Requires: lib%name = %version-%release

%description
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.
%description -n lib%name
  This library provides an easy API for the following features: SSL/TLS,
X509, SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Functionality is supplied via plugins.  This is useful for avoiding
dependence on a particular crypto library and makes upgrading easier,
as there is no need to recompile your application when adding or
upgrading a crypto plugin.  Also, by pushing crypto functionality into
plugins, your application is free of legal issues, such as export
regulation.
%description -n lib%name -l ru_RU.UTF-8
  Эта библиотека предоставляет простой API для следующего: SSL/TLS, X509,
SASL, RSA, Hashing (SHA1, MD5), Ciphers (BlowFish, 3DES, AES)
  Функциональность дополняется с помощью плагинов. Это удобно, так как
избегается зависимость на конкретную криптографическую библиотеку и это
делает обновления проще, так как нет необходимости перекомпилировать
использующее QCA приложение при добавлении или обновлении
крипто-плагина. Также, так как функциональность криптографии вынесена на
уровень плагинов, приложение избавляется от возможных ограничений,
накладываемых законом, например, экспортных ограничений.
%description -n lib%name-devel
This package contains the header files needed to develop programs
that use QCA.
%description -n lib%name-devel -l ru_RU.UTF-8
Этот пакет содержит файлы заголовков, необходимые для разработки
приложений, использующих QCA.

%package ossl
Group: System/Libraries
Summary: QCA SSL Plugin
%description ossl
This is a plugin to provide SSL capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)
%description ossl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SSL для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA0, RIPEMD160, MD2, MD4, MD5
* Hashing - SHA224, SHA256, SHA384 and SHA512 (for openssl 0.9.8)
* Block Ciphers
* Keyed Hash Message Authentication Code (HMAC), using SHA1, MD5, RIPEMD160
* Public keys - RSA, DSA, Diffie-Hellman
* PKCS#12
* SSL/TLS
* CMS (for S/MIME)

%package cyrus-sasl
Group: System/Libraries
Summary: QCA SASL Plugin
%description cyrus-sasl
This is a plugin to provide SASL capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description cyrus-sasl -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования SASL для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package gnupg
Group: System/Libraries
Summary: QCA GnuPG Plugin
%description gnupg
This is a plugin to provide GnuPG capability to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description gnupg -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования GnuPG для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package nss
Group: System/Libraries
Summary: QCA NSS Plugin
%description nss
This is a plugin to provide Mozilla NSS capability to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing
%description nss -l ru_RU.UTF-8
Этот плагин предоставляет возможность использования Mozilla NSS для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование

%package gcrypt
Group: System/Libraries
Summary: QCA GCrypt Plugin
%description gcrypt
This plugin provides features based on libgcrypt to programs that
utilize the Qt Cryptographic Architecture (QCA)
* Hashing - SHA1, SHA256, SHA384, SHA512
* Symmetric encryption - AES128
%description gcrypt -l ru_RU.UTF-8
Этот плагин предоставляет функциональность libgcrypt для
программ, поддерживающих Qt Cryptographic Architecture (QCA)
* Хеширование - SHA1, SHA256, SHA384, SHA512
* Симметричное шифрование - AES128

%package pkcs11
Group: System/Libraries
Summary: QCA pkcs11 smartcard integration
%description pkcs11
This plugin supports the following features:
 - Multiple providers
 - Multiple tokens
 - Private key signature and decryption
 - Keystore objects serialization
 - Keystore update notifications
 - Asker integration for token and PIN

%package logger
Group: System/Libraries
Summary: QCA Logger Plugin
%description logger
Provides simple logger writer to programs that
utilize the Qt Cryptographic Architecture (QCA).
%description logger -l ru_RU.UTF-8
Этот плагин предоставляет возможность записи журналов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package softstore
Group: System/Libraries
Summary: QCA Logger Plugin
%description softstore
Provides simple persistent certificate store to programs that
utilize the for Qt Cryptographic Architecture (QCA).
%description softstore -l ru_RU.UTF-8
Этот плагин предоставляет хранилище сертификатов для
программ, поддерживающих Qt Cryptographic Architecture (QCA).

%package botan
Group: System/Libraries
Summary: QCA Botan Plugin
%description botan
This plugin provides features based on Botan. It implements:
* TBA
%description botan -l ru_RU.UTF-8
Этот плагин предоставляет функциональность Botan. Он реализует:
* TBA

%prep
%setup -q -n %name-%version
%patch10 -p1


%build
export QTDIR=%_qt5_prefix
export QC_CERTSTORE_PATH="%_datadir/ca-certificates/ca-bundle.crt"
%Kbuild \
    -DBUILD_TESTS=OFF \
    -DQCA_INSTALL_IN_QT_PREFIX=ON \
    -Dqca_CERTSTORE=%_datadir/ca-certificates/ca-bundle.crt \
    -DQCA_GPG_EXECUTABLE=gpg \
    -DQT4_BUILD=OFF \
    -DQCA_SUFFIX=qt5 \
    -DQCA_MAN_INSTALL_DIR=%_mandir \
    #

%install
%Kinstall

mkdir -p %buildroot/%_bindir
ls -1d %buildroot/%_qt5_bindir/* 2>/dev/null | while read f ; do
    [ -f "$f" ] || continue
    fname=`basename $f`
    mv $f %buildroot/%_bindir/$fname
    ln -s `relative %_bindir/$fname %_qt5_bindir/$fname` %buildroot/%_qt5_bindir/$fname
done


%files
%_bindir/*
%_qt5_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/libqca-qt5.so.*
%doc README INSTALL TODO

%files logger
%_qt5_plugindir/crypto/libqca-logger.so
%files softstore
%_qt5_plugindir/crypto/libqca-softstore.so
%files ossl
%_qt5_plugindir/crypto/libqca-ossl.so
%files cyrus-sasl
%_qt5_plugindir/crypto/libqca-cyrus-sasl.so
%files gnupg
%_qt5_plugindir/crypto/libqca-gnupg.so
%files gcrypt
%_qt5_plugindir/crypto/libqca-gcrypt.so
%files nss
%_qt5_plugindir/crypto/libqca-nss.so
%files pkcs11
%_qt5_plugindir/crypto/libqca-pkcs11.so
%if_enabled botan
%files botan
%_qt5_plugindir/crypto/libqca-botan.so
%endif

%files -n lib%name-devel
%_libdir/lib*.so
%_pkgconfigdir/qca2-qt5.pc
%_libdir/cmake/Qca-qt5/
%_qt5_archdatadir/mkspecs/features/crypto.prf
%_qt5_headerdir/Qca-qt5/
#%_qt5_headerdir/Qca-qt5/QtCrypto

%changelog
* Fri Sep 18 2020 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1
- new version

* Mon Jun 17 2019 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.2
- dont use ubt macro

* Wed Aug 29 2018 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt0.1
- 2.2.0 snapshot
- disable botan

* Wed Apr 11 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.3-alt3.1
- (NMU) rebuilt with new libbotan.

* Tue Mar 27 2018 Sergey V Turchin <zerg@altlinux.org> 2.1.3-alt3
- build botan plugin only on i86

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.1.3-alt2
- NMU: added URL

* Wed Nov 08 2017 Sergey V Turchin <zerg@altlinux.org> 2.1.3-alt1
- new version
- package botan module

* Tue Oct 06 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.1-alt1
- new version

* Thu Sep 17 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt3
- sync patches with SuSE

* Thu Jun 25 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt2
- rebuild with new libgcrypt

* Wed Jun 03 2015 Sergey V Turchin <zerg@altlinux.org> 2.1.0.3-alt1
- initial build

