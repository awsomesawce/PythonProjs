#!/usr/bin/env pwsh
# Anaconda enhancements

function Search-Anaconda {

<#
.Description
Search anaconda.org for information regarding a package name
#>
param(
    [Parameter()]
    [string]
    $SearchTerm
)
if ($SearchTerm) {
    return Start-Process "https://anaconda.org/search?q=$SearchTerm"
}
else {
    return Write-Error "Need a search term aka package name to search for.  Try again."
}

}
