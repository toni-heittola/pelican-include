Pelican-include - Fetching file content
=======================================

`pelican-include` is an open source Pelican plugin to fetch file content and include it within the content page. 

**Author**

Toni Heittola (toni.heittola@gmail.com), [GitHub](https://github.com/toni-heittola), [Home page](http://www.cs.tut.fi/~heittolt/)

Installation instructions
=========================

## Pelican installation

Make sure the directory where the plugin was installed is set in `pelicanconf.py`. For example if you installed in `plugins/pelican-include`, add:

    PLUGIN_PATHS = ['plugins']

Enable pelican-include:

    PLUGINS = ['pelican-include']

Usage
=====

File content is injected to {include::<path to file>} tags within the content.

Example:

    File content:
     <pre>{include::content/data/data.yaml}</pre>
