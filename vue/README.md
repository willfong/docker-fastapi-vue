# Vue + Facebook Login

## How To Use

1. Download
1. Replace Facebook App ID with your own
1. Customize anything else
1. `npm run build`
1. Copy `dist/*` to your own backend 


## Login Process

1. Call to FB Login
1. Retrieve FB Access Token (FBAT)
1. Call backend login/ with FBAT for verification
1. Backend verifies FBAT with FB
1. Backend sends JSON Web Token (JWT)
1. Call backend api/ with JWT Authorization header


## Set up Facebook Login

https://developers.facebook.com/

Settings -> Basic -> Add Platform

Website -> Callback URL: http://localhost:8080/auth/facebook/callback

`auth/facebook/callback` will be handled by Vue frontend.


## Warnings

`The method FB.login can no longer be called from http pages.`

https://developers.facebook.com/blog/post/2018/06/08/enforce-https-facebook-login/
You will still be able to use HTTP with “localhost” addresses, but only while your app is still in development mode.

