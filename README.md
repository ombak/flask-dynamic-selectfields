# flask-dynamic-selectfields
Dynamic select fields in flask use wtforms and jquery

### install
Create your virtualenv and install file requirements.txt

```
pip install -r requirements.txt
```

Install [yarn pkg](https://yarnpkg.com/en/) and install some pakage.

* [Bulma](https://bulma.io/) 
* [jQuery](https://jquery.com/)
* [dataTables](https://datatables.net/)

```
yarn add bulma
yarn add jquery
yarn add datatables
```

### init database
```
flask init-db
```

### populate database
```
flask pop-db
```

### run application
```
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## Authors

* **Sukma Wijaya Saputra** - *Initial work* - [ombak](https://github.com/ombak)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

