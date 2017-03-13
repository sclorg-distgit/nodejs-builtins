%{?scl:%scl_package nodejs-builtins}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-builtins

%global npm_name builtins
%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:		%{?scl_prefix}nodejs-builtins
Version:	1.0.2
Release:	3%{?dist}
Summary:	List of node.js builtin modules
Url:		https://github.com/juliangruber/builtins
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%description
List of node.js builtin modules

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json builtins.json \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
%{?scl:scl enable %{scl} "}
node test.js
%{?scl:"}
%endif

%files
%{nodejs_sitelib}/builtins

%doc Readme.md History.md
%doc License

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-3
- rebuilt

* Fri Nov 27 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-2
- Enable scl macros

* Mon Jun 29 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-1
- Initial build
