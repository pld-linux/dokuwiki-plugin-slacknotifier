%define		plugin		slacknotifier
%define		php_min_version 5.3.0
Summary:	DokuWiki Slack notify plugin
Summary(pl.UTF-8):	Wtyczka slacknotifier dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/mallchin/dokuwiki-slack-notifier/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	fdc4c6db70aa7a03553aba96fc1ef0c3
URL:		https://www.dokuwiki.org/plugin:slacknotifier
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.520
Requires:	dokuwiki >= 20131208
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Notify page events via Slack.

%prep
%setup -q -n dokuwiki-slack-notifier-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
%{__rm} $RPM_BUILD_ROOT%{plugindir}/README.md

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.png
%{plugindir}/*.txt
%{plugindir}/conf
