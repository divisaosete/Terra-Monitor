# Fontes, proveniência e uso

Verificação de integração: **28/10/2026**. Resultados HTTP e CORS das APIs em `tests/live-results.json`. Endpoints podem sofrer mudanças; a validação nunca autoriza classificar ausência de dados como ausência de fenômenos.

| Instituição / serviço | Endereço | Finalidade e observações |
|---|---|---|
| USGS Earthquake Hazards Program | https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php | Documentação GeoJSON, propriedades e períodos. Os registros podem ser preliminares e revisados. |
| USGS diário | https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson | Todas as magnitudes publicadas nas últimas 24 h; não significa todos os sismos físicos do planeta. |
| USGS semanal | https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson | Últimos 7 dias, magnitude ≥ 2,5. Não comparar contagem diretamente com o feed diário. |
| NOAA SWPC Kp | https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json | Kp preliminar observado, adimensional, intervalos de 3 h; objetos e formato tabular validados separadamente. |
| NOAA SWPC F10.7 | https://services.swpc.noaa.gov/json/f107_cm_flux.json | Fluxo de rádio solar em sfu; usa `time_tag` e `flux`, não um adaptador genérico. |
| NOAA SWPC comunicados | https://services.swpc.noaa.gov/products/alerts.json | Produtos institucionais emitidos; `issue_datetime`, `product_id`, `message`. Não é lista garantida de avisos vigentes. |
| NOAA boletins | https://www.swpc.noaa.gov/products/alerts-watches-and-warnings | Consulta institucional dos avisos e explicações; conferir vigência no texto. |
| NOAA acesso | https://www.swpc.noaa.gov/content/data-access | Orientações de acesso público. Respeitar disponibilidade, evitar chamadas excessivas; não prometer serviço operacional de emergência. |
| Open-Meteo documentação | https://open-meteo.com/en/docs | Condições estimadas e previsão de modelos. Temperatura a 2 m (°C), vento a 10 m (km/h), precipitação (mm). |
| Open-Meteo previsão | https://api.open-meteo.com/v1/forecast | Parâmetros: `latitude`, `longitude`, `current=temperature_2m,wind_speed_10m,precipitation`, `hourly=temperature_2m,wind_speed_10m,precipitation`, `forecast_days=3`, `timezone=GMT`. A precipitação atual corresponde ao intervalo atual de 15 min; a série horária ao intervalo precedente. |
| Open-Meteo geocoding | https://geocoding-api.open-meteo.com/v1/search | Busca submetida pelo usuário, `name`, `count=6`, `language=pt`, `format=json`; sem geolocalização automática. |
| Open-Meteo termos | https://open-meteo.com/en/terms | Dados CC BY 4.0, atribuição obrigatória. API gratuita para uso não comercial; limites publicados de 600 chamadas/min, 5.000/h, 10.000/dia e 300.000/mês por usuário. Rever termos antes de publicar. Uso comercial depende de plano apropriado. |
| OpenStreetMap | https://www.openstreetmap.org/copyright | Dados cartográficos sob ODbL, atribuição visível. |
| OSM tiles | https://operations.osmfoundation.org/policies/tiles/ | URL padrão `https://tile.openstreetmap.org/{z}/{x}/{y}.png`. Sem download em massa, prefetch ou offline; preservar Referer e cache HTTP do navegador. Serviço comunitário sem SLA; demanda elevada requer outro provedor. |
| Smithsonian GVP | https://volcano.si.edu/ | Referência de vulcanologia, sem scraping ou API automática nesta versão. Catálogo editorial não indica atividade atual. Não se afirma licença aberta sobre o conteúdo completo do site. |
| USGS Volcano Hazards Program | https://www.usgs.gov/programs/VHP | Referência institucional e acesso a observatórios. Sem integração de alertas vulcânicos nesta versão. |
| NASA Earth Observatory | https://earthobservatory.nasa.gov/ | Aprofundamento, sem importação automatizada de dados ou imagens. |
| NASA Earthdata | https://www.earthdata.nasa.gov/ | Aprofundamento; alguns conjuntos exigem credenciais e processamento, fora desta integração estática. |

## Catálogo vulcânico editorial

Coordenadas aproximadas para navegação educativa, sem classificação de perigo, atividade ou erupção. Seis locais selecionados, não um catálogo global completo:

- Merapi (Indonésia): https://volcano.si.edu/volcano.cfm?vn=263250
- Etna (Itália): https://volcano.si.edu/volcano.cfm?vn=211060
- Kīlauea (Havaí): https://www.usgs.gov/volcanoes/kilauea
- Mount St. Helens (Washington): https://www.usgs.gov/volcanoes/mount-st.-helens
- Popocatépetl (México): https://volcano.si.edu/volcano.cfm?vn=341090
- Villarrica (Chile): https://volcano.si.edu/volcano.cfm?vn=357120

Páginas do GVP podem restringir acesso automatizado; o catálogo fornece os links para consulta humana e não redistribui relatórios completos. O catálogo não é atualizado automaticamente.

## Ciência e interpretação

- Magnitude, energia e intensidade: https://www.usgs.gov/programs/earthquake-hazards/science/earthquake-magnitude-energy-release-and-shaking-intensity
- Índice Kp: https://www.swpc.noaa.gov/products/planetary-k-index
- Rádio F10.7: https://www.swpc.noaa.gov/phenomena/f107-cm-radio-emissions
- Escalas NOAA: https://www.swpc.noaa.gov/noaa-scales-explanation

USGS e NOAA são fontes públicas governamentais; podem conter materiais de terceiros e não endossam este projeto. A aplicação mantém atribuição e links, não usa logos oficiais nem atribui representação institucional. Políticas: https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits e https://www.noaa.gov/disclaimer.

## Bibliotecas redistribuídas

- Leaflet **1.9.4**, BSD-2-Clause: https://leafletjs.com/ e https://unpkg.com/leaflet@1.9.4/LICENSE
- Chart.js **4.4.8**, MIT: https://www.chartjs.org/ e https://cdn.jsdelivr.net/npm/chart.js@4.4.8/LICENSE.md

Os arquivos e avisos de copyright são mantidos em `vendor/`. Nenhuma dependência usa versão flutuante. Os dados são consultados diretamente pelas APIs em execução, não embutidos no ZIP como se fossem atuais.
