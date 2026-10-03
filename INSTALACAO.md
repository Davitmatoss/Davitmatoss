# Instalação do perfil de Davi

## Conferir antes de publicar

Extraia o ZIP e abra **PREVIEW.html** no Chrome, Edge ou Firefox. Essa prévia contém as imagens incorporadas e reproduz os GIFs sem depender de internet. Leitores de documentos e algumas prévias de Markdown exibem apenas um quadro de GIF; confira o movimento no navegador.

## Publicar no GitHub

1. Use o repositório público **Davitmatoss/Davitmatoss**.
2. Na raiz, coloque `README.md` e as pastas `assets`, `scripts` e `.github`. Preserve os nomes. `PREVIEW.html` serve apenas para conferência e não precisa ser publicado.
3. Substitua o workflow anterior por `.github/workflows/profile.yml`. Se existir o antigo `.github/workflows/snake.yml`, remova-o para não manter duas automações.
4. Faça commit na branch `main` ou `master`. O workflow **Atualizar perfil** inicia quando esse README ou o próprio workflow é enviado. Também pode ser executado em **Actions → Atualizar perfil → Run workflow**.
5. A cascata transparente, os quatro mockups, os ícones oficiais, o texto animado, a cobrinha e os dados iniciais já estão incluídos. A Action atualiza a cobrinha e as estatísticas; ela não é necessária para mostrar a animação inicial.

## Se a atualização automática falhar

Abra o log em **Actions**. A gravação exige **Settings → Actions → General → Workflow permissions → Read and write permissions**. Proteções que impeçam o bot de gravar na branch também impedem a atualização. O workflow usa o `GITHUB_TOKEN` automático; não é preciso inserir um token pessoal no README.

## Conteúdo e fontes

- Os ícones são os SVGs oficiais do Devicon, salvos localmente. Flask e GitHub receberam apenas um fundo claro para contraste.
- Os badges foram obtidos do Shields.io no estilo das referências enviadas.
- A cobrinha inicial usa os níveis do calendário público de Davitmatoss em 28/09/2026 e o caminho calculado pelo Platane/snk. O SVG foi produzido pelo gerador oficial; o GIF inicial renderiza esse mesmo caminho. A Action oficial renova ambos.
- O cartão foi preenchido com a API pública do GitHub. Mostra repositórios públicos, estrelas em repositórios próprios que não são forks e seguidores.
- Os mockups são ilustrações conceituais dos projetos, não screenshots de suas interfaces reais.

Consulte `CREDITOS.md` para fontes e licenças.


## Recuperar os commits depois de perder a pasta

Você pode continuar no repositório atual. Perder a pasta local não exige apagar o histórico do GitHub.

1. Clone o repositório novamente:

```bash
git clone https://github.com/Davitmatoss/Davitmatoss.git
cd Davitmatoss
```

2. Copie o conteúdo deste ZIP para essa pasta, substituindo os arquivos.
3. Faça o commit e envie:

```bash
git add .
git commit -m "Atualiza perfil com cascata de codigo"
git push
```

Se for usar um repositório novo, ele precisa ser público e se chamar `Davitmatoss`. Coloque `README.md` diretamente na raiz, junto de `assets`, `scripts` e `.github`. Não envie o ZIP fechado.

## Animação parada no computador

No GitHub, abra https://github.com/settings/accessibility e escolha **Motion → Autoplay animated images → Enabled**. Recarregue o perfil com Ctrl + F5. Confira também se o GIF roda diretamente ou em outro navegador para identificar interferência de extensões. O GIF já tem repetição infinita; a preferência de movimento de cada visitante continua sendo respeitada.

## Arquivos de apoio

`PREVIEW.html` é uma prévia independente com imagens incorporadas. Não precisa ser enviada ao GitHub. `scripts/generate_header.py` permite recriar a cascata localmente com Python e Pillow; não é necessário executar para publicar o perfil.
