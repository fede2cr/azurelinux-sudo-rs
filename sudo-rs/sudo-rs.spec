#
# spec file for package sudo-rs
#

Name:           sudo-rs
Version:        0.2.6
Release:        1%{?dist}
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
install -Dm1755 target/release/sudo %{buildroot}%{_bindir}/sudo-rs
install -Dm0755 target/release/visudo %{buildroot}%{_bindir}/visudo-rs
install -Dm1755 target/release/su %{buildroot}%{_bindir}/su-rs

%files
%{_bindir}/sudo-rs
%{_bindir}/visudo-rs
%{_bindir}/su-rs
%license LICENSE-APACHE
%license LICENSE-MIT
%doc README.md

%changelog
* Wed Mar 25 2025 Álvaro Figueroa <alvaro.figueroa@microsoft.com> - 0.2.6-1
- Initial package
