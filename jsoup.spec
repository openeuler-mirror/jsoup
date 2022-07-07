Name:           jsoup
Version:        1.14.2
Release:        2
Summary:        Java HTML Parser
License:        MIT
URL:            http://jsoup.org/
Source0:        https://github.com/jhy/jsoup/archive/refs/tags/jsoup-%{version}.tar.gz
Patch01:        Make-the-imports-of-javax.annotation-optional.patch
BuildArch:      noarch

BuildRequires:  maven-local, mvn(org.apache.felix:maven-bundle-plugin)
Provides:	%{name}-javadoc%{?_isa} %{name}-javadoc
Obsoletes:      %{name}-javadoc

%description
jsoup is a Java library for working with real-world HTML. It provides a very convenient API
for extracting and manipulating data, using the best of DOM, CSS, and jquery-like methods.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :japicmp-maven-plugin
%pom_remove_plugin :maven-failsafe-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE
%{_javadocdir}/%{name}/*

%changelog
* Wed Jul 13 2022 xiaoqianlv <xiaoqian@nj.iscas.ac.cn> - 1.14.2-2
- Make the imports of javax.annotation optional

* Fri Sep 3 2021 houyingchao <houyingchao@huawei.com> - 1.14.2-1
- Upgrade to 1.14.2

* Wed Mar 4 2020 chenli <chenli147@huawei.com> - 1.11.3-5
- Modify Spec.

* Tue Dec 3 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11.3-4
- Package init
