# Product Requirements Document — Inteligência Imobiliária Maringá

## 1. Overview

Plataforma data-driven de inteligência imobiliária para Maringá, iniciando pela coleta de anúncios do Sub100 e evoluindo para histórico de preços, deduplicação de imóveis, analytics geoespacial, dashboard de mercado, machine learning de precificação e monetização futura por tokens.

O produto deve transformar anúncios públicos e voláteis em uma base histórica, consultável e confiável o suficiente para apoiar análise de mercado, comparação de preços, identificação de concentração espacial e estimativa futura de preço justo.

Premissa: "Inteligência Imobiliária Maringá" é nome operacional. Marca final ainda será definida.

## 2. Problem

Dados imobiliários disponíveis em portais são fragmentados, sem histórico público confiável e com duplicidade frequente entre imobiliárias. Um mesmo imóvel pode aparecer em múltiplos anúncios, mudar de preço, sumir, retornar, trocar descrição ou aparecer com informações parciais.

Usuários interessados em mercado imobiliário local precisam comparar manualmente anúncios, bairros, preços e características. Isso cria baixa rastreabilidade, dificuldade de medir tendência temporal e pouca confiança para precificação.

## 3. Opportunity

Existe oportunidade de criar uma base proprietária de inteligência imobiliária local com valor progressivo:

- no curto prazo, analytics de mercado e histórico de anúncios;
- no médio prazo, deduplicação e análise geoespacial confiável;
- no longo prazo, modelo preditivo e monetização SaaS por consultas de preço.

## 4. Goals

### 4.1 Business Goals

- Criar base histórica proprietária de anúncios imobiliários de Maringá.
- Validar demanda por dashboard local de inteligência imobiliária.
- Reduzir análise manual via planilhas e buscas repetitivas.
- Preparar fundação técnica para precificação preditiva.
- Viabilizar futura monetização por tokens ou planos SaaS.

### 4.2 User Goals

- Visualizar distribuição espacial de preços de venda e aluguel.
- Comparar bairros, tipos de imóvel, faixas de preço e períodos.
- Acompanhar histórico de preço e disponibilidade de anúncios.
- Entender quando múltiplos anúncios parecem representar o mesmo imóvel.
- Obter estimativa futura de preço justo com base em atributos do imóvel.

## 5. Non-Goals

Não fazem parte do MVP:

- Expansão para outras cidades.
- Integração com múltiplas fontes além do Sub100.
- Compra de tokens, billing e assinatura paga.
- Modelo de ML em produção para usuário final.
- App mobile nativo.
- CRM imobiliário, gestão de leads ou contato com imobiliárias.
- Garantia de que ausência de anúncio significa venda ou locação concluída.

## 6. Users

| Persona | Necessidade | Uso principal | Nível técnico |
|---|---|---|---|
| Investidor local | Encontrar regiões e faixas com oportunidade | Compra, venda, aluguel e comparação | Médio |
| Corretor | Argumentar preço de captação ou anúncio | Comparação com mercado local | Baixo a médio |
| Imobiliária | Monitorar estoque e concorrência | Inteligência comercial | Médio |
| Analista de mercado | Produzir leitura de tendência | Relatórios e exploração de dados | Médio a alto |
| Usuário final | Avaliar preço justo | Decisão de compra, venda ou aluguel | Baixo |

## 7. Scope

### 7.1 MVP Scope

O MVP entrega fundação de dados e dashboard analítico:

- Validação da fonte Sub100.
- Scraping controlado para Maringá.
- Persistência de dados brutos, normalizados e históricos.
- Registro de execuções, erros, volume e duração de coleta.
- Modelo de dados com anúncio, imóvel único provável, snapshots, preços, localização e disponibilidade.
- Deduplicação inicial com score, regra e evidência.
- Histórico de preço por anúncio e por imóvel consolidado quando houver confiança.
- Status operacional: ativo, ausente, retornado e indisponível inferido.
- Dashboard com mapa, filtros, métricas e séries temporais.
- Qualidade operacional da base: últimas coletas, falhas, schema e cobertura.

### 7.2 Post-MVP Scope

