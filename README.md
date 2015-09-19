# heroku-tilefarm

These are components from tilefarm that are suitable for running on Heroku.
Specifically, UTM grids (primarily used by Field Papers) and "boner" (lightened
Bing Imagery + Toner Labels, also primarily used by Field Papers).

## Deployment

```bash
heroku apps:create
heroku config:set SENSIBLE_DEFAULTS=enabled
git push heroku master
```
