# Extensões de imagem
image = [['imagens'], ['.png','.jpg','.jpeg','.gif','.eps','.jfif','.tiff','.svg','.bmp']]
# Extensões de vídeo
video = [['videos'], ['.avi','.mwv','.mkv','.mp4','.m4v','.mov','.mpg','.mpeg']]
# Extensões de audio
audio = [['audios'], ['.mp3','.mwa','.ogg','.aac','.wav','.pcm','.flac','.aiff']]
# Extensões de documento de texto, apresentações, planilhas e gráficos
document = [['documentos'], ['.rtf','.txt','.csv','.odf','.pdf','.ppt','.pptx','.doc','.docx','.docm','.xls','.xlsx','.xlsm']]
# Extensões de arquivos em 3D
dimensions = [['dimensões'], ['.u3d','.prc']]
# Extensões de arquivos geoespaciais e arquivos de banco de dados
database = [['banco'], ['.sql','.xml','.docsql','.shp']]
# Extensões de arquivos do AutoCAD
autocad = [['autocad'], ['.dwg','.dwt','.dxf','.dwf','.dst']]
# Extensões de documentos da Adobe ou CorelDraw
adobedraw = [['adobedraw'], ['.psd','.ai','.indd','.cdr']]
# Extensões de documentos da Adobe ou CorelDraw
compacted = [['compactados'], ['.zip','.gzip','.bzip2','.wim','.tar','.xz','.7z']]
# Extensões de documentos da Adobe ou CorelDraw
executed = [['executaveis'], ['.exe', '.msi']]
# Juntando todas as extensões em uma variável
extensions = []
# Salvando lista de extenções de imagem em um array único
extensions.append(image)
# Salvando lista de extenções de vídeo em um array único
extensions.append(video)
# Salvando lista de extenções de áudio em um array único
extensions.append(audio)
# Salvando lista de extenções de documento em um array único
extensions.append(document)
# Salvando lista de extenções de dimensões em um array único
extensions.append(dimensions)
# Salvando lista de extenções de banco de dados em um array único
extensions.append(database)
# Salvando lista de extenções do autocad em um array único
extensions.append(autocad)
# Salvando lista de extenções do adobe e corel draw em um array único
extensions.append(adobedraw)
# Salvando lista de extenções de arquivos compactados em um array único
extensions.append(compacted)
# Salvando lista de extenções de executáveis em um array único
extensions.append(executed)

# Perfil do utilizador
perfil = 'leonr'
# Diretório da imagem
directory = f'C:\\Users\\{perfil}\\Downloads'