%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
Summary:        A code coverage report generator using GNU gcov
Name:           gcovr
Version:        5.0
Release:        2%{?dist}
License:        BSD
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:            https://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xml
Requires:       python3
Requires:       python3-jinja2
Requires:       python3-lxml
Requires:       python3-pygments
Requires:       python3-setuptools
# for gcov
Requires:       gcc
BuildArch:      noarch

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.

%prep
%autosetup

%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root %{buildroot}

# %%check
# Tests are dependent on individual gcc versions and
# are likely to be flaky/noisy for Mariner

%files
%license LICENSE.txt
%doc README.rst CHANGELOG.rst
%{_bindir}/gcovr
%{python3_sitelib}/gcovr*

%changelog
* Wed Feb 16 2022 Thomas Crain <thcrain@microsoft.com> - 5.0-2
- Backport spec from 2.0 branch to 1.0 branch
- Remove 2.0-isms (doc building conditionals, dependency generation, python macros, etc.)

* Wed Feb 02 2022 Cameron Baird <cameronbaird@microsoft.com> - 5.0-1
- Update to v5.0

* Mon Jun 14 2021 Henry Li <lihl@microsoft.com> - 4.2-6
- Initial CBL-Mariner import from Fedora 34 (license: MIT)
- License Verified
- Disable building docs

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Tommi Rantala <tommi.t.rantala@nokia.com> - 4.2-3
- Add bcond to allow building without docs

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.2-2
- Rebuilt for Python 3.9

* Tue Feb  4 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 4.2-1
- New upstream release 4.2
- Add doc subpackage containing the user-documentation of gcovr

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.1-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Neal Gompa <ngompa13@gmail.com> - 4.1-2
- Add missing files installed in the Python sitelib location

* Fri Sep 07 2018 Neal Gompa <ngompa13@gmail.com> - 4.1-1
- Release 4.1 to Fedora (#1626452)
- Reformatted changelog entry

* Fri Sep 07 2018 Alexis Jeandet <alexis.jeandet@member.fsf.org> - 4.1-0
- Update to latest gcovr version (4.1)
- Removed backported upstream patch as it is part of the release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3-7
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-4
- Fix HTML reports for Python 3 (#1428277)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-2
- Address review comments (#1418804)
- Switch to Python 3

* Thu Feb  2 2017 Neal Gompa <ngompa13@gmail.com> - 3.3-1
- Initial package
