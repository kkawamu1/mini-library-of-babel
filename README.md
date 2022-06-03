# mini-library-of-babel
> Inspired by the short story "La biblioteca de Babel" ("The Library of Babel") by  Argentine author and librarian Jorge Luis Borges, this website genereates a random sequences of 3200 letters with a random tile with 10 letters.

![Python versions](https://img.shields.io/pypi/pyversions/danger-python)

This is a simple website developed with flask, html, css, and Docker. You can visit the hosted version on heroku [link](https://mini-library-of-babel.herokuapp.com/). It generates a random sequence of letters. You might find some coherent sentences or phrases (even Shakespeare if you are really lucky)!

![](header.png)

## Installation


```sh
docker build -t mini_library_of_babel .
docker run -p 5000:5000 -d mini_library_of_babel
```

Visit ```http://localhost:5000/ ```
