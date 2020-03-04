Name:           jsoup
Version:        1.11.3
Release:        5
Summary:        Java HTML Parser
License:        MIT
URL:            http://jsoup.org/
Source0:        https://github.com/jhy/jsoup/archive/jsoup-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local, mvn(org.apache.felix:maven-bundle-plugin)
Provides:       %{name}-javadoc%{?_isa} %{name}-javadoc
Obsoletes:      %{name}-javadoc

%description
jsoup is a Java library for working with real-world HTML. It provides a very convenient API
for extracting and manipulating data, using the best of DOM, CSS, and jquery-like methods.

%prep
%autosetup -n %{name}-%{name}-%{version} -p1

%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE
%{_javadocdir}/%{name}/*

%changelog
* Wed Mar 4 2020 chenli <chenli147@huawei.com> - 1.11.3-5
- Modify Spec.

* Tue Dec 3 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.11.3-4
- Package init
