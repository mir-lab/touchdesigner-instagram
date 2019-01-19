# TouchDesigner Unofficial Python InstagramAPI
*a tox for posting images directly to Instagram*  
[matthew ragan](https://matthewragan.com)  
[zoe sandoval](https://zoesandoval.com)

## TouchDesigner Version
* 099 2018.26750

## OS Support
* Windows 10
* macOS

## Dependencies
* [InstagramAPI](https://github.com/LevPasha/Instagram-API-python)

## Summary
Auto-documenting installations are very slick, but getting the InstagramAPI to work for you might be a little more hassle than you really want to deal with. Luckily there's the Unofficial Instagram API written to support Python as an interface language. That's lovely as we can use that right inside of TouchDesigner. This allows you to post directly to Instagram by using the typical login credentials you would normally use. 

There are a number of convenience functions and elements here that allow the user freedom to focus on the art process rather than managing the connection with a webservice. You can save your credentials for re-use in your project, and before posting to the web the image to be shared is saved locally. This ensures that you have a local copy of your content. The TOX supports a threaded non-blocking approach, as well as a traditional blockinig approach. You may find that you want Touch to pause while the image is uploaded - in which case you want the blocking process, similarly, you may find that you want a non-blocking solution that's thread safe.

A big shout out to Zoe Sandoval here - they did all of the initial research and testing to get this integrated into TouchDesigner. We then collaborated together to find a re-usable and non-blocking approach that allows the user to operate this process without fear of freezing TouchDesigner. 

## Set-up


### Install Python3
Ensure that you've installed a `Python 3.5+` variety.

### Installing Dependencies for Windows Users


### Installing Dependencies for macOS Users


## Parameters