Name:       ecapture
Version:    0.5.0
Release:    1%{?dist}
Summary:    capture SSL/TLS text content without CA cert using eBPF
License:    AGPL-3.0
URL:        https://ecapture.cc
Source0:    %{name}-%{version}.tar.gz

BuildRequires: make,clang

%description
SSL/TLS plaintext capture,
support openssl/libressl/boringssl/gnutls/nspr(nss) libraries.

GoTLS plaintext support go tls library, which refers to encrypted

Communication in https/tls programs written in the golang language.

Bash audit, capture bash command for Host Security Audit.

MySQL query SQL audit, support mysqld 5.6/5.7/8.0, and mariadDB.

%prep
%setup -c
%build
cd ../
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin/
install -m 755 bin/ecapture %{buildroot}/usr/local/bin/ecapture

%files
/usr/local/bin/ecapture

%changelog
* Sun Apr  2 2023 ecapture - 0.5.0
- Support for capturing plaintext communication of TLS/HTTPS encrypted programs written in Golang.
- Refactored the way parameters are obtained from Golang ABI (supports two types of ABI on registers-based and stack-based).
%autochangelog
