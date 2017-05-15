#region Bootstrap PoShTeX
$modules = Get-Module -ListAvailable -Name posh-tex;
if (!$modules) {Install-Module posh-tex -Scope CurrentUser}
if (!($modules | ? {$_.Version -ge "0.1.4"})) {Update-Module posh-tex}
Import-Module posh-tex -Version "0.1.4"
#endregion

Export-ArXivArchive -RunNotebooks @{
    ProjectName = "{{cookiecutter.repo_name}}";
    TeXMain = "tex/{{cookiecutter.repo_name}}.tex";
    AdditionalFiles = @{
        "fig/*.pdf" = "fig/";
        "tex/revquantum.sty" = $null;
        # TODO: conditionally add quantumarticle.
        "README.md" = $null;
        "environment.yml" = $null;
    };
    Notebooks = @(
    )
}
