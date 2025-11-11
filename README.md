Herramienta de IA
============

## Instalacion
----------

Para instalar las herramientas se requiere instalar las dependencias de python.

~~~bash
pip install -r requirements.txt
~~~

Ahora se deben crear las api tokens en la [siguiente pagina](https://openrouter.ai/settings/keys), y añadirlas en el archivo siguiente archivo [connect.py](https://github.com/username01401/use-ia-tool/blob/main/connect.py#L11). Mientras mas api tokens alla, el tiempo se uso de la herramienta de ia sera mayor.

Despues del paso anterior se debe ejeceutar el siguiente comando con nuitka

~~~bash
nuitka connect.py --onefile --windows-console-mode=disable --file-version=1.0 --windows-icon-from-ico=icon.ico --file-description="Host de servicio: Administrador de permisos de seguridad"
~~~

Si no tiene instalado nuitka, instalelo con pip

~~~bash
pip install Nuitka
~~~

--------
## Combinacion de teclas

* __' + ¿ :__ Esta combinacion limpiara la pregunta que el usuario hara a la ia.
* __{ + } :__ Esta combinacion añadira lo que usuario tenga copiado en el portapapeles a la pregunta que se le enviara a la ia.
* __inicio + fin :__ Esta combinacion escribira en el teclado lo que se encuentre en la pregunta que se le enviara a la ia.
* __. + - :__ Esta combinacion enviara la pregunta a la ia.
* __l + - :__ Esta combinacion copiara al portapapeles la respuesta de la ia, le usuario unicamente tendra que teclear Ctrl + V para pegar la respuesta de la ia en el portapapeles.
------

## Ejecucion

Cuando el compilado de nuitka acabe, el archivo .exe se encontrara en la carpeta connect.dist/ . Este .exe se tendra que mover a la carpeta origen y ejecutarlo. 
