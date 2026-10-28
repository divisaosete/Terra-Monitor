# Terra Monitor — Observatório Planetário

**New Era Labs | Divisão 7 · Per Vitam, Ad Astra.**

Aplicação científica estática, em português, sem cadastro, backend ou credenciais. Observações, estimativas e previsões são identificadas. Nenhum dado fictício é usado nos painéis.

## Executar

Requer Node.js 20+ apenas para o servidor local e testes. Não há instalação de pacotes.

```sh
npm start
```

Abra http://127.0.0.1:4173/Terra-Monitor/ no navegador. Alternativa: `python -m http.server 8000` na pasta do projeto e abra http://localhost:8000/. Não abra por duplo clique (`file://`): módulos ES exigem HTTP. Internet é necessária para dados novos e cartografia.

## Funcionalidades

- Visão geral: contagem e maior magnitude do feed selecionado, último Kp, quantidade de comunicados recebidos, resumo factual e horários das fontes.
- Terremotos: mapa Leaflet com renderização Canvas, pop-ups, zoom, arraste, filtros de magnitude/profundidade/região, dois períodos, ordenação, destaque do maior evento, histogramas, série temporal, tabela e CSV.
- Atividade solar: fluxo observado F10.7 e série temporal; comunicados NOAA em texto original com tipo, data e acesso à publicação institucional.
- Campo geomagnético: Kp preliminar observado, escala 0–9, série e tabela.
- Vulcões: seis referências educativas em mapa e catálogo, sem status operacional.
- Clima Global: busca de cidade ou coordenadas, condições atuais estimadas e previsão horária de modelo (temperatura, vento, precipitação).
- Explorador: escolha de conjunto, recorte temporal, gráfico, tabela, CSV de dados efetivamente carregados. Não busca arquivos históricos adicionais.
- Explicações científicas por módulo, fontes, privacidade, cache e preferências locais, navegação por hash e menu mobile.

## Estrutura

```text
index.html              Entrada da aplicação
assets/app.js           Interface, rotas e interações
assets/services.js      Adaptadores, validação, cache, CSV e filtros
assets/content.js       Textos educativos e catálogo editorial
assets/style.css        Identidade, acessibilidade e responsividade
assets/favicon.svg      Ícone próprio
vendor/                 Leaflet, Chart.js, imagens e licenças
tests/                  Testes unitários, servidor e verificações reais
FONTES.md               Proveniência, endpoints e condições
TESTES.md               Evidências e limitações dos testes
```

## Dados e atualização

Veja [FONTES.md](./FONTES.md) para endereços e termos. USGS: `all_day.geojson` ou `2.5_week.geojson`. NOAA: `noaa-planetary-k-index.json`, `f107_cm_flux.json`, `alerts.json`. Open-Meteo: `v1/forecast` e `v1/search` (geocoding).

Cache de 5 minutos por conjunto/local. Atualização automática a cada 5 minutos com a página visível; botão para nova consulta. As chamadas simultâneas à mesma chave são agrupadas, com timeout de 15 s. Mudanças de tela reaproveitam os dados. Cache inválido é ignorado. Falha com cache preserva os dados e marca desatualização; falha sem cache informa indisponibilidade. O bloqueio de armazenamento não impede a consulta.

Horários internos são timestamps UTC. A interface informa o fuso do visitante; CSV usa ISO 8601 em UTC. USGS mostra a geração do feed, os outros conjuntos mostram o último horário disponível da fonte. Limiares editoriais de desatualização: USGS 15 min, Kp 6 h, F10.7 48 h, comunicados 24 h, meteorologia 3 h. No caso de comunicados, a idade do último produto não demonstra falha da instituição nem vigência de aviso; confira o texto oficial.

## Dependências

Bibliotecas incluídas localmente e com versões fixas: **Leaflet 1.9.4 (BSD-2-Clause)** e **Chart.js 4.4.8 (MIT)**. Licenças completas em `vendor/`. Não há fontes externas ou CDN em tempo de execução. Tiles OpenStreetMap são carregados diretamente com atribuição, sem pré-download. O Canvas evita milhares de elementos DOM para os sismos; os feeds selecionados limitam a extensão dos dados. Nenhuma série tem pontos intermediários inventados; linhas unem observações disponíveis sem suavização.

## GitHub Pages (somente quando decidir publicar)

1. Extraia o ZIP; `index.html` deve estar na raiz do conteúdo que será publicado.
2. Envie `index.html`, `assets/` e `vendor/` (e documentos, se desejar) para um repositório escolhido por você.
3. Em Settings → Pages, selecione publicação por branch e a pasta que contém `index.html`.
4. Aguarde a publicação e abra a URL fornecida pelo GitHub.

Não existe build. Todos os caminhos de assets são relativos; rotas usam hash, sem regras de reescrita. Funciona em `https://usuario.github.io/repositorio/`. Não são usados service worker nem chaves privadas. Nenhuma publicação foi feita nesta entrega.

## Testes

```sh
npm test
npm run check
node tests/live.mjs
```

O último comando acessa APIs reais e grava `tests/live-results.json`; execute na pasta do projeto. Testes unitários usam amostras sintéticas explicitamente isoladas em `tests/`, nunca carregadas pela aplicação. Consulte `TESTES.md` para o que foi realmente executado.

## Limitações e responsabilidade

- Vulcões são um catálogo educativo manual. Não foi adotada uma API global documentada e apropriada para monitoramento; não há scraping.
- Comunicados do feed podem ter expirado ou sido substituídos. A aplicação não deduz o estado de alertas ativos e não produz avisos de emergência. Exibe os 25 produtos mais recentes; o total recebido aparece no indicador.
- Eventos solares são acompanhados pelos comunicados; não há catálogo automático próprio de erupções ou ejeções de massa coronal.
- As condições atuais Open-Meteo são estimativas de modelos. A série de 3 dias começa à meia-noite UTC e pode conter horas passadas do dia atual; não é observação de estação. Não descreve tendências climáticas planetárias.
- O endpoint gratuito Open-Meteo é para uso não comercial e tem limites. Avalie os termos antes de uma publicação comercial; não embuta chave privada em uma adaptação estática.
- API, rede, CORS e tiles podem mudar ou ficar indisponíveis. Não há promessa de funcionamento integral offline.
- NASA é uma referência de aprofundamento no documento de fontes; não existe integração NASA operacional nesta versão.
- Não há auditoria completa WCAG, ensaio com leitor de tela ou garantia de funcionamento em todos os navegadores. Navegadores atuais com módulos ES, `fetch`, `dialog` e `AbortSignal.timeout` são necessários.

Projeto independente; não representa oficialmente as instituições. Uso educativo e informativo, sem previsão de terremotos, danos ou desastres. Não substitui defesa civil nem serviços oficiais de emergência.