- Melhorias de geocodificação e precisão espacial.
- Revisão assistida de deduplicação incerta.
- Indicadores avançados de pressão de preço e liquidez inferida.
- Exportações analíticas.
- Pipeline versionado de features para ML.
- Treino offline de modelos de precificação.

### 7.3 Future SaaS Scope

- Autenticação e contas de usuário.
- Carteira de tokens.
- Inferência paga de preço justo.
- Billing com gateway de pagamento.
- Histórico de previsões por usuário.
- Planos B2B para imobiliárias, corretores ou analistas.

## 8. Skills Required

| Área | Skills necessárias | Uso no projeto |
|---|---|---|
| Produto | PRD, discovery, priorização, critérios de aceite | Definir escopo, fases, métricas e limites |
| Scraping | HTTP, paginação, rate limit, retries, parsing, contrato de API | Coletar Sub100 com rastreabilidade |
| Backend | Python, APIs, serviços, validação, jobs | Expor dados e coordenar pipelines |
| Banco de dados | PostgreSQL, PostGIS, modelagem temporal, índices | Persistir histórico, geodados e consultas |
| Data engineering | bronze/silver/gold, qualidade, lineage, idempotência | Transformar anúncios em base analítica |
| Deduplicação | record linkage, fuzzy matching, normalização textual | Agrupar anúncios do mesmo imóvel provável |
| Analytics | métricas, séries temporais, segmentação | Criar indicadores de mercado |
| Frontend | dashboard, mapas, gráficos, filtros | Entregar exploração visual |
| Geoprocessamento | coordenadas, bairros, polígonos, heatmaps | Mapas e agregações espaciais |
| Machine learning | regressão, validação, features, drift | Precificação futura |
| QA | testes unitários, integração, contrato, fixtures | Evitar regressões em coleta e matching |
| DevOps | Docker, deploy, scheduler, backups | Operação confiável |
| Observabilidade | logs estruturados, métricas, alertas | Monitorar coleta, dados e aplicação |
| Segurança | secrets, autenticação futura, isolamento de dados | Preparar SaaS |
| Billing | tokens, ledger, pagamento, conciliação | Monetização futura |

## 9. Functional Requirements

| ID | Requirement | Description | Priority | Acceptance Criteria |
|---|---|---|---|---|
| RF-001 | Source validation | Validar campos, paginação, limites e estabilidade do Sub100 | P0 | Existe relatório/documento com endpoints, parâmetros, campos críticos, riscos e amostras |
| RF-002 | Scraping run tracking | Registrar cada execução de coleta | P0 | Toda execução possui início, fim, status, parâmetros, contagens e erro quando falhar |
| RF-003 | Raw snapshot storage | Persistir payload bruto imutável | P0 | Cada item coletado possui payload bruto rastreável ao run |
| RF-004 | Normalized listing | Normalizar anúncio em campos analíticos | P0 | Campos críticos são tipados; ausências são nulas; schema drift é registrado |
| RF-005 | Price history | Registrar observações temporais de preço | P0 | Mudança de preço gera nova observação sem sobrescrever histórico |
| RF-006 | Availability status | Inferir presença, ausência e retorno | P0 | Ausência gera status inferido sem afirmar venda/locação |
| RF-007 | Unique property entity | Criar entidade de imóvel único provável | P0 | Anúncios compatíveis podem compartilhar `property_id` com score registrado |
| RF-008 | Deduplication scoring | Calcular score de matching entre anúncios | P0 | Match automático só ocorre acima de limiar configurado e versionado |
| RF-009 | Regional aggregation | Calcular métricas por bairro/região | P1 | Dashboard/API retornam contagem, média, mediana e dispersão por recorte |
| RF-010 | Geospatial dashboard | Exibir mapa de pontos e densidade | P1 | Usuário filtra venda/aluguel, bairro, preço, tipo e período |
| RF-011 | Time series dashboard | Exibir evolução temporal | P1 | Usuário vê séries por cidade, bairro, tipo e transação |
| RF-012 | Property detail | Exibir histórico de imóvel consolidado | P1 | Imóvel com match confiável mostra anúncios relacionados, preços e status |
| RF-013 | Data quality panel | Mostrar saúde da base | P1 | Operador vê últimas coletas, falhas, volume e campos ausentes |
| RF-014 | ML dataset | Gerar dataset versionado para treino | P2 | Dataset inclui features, alvo, filtros, data de geração e versão |
| RF-015 | Price prediction | Estimar preço justo por atributos | P2 | Modelo offline aprovado retorna estimativa, intervalo e versão |
| RF-016 | Token charging | Consumir token por previsão paga | P3 | Token só é debitado quando inferência conclui com sucesso |
| RF-017 | Token purchase | Comprar pacotes de tokens | P3 | Saldo aumenta apenas após confirmação de pagamento |

