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
