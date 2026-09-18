OrdinaryDictionaryReplacement: #.boilerplate-properties-override
- queue_position: BEFORE #boilerplate-properties
- apply_mode: SEQUENTIAL
* %title --> Stroke input method (筆畫輸入法): Lookup v0.0.0
* %head-elements-before-viewport -->
    <meta name="description" content="Stroke lookup for the stroke input method (筆畫輸入法).">
* %head-elements-after-viewport -->
    <link rel="icon" type="image/png" href="/favicon-48x48.png" sizes="48x48">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <link rel="shortcut icon" href="/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
    <link rel="manifest" href="/site.webmanifest">
    <link rel="stylesheet" href="/javascript/stroke-input.min.css">
    <script>let FIREFOX_FOUC_FIX;</script>

RegexDictionaryReplacement: #.chinese-lang
- queue_position: BEFORE #escape-idle-html
* (?P<chinese_run> [⺀-〿㇀-㇣㐀-鿼豈-龎！-｠𠀀-𱍊]+ )
    -->
  <span lang="zh-Hant">\g<chinese_run></span>

OrdinaryDictionaryReplacement: #.typography.typography
- queue_position: BEFORE #whitespace
- apply_mode: SIMULTANEOUS
* (C)~ --> "© "
* -- --> –

OrdinaryDictionaryReplacement: #.links.license-links
- queue_position: BEFORE #explicit-links
- apply_mode: SIMULTANEOUS
* [gpl-3] --> b<https://www.gnu.org/licenses/>
* [apache-2] --> b<https://www.apache.org/licenses/LICENSE-2.0.html>
* [cc-by-4] --> b<https://creativecommons.org/licenses/by/4.0/>
* [cc0] --> b<https://creativecommons.org/publicdomain/zero/1.0/>

%%%

# %title

<noscript>
--
**{.disabled} JavaScript is required for lookup to function.**
--
</noscript>


''''{.controls}
|^
  //
    ; Codepoint
    ; Character
    ; Sequence regex
    ; Sequences (as digits)
|:
''''


## Dependencies

### [Conway Stroke Data] (v2.0.2)

--
`sequence-characters.txt` is:
--
--{.notice}
(C)~2021--2026 Conway <br>
Licensed under CC-BY-4.0, see [cc-by-4]. <br>
--

--
Other files are:
--
--{.notice}
Released into the Public Domain, see [cc0].
--

[Conway Stroke Data]: https://github.com/stroke-input/stroke-input-data


<footer>
[Go up a level to home page](/) <## (this repository will be a submodule of stroke-input.github.io) ##>
</footer>
