OrdinaryDictionaryReplacement: #.boilerplate-properties-override
- queue_position: BEFORE #boilerplate-properties
- apply_mode: SEQUENTIAL
* %title --> Stroke input method (筆畫輸入法)
* %head-elements-before-viewport -->
    <meta name="description" content="Website for the stroke input method (筆畫輸入法).">
* %head-elements-after-viewport -->
    <link rel="icon" type="image/png" href="/favicon-48x48.png" sizes="48x48">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" href="/javascript/stroke-input.min.css">
* %styles -->
    img {
      vertical-align: middle;
    }

RegexDictionaryReplacement: #.chinese-lang
- queue_position: BEFORE #escape-idle-html
* (?P<chinese_run> [⺀-〿㇀-㇣㐀-鿼豈-龎！-｠𠀀-𱍊]+ )
    -->
  <span lang="zh-Hant">\g<chinese_run></span>

%%%

# %title

--
See b<https://github.com/stroke-input> for the GitHub organisation.
--


## Stroke Input Method (筆畫輸入法) for Android

==
- [![Get it on F-Droid]{width=240 height=auto}(https://fdroid.gitlab.io/artwork/badge/get-it-on.png)][f-droid]
- [![Get it on Google Play]{width=240 height=auto}(https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png)][google-play]
- [Source code on GitHub](https://github.com/stroke-input/stroke-input-android)
==

[f-droid]: https://f-droid.org/en/packages/io.github.yawnoc.strokeinput/
[google-play]: https://play.google.com/store/apps/details?id=io.github.yawnoc.strokeinput


## Stroke input method (筆畫輸入法): JavaScript

==
- [Try it online](/javascript/)
- [Source code on GitHub](https://github.com/stroke-input/stroke-input-javascript)
==
