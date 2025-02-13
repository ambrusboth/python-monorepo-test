# Python Monorepo Test

Testing how to structure a python monorepo




## Installation 

```
asdf install
npm install -g nx
```



## Steps to set up repository

Create in `$HOME` a `.tool-versions` file, to be used with `asdf`:
```
echo "nodejs 22.1.0" >> .tool-versions
```

If you have some custom certificates, you may need to create an environment variable like this, so nodejs can use the certificate
```
export NODE_EXTRA_CA_CERTS="/usr/local/share/ca-certificates/zscaler-root.crt"
```

Create a new Nx workspace together with a github repository:
```
npx create-nx-workspace@latest python-monorepo-test
...
✔ Which stack do you want to use? · none
✔ Would you like to use Prettier for code formatting? · No
✔ Which CI provider would you like to use? · github
```

Create a remote repository in github.
Then set the remote repo in the freshly created nx workspace:
```
git remote add origin https://github.com/ambrusboth/python-monorepo-test.git
git push -u origin main
```

Add Nx python plugin:
```
npm install @nxlv/python
```
and include this plugin in the `nx.json`.


Add a poetry project:
```
npx nx generate @nxlv/python:poetry-project my-arithmetics --directory=libs --projectNameAndRootFormat=derived --projectType=library --linter=flake8 --unitTestRunner=pytest --unitTestHtmlReport=true --unitTestJUnitReport=true --codeCoverage=true --codeCoverageHtmlReport=true --codeCoverageXmlReport=true --codeCoverageThreshold=80 --pyprojectPythonDependency=">=3.12,<4" 
```

Add an external dependency to it:
```
npx nx run my-arithmetics:add --name=numpy
```

Add some arithmetic functions there.


Now add another poetry project, this time an app:
```
npx nx generate @nxlv/python:poetry-project my-calcs --directory=apps --projectNameAndRootFormat=derived --projectType=application --linter=flake8 --unitTestRunner=pytest --unitTestHtmlReport=true --unitTestJUnitReport=true --codeCoverage=true --codeCoverageHtmlReport=true --codeCoverageXmlReport=true --codeCoverageThreshold=80 --pyprojectPythonDependency=">=3.12,<4"
```

List the available projects:
```
npx nx show projects
```

Add the libs project to the apps project:
```
npx nx run my-calcs:add --name=libs-my-arithmetics --local
```