## 10. Non-Functional Requirements

| ID | Category | Requirement | Target |
|---|---|---|---|
| RNF-001 | Traceability | Coletas e transformações devem ser auditáveis | 100% dos runs com status e logs |
| RNF-002 | Data quality | Mudanças de schema devem ser detectadas | Campos críticos ausentes geram alerta operacional |
| RNF-003 | Performance | Dashboard deve responder filtros comuns rapidamente | < 3s no MVP para recortes principais |
| RNF-004 | Scalability | Banco deve suportar histórico diário crescente | Índices por data, transação, bairro, localização e status |
| RNF-005 | Reliability | Scraper deve lidar com falhas temporárias | Retry, backoff, timeout e falha rastreável |
| RNF-006 | Security | Secrets fora do código | 100% via variáveis de ambiente |
| RNF-007 | Privacy | Dados SaaS futuros separados dos dados públicos | Isolamento lógico por domínio |
| RNF-008 | Maintainability | Matching e normalização devem ser testáveis | Funções pequenas, fixtures e testes unitários |
| RNF-009 | Observability | Operação deve mostrar falhas e volumes | Logs estruturados, métricas e health checks |
| RNF-010 | Usability | Dashboard deve ser claro para não técnicos | Filtros legíveis, legendas e métricas definidas |

## 11. Data Model

### 11.1 Core Entities

| Entity | Purpose | Key Fields |
|---|---|---|
| `source` | Origem dos dados | `id`, `name`, `base_url`, `active` |
| `scraping_run` | Execução de coleta | `id`, `source_id`, `started_at`, `finished_at`, `status`, `params`, `item_count`, `error_summary` |
| `raw_listing_snapshot` | Payload bruto | `id`, `run_id`, `source_listing_key`, `payload`, `collected_at`, `payload_hash` |
| `listing` | Anúncio normalizado | `id`, `source_id`, `source_listing_key`, `advertiser`, `transaction_type`, `type`, `first_seen_at`, `last_seen_at` |
| `property` | Imóvel único provável | `id`, `fingerprint`, `type`, `canonical_location_id`, `confidence_status`, `created_at` |
| `property_listing_match` | Relação anúncio-imóvel | `property_id`, `listing_id`, `match_score`, `match_rule`, `algorithm_version`, `review_status` |
| `price_observation` | Preço observado | `id`, `listing_id`, `property_id`, `price`, `condo_fee`, `tax`, `observed_at` |
| `availability_event` | Evento de disponibilidade | `id`, `listing_id`, `property_id`, `event_type`, `event_date`, `evidence` |
| `location` | Localização normalizada | `id`, `address`, `neighborhood`, `city`, `state`, `lat`, `lng`, `geo_precision` |
| `region` | Recorte geográfico | `id`, `name`, `type`, `geometry` |
| `metric_snapshot` | Agregação analítica | `id`, `period`, `region_id`, `transaction_type`, `metrics` |
| `ml_dataset_version` | Dataset ML versionado | `id`, `generated_at`, `feature_version`, `row_count`, `quality_filters` |
| `model_version` | Modelo treinado | `id`, `target`, `algorithm`, `metrics`, `trained_at`, `status` |
| `prediction_request` | Inferência futura | `id`, `user_id`, `input`, `output`, `model_version_id`, `tokens_charged` |
| `user_token_wallet` | Saldo futuro | `user_id`, `balance`, `updated_at` |
| `token_transaction` | Ledger de tokens | `id`, `user_id`, `type`, `amount`, `reason`, `created_at` |

### 11.2 Lifecycle Rules

