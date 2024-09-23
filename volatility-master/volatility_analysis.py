import volatility.conf as conf
import volatility.registry as registry
import volatility.commands as commands
import volatility.utils as utils

config = conf.ConfObject()

registry.PluginImporter()
config.parse_options()
config.PROFILE  = "Win10x64_14393" # Replace with the actual profile if you know it
config.LOCATION = "D:///2024/NIDIA/Win10x64_14393.img" # Replace with the actual path

ctx = registry.Context()
ctx.config = config

imageinfo_command = commands.Command.get_command("imageinfo")
imageinfo_command(ctx, config_path=config.PROFILE, progress_callback=None)

import volatility.framework.interfaces.configuration as configuration
import volatility.framework.automagic.run as automagic

# Configuración (ajusta la ruta de la imagen según sea necesario)
config_path = "D:///2024/NIDIA/Win10x64_14393.img"  
symbol_path = "D:\\2024/NIDIA\\volatility\\volatility-master"  # Asegúrate de tener los símbolos correctos
profile = "Win10x64_14393"  # Ajusta el perfil según tu imagen de memoria

# Crear un contexto y configuración
ctx = context.Context()
ctx.config['automagic.LayerStacker.single_location'] = config_path
ctx.config['PROFILES'] = profile
ctx.symbol_space = vmlinux_symbols

# Ejecutar el plugin imageinfo automáticamente
automagic.run(ctx, ['imageinfo'])

import volatility.framework.interfaces.configuration as configuration
import volatility.framework.automagic.run as automagic

# Configuración (ajusta la ruta de la imagen según sea necesario)
config_path = "D:///2024/NIDIA/Win10x64_14393.img"  
symbol_path = "D:\\2024/NIDIA\\volatility\\volatility-master\\symbols"  # Asegúrate de tener los símbolos correctos
profile = "Win10x64_14393"  # Ajusta el perfil según tu imagen de memoria

# Crear un contexto y configuración
ctx = context.Context()
ctx.config['automagic.LayerStacker.single_location'] = config_path
ctx.config['PROFILES'] = profile
ctx.symbol_space = vmlinux_symbols

# Ejecutar el plugin imageinfo automáticamente
automagic.run(ctx, ['imageinfo'])


python vol.py -f D:///2024/NIDIA/Win10x64_14393.img linux_pslist
