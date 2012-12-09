# revision 21606
# category Package
# catalog-ctan /macros/latex/contrib/kix
# catalog-date 2011-03-04 11:12:16 +0100
# catalog-license lppl1
# catalog-version undef
Name:		texlive-kix
Version:	20110304
Release:	2
Summary:	Typeset KIX codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kix
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kix.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Implements KIX codes as used by the Dutch PTT for bulk mail
addressing. (Royal Mail 4 State Code.) KIX is a registered
trade mark of PTT Post Holdings B. V.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kix/kix.sty
%doc %{_texmfdistdir}/doc/latex/kix/kix.pdf
%doc %{_texmfdistdir}/doc/latex/kix/kix.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110304-2
+ Revision: 752986
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110304-1
+ Revision: 718775
- texlive-kix
- texlive-kix
- texlive-kix
- texlive-kix

