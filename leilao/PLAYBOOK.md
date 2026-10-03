# Playbook de Compra em Leilão — Waltham Auto Gallery

> Metodologia usada pela rotina diária (seg–sex, 10h ET) para pré-selecionar oportunidades na **ADESA Clear** (e leilões com inspeção equivalente).
> Duas "cabeças" analisam cada carro: o **Técnico** (mecânica e histórico) e o **Vendedor** (mercado e giro).

---

## 1. Fontes de inventário (prioridade)

| Leilão | Nível de inspeção | Por que entra |
|---|---|---|
| **ADESA Clear** (Carvana/ADESA) | Fotos 360°, scan OBD-II, áudio do motor, VDP como laudo | Fonte principal — melhor laudo digital do mercado |
| **OPENLANE** (ex-ADESA.com) | CR com fotos, códigos OBD, AutoGrade | Muito volume off-lease (bancos/financeiras) — carros de 1 dono |
| **ACV Auctions** | Inspetor presencial, **áudio do motor**, scan OBD, medidor de pintura | Nível de detalhe muito parecido com Clear; forte no Nordeste |
| **Manheim (Express / Simulcast)** | CR + AutoGrade + MMR | Referência de preço (MMR) para tudo o resto |
| Copart / IAA | Fraco (salvage) | **Fora** do escopo, exceto pedido explícito |

## 1b. Perfil real de compra (extraído do Gmail — 43 arremates mai–out/2026)

- **Marcas**: quase só **Honda / Toyota / Acura / Lexus** (CR-V, Civic, Accord, Fit, Pilot, Odyssey, Camry, Corolla, Prius, RAV4, Highlander, Sienna, Avalon, RX 350, RDX, TSX).
- **Anos**: 2010–2020, concentrado em **2010–2016**. Muito híbrido Toyota (Prius, Camry Hybrid, Highlander Hybrid).
- **Ticket**: ~**$4k–$12k** de martelo (ex.: CR-V 2013 → $7.300 + $400 buyer fee + $25 floor plan Westlake).
- **Origem**: ADESA Boston, New Jersey, Syracuse, Buffalo, Pittsburgh e pátios Carvana (Elyria, Chesterfield, Trenton).
- **Lição recente**: 2013 Accord EX-L (ADESA Boston) foi para **arbitragem/unwind** — reforça checar áudio do motor e fotos antes do lance.

> Regra: o Vendedor dá **bônus** para carros dentro desse perfil (a loja já sabe vender, preparar e precificar) e exige margem maior fora dele.

## 2. Filtros de entrada (descartar antes de analisar)

