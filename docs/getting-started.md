# Getting Started

## Requirements

All ChafficPlugins require:

- **Java 16+**
- **Spigot** or **Paper** server (1.18+)
- **CrucialLib** (shared library, required by all plugins)

## Installation

### 1. Install CrucialLib

Download the latest release from [GitHub Releases](https://github.com/ChafficPlugins/CrucialLib/releases) and place the `.jar` in your server's `plugins/` folder.

!!! tip "Auto-Download"
    Our plugins can automatically download CrucialLib if it's missing. However, we recommend installing it manually to control the version.

### 2. Install Your Plugin

Download the plugin you want:

- **MyTrip**: [SpigotMC](https://www.spigotmc.org/resources/mytrip-amazing-drugs-in-minecraft.76816/) or [GitHub Releases](https://github.com/ChafficPlugins/MyTrip/releases)
- **MiningLevels**: [SpigotMC](https://www.spigotmc.org/resources/mininglevels.100886/) or [GitHub Releases](https://github.com/ChafficPlugins/MiningLevels/releases)

Place the `.jar` in your `plugins/` folder and restart the server.

### 3. Configure

Each plugin creates a default configuration in `plugins/<PluginName>/config.yml` on first startup. See the individual plugin docs for configuration details.

## For Developers

If you want to use our plugins as dependencies in your own plugin, see the [CrucialLib Setup Guide](cruciallib/setup.md) and the individual plugin API docs.
