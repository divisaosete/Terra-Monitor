# Verificação da entrega v1.0

Execução em **28/10/2026**, Windows, Node.js 24 e navegador integrado baseado em Chromium. Não houve publicação externa nem alteração no WordPress.

## Testes automatizados

`npm test`: **10 testes aprovados**, nenhum reprovado. Cobrem UTC, validação GeoJSON, geometria inválida, valores ausentes, estruturas NOAA tabulares/objetos, limites Kp, fluxo solar, comunicados, zero meteorológico, filtros, ordenação, CSV/aspas/fórmulas, URLs, dados antigos, cache, erro HTTP, falha de rede e respostas inválidas. `npm run check`: sintaxe dos módulos aprovada.

`node tests/live.mjs`: **6 de 6 integrações responderam HTTP 200**, com `Access-Control-Allow-Origin: *` e dados aceitos pelos adaptadores. Primeira execução: USGS diário 239 eventos, USGS semanal 351, Kp 62, F10.7 123, comunicados 89, meteorologia 72 horas. Os números mudam com atualização e não são um resultado esperado fixo. Evidência completa em `tests/live-results.json`.

## Verificações no navegador

| Item | Execução e resultado |
|---|---|
| Carregamento inicial | Dados reais, indicadores, cartografia e gráficos renderizados. |
| Navegação | As oito áreas abriram, com título e conteúdo correspondentes. |
| Subdiretório estático | Aplicação servida em `/Terra-Monitor/`; assets locais e rotas hash funcionaram. Não foi publicada no GitHub Pages. |
| Mapas e marcadores | Sismos renderizados; seis marcadores SVG do catálogo identificados. Clique no Merapi abriu nome, país, coordenadas, limitação e link institucional. Zoom testado pelo controle. |
| Filtros sísmicos | Magnitude mínima 5 reduziu o conjunto diário de 240 para 15 eventos naquele momento. Troca para feed semanal retornou 348 eventos e 73 após o filtro. Região, profundidade e ordenação também têm cobertura unitária. |
| Gráficos | Histogramas e séries USGS/NOAA/Open-Meteo renderizados com resumos textuais; dados tabulares disponíveis. |
| Exportação | Botão gerou CSV dos terremotos filtrados; codificação, UTC, escapes e proteção contra fórmulas cobertos em teste unitário. |
| Educação e teclado | Painel abriu por Enter, Tab alcançou o link científico, Escape fechou. Não equivale a auditoria completa com tecnologia assistiva. |
| Meteorologia | São Paulo retornou estimativas e 72 horas; busca Recife retornou cidades e permitiu selecionar Recife/Pernambuco. |
| Explorador | Seleção Kp e intervalo 27–28/10 retornou 9 pontos no fuso local. Início posterior ao fim exibiu mensagem e impediu o recorte inválido. |
| Mobile | Menu recolhível abriu/fechou e permitiu navegar. As oito áreas foram inspecionadas em 360, 768 e 1440 px: largura rolável da página não excedeu a largura da tela. Tabelas mantêm rolagem interna. |
| Persistência | Filtro magnitude 5 permaneceu após recarregar; cidade selecionada e escolha de conjunto foram armazenadas. |
| Falha total | Harness isolado `tests/offline.html` bloqueou fetch e removeu acesso a cache real da sessão de teste. Visão geral e meteorologia continuaram navegáveis, com “—”, status indisponível, mensagens e novas tentativas, sem mostrar zero eventos como se fosse ausência de fenômenos. |

Foi corrigido um erro de redimensionamento de mapas já removidos durante navegação rápida. Também foi corrigido o acesso ao objeto meteorológico quando uma consulta falha sem cache. Os cenários foram repetidos após os ajustes.

## Links externos

Verificação HTTP registrada em `tests/link-results.json`: NOAA, documentação Open-Meteo, documentação dos feeds USGS e retorno ao New Era Labs responderam 200. Páginas institucionais `www.usgs.gov` e Smithsonian GVP responderam **403 ao acesso automatizado**; OpenStreetMap copyright respondeu **429**. Esses resultados não comprovam links inexistentes, mas impedem afirmar que todos foram validados integralmente. Os endereços oficiais foram mantidos e a limitação está registrada; não foi tentado contornar os bloqueios.

## Empacotamento

`python tests/package.py` cria `delivery/Terra-Monitor-v1.0.zip` com `index.html` na raiz, testa CRC, extrai uma cópia em diretório novo e compara SHA-256 de todos os arquivos. O relatório de integridade fica em `delivery/integridade.json`. A pasta de entrega, arquivos temporários de edição e quaisquer arquivos externos não entram no ZIP. Execute os testes da cópia extraída conforme a evidência que acompanha a entrega.

## Limites da verificação

- Não foram executados testes em Safari/Firefox, leitores de tela ou dispositivos físicos por toque.
- Não foi realizada auditoria completa WCAG, teste de carga ou simulação de todas as falhas possíveis dos provedores.
- Arraste do mapa e interação por toque usam o comportamento padrão Leaflet, sem ensaio em dispositivo físico nesta sessão.
- Testes HTTP não garantem disponibilidade futura ou correção científica de cada registro publicado pela instituição.
- Vulcões não possuem integração em tempo real; textos solares não constituem um catálogo completo de erupções. Vigência de comunicados deve ser confirmada nas publicações oficiais.
