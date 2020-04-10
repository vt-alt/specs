%define _unpackaged_files_terminate_build 1

%define realname jose

%add_erlang_req_modules_skiplist Elixir.Atom
%add_erlang_req_modules_skiplist Elixir.Enum
%add_erlang_req_modules_skiplist Elixir.HashDict
%add_erlang_req_modules_skiplist Elixir.IO
%add_erlang_req_modules_skiplist Elixir.Jason
%add_erlang_req_modules_skiplist Elixir.JOSE.Poison
%add_erlang_req_modules_skiplist Elixir.Kernel
%add_erlang_req_modules_skiplist Elixir.Map
%add_erlang_req_modules_skiplist Elixir.Poison
%add_erlang_req_modules_skiplist Elixir.Poison.EncodeError
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Atom
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.BitString
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Float
%add_erlang_req_modules_skiplist Elixir.Poison.Encoder.Integer
%add_erlang_req_modules_skiplist cutkey
%add_erlang_req_modules_skiplist jsone
%add_erlang_req_modules_skiplist jsx
%add_erlang_req_modules_skiplist keccakf1600
%add_erlang_req_modules_skiplist keccakf1600_fips202
%add_erlang_req_modules_skiplist libdecaf_curve25519
%add_erlang_req_modules_skiplist libdecaf_curve448
%add_erlang_req_modules_skiplist libdecaf_sha3
%add_erlang_req_modules_skiplist libsodium_crypto_aead_chacha20poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_box_curve25519xsalsa20poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_hash_sha512
%add_erlang_req_modules_skiplist libsodium_crypto_onetimeauth_poly1305
%add_erlang_req_modules_skiplist libsodium_crypto_scalarmult_curve25519
%add_erlang_req_modules_skiplist libsodium_crypto_sign_ed25519
%add_erlang_req_modules_skiplist libsodium_crypto_stream_chacha20
%add_erlang_req_modules_skiplist ojson

Name: erlang-%realname
Version: 1.9.0
Release: alt1
Summary: JSON Object Signing and Encryption (JOSE) for Erlang and Elixir
Group: Development/Erlang
License: MIT
Url: https://github.com/potatosalad/erlang-jose

BuildArch: noarch

# https://github.com/potatosalad/erlang-jose.git
Source: %name-%version.tar

Patch1: erlang-jose-fedora-remove-warnings_as_errors-to-work-around-47.patch
Patch2: erlang-jose-alt-base64url-version.patch

BuildRequires(pre): rpm-build-erlang
BuildRequires: erlang-otp-devel erlang-devel
BuildRequires: /usr/bin/rebar
BuildRequires: erlang-common_test-devel
BuildRequires: erlang-base64url
BuildRequires: erlang-triq
BuildRequires: erlang-proper

%description
JSON Object Signing and Encryption (JOSE) for Erlang and Elixir.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%rebar_compile

%install
%rebar_install %realname

%check
%rebar_eunit -C rebar.test.config

%files
%doc LICENSE.md
%doc README.md
%_erllibdir/%realname-%version

%changelog
* Mon Mar 30 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.0-alt1
- Updated to upstream version 1.9.0.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2
- NMU: remove %%ubt from release

* Tue Apr 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt1
- Initial build for ALT.
