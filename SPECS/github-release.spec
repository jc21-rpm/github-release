%define debug_package %{nil}

%global gh_user aktau

Name:           github-release
Version:        0.7.2
Release:        1%{?dist}
Summary:        Commandline app to create and edit releases on Github (and upload artifacts)
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  git golang

%description
A small commandline app written in Go that allows you to easily create
and delete releases of your projects on Github. In addition it allows
you to attach files to those releases. It interacts with the github releases
API. Though it's entirely possibly to do all these things with cURL, It's
not really that user-friendly. For example, you need to first query the API
to find the id of the release you want, before you can upload an artifact.

%prep
wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
ln -snf %{_builddir}/%{name}-%{version} %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
go list -f '{{join .Deps "\n"}}' | xargs go list -e -f '{{if not .Standard}}{{.ImportPath}}{{end}}' | grep -v "%{name}/github" | xargs go get -u
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Mon Sep 9 2019 Jamie Curnow <jc@jc21.com> 0.7.2-1
- Initial Spec

