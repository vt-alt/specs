%define pname iltorb

Name: node-iltorb
Version: 2.4.5
Release: alt1

Summary: Node.js module for brotli compression/decompression with native bindings

License: MIT License
Group: Development/Other
Url: https://github.com/nstepien/iltorb

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Note: use git due brotli submodule in the tarball
# Source-git: https://github.com/nstepien/iltorb.git
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-build-intro >= 1.9.18

BuildRequires: rpm-build-nodejs node
BuildRequires(pre): rpm-macros-nodejs

BuildRequires: node-nan

BuildRequires: libbrotli-devel

Provides: npm(%pname) = %version
#AutoReq: no
AutoProv: no

%description
iltorb is a Node.js package offering native bindings for the brotli compression library.

This package has been deprecated
Author message:

The zlib module provides APIs for brotli compression/decompression starting with Node.js v10.16.0, please use it over iltorb.


%prep
%setup -a 1
# FIXME: bug with double packing %name-development
rm -rf .gear/
rm -rfv brotli/

# npm_install will copy only build/Release/*.node
%__subst "s|/build/bindings/|/build/Release/|" index.js test/iltorb.js

cat <<EOF >binding.gyp
{
    "targets": [
        {
            'target_name': 'iltorb',
            'sources': [
              "src/common/allocator.cc",
              "src/common/stream_coder.cc",

              "src/dec/stream_decode.cc",
              "src/dec/stream_decode_worker.cc",

              "src/enc/stream_encode.cc",
              "src/enc/stream_encode_worker.cc",

              "src/iltorb.cc"
            ],
            'include_dirs': [
               '<!(node -e "require(\'nan\')")'
            ],
            "defines": ["NOMINMAX"],
            'cflags': [
                    '$CFLAGS',
                ],
          'link_settings': {
            'libraries': [
              '<!(pkg-config --libs libbrotlidec libbrotlienc)',
            ],
          }

        }
    ]
}
EOF

%build
%npm_build

npm test
npm prune --production

# tests need development modules, run it before npm prune
#%check
#npm test

%install
%npm_install
rm -rf %buildroot/%nodejs_sitelib/%pname/{test,scripts,src,.[a-z]*,*.gyp}/

%files
%doc LICENSE README.md
%nodejs_sitelib/%pname/

%changelog
* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- initial build for ALT Sisyphus
