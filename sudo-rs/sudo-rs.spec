#
# spec file for package sudo-rs
#

Name:           sudo-rs
Version:        %{version}
Release:        2%{?dist}
Summary:        Memory safe implementation of sudo and su

License:        MIT OR Apache-2.0
URL:            https://github.com/trifectatechfoundation/sudo-rs
Source:         %{url}/archive/v%{version}/sudo-rs-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  pam-devel

%global debug_package %{nil}

%description
Memory safe implementation of sudo and su

%prep
%setup -n sudo-rs-%{version}

%build
cargo build --release --features pam-login

%install
mkdir -p %{buildroot}/usr/lib/cargo/bin
install -Dm4755 target/release/sudo %{buildroot}/usr/lib/cargo/bin/sudo
install -Dm0755 target/release/visudo %{buildroot}/usr/lib/cargo/bin/visudo
install -Dm4755 target/release/su %{buildroot}/usr/lib/cargo/bin/su

%files
/usr/lib/cargo/bin/sudo
/usr/lib/cargo/bin/visudo
/usr/lib/cargo/bin/su
%license LICENSE-APACHE
%license LICENSE-MIT
%doc README.md

%changelog
* Wed Mar 27 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.2.7-1
- Dynamic version
* Wed Mar 27 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.2.6-2
- Compat paths with oxidizr tool
* Wed Mar 25 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.2.6-1
- Initial package