- Snapshot bruto é imutável.
- Normalização pode ser reprocessada, mas deve manter rastreabilidade ao snapshot bruto.
- Preço é evento temporal, não apenas campo atual.
- Status de disponibilidade é inferência operacional, não confirmação de transação real.
- Imóvel único é uma hipótese versionada, não verdade absoluta.
- Mudança de algoritmo de deduplicação deve preservar versão anterior ou permitir reprocessamento auditável.

## 12. Deduplication Strategy

Deduplicação combina regras determinísticas e score probabilístico.

### 12.1 Candidate Blocking

Blocos iniciais reduzem comparações:

- cidade;
- transação: venda ou aluguel;
- tipo de imóvel;
- bairro normalizado;
- faixa de área;
- faixa de preço;
- coordenada aproximada quando existir;
- nome de condomínio quando existir.

### 12.2 Matching Features

Campos usados no score:

- endereço normalizado;
- bairro;
- latitude/longitude;
- tipo de imóvel;
- área privativa e total;
- dormitórios, suítes, banheiros e vagas;
- preço e condomínio;
- descrição normalizada;
- nome do condomínio;
- anunciante/imobiliária;
- imagens ou hashes de imagem, se disponíveis no futuro.

### 12.3 Initial Thresholds

Premissa inicial a validar com amostra real:

- `score >= 0.85`: match automático;
- `0.65 <= score < 0.85`: candidato para revisão futura;
- `score < 0.65`: manter separado.

### 12.4 Acceptance Rules

- Todo match deve registrar score, regra, versão e evidências.
- O dashboard deve diferenciar anúncio de imóvel consolidado.
- Métricas podem ser calculadas por anúncio ou por imóvel único, com rótulo claro.
- Falsos positivos são mais graves que falsos negativos no MVP; priorizar precisão.

## 13. Architecture

### 13.1 Logical Layers

1. **Collection**: scraper Sub100, paginação, retries, rate limit e contrato de resposta.
2. **Bronze**: armazenamento bruto de snapshots e runs.
3. **Silver**: normalização, entidades, histórico de preço, localização e disponibilidade.
4. **Matching**: deduplicação, scoring, versionamento e evidências.
5. **Gold**: métricas agregadas por região, tempo, transação e tipo.
6. **API**: endpoints para dashboard, detalhes, qualidade e futuras previsões.
7. **Dashboard**: mapa, filtros, séries, métricas e painel operacional.
8. **ML Pipeline**: features, treino, avaliação, versionamento e inferência futura.
9. **SaaS**: autenticação, tokens, billing e histórico de previsões.

### 13.2 Core Flow

1. Scheduler inicia run diário.
2. Scraper coleta páginas do Sub100.
3. Sistema salva payload bruto e metadados da execução.
4. Normalizador converte dados para entidades analíticas.
5. Pipeline compara presença atual versus histórico anterior.
6. Matching agrupa anúncios em imóveis prováveis.
7. Agregações alimentam dashboard.
8. Dataset versionado alimenta treino ML futuro.
9. Inferência futura usa modelo publicado e ledger de tokens.

## 14. Recommended Stack

Stack recomendada pragmática, alinhada ao repositório Python atual e ao caráter data-driven.

