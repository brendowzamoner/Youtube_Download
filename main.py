import yt_dlp

def menu():
    print("=" * 50)
    print(" BAIXADOR DE VÍDEOS - YOUTUBE (yt-dlp + ffmpeg)")
    print("=" * 50)
    print("[1] Baixar vídeo em 1080p (MP4)")
    print("[2] Baixar vídeo em 720p (MP4)")
    print("[3] Baixar apenas áudio (MP3)")
    print("[4] Baixar playlist completa (melhor qualidade)")
    print("[0] Sair")
    print()

def baixar(url, op):
    opcoes = {
        'outtmpl': '%(title)s [%(id)s].%(ext)s',
        'merge_output_format': 'mp4',
    }

    if op == "1":
        opcoes['format'] = 'bestvideo+bestaudio'
        opcoes['postprocessors'] = [{
            'key': 'FFmpegMerger',
        }]

    elif op == "2":
        opcoes['format'] = '22'

    elif op == "3":
        opcoes.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s [%(id)s].mp3'
        })

    elif op == "4":
        opcoes['format'] = 'bestvideo+bestaudio'
        opcoes['yes_playlist'] = True
        opcoes['postprocessors'] = [{
            'key': 'FFmpegMerger',
            'preferredformat': 'mp4',
        }]

    else:
        print("Opção inválida.")
        return

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            break

        link = input("Cole o link do vídeo ou playlist: ").strip()
        baixar(link, opcao)
        print("\nDownload finalizado!\n")