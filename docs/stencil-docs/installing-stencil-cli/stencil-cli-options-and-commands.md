# Stencil CLI Options and Commands

<div class="otp" id="no-index">

### On this Page

* [Commands Overview](#commands-overview)
* [stencil help](#stencil-help)
* [stencil init](#stencil-init)
* [stencil start](#stencil-start)
* [stencil bundle](#stencil-bundle)
* [stencil push](#stencil-push)
* [stencil release](#stencil-release)

</div>

This article is a comprehensive command reference for Stencil CLI (BigCommerce's powerful theme development and deployment tool). For installation instructions for your OS, see: [Installing Stencil CLI](https://developer.bigcommerce.com/stencil-docs/installing-stencil-cli/installing-stencil). For more information on BigCommerce's Stencil Theme Engine, see: [About Stencil](https://developer.bigcommerce.com/stencil-docs/getting-started/about-stencil). Continue reading below for detailed information on each Stencil CLI command and option.

---

<a id="commands-overview"></a>

## Commands Overview

The syntax to run a Stencil CLI command is as follows: 

```shell
stencil <COMMANDS> [<OPTIONS>] <PARAMETERS>
```

Running `stencil help` outputs a full list of commands and their descriptions. For more detailed information and usage examples, click a link in the table below:

|Command                     |Description                                                                                 |
|----------------------------|--------------------------------------------------------------------------------------------|
|[init](#stencil-init)       |Interactively creates a `.stencil`, which configures how to run a BigCommerce store locally.|
|[start](#stencil-init)      |Starts up the BigCommerce store, using theme files in the current directory.                |
|[bundle](#stencil-bundle)   |Bundles up the theme into a structured .zip file, which can be uploaded to BigCommerce      |
|[push](#stencil-push)       |Bundles the theme into `.zip` file; then directly uploads the `.zip` to igCommerce.         |
|[release]()                 |Creates a new release in a theme's GitHub repository.                                       |
|[help](#stencil-help)       |display help and returns all the options available to use for the specified command.        |

<!--
    title: #### Basic Stencil CLI Options and Commands

    data: //s3.amazonaws.com/user-content.stoplight.io/6116/1538055264839
-->

---

<a id="stencil-help"></a>

## `stencil help`

Displays help and returns all options available for the specified command.

**Usage:**

```shell
stencil help [<COMMAND>]
```

**Example:**

```shell
~ $ stencil help
Usage: stencil [options] [command]

Options:
  -V, --version  output the version number
  -h, --help     output usage information
...
```

---

<a id="stencil-init"></a>

## `stencil init`

Creates a `.stencil` file used to configure the live preview when `stencil start` is run. The configuration information can be specified using the optional switches; if the configuration information is not specified via options, a prompt for the information will be displayed. 

**Usage:**

```shell
stencil init [--url <STORE_URL>] [--token <API_TOKEN>]
```

| Option                  | Alias | Description                                                                               |
|-------------------------|-------|-------------------------------------------------------------------------------------------|
| `--port [<HTTP_PORT>]`  |`-p`   | The `HTTP` port number to use when serving the live theme preview                         |
| `--token [<API_TOKEN>]` |`-t`   | The [BigCommerce API Token](https://support.bigcommerce.com/s/article/Store-API-Accounts) |
| `--url [<STORE_URL>]`   |`-u`   | The BigCommerce storefront URL                                                            |

---

<a id="stencil-start"></a>

## `stencil start`

Starts the live theme preview using the theme files in the current directory.

**Usage:**

```shell
stencil start [-V|--version] [-o|--open] [-v|--variation] [-t|--test] [-t|--tunnel] 
stencil start [-e|--theme-editor] [-n|--no-cache] [--theme-editor-port <PORT>]
stencil start [-h|--help]
```

**Example:**

```shell
stencil start --open # opens live theme preview in default browser
```

| Option                       |Alias| Description                                                                           |
|------------------------------|-----|---------------------------------------------------------------------------------------|
| `--version`                  |`-V` | Outputs the version number                                                            |
| `--open`                     |`-o` | Automatically open default browser                                                    |
| `--variation [<NAME>]`       |`-v` | Set which theme variation to use while developing                                     |
| `--test`                     |`-t` | Enable QA mode which will bundle all javascript for speed to test locally             |
| `--tunnel`                   |     | Create a tunnel URL which points to your local server which anyone can use            |
| `--theme-editor`             |`-e` | Run Theme Editor server                                                               |
| `--no-cache`                 |`-n` | Turns off caching for API resource data (cache refreshes every 5 minutes)             |
| `--theme-editor-port [port]` |     |Run the Theme Editor on a different port                                               |
| `--help`                     |`-h` | output usage information                                                              |

<div class="HubBlock--callout">
<div class="CalloutBlock--warning">
<div class="HubBlock-content">

<!-- theme: warning -->

### Authentication Errors
> If you receive an `Unauthorized, please use a valid username/token` error, authentication has failed. Check the API token supplied is correct. For more information on creating store API accounts and generating tokens, see: [Obtaining Store API Credentials](https://developer.bigcommerce.com/stencil-docs/installing-stencil-cli/live-previewing-a-theme#step-3-serve-live-preview). 

</div>
</div>
</div>

---

<a id="stencil-bundle"></a>

## `stencil bundle`

Bundles up the theme into a structured `.zip` file, which can be uploaded to BigCommerce.

**Usage:**

```shell
stencil bundle
```

---

<a id="stencil-push"></a>

## `stencil push`

Bundles up the theme into a structured `.zip file`; then directly uploads (pushes) the `.zip` to BigCommerce.

**Usage:**

```shell
Usage: stencil push [<OPTIONS>]
```

| Option                        |Alias| Description                                                                          |
|-------------------------------|-----|--------------------------------------------------------------------------------------|
|`--version`                    |`-V` | Outputs the version number                                                           |
|`--host [HOSTNAME]`            |     | Specify the API host (default: https://api.bigcommerce.com)                          |
|`--file [<FILENAME>]`          |`-f` | Specify the filename of the bundle to upload                                         |
|`--save [<FILENAME]`           |`s`  | Specify the filename to save the bundle as                                           |
|`--activate [<VARIATIONNAME>]` |`-a` | Skips activation prompt; specify variation or leave blank to select first variation |
|`--help`                       |`-h` | Output usage information.                                                            |

**Example:**

```shell
stencil push -f Cornerstone-2.3.2.zip # uploads specified file, skips bundling if file already exists
```
<div class="HubBlock--callout">
<div class="CalloutBlock--info">
<div class="HubBlock-content">
    
<!-- theme: {{callout_type}} -->

### --filename:
> You can use the `-f` or `--filename` option in cases where you have already run `stencil bundle` to bundle your theme, but the resulting .zip file has not yet been uploaded to BigCommerce. Use the generated .zip file's **filename** as a parameter to identify the generated file in your theme directory. An example of the command is outlined below.

>When you run `stencil push` with the `-f` or `--filename` option, Stencil CLI skips all its bundling steps and diagnostics. It proceeds directly to uploading the specified file, displaying its processing progress bar to show upload status.

</div>
</div>
</div>

---

<a id="stencil-release"></a>

## `stencil release`

Creates a new release in a theme’s GitHub repository. Developers outside BigCommerce can use this for forks (not master) of Stencil’s Cornerstone base theme, or for their own parallel themes independent of Cornerstone.

**Usage:**

```shell
stencil release [<OPTIONS>]
```

| Option      | Alias | Description                |
|-------------|-------|----------------------------|
| `--version` | `-V`  | Outputs the version number |
| `--help`    | `-h`  | Output usage information.  |

---

## Resources

### Related Articles
* [Authorizing and Initializing the CLI](/stencil-docs/installing-stencil-cli/installing-stencil)
* [Troubleshooting Your Setup](/stencil-docs/installing-stencil-cli/troubleshooting-your-setup)
