# app
Small flask application which displays hardware stats on a Linux system.

# system requirements
- nvidia-smi
- [xml2json](https://github.com/Cheedoong/xml2json)
- jq

# running the app

Clone or download the app and install the requirements.

```sh
pip install requirements.txt
```

Then `cd` into the app dir.

```sh
cd app
```

Run the app with flask.

```sh
flask run --host=198.51.100.10
```

Replace `198.51.100.10` with the IP address of your host.
View the stats via a browser or the ModBros app (custom URL).

```sh
http://198.51.100.10:5000/getjson
```

<img src="https://i.imgur.com/EpJ7wxP.png" alt="Image"/>