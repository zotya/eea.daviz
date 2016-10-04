#  EEA Daviz

[![DaViz
logo](https://camo.githubusercontent.com/db2a5c2f5ec461fdb7c4a7fa71c68c6414031639/687474703a2f2f646176697a2e65696f6e65742e6575726f70612e65752f6c6f676f2e706e67)](https://camo.githubusercontent.com/db2a5c2f5ec461fdb7c4a7fa71c68c6414031639/687474703a2f2f646176697a2e65696f6e65742e6575726f70612e65752f6c6f676f2e706e67)

[![http://ci.eionet.europa.eu/job/eea.daviz-
www/badge/icon](https://camo.githubusercontent.com/87ec954640616b295acf68026845281736a19248/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e646176697a2d7777772f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.daviz-www/lastBuild) [![http://ci.eionet.europa.eu/job/eea.daviz-
plone4/badge/icon](https://camo.githubusercontent.com/e6ca86b45720f294dcb591b18b1326a7c6600a93/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e646176697a2d706c6f6e65342f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.daviz-plone4/lastBuild) [![http://ci.eionet.europa.eu/job/eea.daviz-
zope/badge/icon](https://camo.githubusercontent.com/abfccfea4e42600bfa1d2e4ef2c8ecd9216b2804/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e646176697a2d7a6f70652f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.daviz-zope/lastBuild)

##  Introduction

[EEA Daviz](http://eea.github.com/docs/eea.daviz) is a web tool developed by
the European Environment Agency which helps creating interactive data
visualizations easily through the web browser, no extra tools are necessary.
It is free and open source.

You can generate attractive and interactive charts and combine them in a
dashboard with facets/filters which updates the charts simultaneously. Data
can be uploaded as CSV/TSV or you can specify SPARQL to query online Linked
open data servers (aka sparql endpoints).

> **Daviz is the first Semantic web data visualisation tool for Plone CMS,
entirely web-based!**

At the moment [Simile Exhibit](http://www.simile-widgets.org/exhibit3) and
[Google Charts](http://code.google.com/apis/chart) visualizations are
supported. The architecture allows to extend Daviz with more visualisation
libraries (visualisations plugins).

[![http://eea.github.io/_images/eea.daviz.cover.png](https://camo.githubusercontent.com/6b77ec9c9d9ded373afc7648e24f9327c8194223/687474703a2f2f6565612e6769746875622e696f2f5f696d616765732f6565612e646176697a2e636f7665722e706e67)](http://www.youtube.com/watch?list=PLVPSQz7ahsByeq8nVKC7TT9apArEXBrV0&v=CYEAAAdyWII)

Contents

  * Introduction
  * Main features
  * Video Tutorials
  * Live demos
  * Architecture overview
  * Installation
    * Google Maps API Key
      * Plone
      * Zope
  * Dependencies
  * Source code
  * Copyright and license
  * More documentation
  * Links
  * Funding and project management

##  Main features

[![Daviz features
diagram](https://camo.githubusercontent.com/2520ee2c687f03f70c33771ed8f0e878ce4b3222/687474703a2f2f646176697a2e65696f6e65742e6575726f70612e65752f6c6561726e2d6d6f72652f646176697a6469616772616d2e706e672f696d6167655f6c61726765)](https://camo.githubusercontent.com/2520ee2c687f03f70c33771ed8f0e878ce4b3222/687474703a2f2f646176697a2e65696f6e65742e6575726f70612e65752f6c6561726e2d6d6f72652f646176697a6469616772616d2e706e672f696d6167655f6c61726765)

  1. No desktop tools needed to make visualizations. all web based.
  2. Data input: easy copy and paste of data table from any webpage or excel sheet
  3. Data input from URL (CSV/TSV/JSON)
  4. Data input: drag-and-drop your data from CSV/TSV files, and we do the rest
  5. Data input advanced: retrieve data from any SPARQL endpoint on the fly
  6. Intuitive visualization editor to create interactive charts.
  7. Large amount of visualizations available: Area, Bar, Bubble, Candlestick, Column, Combo Chart, Gauge, Geo Intensity Maps, Line, Pie, Radar, Scatter, Stepped Area, Table, Tree Map, Motion Charts, Faceted search table, Faceted tiles, Faceted timeline, Faceted map and more...
  8. Dashboard. Group charts into one or more dashboards.
  9. Share any chart. Embeddable visualization in any webpage.
  10. Customizable chart options and colors
  11. Data table manipulation via drag and drop, preparing table for chart
  12. Pivot table (Transpose), transform row values into columns
  13. Modular framework for extending it with more visualizations
  14. Branding: add your own logo to each chart + QR code
  15. And much more...

It is simple to use, needs no desktop application, everything is done through
the web by uploading an "excel file", CSV, TSV. You can also query the "web of
data" via public available sparql endpoints.

You can easily make visualizations like:

  1. [Simile Exhibit](http://www.simile-widgets.org/exhibit3)
  2. [Google Charts](http://code.google.com/apis/chart)

See also initial project [wiki
page](http://taskman.eionet.europa.eu/projects/zope/wiki/DaViz) for the
reasoning behind this project.

##  Video Tutorials

Most of DaViz features are presented throughout a series of video tutorials
available under the [EEA Web Systems
Training](https://www.youtube.com/channel/UCAjXKVcpfF05urEk9uYFveA) YouTube
channel. The screencasts are divided in two playlists:
[Basic](http://www.youtube.com/playlist?list=PLVPSQz7ahsByeq8nVKC7TT9apArEXBrV0)
and
[Advanced](http://www.youtube.com/playlist?list=PLVPSQz7ahsBxbe8pwzFWLQuvDSP9JFn8I).

##  Live demos

  * [Basic tutorials](http://www.youtube.com/playlist?list=PLVPSQz7ahsByeq8nVKC7TT9apArEXBrV0)
  * [Advanced tutorials](http://www.youtube.com/playlist?list=PLVPSQz7ahsBxbe8pwzFWLQuvDSP9JFn8I)
  * [Daviz showroom](http://daviz.eionet.europa.eu)
  * [Google charts demos](http://code.google.com/apis/chart)
  * [MIT Simile Exhibit demos](http://www.simile-widgets.org/exhibit3)

##  Architecture overview

At the moment [Simile Exhibit](http://www.simile-widgets.org/exhibit3) and
[Google Charts](http://code.google.com/apis/chart) visualizations are
supported. The architecture allows to extend Daviz with more visualisation
libraries (visualisations plugins).

[![](https://camo.githubusercontent.com/cddc9aeb767e719698477be1025c068fd141f91e/687474703a2f2f6565612e6769746875622e636f6d2f5f696d616765732f6565612e646176697a2e6c61796572732e737667)](https://camo.githubusercontent.com/cddc9aeb767e719698477be1025c068fd141f91e/687474703a2f2f6565612e6769746875622e636f6d2f5f696d616765732f6565612e646176697a2e6c61796572732e737667)

##  Installation

##  zc.buildout

If you are using [zc.buildout](http://pypi.python.org/pypi/zc.buildout) and
the
[plone.recipe.zope2instance](http://pypi.python.org/pypi/plone.recipe.zope2instance)
recipe to manage your project, you can do this:

  * Update your buildout.cfg file:

    * Add `eea.daviz` to the list of eggs to install
    
        [instance]
    ...
    eggs =
      ...
      eea.daviz
    

  * Re-run buildout, e.g. with:
    
        $ ./bin/buildout
    

###  Google Maps API Key

####  Plone

Within ZMI -&gt; Plone Site -&gt; portal_properties add a plone property sheet
called geographical_properties and inside it add a new string property called
google_key.

####  Zope

Within ZMI -&gt; Top Folder -&gt; manage_propertiesForm add a string property
called google_key

In this property you have to paste the Google maps API KEY, follow instruction
<https://developers.google.com/maps/documentation/javascript/tutorial#api_key>

The Google account you use to generate the key has to be owner of the site,
this is done by verification via Google webmaster tools.

##  Dependencies

[EEA Daviz](http://eea.github.com/docs/eea.daviz) has the following
dependencies:

    

  * [Plone 4.x](http://plone.org)
  * [eea.app.visualization](http://eea.github.com/docs/eea.app.visualization)
  * [eea.sparql](http://eea.github.com/docs/eea.sparql)
  * [eea.forms](http://eea.github.com/docs/eea.forms)
  * [eea.googlecharts](http://eea.github.com/docs/eea.googlecharts)
  * [eea.exhibit](http://eea.github.com/docs/eea.exhibit)
  * [collective.js.jqueryui &lt; 1.9](https://pypi.python.org/pypi/collective.js.jqueryui) (Plone 4.0, 4.1, 4.2)
  * [collective.js.jqueryui &gt; 1.9](https://pypi.python.org/pypi/collective.js.jqueryui) (Plone 4.3+)

The following package are optional. Still they can improve the user experience
with this tool:

    

  * [eea.relations](http://eea.github.com/docs/eea.relations)
  * [eea.cache](http://eea.github.com/docs/eea.cache) (Check [eea.cache](http://eea.github.com/docs/eea.cache) documentation for more about memcache configuration)
  * [eea.depiction](http://eea.github.com/docs/eea.depiction)

    
    
    [instance]
    ...
    eggs =
      ...
      eea.daviz [full]
    
    zcml =
      ...
      eea.daviz-overrides
      eea.daviz-full
    

[![](https://camo.githubusercontent.com/1cc34aab15188eec03f811ea45d06bcbb137b948/687474703a2f2f6565612e6769746875622e636f6d2f5f696d616765732f6565612e646176697a2e646570656e64656e636965732e737667)](https://camo.githubusercontent.com/1cc34aab15188eec03f811ea45d06bcbb137b948/687474703a2f2f6565612e6769746875622e636f6d2f5f696d616765732f6565612e646176697a2e646570656e64656e636965732e737667)

##  Source code

Latest source code (Plone 4 compatible):

    

  * [Plone Collective on Github](https://github.com/collective/eea.daviz)
  * [EEA on Github](https://github.com/eea/eea.daviz)

Plone 2 and 3 compatible (Simile Exhibit visualisations only):

    <https://github.com/collective/eea.daviz/tree/plone25>

##  Copyright and license

The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Daviz (the Original Code) is free software; you can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

More details under eea.daviz/docs/License.txt

##  More documentation

  * [Daviz technical documentation on github](http://eea.github.com/docs/eea.daviz)
  * [Daviz plone product summary](http://plone.org/products/eea.daviz)
  * [Data input examples](http://www.eea.europa.eu/data-and-maps/daviz/learn-more/examples)
  * [How to prepare your data](http://www.eea.europa.eu/data-and-maps/daviz/learn-more/prepare-data)

##  Links

  1. Simile Wiki - Exhibit 2.0: <http://simile.mit.edu/wiki/Exhibit>
  2. Simile widgets: <http://www.simile-widgets.org/exhibit>
  3. EEA Daviz how-to: <http://taskman.eionet.europa.eu/projects/zope/wiki/HowToDaViz>
  4. EEA Daviz backlog wiki: <http://taskman.eionet.europa.eu/projects/zope/wiki/DaViz>
  5. Google charts: <http://code.google.com/apis/chart/>

##  Funding and project management

[EEA](http://www.eea.europa.eu/) \- European Environment Agency (EU)

