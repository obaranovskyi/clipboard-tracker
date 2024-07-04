# Clipboard tracker (`clipboard-tracker`)

# About

## Tracking the clipboard text content

The `clipboard-tracker` tracks clipboard changes and saves them to a file.

To run the `clipboard-tracker`, you can use the following command:

```bash
clipboard-tracker <filename>
```

In this way, the clipboard content will be saved to the specified file.

If you run the `clipboard-tracker` without arguments,
it will save the clipboard content to a default file.

## Tracking the clipboard image content

The `clipboard-tracker` can also track clipboard image content.
When we copy an image to the clipboard, the `clipboard-tracker` saves it to a file.
Before that the `clipboard-tracker` creates folder `images` next to the
file where the clipboard content is saved.

After the image is saved, the `clipboard-tracker` saves the path to the image file
to the clipboard content file in a markdown format.

# Installation

To install:

```bash
wget https://github.com/obaranovskyi/clipboard-tracker/raw/main/dist/clipboard-tracker -O ~/.local/bin/clipboard-tracker && chmod +x ~/.local/bin/clipboard-tracker
```