| Layer | Recommendation | Reason | Secondary Option |
|---|---|---|---|
| Language | Python 3.13 | Já usado no projeto; forte para scraping, dados e ML | Python 3.12 se dependências bloquearem 3.13 |
| Package manager | Poetry | Já presente no repo | uv |
| Scraping | `requests` + parser próprio inicial; evoluir para `httpx` se async for necessário | Simples e suficiente para API JSON | Scrapy para múltiplas fontes futuras |
| Backend API | FastAPI | Boa tipagem, OpenAPI, leve para APIs data-driven | Django se admin/auth integrado virar prioridade |
| Database | PostgreSQL + PostGIS | Histórico relacional, consultas geoespaciais e escalabilidade | DuckDB apenas para análise local |
| Migrations | Alembic | Padrão com SQLAlchemy/FastAPI | Django migrations se stack virar Django |
| ORM/Data access | SQLAlchemy 2.x | Controle explícito e boa integração com Alembic | SQLModel |
| Jobs | APScheduler no MVP; Celery/RQ quando houver fila real | Baixa complexidade inicial | Prefect/Kestra para orquestração mais pesada |
| Frontend | Next.js + React + TypeScript | Dashboard web, roteamento e futura SaaS | Vite React se app for só SPA |
| UI | Tailwind CSS + shadcn/ui | Velocidade e consistência | CSS Modules |
| Charts | ECharts ou Recharts | Séries e gráficos analíticos | Plotly para exploração pesada |
| Maps | MapLibre GL + PostGIS tiles/GeoJSON | Evita lock-in e suporta mapas ricos | Leaflet para MVP simples |
| ML | scikit-learn + XGBoost/LightGBM | Regressão tabular robusta | CatBoost se categóricas dominarem |
| Experiment tracking | MLflow no pós-MVP | Versionar modelos e métricas | Artefatos simples em tabela no MVP |
| Observability | logs estruturados + Sentry + health endpoints | Diagnóstico rápido | OpenTelemetry no futuro |
| Deploy MVP | Docker Compose em VPS | Barato, simples, controlável | Render/Fly.io |
| Auth future | Auth própria com FastAPI/JWT ou Clerk | SaaS com contas e tokens | Supabase Auth |
| Billing future | Stripe | Ledger e pagamentos maduros | Mercado Pago se foco Brasil exigir |

## 15. Roadmap

### Phase 0 — Discovery and Specification

**Goal:** fechar base documental antes de construir.

**Deliverables:**

- PRD consolidado.
- TASKS.md executável.
- decisões de stack registradas.
- perguntas abertas documentadas.

**Dependencies:** contexto de produto e repo atual.

**Done:** PRD e TASKS revisados como fonte de execução.

### Phase 1 — Source Validation and Data Contract

**Goal:** entender o Sub100 antes de depender dele.

**Deliverables:**

- contrato da API;
- campos críticos;
- amostras controladas;
- riscos de paginação, schema e rate limit;
- critérios de sucesso do scraper.

**Dependencies:** Phase 0.

**Done:** fonte validada com amostras e limites documentados.

### Phase 2 — Data Foundation

**Goal:** criar persistência histórica confiável.

**Deliverables:**

- banco PostgreSQL/PostGIS;
- schema bronze/silver;
- migrations;
- runs, snapshots, listings, preços, disponibilidade e localização;
- testes de normalização e persistência.

**Dependencies:** Phase 1.

**Done:** coleta salva dados brutos e normalizados sem sobrescrever histórico.

### Phase 3 — Deduplication and Lifecycle

**Goal:** diferenciar anúncio de imóvel único provável.

**Deliverables:**

- normalização de texto/endereço;
- blocos de comparação;
- score de matching;
- versionamento de algoritmo;
- eventos de preço, ausência e retorno;
- amostra de validação manual.

**Dependencies:** Phase 2.

**Done:** matches são rastreáveis e conservadores.

### Phase 4 — Analytics API and Dashboard MVP

**Goal:** entregar primeira experiência analítica útil.

**Deliverables:**

- endpoints de métricas, mapa, séries e detalhe;
- dashboard com filtros;
- mapa de pontos/densidade;
- painel de qualidade da base;
- testes e validação visual.

**Dependencies:** Phase 2 e Phase 3.

**Done:** usuário explora venda/aluguel por bairro, preço, período, tipo e status.

### Phase 5 — Data Quality and ML Preparation

**Goal:** preparar base para treino preditivo sem expor ML prematuro.

**Deliverables:**

- dataset versionado;
- filtros de qualidade;
- features iniciais;
- baseline estatístico;
- avaliação de viabilidade.

**Dependencies:** Phase 4 e histórico mínimo.

**Done:** existe dataset reproduzível e métrica baseline.

### Phase 6 — Predictive Pricing

**Goal:** criar modelo de preço justo validado.

**Deliverables:**

- modelos separados para venda e aluguel quando necessário;
- avaliação por MAE, RMSE, MAPE e erro por segmento;
- API interna de inferência;
- explicabilidade mínima;
- monitoramento de erro.

**Dependencies:** Phase 5.

**Done:** modelo supera baseline e tem limitações documentadas.

### Phase 7 — SaaS and Monetization

**Goal:** transformar inferência em produto monetizável.

**Deliverables:**

