![StringToPngForPapirus](https://lh3.googleusercontent.com/KdiVf6j3LePCfmnpix-ZWNeV6WH7WkjHZuk7prS73T_iGgVWdp749CpxwIdurE0vqkNhE5IotU4YVkpxg46dl3s46qkyCkNzVjfFMwsmPwWqt0uTJFeAQLeLGxxoJfMmdSq3Qdkb9po=s600 "StringToPngForPapirus")


# StringToPngForPapirus
PNG image generator for PaPiRus e-papers. This python convert texts to suitable PNG images for PaPiRus. This can be used for Japanese texts.

> 再配布可能なIPAフォントで日本語の文字列も変換できます。他のフォントを使いたい方は、スクリプトをいい感じに直して使ってください。


# How to use
Just run the script like this.

```
python string_to_png.py -s StringToPngForPapirus
```

Then you can get `output.png` like following.

![StringToPngForPapirus](https://lh3.googleusercontent.com/FaE4ouQKO4oNHKMi7JOWakvjnnFd0Z7mDlta5FgZ8enSp9hExJaOuelIw2ROaacvOnFpjI9xKtqRgcAUp2iICWWb3SQCwLSGIHzKBJHSFe5KXJJ_iGgKMdVcke3ZMkAUjkcomsT3uOk=s600 "StringToPngForPapirus")


After that, set the image to a PaPiRus e-paper like this.

```
papirus-draw output.png
```

Now you can set the image.

![StringToPngForPapirus](https://lh3.googleusercontent.com/gHFBSst64jE_t1UrogGkPcys8V6ApyKFesctotFuKwI9Wf-LHfZ8mwt1LKzdsWLeJCpAZWY1EvxvEK-zU3LOi01Y3FVCRSlQSK0zEcsTYVjSW-PtRxJ2Qp1_lbHoWzHZY_7FP4VBQKE=s600 "StringToPngForPapirus")


# Options

Here are some options.


## Invert color

Use `-i` option to invert color.


```
python string_to_png.py -s ポキオ -i
```

![StringToPngForPapirus](https://lh3.googleusercontent.com/5se6SfDN_HJSxsOJFOEtqZpAgrGMo8NJm88jPyfpDP3XeYgTSV7P1j6SMwfMyo0YDaR2NEGkn7FcaRWZbfWov89Jwwt8UxzY2OxNtfyWdPhdrwcRbfrZi2WznaA79ZjQ8iiirZsRLlo=s600 "StringToPngForPapirus")

## Different sizes

Use `-L`, `-M`, and `-S` for large, medium, and small PaPiRus e-papers. For detail, run `python string_to_png.py -s` to show help.


![StringToPngForPapirus](https://lh3.googleusercontent.com/YmXsCb97TqK7vwZMXdgMOFUJk3OINIghmta9Ktry5Ax3gl-zbKrhRkVyt2RmqEF_2CD0klcvNinEubP-NLg4aU0iZEZHmocd-chGjZTz_tfbvALabSphOpFEB90xrLJxe5FnAWTJCCY=s600 "StringToPngForPapirus")