- Título: só **Clean**. Nada de salvage, rebuilt, flood, lemon/buyback, TMU.
- Ano ≥ 2009, milhagem ≤ 140k, grade ≥ 2.5 (igual às buscas salvas "Cris"/"Cris1"; ajustável em `config.example.json`).
- Distância: até ~250 mi de Waltham (02453) por padrão; até 600 mi só se o desconto pagar o frete (≈ $1,50/mi).
- Condição Clear/CR: sem alerta de **frame/estrutura**, sem airbag acionado, sem odômetro inconsistente.
- OBD: descartar códigos de transmissão (P07xx), catalisador (P0420/P0430) sem desconto, misfire (P030x) recorrente.
- **MA inspection**: nenhum item que reprove na vistoria estadual (check engine aceso, vidro trincado na área do limpador, pneu < 2/32").

## 3. Cabeça do Técnico — "a manutenção seguiu o manual?"

Para cada carro, cruzar **histórico de serviço do CARFAX/AutoCheck** com o **cronograma do fabricante**:

| Item | Intervalo típico (verificar manual do modelo) | Sinal de alerta |
|---|---|---|
| Troca de óleo | 5k–10k mi / 12 meses | Lacunas > 15k mi entre registros |
| Fluido de transmissão (CVT Nissan/Subaru/Honda) | 25k–60k mi | CVT > 60k sem troca registrada = **risco alto** |
| Correia dentada (ex.: Subaru antigos, alguns VW/Audi, Honda V6) | 90k–105k mi | Passou do intervalo sem registro → descontar ~$800–1.500 |
| Velas | 60k–120k mi | — |
| Fluido de freio | 2–3 anos | — |
| Arrefecimento | 100k mi / 5–10 anos | — |
| Recalls (NHTSA) | — | Recall aberto = desconto ou fila na concessionária |

**Áudio do motor / OBD (Clear e ACV):** ouvir batida de válvula, ruído de corrente de comando (VW 2.0T, Ford 3.5 EcoBoost, Hyundai/Kia 2.4/2.0T — atenção ao recall de motor Theta II), rolamento.

**Problemas crônicos conhecidos** (puxar sempre): Nissan CVT, Hyundai/Kia Theta II, Ford PowerShift (Focus/Fiesta 12–16), Jeep 9-speed, motores 1.5T Honda (diluição de óleo), consumo de óleo Subaru FB25 antigos, BMW N20/N26 corrente.

**Nota técnica (0–10)** = histórico de manutenção (40%) + laudo/OBD/áudio (40%) + confiabilidade do modelo (20%).

## 4. Cabeça do Vendedor — "esse carro gira rápido e com margem?"

- **Demanda Greater Boston**: modelos com maior procura e menor Days-to-Turn (CarGurus/Cars.com market data): Toyota RAV4/Camry/Corolla/Highlander, Honda CR-V/Civic/Accord/Pilot, Subaru Outback/Forester/Crosstown (AWD vende muito na Nova Inglaterra), Mazda CX-5, Hyundai Tucson/Santa Fe, Ford F-150, Jeep Grand Cherokee, Tesla Model 3/Y (atenção à depreciação).
- **Avaliação de consumidor**: Consumer Reports / J.D. Power reliability ≥ média.
- **Busca e IA**: modelos que aparecem mais em buscas "best used SUV under $20k" / respostas de ChatGPT, Gemini e Perplexity — normalmente Toyota/Honda/Mazda/Subaru/Lexus. Isso puxa lead orgânico.
- **AWD + baixo km + 1 dono + histórico completo** = premium de preço no varejo MA.

**Nota de mercado (0–10)** = demanda local / giro (50%) + margem estimada (35%) + "buscabilidade" do modelo (15%).

## 5. Conta do lance máximo (cálculo padrão)

$$\text{Lance máx} = \text{Varejo esperado} - \text{Margem alvo} - \text{Taxa leilão} - \text{Frete} - \text{Recon} - \text{Registro/Inspeção MA} - \text{Custo de capital}$$

- **Varejo esperado**: mediana de anúncios comparáveis (mesmo ano ±1, km ±15k, raio 100 mi de Waltham) − 3–5% de negociação.
- **Taxas ADESA**: buyer fee ~**$400** + floor plan fee ~$25 (conferir na confirmação de pagamento).
- **Margem alvo**: mínimo **$1.500** ou **15%**, o que for maior (carros de $4k–$12k giram rápido, mas cada $ de recon pesa).
- **Recon**: detalhamento interno (~$60–120 consumíveis) + pneus/freios conforme laudo + reparos citados.
- **Custo de capital**: floor plan ~ (taxa anual ÷ 365) × 45 dias × preço.
- Comparar sempre com **MMR** (Manheim): comprar acima do MMR só se nota técnica ≥ 8 e giro alto.

## 6. Score final e ranking

$$\text{Score} = 0{,}45 \cdot \text{Técnico} + 0{,}40 \cdot \text{Mercado} + 0{,}15 \cdot \text{Desconto vs. MMR}$$

- **≥ 8,0** 🟢 Comprar até o lance máx · **6,5–7,9** 🟡 Só abaixo do lance máx − $500 · **< 6,5** 🔴 Passar.
- Relatório traz no máximo **10 carros/dia**, ordenados por score.

## 7. Regras de proteção

- Conferir a **janela de arbitragem** da ADESA Clear e pedir inspeção pós-venda (PSI) em carros > $15k.
- Nada de lance sem ver o áudio do motor e as fotos de assoalho/longarinas.
- A rotina **sugere**; o lance é sempre decisão humana.