- autenticação;
- carteira de tokens;
- ledger;
- checkout;
- histórico de previsões;
- auditoria de cobrança;
- métricas de receita e uso.

**Dependencies:** Phase 6.

**Done:** previsão paga debita token apenas em sucesso e registra transação auditável.

## 16. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| API Sub100 muda sem aviso | Scraper quebra | Contrato, testes, schema drift e alertas |
| Bloqueio por volume de requests | Coleta falha | Rate limit, backoff e limites conservadores |
| Dados incompletos de localização | Mapas menos precisos | Geo precision explícita e geocodificação futura |
| Deduplicação falsa positiva | Métricas distorcidas | Threshold conservador, evidências e revisão |
| Histórico insuficiente para ML | Modelo fraco | Adiar ML produção até baseline confiável |
| Custo de mapas/geocoding | Margem reduzida | Cache e fornecedores com free tier |
| Ambiguidade legal/termos de uso | Risco operacional | Revisão de termos antes de escala |
| Stack excessiva cedo demais | Atraso do MVP | Começar simples e evoluir por gates |

## 17. Assumptions

- Foco inicial é Maringá.
- Sub100 é única fonte do MVP.
- Coleta diária é suficiente no início.
- PostgreSQL com PostGIS será banco principal.
- FastAPI será backend API recomendado.
- Next.js será frontend recomendado.
- Docker Compose em VPS é deploy inicial recomendado.
- Dashboard pode iniciar sem autenticação ou com acesso restrito simples.
- ML só entra depois de base histórica e qualidade mínima.
- Monetização por tokens fica fora do MVP.
- Ausência de anúncio é inferência, não confirmação de venda ou locação.
- Deduplicação deve priorizar precisão sobre recall no MVP.

## 18. Open Questions

- O dashboard MVP será privado, público ou protegido por login simples?
- Qual frequência real desejada de coleta: diária, mais de uma vez ao dia ou manual sob demanda?
- Existe restrição formal de uso dos dados do Sub100 que precise revisão jurídica?
- Quais campos do Sub100 são obrigatórios para considerar um anúncio utilizável?
- Qual histórico mínimo será exigido antes do primeiro treino ML: 30, 60, 90 ou mais dias?
- Haverá revisão manual de matches incertos no MVP ou só no pós-MVP?
- Qual fornecedor de mapa/geocodificação será usado se coordenadas forem insuficientes?
- Billing futuro deve usar Stripe, Mercado Pago ou outro gateway?
- O produto mira primeiro uso interno, corretores, investidores ou imobiliárias B2B?

## 19. Acceptance Criteria

### 19.1 Source and Scraping

- Fonte Sub100 documentada com endpoint, parâmetros, paginação e campos críticos.
- Coleta possui timeout, retry, delay e erro rastreável.
- Cada execução registra status, contagens, início, fim e parâmetros.
- Payload bruto é salvo antes de qualquer transformação.

### 19.2 Data Foundation

- Schema separa fonte, run, snapshot bruto, anúncio, imóvel, preço, localização e status.
- Dados normalizados preservam referência ao bruto.
- Histórico de preço não é sobrescrito.
- Mudança de schema ou campo crítico ausente é detectada.

### 19.3 Deduplication

- Matching registra score, regra, versão e evidências.
- Match automático usa threshold conservador.
- Anúncio e imóvel único são entidades separadas.
- Métricas deixam claro se usam anúncios ou imóveis consolidados.

### 19.4 Dashboard MVP

- Dashboard mostra venda e aluguel separadamente.
- Usuário filtra por bairro, tipo, período, faixa de preço e status.
- Mapa mostra pontos ou densidade.
- Séries temporais mostram evolução de preço e estoque.
- Painel operacional mostra últimas coletas e falhas.

### 19.5 ML Preparation

- Dataset de treino é versionado e reproduzível.
- Features e alvo são documentados.
- Baseline estatístico existe antes de modelo avançado.
- Métricas de erro são calculadas por segmento relevante.

### 19.6 SaaS Future

- Token só é consumido após inferência concluída com sucesso.
- Toda movimentação de token gera ledger auditável.
- Falha técnica não consome saldo.
- Usuário consegue consultar histórico de previsões.

