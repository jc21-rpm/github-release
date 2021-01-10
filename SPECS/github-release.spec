%define debug_package %{nil}

%global gh_user github-release

Name:           github-release
Version:        0.10.0
Release:        1%{?dist}
Summary:        Commandline app to create and edit releases on Github (and upload artifacts)
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
A small commandline app written in Go that allows you to easily create
and delete releases of your projects on Github. In addition it allows
you to attach files to those releases. It interacts with the github releases
API. Though it's entirely possibly to do all these things with cURL, It's
not really that user-friendly. For example, you need to first query the API
to find the id of the release you want, before you can upload an artifact.

%prep
%setup -qn %{name}-%{version}

%build
make

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Jan 11 2021 Jamie Curnow <jc@jc21.com> 0.10.0-1
- v0.10.0

* Sat May 2 2020 Jamie Curnow <jc@jc21.com> 0.8.1-1
- v0.8.1

* Thu Apr 30 2020 Jamie Curnow <jc@jc21.com> 0.8.0-1
- v0.8.0

* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> 0.7.2-1
- Initial Spec

