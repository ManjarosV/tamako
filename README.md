# Tamako Market PT-BR para Kodi

Este é um projeto pessoal para disponibilizar legendas em português brasileiro de **Tamako Market** no Kodi, especialmente em instalações do Kodi para TVs LG com webOS.

O repositório contém um pequeno addon de legendas que lista os episódios disponíveis e baixa os arquivos `.ass` diretamente do GitHub. Ele não é um addon oficial de *Tamako Market*, da Kyoto Animation, da distribuidora ou do Kodi.

## O que está disponível

Atualmente estão disponíveis as legendas dos episódios:

- Temporada 1, episódios 03 a 12;
- formato `.ass`, preservando estilos, posições e efeitos da legenda quando o player suporta esses recursos;
- seleção manual do episódio pelo menu de download de legendas do Kodi.

Os episódios 01 e 02 não fazem parte deste repositório neste momento.

## Como o addon funciona

Quando o Kodi abre o serviço **Tamako Market PT-BR**, o addon mostra uma lista dos episódios. Ao escolher um episódio, o Kodi baixa a legenda correspondente deste repositório e a aplica ao vídeo em reprodução.

Por isso, o nome do episódio do vídeo não precisa ser reconhecido automaticamente: basta selecionar manualmente o episódio correto na lista.

## Instalação no Kodi para LG webOS

Em algumas versões do Kodi para webOS, a instalação normal por ZIP pode mostrar erro de estrutura. A forma que funcionou nesta TV foi copiar a pasta do addon pelo Gerenciador de arquivos do próprio Kodi.

1. No Kodi, abra **Configurações → Gerenciador de arquivos → Adicionar fonte**.
2. Adicione a fonte HTTP do projeto ou abra a fonte que já foi criada para o repositório.
3. Entre em `service.subtitles.tamako/`.
4. Copie a pasta inteira para:

   ```text
   special://home/addons/
   ```

5. Confirme que o caminho final ficou assim:

   ```text
   special://home/addons/service.subtitles.tamako/addon.xml
   special://home/addons/service.subtitles.tamako/service.py
   special://home/addons/service.subtitles.tamako/icon.png
   ```

6. Feche e abra o Kodi novamente.
7. Procure o addon em **Add-ons → Meus Add-ons → Legendas/Subtitle**.

Se o Kodi aceitar a instalação por ZIP, também existe um pacote em `packages/`. Nesse caso, use a versão mais recente disponível e mantenha a pasta do addon com o mesmo nome do ID: `service.subtitles.tamako`.

## Como usar

Durante a reprodução do episódio:

```text
OK
→ Áudio/Legenda
→ Baixar legenda
→ Tamako Market PT-BR
```

Depois escolha o episódio correspondente, por exemplo **Episódio 06 — Tamako Market PT-BR**.

Se houver atraso ou adiantamento, use o ajuste de sincronização de legendas do Kodi durante a reprodução.

## Estrutura do projeto

```text
service.subtitles.tamako/   # addon Kodi
packages/                   # pacotes ZIP opcionais
repository.tamako/          # metadados do repositório Kodi
subtitles/                  # arquivos de legenda .ass
```

## Avisos

Este é um projeto comunitário e não oficial, mantido para uso pessoal. Verifique sempre se você tem o direito de acessar o vídeo e usar a legenda na sua região. Não há anúncios, rastreadores ou autenticação no addon.

O projeto depende de o GitHub estar acessível pela TV. Se o GitHub estiver bloqueado ou sem conexão, o addon poderá aparecer normalmente, mas não conseguirá baixar as legendas.

## Repositório

[github.com/ManjarosV/tamako](https://github.com/ManjarosV/tamako)
