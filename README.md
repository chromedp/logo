# chromedp logo

<img src="chromedp.svg" alt="chromedp logo" width="200">

Logo for [chromedp](https://github.com/chromedp/chromedp), a Go package for
driving Chrome and other Chromium-based browsers through the
[Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/).

The mark is the Chrome logo set inside a gear, to show that the browser is
being mechanized.

## Files

| File           | Description                                         |
|----------------|-----------------------------------------------------|
| `chromedp.svg` | The logo, as a 200×200 SVG with a transparent background. |
| `chromedp.png` | A 512px PNG render of the SVG.                      |
| `gen.py`       | Python script that generates `chromedp.svg`.        |

## Regenerating

```sh
python3 gen.py
rsvg-convert -w 512 chromedp.svg -o chromedp.png
```

The gear size, tooth count, and colors are variables at the top of `gen.py`.
